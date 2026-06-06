from stochastic_em_theory.io import write_csv


def test_write_csv_uses_lf_line_endings(tmp_path) -> None:
    csv_path = tmp_path / "values.csv"

    write_csv(csv_path, [{"state": "coherent", "value": 1.0}], ["state", "value"])

    assert csv_path.read_bytes() == b"state,value\ncoherent,1.0\n"
