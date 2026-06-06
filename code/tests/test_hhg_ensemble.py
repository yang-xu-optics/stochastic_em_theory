import csv
import json

import yaml

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.ensemble import run_proxy_hhg_ensemble
from stochastic_em_theory.mechanisms import MechanismFamily
from stochastic_em_theory.source_models import single_mode_source


def test_proxy_hhg_ensemble_writes_labeled_outputs_and_shot_records(tmp_path) -> None:
    source_model = single_mode_source(r=0.8, label="test_single_mode")
    result = run_proxy_hhg_ensemble(
        r=0.8,
        phase=0.0,
        shots=64,
        seed=42,
        base_field_amplitude_au=0.035,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=21,
        output_dir=tmp_path,
        source_model=source_model,
    )

    shot_records_path = tmp_path / "shot_records.csv"
    assert result.csv_path.exists()
    assert result.summary_path.exists()
    assert result.manifest_path.exists()
    assert shot_records_path.exists()

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 11
    assert all(float(row["mean_intensity"]) >= 0.0 for row in rows)
    assert all(row["claim_level"] == ClaimLevel.HHG_INTENSITY_PREDICTION.value for row in rows)
    assert all(row["mechanism"] == MechanismFamily.BSV_PUMP_ENSEMBLE.value for row in rows)

    with shot_records_path.open(newline="") as handle:
        shot_rows = list(csv.DictReader(handle))

    assert len(shot_rows) == 64
    assert shot_rows[0]["source_model_kind"] == "single_mode"
    assert shot_rows[0]["source_model_label"] == "test_single_mode"
    assert shot_rows[0]["mechanism"] == MechanismFamily.BSV_PUMP_ENSEMBLE.value
    assert float(shot_rows[0]["ionization_rate_proxy"]) >= 0.0

    expected_parameters = {
        "r": 0.8,
        "phase": 0.0,
        "shots": 64,
        "seed": 42,
        "base_field_amplitude_au": 0.035,
        "omega_au": 0.057,
        "ionization_potential_au": 0.7924,
        "max_order": 21,
        "driver_sampling": "single_mode_husimi_q",
        "field_normalization": "field_amplitude = base_field_amplitude_au * sqrt(|alpha|^2 / mean(|alpha|^2))",
    }

    summary = json.loads(result.summary_path.read_text())
    assert summary["parameters"] == expected_parameters
    assert summary["source_model"]["kind"] == "single_mode"
    assert summary["source_model"]["label"] == "test_single_mode"
    assert set(summary["conditional_bin_counts"]) == {"low", "middle", "high"}
    assert sum(summary["conditional_bin_counts"].values()) == 64
    assert all(count > 0 for count in summary["conditional_bin_counts"].values())

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["claim_level"] == ClaimLevel.HHG_INTENSITY_PREDICTION.value
    assert manifest["mechanism"] == MechanismFamily.BSV_PUMP_ENSEMBLE.value
    assert manifest["random_seeds"] == [42]
    assert manifest["source_model"]["kind"] == "single_mode"
    assert manifest["source_model"]["label"] == "test_single_mode"
    assert manifest["parameters"] == expected_parameters
