import csv
import json

import numpy as np
import yaml

from stochastic_em_theory.ati import PhotonStatisticsKind, estimate_intensity_g2, run_ati_statistics_benchmark, sample_matched_intensities
from stochastic_em_theory.mechanisms import MechanismFamily


def test_matched_intensity_samples_reproduce_g2_hierarchy() -> None:
    rng = np.random.default_rng(2026)
    shots = 240_000
    mean_intensity = 1.0

    coherent = sample_matched_intensities(
        kind=PhotonStatisticsKind.COHERENT,
        mean_intensity=mean_intensity,
        shots=shots,
        rng=rng,
    )
    thermal = sample_matched_intensities(
        kind=PhotonStatisticsKind.THERMAL,
        mean_intensity=mean_intensity,
        shots=shots,
        rng=rng,
    )
    bsv = sample_matched_intensities(
        kind=PhotonStatisticsKind.BSV,
        mean_intensity=mean_intensity,
        shots=shots,
        rng=rng,
    )

    assert np.isclose(estimate_intensity_g2(coherent), 1.0, rtol=0.01)
    assert np.isclose(estimate_intensity_g2(thermal), 2.0, rtol=0.04)
    assert np.isclose(estimate_intensity_g2(bsv), 3.0, rtol=0.06)


def test_ati_statistics_benchmark_writes_manifest_and_rows(tmp_path) -> None:
    result = run_ati_statistics_benchmark(
        mean_field_amplitude_au=0.035,
        ionization_potential_au=0.7924,
        shots=80_000,
        seed=44,
        output_dir=tmp_path,
    )

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert [row["statistics"] for row in rows] == ["coherent", "thermal", "bsv"]
    assert float(rows[0]["estimated_g2"]) < float(rows[1]["estimated_g2"]) < float(rows[2]["estimated_g2"])
    assert all("ionization_yield_enhancement" in row for row in rows)
    assert np.isclose(float(rows[0]["ionization_yield_enhancement"]), 1.0)
    assert float(rows[1]["ionization_yield_enhancement"]) > 0.0
    assert float(rows[2]["ionization_yield_enhancement"]) > float(rows[1]["ionization_yield_enhancement"])
    assert all(row["mechanism"] == MechanismFamily.ATI_PHOTON_STATISTICS.value for row in rows)

    summary = json.loads(result.summary_path.read_text())
    assert summary["mean_field_amplitude_au"] == 0.035
    assert summary["ionization_potential_au"] == 0.7924
    assert summary["shots"] == 80_000
    assert summary["mean_intensity_target"] == 0.035**2
    assert summary["ionization_yield_enhancement_order"] == [
        float(row["ionization_yield_enhancement"]) for row in rows
    ]

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["mechanism"] == MechanismFamily.ATI_PHOTON_STATISTICS.value
    assert manifest["random_seeds"] == [44]
