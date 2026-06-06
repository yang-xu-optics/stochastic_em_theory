from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.fields import sample_single_mode_husimi_q
from stochastic_em_theory.hhg_proxy import proxy_hhg_spectrum
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.mechanisms import MechanismFamily


def _conditional_means(values: np.ndarray, spectra: np.ndarray) -> dict[str, np.ndarray]:
    quantiles = np.quantile(values, [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    bins: dict[str, np.ndarray] = {}
    labels = ["low", "middle", "high"]
    for index, label in enumerate(labels):
        left = quantiles[index]
        right = quantiles[index + 1]
        if index == len(labels) - 1:
            mask = (values >= left) & (values <= right)
        else:
            mask = (values >= left) & (values < right)
        if not np.any(mask):
            bins[label] = np.zeros(spectra.shape[1], dtype=np.float64)
        else:
            bins[label] = np.mean(spectra[mask], axis=0)
    return bins


def run_proxy_hhg_ensemble(
    *,
    r: float,
    phase: float,
    shots: int,
    seed: int,
    base_field_amplitude_au: float,
    omega_au: float,
    ionization_potential_au: float,
    max_order: int,
    output_dir: Path,
) -> RunArtifacts:
    if shots <= 0:
        raise ValueError("shots must be positive")
    if base_field_amplitude_au <= 0:
        raise ValueError("base_field_amplitude_au must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    alpha = sample_single_mode_husimi_q(r=r, phase=phase, shots=shots, rng=rng)
    sampled_intensity = np.abs(alpha) ** 2
    normalized_amplitude = np.sqrt(sampled_intensity / max(float(np.mean(sampled_intensity)), 1e-12))
    field_amplitudes = base_field_amplitude_au * normalized_amplitude

    spectra = []
    cutoff_orders = []
    orders = None
    for field_amplitude in field_amplitudes:
        spectrum = proxy_hhg_spectrum(
            field_amplitude_au=float(field_amplitude),
            omega_au=omega_au,
            ionization_potential_au=ionization_potential_au,
            max_order=max_order,
        )
        orders = spectrum.orders
        spectra.append(spectrum.intensity)
        cutoff_orders.append(spectrum.cutoff_order)

    if orders is None:
        raise ValueError("no spectra were generated")

    spectra_array = np.vstack(spectra)
    conditional = _conditional_means(sampled_intensity, spectra_array)
    mean_spectrum = np.mean(spectra_array, axis=0)
    std_spectrum = np.std(spectra_array, axis=0, ddof=1) if shots > 1 else np.zeros_like(mean_spectrum)

    rows = []
    for index, order in enumerate(orders):
        rows.append(
            {
                "harmonic_order": float(order),
                "mean_intensity": float(mean_spectrum[index]),
                "std_intensity": float(std_spectrum[index]),
                "conditional_low": float(conditional["low"][index]),
                "conditional_middle": float(conditional["middle"][index]),
                "conditional_high": float(conditional["high"][index]),
                "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
                "mechanism": MechanismFamily.BSV_PUMP_ENSEMBLE.value,
            }
        )

    csv_path = output_dir / "proxy_hhg_spectrum.csv"
    summary_path = output_dir / "proxy_hhg_summary.json"
    manifest_path = output_dir / "manifest.yaml"
    write_csv(
        csv_path,
        rows,
        [
            "harmonic_order",
            "mean_intensity",
            "std_intensity",
            "conditional_low",
            "conditional_middle",
            "conditional_high",
            "claim_level",
            "mechanism",
        ],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mechanism": MechanismFamily.BSV_PUMP_ENSEMBLE.value,
            "mean_cutoff_order": float(np.mean(cutoff_orders)),
            "std_cutoff_order": float(np.std(cutoff_orders, ddof=1)) if shots > 1 else 0.0,
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mechanism": MechanismFamily.BSV_PUMP_ENSEMBLE.value,
            "code_entrypoint": "stochastic_em_theory.ensemble.run_proxy_hhg_ensemble",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "proxy_hhg_intensity_spectrum",
            "units": "atomic units for fields and energies; dimensionless harmonic order",
            "notes": "Fast cutoff-weighted HHG proxy used for ensemble-pipeline development, not TDSE publication result.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
