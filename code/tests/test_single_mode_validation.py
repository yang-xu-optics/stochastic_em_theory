import csv
import json

import yaml

from stochastic_em_theory.validation import run_single_mode_validation


def test_single_mode_validation_writes_csv_summary_and_manifest(tmp_path) -> None:
    result = run_single_mode_validation(
        r_values=[0.4, 0.8],
        shots=60_000,
        seed=123,
        output_dir=tmp_path,
    )

    assert result.csv_path.exists()
    assert result.summary_path.exists()
    assert result.manifest_path.exists()

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert [float(row["r"]) for row in rows] == [0.4, 0.8]
    assert all(float(row["g2_corrected"]) > 3.0 for row in rows)
    assert all(float(row["g2_corrected_standard_error"]) > 0.0 for row in rows)
    assert all(float(row["estimated_n_standard_error"]) > 0.0 for row in rows)
    assert any(abs(float(row["g2_naive"]) - float(row["g2_corrected"])) > 0.15 for row in rows)

    summary = json.loads(result.summary_path.read_text())
    assert summary["rows"] == 2
    assert summary["claim_level"] == "exact_input_correspondence"
    assert summary["mechanism"] == "bsv_pump_ensemble"
    assert summary["source_model"] == "single_mode"
    assert [source["kind"] for source in summary["source_model_summary"]] == ["single_mode", "single_mode"]
    assert all(source["effective_mode_count"] == 1.0 for source in summary["source_model_summary"])

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["random_seeds"] == [123]
    assert manifest["observable"] == "single_mode_squeezed_vacuum_g2"
    assert manifest["claim_level"] == "exact_input_correspondence"
    assert manifest["mechanism"] == "bsv_pump_ensemble"
    assert manifest["source_model"] == "single_mode"
    assert manifest["source_model_summary"][0]["source_refs"]
