from __future__ import annotations

import numpy as np
import pytest

from stochastic_em_theory.thz_waveform_noise import (
    FWHM_TO_RMS,
    analytic_noise_coefficients,
    coherence_time_for_temporal_modes,
    exact_variance,
    fit_noise_templates,
    gaussian_schell_covariance,
    model_response_matrix,
    sample_photon_flux,
    temporal_mode_number,
    waveform_noise,
)

T_RMS = 100.0 * FWHM_TO_RMS
T_PUMP = np.arange(-220.0, 220.0 + 1e-9, 4.0)
T_THZ = np.arange(-800.0, 800.0 + 1e-9, 10.0)
RESPONSE = model_response_matrix(T_THZ, T_PUMP)


@pytest.mark.parametrize("modes", [1.0, 2.0, 5.0])
def test_discretized_covariance_has_the_requested_temporal_mode_number(modes: float) -> None:
    covariance = gaussian_schell_covariance(T_PUMP, rms_duration=T_RMS, temporal_modes=modes)
    assert temporal_mode_number(covariance) == pytest.approx(modes, rel=2e-3)
    assert covariance[T_PUMP.size // 2, T_PUMP.size // 2] == pytest.approx(1.0)


def test_coherence_time_is_infinite_for_one_mode_and_finite_otherwise() -> None:
    assert np.isinf(coherence_time_for_temporal_modes(rms_duration=T_RMS, temporal_modes=1.0))
    assert coherence_time_for_temporal_modes(rms_duration=T_RMS, temporal_modes=2.0) == pytest.approx(
        2.0 * T_RMS / np.sqrt(3.0)
    )


@pytest.mark.parametrize(("spatial", "temporal"), [(10, 1.0), (5, 2.0), (2, 5.0)])
def test_sampled_moments_match_closed_forms(spatial: int, temporal: float) -> None:
    rng = np.random.default_rng(3)
    covariance = gaussian_schell_covariance(T_PUMP, rms_duration=T_RMS, temporal_modes=temporal)
    flux = sample_photon_flux(covariance, spatial_modes=spatial, shots=40_000, rng=rng)
    noise = waveform_noise(flux, RESPONSE, T_PUMP)
    a, b = analytic_noise_coefficients(rms_duration=T_RMS, temporal_modes=temporal, spatial_modes=spatial)
    assert a == pytest.approx(0.2)
    assert noise.number_coefficient == pytest.approx(a, rel=0.04)
    if temporal == 1.0:
        assert b == 0.0
        assert noise.timing_coefficient < 1e-12 * T_RMS**2
    else:
        assert noise.timing_coefficient == pytest.approx(b, rel=0.05)
    assert abs(noise.cross_coefficient) < 0.03 * np.sqrt(a * max(b, 1.0))


def test_sampled_variance_matches_exact_double_integral() -> None:
    rng = np.random.default_rng(4)
    covariance = gaussian_schell_covariance(T_PUMP, rms_duration=T_RMS, temporal_modes=2.0)
    flux = sample_photon_flux(covariance, spatial_modes=5, shots=60_000, rng=rng)
    noise = waveform_noise(flux, RESPONSE, T_PUMP)
    exact = exact_variance(RESPONSE, covariance, dt_pump=4.0, spatial_modes=5)
    strong = exact > 0.05 * exact.max()
    assert np.allclose(noise.variance[strong], exact[strong], rtol=0.06)


def test_single_temporal_mode_noise_is_proportional_to_the_mean_field() -> None:
    covariance = gaussian_schell_covariance(T_PUMP, rms_duration=T_RMS, temporal_modes=1.0)
    exact = exact_variance(RESPONSE, covariance, dt_pump=4.0, spatial_modes=10)
    mean = RESPONSE @ np.diag(covariance) * 4.0
    assert np.allclose(exact, 0.2 * mean**2, rtol=1e-9, atol=1e-12 * exact.max())
    node = int(np.argmin(np.abs(mean[60:100]))) + 60
    assert exact[node] < 1e-6 * exact.max()


def test_template_fit_recovers_number_and_timing_coefficients() -> None:
    covariance = gaussian_schell_covariance(T_PUMP, rms_duration=T_RMS, temporal_modes=2.0)
    exact = exact_variance(RESPONSE, covariance, dt_pump=4.0, spatial_modes=5)
    mean = RESPONSE @ np.diag(covariance) * 4.0
    mean_number = float(np.diag(covariance).sum() * 4.0)
    a_fit, b_fit, c_fit = fit_noise_templates(mean, exact, dt_thz=10.0, mean_photon_number=mean_number)
    a, b = analytic_noise_coefficients(rms_duration=T_RMS, temporal_modes=2.0, spatial_modes=5)
    assert a_fit == pytest.approx(a, rel=0.05)
    assert b_fit == pytest.approx(b, rel=0.15)
    assert abs(c_fit) < 0.02 * np.sqrt(a * b)


def test_thermal_light_has_half_the_variance_of_bsv() -> None:
    covariance = gaussian_schell_covariance(T_PUMP, rms_duration=T_RMS, temporal_modes=2.0)
    bsv = exact_variance(RESPONSE, covariance, dt_pump=4.0, spatial_modes=5)
    thermal = exact_variance(RESPONSE, covariance, dt_pump=4.0, spatial_modes=5, statistics="thermal")
    assert np.allclose(thermal, 0.5 * bsv)
    rng = np.random.default_rng(8)
    flux = sample_photon_flux(covariance, spatial_modes=5, shots=40_000, rng=rng, statistics="thermal")
    noise = waveform_noise(flux, RESPONSE, T_PUMP)
    assert noise.number_coefficient == pytest.approx(0.1, rel=0.05)
