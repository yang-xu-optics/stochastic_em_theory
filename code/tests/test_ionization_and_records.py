import numpy as np

from stochastic_em_theory.ionization import adk_like_rate_au, keldysh_parameter
from stochastic_em_theory.mechanisms import MechanismFamily
from stochastic_em_theory.shot_records import HHGShotRecord, shot_records_to_rows


def test_keldysh_parameter_decreases_with_field_strength() -> None:
    weak = keldysh_parameter(field_amplitude_au=0.03, omega_au=0.057, ionization_potential_au=0.7924)
    strong = keldysh_parameter(field_amplitude_au=0.06, omega_au=0.057, ionization_potential_au=0.7924)

    assert strong < weak


def test_adk_like_rate_increases_with_field_strength() -> None:
    weak = adk_like_rate_au(field_amplitude_au=0.03, ionization_potential_au=0.7924)
    strong = adk_like_rate_au(field_amplitude_au=0.06, ionization_potential_au=0.7924)

    assert strong > weak
    assert weak > 0.0


def test_shot_records_convert_to_csv_rows() -> None:
    records = [
        HHGShotRecord(
            shot_index=0,
            source_model_kind="single_mode",
            source_model_label="paper_one",
            mechanism=MechanismFamily.BSV_PUMP_ENSEMBLE.value,
            driver_x=0.1,
            driver_p=-0.2,
            driver_intensity=0.05,
            driver_phase=-1.1,
            field_amplitude_au=0.04,
            ionization_rate_proxy=1.0e-4,
            cutoff_order=21.0,
            harmonic_phase_proxy=0.3,
        )
    ]

    rows = shot_records_to_rows(records)

    assert rows[0]["source_model_kind"] == "single_mode"
    assert rows[0]["mechanism"] == "bsv_pump_ensemble"
    assert np.isclose(float(rows[0]["cutoff_order"]), 21.0)
