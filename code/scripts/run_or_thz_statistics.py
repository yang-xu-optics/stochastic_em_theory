"""THz field statistics for optical rectification of bright squeezed vacuum.

Spec: wiki/simulations/bsv-optical-rectification-thz-statistics.md.
Writes exact quantum statistics versus photon number and mode number, the
single-shot amplitude distribution in the bright limit (with a sampler
cross-check), and the spectral decomposition into classical-noise and
spontaneous terms.

All quantities are dimensionless (see the spec for the units).
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

from stochastic_em_theory.io import current_git_commit, write_csv, write_json, write_manifest
from stochastic_em_theory.optical_rectification import (
    bright_limit_statistics,
    gaussian_mode_overlap_squared,
    sample_classical_noise_amplitudes,
    sample_cumulants,
    schmidt_number_estimates,
    thz_field_statistics,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "runs" / "20261114-bsv-or-thz-statistics"

SEED = 20261114
SAMPLER_SHOTS = 200_000
MODE_NUMBERS = (1, 2, 5, 20)
NBAR_GRID = np.logspace(-2.0, 6.0, 81)
SPECTRUM_NBAR = 1.0e6

# Chart tokens: validated with the dataviz palette checker (light surface).
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
ORDINAL_BLUE = ("#86b6ef", "#3987e5", "#1c5cab", "#0d366b")  # K = 1, 2, 5, 20
SERIES = ("#2a78d6", "#eb6834", "#1baf7a")


def _style(ax: plt.Axes, *, title: str, xlabel: str, ylabel: str) -> None:
    ax.set_facecolor(SURFACE)
    ax.set_title(title, loc="left", fontsize=10.5, color=INK, pad=8)
    ax.set_xlabel(xlabel, fontsize=9, color=INK_SECONDARY)
    ax.set_ylabel(ylabel, fontsize=9, color=INK_SECONDARY)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
    ax.tick_params(colors=INK_MUTED, labelsize=8, length=3)


def _plot(output: Path, rows_nbar: list[dict], w: np.ndarray, densities: dict[int, np.ndarray],
          spectrum: dict[str, np.ndarray]) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.4), constrained_layout=True)
    fig.patch.set_facecolor(SURFACE)

    # (a) single-shot amplitude distribution
    ax = axes[0, 0]
    _style(ax, title="(a) Single-shot THz field distribution, bright limit",
           xlabel="THz field amplitude / mean", ylabel="probability density")
    label_positions = {1: (0.10, 1.52), 2: (0.42, 0.88), 5: (1.52, 0.60), 20: (1.33, 1.16)}
    for color, modes in zip(ORDINAL_BLUE, MODE_NUMBERS, strict=True):
        ax.plot(w, densities[modes], color=color, linewidth=2.0, solid_capstyle="round", label=f"K = {modes}")
        ax.text(*label_positions[modes], f"K = {modes}", fontsize=8.5, color=INK_SECONDARY)
    ax.axvline(1.0, color=INK_MUTED, linewidth=1.0, linestyle=(0, (3, 3)))
    ax.text(1.03, 1.42, "coherent pump", fontsize=8, color=INK_MUTED)
    ax.set_xlim(0.0, 3.5)
    ax.set_ylim(0.0, 1.6)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="upper right", title="pump modes",
              title_fontsize=8)

    by_modes = {m: [r for r in rows_nbar if r["modes"] == m] for m in MODE_NUMBERS}

    # (b) energy enhancement
    ax = axes[0, 1]
    _style(ax, title="(b) Mean THz energy relative to a coherent pump",
           xlabel="mean photon number per mode", ylabel="energy ratio")
    for color, modes in zip(ORDINAL_BLUE, MODE_NUMBERS, strict=True):
        rows = by_modes[modes]
        x = [r["nbar_per_mode"] for r in rows]
        y = [r["energy_enhancement_over_coherent"] for r in rows]
        ax.plot(x, y, color=color, linewidth=2.0, solid_capstyle="round", label=f"K = {modes}")
        ax.text(1.6e6, y[-1], f"{1 + 2 / modes:.2g}", fontsize=8.5, color=INK_SECONDARY, va="center")
    ax.set_xscale("log")
    ax.set_xlim(1e-2, 2.0e7)
    ax.set_ylim(0.9, 3.2)
    ax.text(1.5e-2, 3.05, "bright limit: 1 + 2/K", fontsize=8, color=INK_MUTED)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="center", bbox_to_anchor=(0.62, 0.70))

    # (c) energy fluctuation ratio
    ax = axes[1, 0]
    _style(ax, title="(c) THz energy fluctuation ratio  <U²> / <U>²",
           xlabel="mean photon number per mode", ylabel="ratio")
    for color, modes in zip(ORDINAL_BLUE, MODE_NUMBERS, strict=True):
        rows = by_modes[modes]
        x = [r["nbar_per_mode"] for r in rows]
        y = [r["energy_g2"] for r in rows]
        ax.plot(x, y, color=color, linewidth=2.0, solid_capstyle="round", label=f"K = {modes}")
        ax.text(1.6e6, y[-1], f"{bright_limit_statistics(float(modes))['energy_g2']:.3g}", fontsize=8.5,
                color=INK_SECONDARY, va="center")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-2, 2.0e7)
    ax.set_ylim(0.9, 400.0)
    ax.text(2.0e-2, 1.15, "pair regime: 2 / (K n) for K n << 1", fontsize=8, color=INK_MUTED)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="upper right")

    # (d) spectral decomposition
    ax = axes[1, 1]
    _style(ax, title=rf"(d) THz spectrum terms, one mode, $n = 10^{{{int(np.log10(SPECTRUM_NBAR))}}}$",
           xlabel="THz frequency / pump spectral width", ylabel="relative to zero frequency")
    x = spectrum["omega_over_sigma"]
    ax.plot(x, spectrum["classical_noise"], color=SERIES[0], linewidth=2.0, label="classical-noise terms")
    ax.plot(x, spectrum["spontaneous"], color=SERIES[1], linewidth=2.0, label="spontaneous term")
    ax.plot(x, spectrum["total"], color=SERIES[2], linewidth=2.0, linestyle=(0, (4, 2)), label="quantum total")
    ax.set_yscale("log")
    ax.set_xlim(0.0, 10.0)
    ax.set_ylim(1e-9, 3.0)
    ax.text(3.4, 0.12, "classical-noise terms", fontsize=8.5, color=INK_SECONDARY)
    ax.text(0.3, 6.0e-7, "spontaneous term, 1 / (3n)", fontsize=8.5, color=INK_SECONDARY)
    ax.text(7.9, 1.2e-6, "quantum total", fontsize=8.5, color=INK_SECONDARY)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="lower left")

    fig.savefig(output, dpi=200, facecolor=SURFACE)
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    out: Path = args.output_dir
    out.mkdir(parents=True, exist_ok=True)

    rows_nbar: list[dict] = []
    for modes in MODE_NUMBERS:
        for nbar in NBAR_GRID:
            stats = thz_field_statistics(np.full(modes, float(nbar)))
            rows_nbar.append(
                {
                    "modes": modes,
                    "nbar_per_mode": float(nbar),
                    "mean_field_per_photon_units": stats.mean_field,
                    "relative_field_fluctuation": stats.relative_field_fluctuation,
                    "skewness": stats.skewness,
                    "excess_kurtosis": stats.excess_kurtosis,
                    "energy_enhancement_over_coherent": stats.energy_enhancement_over_coherent,
                    "energy_g2": stats.energy_g2,
                }
            )
    write_csv(out / "or_statistics_vs_nbar.csv", rows_nbar, list(rows_nbar[0].keys()))

    w = np.linspace(1.0e-3, 3.5, 700)
    densities = {modes: gamma.pdf(w, a=0.5 * modes, scale=2.0 / modes) for modes in MODE_NUMBERS}
    rng = np.random.default_rng(SEED)
    sampler_rows = []
    for modes in MODE_NUMBERS:
        samples = sample_classical_noise_amplitudes(nbars=np.full(modes, 1.0 / modes), shots=SAMPLER_SHOTS, rng=rng)
        cumulants = sample_cumulants(samples)
        estimates = schmidt_number_estimates(cumulants)
        limit = bright_limit_statistics(float(modes))
        sampler_rows.append(
            {
                "modes": modes,
                "shots": SAMPLER_SHOTS,
                "sample_mean": cumulants[0],
                "sample_relative_fluctuation": float(np.sqrt(cumulants[1]) / cumulants[0]),
                "limit_relative_fluctuation": limit["relative_field_fluctuation"],
                "sample_energy_enhancement": float(np.mean(samples**2) / np.mean(samples) ** 2),
                "limit_energy_enhancement": limit["energy_enhancement_over_coherent"],
                "sample_energy_g2": float(np.mean(samples**4) / np.mean(samples**2) ** 2),
                "limit_energy_g2": limit["energy_g2"],
                "fraction_negative": float(np.mean(samples < 0.0)),
                "mode_number_from_skewness": estimates["from_skewness"],
                "mode_number_from_kurtosis": estimates["from_kurtosis"],
            }
        )
    density_rows = [
        {"amplitude_over_mean": float(x), **{f"density_K{m}": float(densities[m][i]) for m in MODE_NUMBERS}}
        for i, x in enumerate(w)
    ]
    write_csv(out / "or_amplitude_distribution.csv", density_rows, list(density_rows[0].keys()))

    omega = np.linspace(0.0, 10.0, 401)
    overlap2 = gaussian_mode_overlap_squared(omega)
    n = SPECTRUM_NBAR
    zero = 3.0 * n**2 + 2.0 * n
    classical = overlap2 * 3.0 * n**2 / zero
    spontaneous = np.full_like(omega, n / zero)
    total = (overlap2 * (3.0 * n**2 + n) + n) / zero
    spectrum = {"omega_over_sigma": omega, "classical_noise": classical, "spontaneous": spontaneous, "total": total}
    spectrum_rows = [
        {"omega_over_sigma": float(omega[i]), "classical_noise": float(classical[i]),
         "spontaneous": float(spontaneous[i]), "quantum_total": float(total[i])}
        for i in range(omega.size)
    ]
    write_csv(out / "or_spectrum_terms.csv", spectrum_rows, list(spectrum_rows[0].keys()))

    single_bright = thz_field_statistics(1.0e6)
    summary = {
        "single_mode_bright": {
            "nbar": 1.0e6,
            "energy_enhancement_over_coherent": single_bright.energy_enhancement_over_coherent,
            "energy_g2": single_bright.energy_g2,
            "relative_field_fluctuation": single_bright.relative_field_fluctuation,
            "skewness": single_bright.skewness,
            "excess_kurtosis": single_bright.excess_kurtosis,
        },
        "bright_limit_by_mode_number": {str(m): bright_limit_statistics(float(m)) for m in MODE_NUMBERS},
        "sampler_cross_check": sampler_rows,
        "spontaneous_crossover_omega_over_sigma": {
            f"{value:.0e}": float(2.0 * np.sqrt(np.log(3.0 * value))) for value in (1.0e6, 1.0e12)
        },
    }
    write_json(out / "or_summary.json", summary)
    _plot(out / "or_thz_statistics.png", rows_nbar, w, densities, spectrum)

    parameters = {
        "seed": SEED,
        "sampler_shots": SAMPLER_SHOTS,
        "mode_numbers": list(MODE_NUMBERS),
        "nbar_grid": {"min": float(NBAR_GRID[0]), "max": float(NBAR_GRID[-1]), "points": int(NBAR_GRID.size), "spacing": "log"},
        "spectrum_nbar": SPECTRUM_NBAR,
        "spectrum_mode": "one Gaussian mode, |c|^2 = exp(-Omega^2 / (4 sigma^2))",
    }
    write_manifest(out / "parameters.yaml", parameters)
    write_manifest(
        out / "manifest.yaml",
        {
            "run_id": out.name,
            "created": date.today().isoformat(),
            "claim_level": "exact_input_correspondence",
            "mechanism": "optical_rectification_of_bsv",
            "code_entrypoint": "code/scripts/run_or_thz_statistics.py",
            "git_commit": current_git_commit(REPO_ROOT),
            "parameter_file": "parameters.yaml",
            "random_seeds": [SEED],
            "observable": "THz field cumulants, energy enhancement, energy fluctuation ratio, amplitude density, spectrum terms",
            "units": "dimensionless: photon numbers; THz amplitude per pump photon; frequency over pump spectral width",
            "notes": (
                "First-order, undepleted, no propagation. Exact photon-number statistics of independent "
                "squeezed-vacuum modes; the sampler is the classical Gaussian amplitude-noise model and is a "
                "cross-check only."
            ),
            "outputs": {
                "statistics_csv": "or_statistics_vs_nbar.csv",
                "distribution_csv": "or_amplitude_distribution.csv",
                "spectrum_csv": "or_spectrum_terms.csv",
                "summary_json": "or_summary.json",
                "figure_png": "or_thz_statistics.png",
            },
        },
    )
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
