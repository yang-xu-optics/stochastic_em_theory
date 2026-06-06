from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.fields import sample_single_mode_husimi_q
from stochastic_em_theory.hhg_proxy import proxy_hhg_spectrum
from stochastic_em_theory.ionization import adk_like_rate_au
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.mechanisms import MechanismFamily
from stochastic_em_theory.shot_records import HHGShotRecord, shot_records_to_rows
from stochastic_em_theory.source_models import SourceModelSpec, single_mode_source


FIELD_NORMALIZATION = "field_amplitude = base_field_amplitude_au * sqrt(|alpha|^2 / mean(|alpha|^2))"


def _conditional_statistics(values: np.ndarray, spectra: np.ndarray) -> tuple[dict[str, np.ndarray], dict[str, int]]:
    quantiles = np.quantile(values, [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    bins: dict[str, np.ndarray] = {}
    counts: dict[str, int] = {}
    labels = ["low", "middle", "high"]
    for index, label in enumerate(labels):
        left = quantiles[index]
        right = quantiles[index + 1]
        if index == len(labels) - 1:
            mask = (values >= left) & (values <= right)
        else:
            mask = (values >= left) & (values < right)
        counts[label] = int(np.count_nonzero(mask))
        if not np.any(mask):
            bins[label] = np.zeros(spectra.shape[1], dtype=np.float64)
        else:
            bins[label] = np.mean(spectra[mask], axis=0)
    return bins, counts


def _source_model_manifest(source_model: SourceModelSpec) -> dict[str, object]:
    return {
        "kind": source_model.kind.value,
        "label": source_model.label,
        "mode_weights": [
            {"label": mode.label, "nbar": mode.nbar, "weight": mode.weight}
            for mode in source_model.mode_weights
        ],
        "source_refs": list(source_model.source_refs),
        "notes": source_model.notes,
    }


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
    source_model: SourceModelSpec | None = None,
) -> RunArtifacts:
    if shots <= 0:
        raise ValueError("shots must be positive")
    if base_field_amplitude_au <= 0:
        raise ValueError("base_field_amplitude_au must be positive")

    output_dir = ensure_output_dir(output_dir)
    source_model = source_model if source_model is not None else single_mode_source(r=r, label="default_single_mode")
    rng = np.random.default_rng(seed)
    alpha = sample_single_mode_husimi_q(r=r, phase=phase, shots=shots, rng=rng)
    sampled_intensity = np.abs(alpha) ** 2
    normalized_amplitude = np.sqrt(sampled_intensity / max(float(np.mean(sampled_intensity)), 1e-12))
    field_amplitudes = base_field_amplitude_au * normalized_amplitude

    spectra = []
    cutoff_orders = []
    shot_records: list[HHGShotRecord] = []
    orders = None
    for shot_index, (field_amplitude, alpha_value, intensity_value) in enumerate(
        zip(field_amplitudes, alpha, sampled_intensity, strict=True)
    ):
        spectrum = proxy_hhg_spectrum(
            field_amplitude_au=float(field_amplitude),
            omega_au=omega_au,
            ionization_potential_au=ionization_potential_au,
            max_order=max_order,
        )
        orders = spectrum.orders
        spectra.append(spectrum.intensity)
        cutoff_orders.append(spectrum.cutoff_order)
        shot_records.append(
            HHGShotRecord(
                shot_index=shot_index,
                source_model_kind=source_model.kind.value,
                source_model_label=source_model.label,
                mechanism=MechanismFamily.BSV_PUMP_ENSEMBLE.value,
                driver_x=float(np.sqrt(2.0) * np.real(alpha_value)),
                driver_p=float(np.sqrt(2.0) * np.imag(alpha_value)),
                driver_intensity=float(intensity_value),
                driver_phase=float(np.angle(alpha_value)),
                field_amplitude_au=float(field_amplitude),
                ionization_rate_proxy=adk_like_rate_au(
                    field_amplitude_au=max(float(field_amplitude), 1.0e-12),
                    ionization_potential_au=ionization_potential_au,
                ),
                cutoff_order=float(spectrum.cutoff_order),
                harmonic_phase_proxy=float(np.angle(alpha_value)),
            )
        )

    if orders is None:
        raise ValueError("no spectra were generated")

    spectra_array = np.vstack(spectra)
    conditional, conditional_bin_counts = _conditional_statistics(sampled_intensity, spectra_array)
    mean_spectrum = np.mean(spectra_array, axis=0)
    std_spectrum = np.std(spectra_array, axis=0, ddof=1) if shots > 1 else np.zeros_like(mean_spectrum)
    parameters = {
        "r": float(r),
        "phase": float(phase),
        "shots": int(shots),
        "seed": int(seed),
        "base_field_amplitude_au": float(base_field_amplitude_au),
        "omega_au": float(omega_au),
        "ionization_potential_au": float(ionization_potential_au),
        "max_order": int(max_order),
        "driver_sampling": "single_mode_husimi_q",
        "field_normalization": FIELD_NORMALIZATION,
    }

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
    shot_records_path = output_dir / "shot_records.csv"
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
    write_csv(
        shot_records_path,
        shot_records_to_rows(shot_records),
        [
            "shot_index",
            "source_model_kind",
            "source_model_label",
            "mechanism",
            "driver_x",
            "driver_p",
            "driver_intensity",
            "driver_phase",
            "field_amplitude_au",
            "ionization_rate_proxy",
            "cutoff_order",
            "harmonic_phase_proxy",
        ],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "shots": len(shot_records),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mechanism": MechanismFamily.BSV_PUMP_ENSEMBLE.value,
            "source_model": _source_model_manifest(source_model),
            "parameters": parameters,
            "conditional_bin_counts": conditional_bin_counts,
            "mean_cutoff_order": float(np.mean(cutoff_orders)),
            "std_cutoff_order": float(np.std(cutoff_orders, ddof=1)) if shots > 1 else 0.0,
            "mean_ionization_rate_proxy": float(
                np.mean([record.ionization_rate_proxy for record in shot_records])
            ),
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
            "source_model": _source_model_manifest(source_model),
            "parameters": parameters,
            "random_seeds": [seed],
            "observable": "proxy_hhg_intensity_spectrum_with_shot_records",
            "units": "atomic units for fields and energies; dimensionless harmonic order",
            "notes": "Fast cutoff-weighted HHG proxy used for ensemble-pipeline development, not TDSE publication result.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
