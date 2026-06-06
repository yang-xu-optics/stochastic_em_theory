from stochastic_em_theory.mechanisms import MechanismFamily, mechanism_manifest_value


def test_mechanism_values_are_manifest_strings() -> None:
    assert MechanismFamily.BSV_PUMP_ENSEMBLE.value == "bsv_pump_ensemble"
    assert MechanismFamily.ATI_PHOTON_STATISTICS.value == "ati_photon_statistics"
    assert (
        MechanismFamily.SQUEEZED_EMISSION_MODE_ENVIRONMENT.value
        == "squeezed_emission_mode_environment"
    )


def test_mechanism_manifest_value_accepts_enum_or_string() -> None:
    assert mechanism_manifest_value(MechanismFamily.BSV_PUMP_ENSEMBLE) == "bsv_pump_ensemble"
    assert mechanism_manifest_value("custom_boundary_check") == "custom_boundary_check"
