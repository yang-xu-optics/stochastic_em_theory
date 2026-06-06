from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np

from stochastic_em_theory.fields import sample_single_mode_wigner
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.observables import (
    analytic_single_mode_g2,
    analytic_single_mode_n,
    estimate_single_mode_moments,
)


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
        rows.append(
            {
                "r": float(r),
                "shots": int(shots),
                "analytic_n": analytic_single_mode_n(r),
                "estimated_n": estimate.n_corrected,
                "analytic_g2": analytic_single_mode_g2(r),
                "g2_corrected": estimate.g2_corrected,
                "g2_naive": estimate.g2_naive,
                "abs2_wigner": estimate.abs2_wigner,
                "abs4_wigner": estimate.abs4_wigner,
            }
        )

    csv_path = output_dir / "single_mode_g2.csv"
    summary_path = output_dir / "single_mode_summary.json"
    manifest_path = output_dir / "manifest.yaml"

    write_csv(
        csv_path,
        rows,
        [
            "r",
            "shots",
            "analytic_n",
            "estimated_n",
            "analytic_g2",
            "g2_corrected",
            "g2_naive",
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
