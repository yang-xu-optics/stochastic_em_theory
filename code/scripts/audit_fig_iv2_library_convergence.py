"""Convergence audit for the Gorlach 2023 Fig. IV.2 reproduction.

Question: does the ensemble-mean BSV HHG spectrum converge with the number of
TDSE field-amplitude library nodes used for log-spectrum interpolation?

Everything except the library size is identical to
results/runs/gorlach-2023-fig-iv2-bsv-threshold-20260606 (seed, shots, grid,
time step, pulse, absorber). The node sets are nested (13, 25, 49, 97), so the
13-node set is exactly the library of that run. The same Monte Carlo shots are
used for every library size, so differences isolate interpolation error.

The script also reports how much a 0.999 intensity-tail cap changes the result
at the finest library, and the ground-state energy reached by the
imaginary-time settings used in production.

Units: atomic units for fields and energies; W/cm^2 for mean peak intensity.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from multiprocessing import Pool
from pathlib import Path

import numpy as np

from stochastic_em_theory.fig3b import _interpolate_tdse_spectra, _tdse_library_field_amplitudes
from stochastic_em_theory.fig_iv2 import (
    bsv_intensity_quantile_au,
    intensity_w_cm2_to_field_au,
    sample_bsv_intensity_au,
)
from stochastic_em_theory.io import current_git_commit, write_manifest
from stochastic_em_theory.tdse1d import (
    SoftCoreGrid,
    imaginary_time_ground_state,
    soft_core_potential,
    tdse_harmonic_spectrum,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "runs" / "20261114-fig-iv2-library-convergence-audit"

OMEGA_AU = 0.057
MAX_ORDER = 40
SHOTS = 50_000
SEED = 20230604
INTENSITIES_W_CM2 = (1.0e13, 2.0e13)
TAIL_QUANTILE = 0.999
PEAK_WINDOW_HALF_WIDTH = 0.35
LIBRARY_SIZES = ((8, 13), (4, 25), (2, 49), (1, 97))  # (stride into the 97-node set, node count)
TDSE = dict(
    omega_au=OMEGA_AU,
    max_order=MAX_ORDER,
    x_min=-100.0,
    x_max=100.0,
    grid_points=2048,
    softening=0.8160,
    dt_au=0.05,
    ramp_cycles=5.0,
    flat_cycles=15.0,
    ground_state_iterations=220,
    ground_state_dt_au=0.08,
    carrier_phase=0.0,
    absorber_start_au=75.0,
    absorber_strength=5.0e-4,
)


def _solve(amplitude: float) -> tuple[np.ndarray, np.ndarray]:
    spectrum = tdse_harmonic_spectrum(field_amplitude_au=float(amplitude), **TDSE)
    orders = spectrum.angular_frequency / OMEGA_AU
    mask = orders <= MAX_ORDER
    return orders[mask], spectrum.raw_power[mask]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(SEED)
    cases: dict[float, tuple[float, np.ndarray]] = {}
    for intensity in INTENSITIES_W_CM2:
        mean_intensity_au = intensity_w_cm2_to_field_au(intensity) ** 2
        cases[intensity] = (
            mean_intensity_au,
            sample_bsv_intensity_au(mean_intensity_au=mean_intensity_au, shots=SHOTS, rng=rng),
        )
    all_amplitudes = np.concatenate([np.sqrt(raw) for _, raw in cases.values()])
    nodes = _tdse_library_field_amplitudes(field_amplitudes_au=all_amplitudes, bins=97)

    with Pool(args.workers) as pool:
        solved = pool.map(_solve, nodes, chunksize=1)
    orders = solved[0][0]
    library = np.vstack([power for _, power in solved])

    odd_orders = np.arange(1, MAX_ORDER, 2)
    windows = [np.nonzero(np.abs(orders - q) <= PEAK_WINDOW_HALF_WIDTH)[0] for q in odd_orders]

    results: dict[str, object] = {
        "library_nodes_au": nodes.tolist(),
        "odd_harmonic_orders": odd_orders.tolist(),
        "peak_yield_definition": "max over FFT bins within +-0.35 of each odd order of the ensemble-mean spectrum",
        "cases": {},
    }
    for intensity, (mean_intensity_au, raw) in cases.items():
        cap = bsv_intensity_quantile_au(mean_intensity_au=mean_intensity_au, quantile=TAIL_QUANTILE)
        entry: dict[str, dict[str, list[float]]] = {}
        for label, sample in (("raw", raw), (f"tailcap_{TAIL_QUANTILE}", np.minimum(raw, cap))):
            amplitudes = np.sqrt(sample)
            per_size: dict[str, list[float]] = {}
            for stride, size in LIBRARY_SIZES:
                index = np.arange(0, nodes.size, stride)
                peaks = []
                for window in windows:
                    spectra = _interpolate_tdse_spectra(
                        field_amplitudes_au=amplitudes,
                        library_amplitudes_au=nodes[index],
                        library_spectra=library[np.ix_(index, window)],
                    )
                    peaks.append(float(np.max(spectra.mean(axis=0))))
                per_size[str(size)] = peaks
            entry[label] = per_size
        results["cases"][f"{intensity:.0e}"] = entry

    grid = SoftCoreGrid.create(x_min=TDSE["x_min"], x_max=TDSE["x_max"], points=TDSE["grid_points"])
    potential = soft_core_potential(grid.x, softening=TDSE["softening"])
    energies = {}
    for iterations in (TDSE["ground_state_iterations"], 2000):
        psi = imaginary_time_ground_state(
            grid=grid, potential=potential, steps=iterations, dt_au=TDSE["ground_state_dt_au"]
        )
        kinetic = float(np.sum(np.conj(psi) * np.fft.ifft(0.5 * grid.k**2 * np.fft.fft(psi))).real * grid.dx)
        energies[str(iterations)] = kinetic + float(np.sum(potential * np.abs(psi) ** 2) * grid.dx)
    results["ground_state_energy_au_by_iterations"] = energies

    (args.output_dir / "library_convergence.json").write_text(json.dumps(results, indent=1) + "\n")
    parameters = {
        "seed": SEED,
        "shots": SHOTS,
        "intensities_w_cm2": list(INTENSITIES_W_CM2),
        "tail_quantile": TAIL_QUANTILE,
        "library_node_counts": [size for _, size in LIBRARY_SIZES],
        "peak_window_half_width": PEAK_WINDOW_HALF_WIDTH,
        "tdse": TDSE,
    }
    write_manifest(args.output_dir / "parameters.yaml", parameters)
    write_manifest(
        args.output_dir / "manifest.yaml",
        {
            "run_id": args.output_dir.name,
            "created": date.today().isoformat(),
            "code_entrypoint": "code/scripts/audit_fig_iv2_library_convergence.py",
            "git_commit": current_git_commit(REPO_ROOT),
            "parameter_file": "parameters.yaml",
            "random_seeds": [SEED],
            "observable": "ensemble-mean odd-harmonic peak yield versus TDSE amplitude-library size",
            "units": "atomic units for fields and energies; W/cm^2 for mean peak intensity",
            "notes": (
                "Convergence audit of gorlach-2023-fig-iv2-bsv-threshold-20260606. Nested node sets; "
                "common random numbers. The tail-capped ensemble is interpolated on the uncapped node "
                "set, so its nodes differ from those of the committed tail-capped run."
            ),
            "outputs": {"results_json": "library_convergence.json"},
        },
    )
    print(args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
