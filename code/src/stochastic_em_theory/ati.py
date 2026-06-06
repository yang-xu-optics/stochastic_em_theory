from __future__ import annotations

from datetime import date
from enum import Enum
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

from stochastic_em_theory.ionization import adk_like_rate_au
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.mechanisms import MechanismFamily


FloatArray = NDArray[np.float64]


class PhotonStatisticsKind(str, Enum):
    COHERENT = "coherent"
    THERMAL = "thermal"
    BSV = "bsv"


def sample_matched_intensities(
    *,
    kind: PhotonStatisticsKind | str,
    mean_intensity: float,
    shots: int,
    rng: np.random.Generator | None = None,
) -> FloatArray:
    if mean_intensity <= 0:
        raise ValueError("mean_intensity must be positive")
    if shots <= 0:
        raise ValueError("shots must be positive")

    generator = np.random.default_rng() if rng is None else rng
    statistics = PhotonStatisticsKind(kind)
    if statistics is PhotonStatisticsKind.COHERENT:
        samples = np.full(shots, mean_intensity, dtype=np.float64)
    elif statistics is PhotonStatisticsKind.THERMAL:
        samples = generator.exponential(scale=mean_intensity, size=shots)
    elif statistics is PhotonStatisticsKind.BSV:
        samples = generator.gamma(shape=0.5, scale=2.0 * mean_intensity, size=shots)
    else:
        raise ValueError(f"unsupported photon statistics {kind}")
    return samples.astype(np.float64)


def estimate_intensity_g2(intensity: FloatArray) -> float:
    if intensity.ndim != 1 or intensity.size == 0:
        raise ValueError("intensity must be a non-empty one-dimensional array")
    mean_intensity = float(np.mean(intensity))
    if mean_intensity <= 0:
        raise ValueError("mean intensity must be positive")
    return float(np.mean(intensity**2) / mean_intensity**2)


def _electron_number_bunching_proxy(rates: FloatArray) -> float:
    mean_rate = float(np.mean(rates))
    if mean_rate <= 0:
        raise ValueError("mean ionization-rate proxy must be positive")
    return float(np.mean(rates**2) / mean_rate**2)


def run_ati_statistics_benchmark(
    *,
    mean_field_amplitude_au: float,
    ionization_potential_au: float,
    shots: int,
    seed: int,
    output_dir: Path,
) -> RunArtifacts:
    if mean_field_amplitude_au <= 0:
        raise ValueError("mean_field_amplitude_au must be positive")
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    if shots <= 0:
        raise ValueError("shots must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    mean_intensity = mean_field_amplitude_au**2
    rows: list[dict[str, float | int | str]] = []

    for statistics in (PhotonStatisticsKind.COHERENT, PhotonStatisticsKind.THERMAL, PhotonStatisticsKind.BSV):
        intensity = sample_matched_intensities(
            kind=statistics,
            mean_intensity=mean_intensity,
            shots=shots,
            rng=rng,
        )
        field_amplitudes = np.sqrt(np.maximum(intensity, 1.0e-30))
        rates = np.asarray(
            [
                adk_like_rate_au(
                    field_amplitude_au=float(field_amplitude),
                    ionization_potential_au=ionization_potential_au,
                )
                for field_amplitude in field_amplitudes
            ],
            dtype=np.float64,
        )
        rows.append(
            {
                "statistics": statistics.value,
                "shots": int(shots),
                "mean_intensity": float(np.mean(intensity)),
                "estimated_g2": estimate_intensity_g2(intensity),
                "mean_ionization_rate_proxy": float(np.mean(rates)),
                "electron_number_bunching_proxy": _electron_number_bunching_proxy(rates),
                "mechanism": MechanismFamily.ATI_PHOTON_STATISTICS.value,
            }
        )

    coherent_rate = float(rows[0]["mean_ionization_rate_proxy"])
    if coherent_rate <= 0:
        raise ValueError("coherent ionization-rate proxy must be positive")
    for row in rows:
        row["ionization_yield_enhancement"] = float(row["mean_ionization_rate_proxy"]) / coherent_rate

    csv_path = output_dir / "ati_statistics.csv"
    summary_path = output_dir / "ati_statistics_summary.json"
    manifest_path = output_dir / "manifest.yaml"
    write_csv(
        csv_path,
        rows,
        [
            "statistics",
            "shots",
            "mean_intensity",
            "estimated_g2",
            "mean_ionization_rate_proxy",
            "ionization_yield_enhancement",
            "electron_number_bunching_proxy",
            "mechanism",
        ],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "mechanism": MechanismFamily.ATI_PHOTON_STATISTICS.value,
            "mean_field_amplitude_au": mean_field_amplitude_au,
            "ionization_potential_au": ionization_potential_au,
            "shots": shots,
            "mean_intensity_target": mean_intensity,
            "statistics_order": [row["statistics"] for row in rows],
            "g2_order": [row["estimated_g2"] for row in rows],
            "ionization_yield_enhancement_order": [row["ionization_yield_enhancement"] for row in rows],
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": "validated_stochastic_simulation",
            "mechanism": MechanismFamily.ATI_PHOTON_STATISTICS.value,
            "source_model": "matched_coherent_thermal_bsv_intensity_statistics",
            "code_entrypoint": "stochastic_em_theory.ati.run_ati_statistics_benchmark",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "ati_ionization_rate_proxy_and_electron_number_bunching",
            "units": "atomic units for field amplitude and ionization potential",
            "notes": "Diagonal coherent-component averaging proxy inspired by Lyu 2025; not a quantitative qSFA momentum solver.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
