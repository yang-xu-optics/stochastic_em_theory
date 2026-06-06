import numpy as np

from stochastic_em_theory.source_models import (
    SourceModelKind,
    effective_mode_count,
    equal_mode_source,
    schmidt_mode_source,
    single_mode_source,
    two_color_twin_beam_source,
)


def test_single_mode_source_has_unit_effective_mode_count() -> None:
    source = single_mode_source(r=0.8)

    assert source.kind == SourceModelKind.SINGLE_MODE
    assert np.isclose(effective_mode_count(source), 1.0)
    assert source.mode_weights[0].label == "mode_0"


def test_equal_mode_source_has_expected_effective_mode_count() -> None:
    source = equal_mode_source(r=0.7, modes=4)

    assert source.kind == SourceModelKind.EQUAL_MODE
    assert np.isclose(effective_mode_count(source), 4.0)
    assert len(source.mode_weights) == 4


def test_schmidt_mode_source_normalizes_brightness_weights() -> None:
    source = schmidt_mode_source(gain=1.2, eigenvalues=[0.7, 0.2, 0.1])

    assert source.kind == SourceModelKind.SCHMIDT_MODE
    assert np.isclose(sum(mode.weight for mode in source.mode_weights), 1.0)
    assert effective_mode_count(source) < 3.0


def test_two_color_source_records_signal_and_idler_modes() -> None:
    source = two_color_twin_beam_source(r=0.9, signal_label="signal", idler_label="idler")

    assert source.kind == SourceModelKind.TWO_COLOR_TWIN_BEAM
    assert [mode.label for mode in source.mode_weights] == ["signal", "idler"]
    assert np.isclose(sum(mode.weight for mode in source.mode_weights), 1.0)
