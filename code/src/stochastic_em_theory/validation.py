from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np

from stochastic_em_theory.fields import sample_multimode_wigner, sample_single_mode_wigner
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.observables import (
    analytic_equal_mode_g2,
    analytic_single_mode_g2,
    analytic_single_mode_n,
    estimate_total_photon_moments,
    estimate_single_mode_moments,
)
from stochastic_em_theory.source_models import (
    SourceModelSpec,
    effective_mode_count,
    equal_mode_source,
    single_mode_source,
)


def _batched_standard_error(
    values: np.ndarray,
    statistic,
    *,
    max_batches: int = 64,
) -> float:
    if values.shape[0] < 2:
        return 0.0

    batch_count = min(max_batches, max(2, values.shape[0] // 1_000), values.shape[0])
    if batch_count < 2:
        return 0.0
    batch_size = values.shape[0] // batch_count
    usable = batch_count * batch_size
    if usable < 2:
        return 0.0

    batch_values = values[:usable].reshape((batch_count, batch_size, *values.shape[1:]))
    estimates = np.asarray([statistic(batch) for batch in batch_values], dtype=np.float64)
    return float(np.std(estimates, ddof=1) / np.sqrt(batch_count))


def _single_mode_n_from_intensity(intensity: np.ndarray) -> float:
    return float(np.mean(intensity) - 0.5)


def _single_mode_corrected_g2_from_intensity(intensity: np.ndarray) -> float:
    abs2_w = float(np.mean(intensity))
    abs4_w = float(np.mean(intensity**2))
    n = abs2_w - 0.5
    if n <= 0:
        return float("nan")
    factorial2 = abs4_w - 2.0 * abs2_w + 0.5
    return float(factorial2 / n**2)


def _single_mode_naive_g2_from_intensity(intensity: np.ndarray) -> float:
    abs2_w = float(np.mean(intensity))
    if abs2_w <= 0:
        return float("nan")
    abs4_w = float(np.mean(intensity**2))
    return float(abs4_w / abs2_w**2)


def _source_model_summary(source_model: SourceModelSpec) -> dict[str, object]:
    return {
        "kind": source_model.kind.value,
        "label": source_model.label,
        "effective_mode_count": effective_mode_count(source_model),
        "mode_weights": [
            {"label": mode.label, "nbar": mode.nbar, "weight": mode.weight}
            for mode in source_model.mode_weights
        ],
        "source_refs": list(source_model.source_refs),
        "notes": source_model.notes,
    }


def run_single_mode_validation(
    *,
    r_values: list[float],
    shots: int,
    seed: int,
    output_dir: Path,
) -> RunArtifacts:
    if not r_values:
        raise ValueError("r_values must contain at least one squeezing parameter")
    if shots <= 0:
        raise ValueError("shots must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    rows: list[dict[str, float | int]] = []

    for r in r_values:
        alpha = sample_single_mode_wigner(r=r, shots=shots, rng=rng)
        estimate = estimate_single_mode_moments(alpha)
        intensity = np.abs(alpha) ** 2
        rows.append(
            {
                "r": float(r),
                "shots": int(shots),
                "analytic_n": analytic_single_mode_n(r),
                "estimated_n": estimate.n_corrected,
                "estimated_n_standard_error": _batched_standard_error(
                    intensity,
                    _single_mode_n_from_intensity,
                ),
                "analytic_g2": analytic_single_mode_g2(r),
                "g2_corrected": estimate.g2_corrected,
                "g2_corrected_standard_error": _batched_standard_error(
                    intensity,
                    _single_mode_corrected_g2_from_intensity,
                ),
                "g2_naive": estimate.g2_naive,
                "g2_naive_standard_error": _batched_standard_error(
                    intensity,
                    _single_mode_naive_g2_from_intensity,
                ),
                "abs2_wigner": estimate.abs2_wigner,
                "abs4_wigner": estimate.abs4_wigner,
            }
        )

    csv_path = output_dir / "single_mode_g2.csv"
    summary_path = output_dir / "single_mode_summary.json"
    manifest_path = output_dir / "manifest.yaml"
    source_models = [
        single_mode_source(r=float(r), label=f"single_mode_r_{float(r):g}")
        for r in r_values
    ]

    write_csv(
        csv_path,
        rows,
        [
            "r",
            "shots",
            "analytic_n",
            "estimated_n",
            "estimated_n_standard_error",
            "analytic_g2",
            "g2_corrected",
            "g2_corrected_standard_error",
            "g2_naive",
            "g2_naive_standard_error",
            "abs2_wigner",
            "abs4_wigner",
        ],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "claim_level": "exact_input_correspondence",
            "mechanism": "bsv_pump_ensemble",
            "source_model": "single_mode",
            "source_model_summary": [_source_model_summary(source_model) for source_model in source_models],
            "max_abs_g2_error": max(abs(float(row["g2_corrected"]) - float(row["analytic_g2"])) for row in rows),
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": "exact_input_correspondence",
            "mechanism": "bsv_pump_ensemble",
            "source_model": "single_mode",
            "source_model_summary": [_source_model_summary(source_model) for source_model in source_models],
            "code_entrypoint": "stochastic_em_theory.validation.run_single_mode_validation",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "single_mode_squeezed_vacuum_g2",
            "units": "dimensionless oscillator units",
            "notes": "Wigner samples converted to normally ordered photon-counting observables.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)


def run_multimode_validation(
    *,
    r: float,
    mode_counts: list[int],
    shots: int,
    seed: int,
    output_dir: Path,
) -> RunArtifacts:
    if not mode_counts:
        raise ValueError("mode_counts must contain at least one mode count")
    if shots <= 0:
        raise ValueError("shots must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    rows: list[dict[str, float | int]] = []

    for modes in mode_counts:
        alpha = sample_multimode_wigner(r=r, modes=modes, shots=shots, rng=rng)
        estimate = estimate_total_photon_moments(alpha)
        rows.append(
            {
                "r": float(r),
                "modes": int(modes),
                "shots": int(shots),
                "analytic_g2": analytic_equal_mode_g2(r=r, modes=modes),
                "g2_corrected": estimate.g2_corrected,
                "g2_corrected_standard_error": _batched_standard_error(
                    alpha,
                    lambda batch: estimate_total_photon_moments(batch).g2_corrected,
                ),
                "n_total_corrected": estimate.n_total_corrected,
                "n_total_standard_error": _batched_standard_error(
                    alpha,
                    lambda batch: estimate_total_photon_moments(batch).n_total_corrected,
                ),
            }
        )

    csv_path = output_dir / "multimode_g2.csv"
    summary_path = output_dir / "multimode_summary.json"
    manifest_path = output_dir / "manifest.yaml"

    write_csv(
        csv_path,
        rows,
        [
            "r",
            "modes",
            "shots",
            "analytic_g2",
            "g2_corrected",
            "g2_corrected_standard_error",
            "n_total_corrected",
            "n_total_standard_error",
        ],
    )
    source_models = [equal_mode_source(r=r, modes=modes) for modes in mode_counts]
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "claim_level": "exact_input_correspondence",
            "mechanism": "bsv_pump_ensemble",
            "source_model": "equal_mode",
            "source_model_summary": [_source_model_summary(source_model) for source_model in source_models],
            "max_abs_g2_error": max(abs(float(row["g2_corrected"]) - float(row["analytic_g2"])) for row in rows),
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": "exact_input_correspondence",
            "mechanism": "bsv_pump_ensemble",
            "source_model": "equal_mode",
            "source_model_summary": [_source_model_summary(source_model) for source_model in source_models],
            "code_entrypoint": "stochastic_em_theory.validation.run_multimode_validation",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "mode_filtered_squeezed_vacuum_g2",
            "units": "dimensionless oscillator units",
            "notes": "Independent equal squeezed modes with normally ordered total photon-counting estimator.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
