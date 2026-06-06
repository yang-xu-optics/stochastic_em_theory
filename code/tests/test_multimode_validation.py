import csv

import numpy as np
import yaml

from stochastic_em_theory.fields import sample_multimode_wigner
from stochastic_em_theory.observables import analytic_equal_mode_g2, estimate_total_photon_moments
from stochastic_em_theory.validation import run_multimode_validation


def test_equal_mode_g2_formula_matches_single_mode_limit() -> None:
    r = 0.9
    assert np.isclose(analytic_equal_mode_g2(r=r, modes=1), 3.0 + 1.0 / (np.sinh(r) ** 2))


def test_multimode_estimator_matches_equal_mode_target() -> None:
    rng = np.random.default_rng(99)
    r = 0.75
    modes = 4
    alpha = sample_multimode_wigner(r=r, modes=modes, shots=180_000, rng=rng)

    estimate = estimate_total_photon_moments(alpha)

    assert np.isclose(estimate.g2_corrected, analytic_equal_mode_g2(r=r, modes=modes), rtol=0.08)
    assert estimate.mode_count == modes


def test_multimode_validation_writes_mode_count_csv(tmp_path) -> None:
    result = run_multimode_validation(
        r=0.7,
        mode_counts=[1, 2, 5],
        shots=70_000,
        seed=321,
        output_dir=tmp_path,
    )

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert [int(row["modes"]) for row in rows] == [1, 2, 5]
    assert float(rows[0]["analytic_g2"]) > float(rows[-1]["analytic_g2"])

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["mechanism"] == "bsv_pump_ensemble"
    assert manifest["source_model"] == "equal_mode"
