from __future__ import annotations

import numpy as np
import pytest

from stochastic_em_theory.fields import sample_single_mode_husimi_q
from stochastic_em_theory.optical_rectification import (
    bright_limit_statistics,
    flux_second_moment_terms,
    gaussian_mode_overlap_squared,
    moments_from_cumulants,
    sample_classical_noise_amplitudes,
    sample_cumulants,
    schmidt_number,
    schmidt_number_estimates,
    squeezed_vacuum_photon_number_cumulants,
    squeezed_vacuum_photon_number_pmf,
    thermal_photon_number_cumulants,
    thz_field_statistics,
)


@pytest.mark.parametrize("nbar", [0.05, 0.7, 3.0, 12.0])
def test_squeezed_vacuum_cumulants_match_photon_number_distribution(nbar: float) -> None:
    pmf = squeezed_vacuum_photon_number_pmf(nbar, n_max=4000)
    n = np.arange(pmf.size, dtype=np.float64)
    assert np.sum(pmf) == pytest.approx(1.0, abs=1e-10)
    assert np.all(pmf[1::2] == 0.0)
    numeric = tuple(float(np.sum(pmf * n**order)) for order in (1, 2, 3, 4))
    analytic = moments_from_cumulants(squeezed_vacuum_photon_number_cumulants(nbar))
    assert numeric == pytest.approx(analytic, rel=1e-8)


@pytest.mark.parametrize("nbar", [0.2, 1.5, 40.0])
def test_single_mode_moments_have_closed_polynomial_form(nbar: float) -> None:
    m1, m2, _, m4 = moments_from_cumulants(squeezed_vacuum_photon_number_cumulants(nbar))
    assert m1 == pytest.approx(nbar)
    assert m2 == pytest.approx(3 * nbar**2 + 2 * nbar)
    assert m4 == pytest.approx(105 * nbar**4 + 180 * nbar**3 + 84 * nbar**2 + 8 * nbar)


def test_single_mode_statistics_reach_the_bright_limit() -> None:
    stats = thz_field_statistics(1.0e6)
    limit = bright_limit_statistics(1.0)
    assert stats.schmidt_number == pytest.approx(1.0)
    assert stats.energy_enhancement_over_coherent == pytest.approx(3.0, rel=1e-5)
    assert stats.energy_g2 == pytest.approx(35.0 / 3.0, rel=1e-5)
    assert limit["energy_enhancement_over_coherent"] == pytest.approx(3.0)
    assert limit["energy_g2"] == pytest.approx(35.0 / 3.0)
    assert stats.relative_field_fluctuation == pytest.approx(np.sqrt(2.0), rel=1e-5)
    assert stats.skewness == pytest.approx(limit["skewness"], rel=1e-5)
    assert stats.excess_kurtosis == pytest.approx(limit["excess_kurtosis"], rel=1e-5)


def test_single_mode_statistics_have_the_stated_leading_corrections() -> None:
    nbar = 500.0
    stats = thz_field_statistics(nbar)
    assert stats.energy_enhancement_over_coherent == pytest.approx((3 * nbar + 2) / (nbar + 1))
    assert stats.energy_g2 == pytest.approx(35.0 / 3.0 + 40.0 / (9.0 * nbar), rel=1e-4)


def test_weak_squeezing_limit_is_pair_dominated() -> None:
    nbar = 1.0e-4
    stats = thz_field_statistics(nbar)
    assert stats.energy_enhancement_over_coherent == pytest.approx(2.0, rel=1e-3)
    assert stats.energy_g2 == pytest.approx(2.0 / nbar, rel=1e-2)


@pytest.mark.parametrize("modes", [2, 5, 20])
def test_equal_mode_statistics_match_gamma_limit(modes: int) -> None:
    stats = thz_field_statistics(np.full(modes, 1.0e7))
    limit = bright_limit_statistics(float(modes))
    assert stats.schmidt_number == pytest.approx(float(modes))
    for key in ("relative_field_fluctuation", "skewness", "excess_kurtosis", "energy_enhancement_over_coherent", "energy_g2"):
        assert getattr(stats, key) == pytest.approx(limit[key], rel=1e-5)
    assert limit["energy_enhancement_over_coherent"] == pytest.approx(1.0 + 2.0 / modes)


def test_unequal_modes_use_the_schmidt_number_for_the_variance() -> None:
    nbars = np.array([4.0e6, 1.0e6, 2.5e5])
    stats = thz_field_statistics(nbars)
    k = schmidt_number(nbars)
    assert stats.energy_enhancement_over_coherent == pytest.approx(1.0 + 2.0 / k, rel=1e-5)


def test_thermal_cumulants_give_factor_two_and_six() -> None:
    moments = moments_from_cumulants(thermal_photon_number_cumulants(1.0e7))
    assert moments[1] / moments[0] ** 2 == pytest.approx(2.0, rel=1e-5)
    assert moments[3] / moments[1] ** 2 == pytest.approx(6.0, rel=1e-5)


def _ladder(cutoff: int) -> np.ndarray:
    return np.diag(np.sqrt(np.arange(1, cutoff, dtype=np.float64)), k=1)


def _squeezed_vacuum_vector(nbar: float, cutoff: int) -> np.ndarray:
    pmf = squeezed_vacuum_photon_number_pmf(nbar, n_max=cutoff - 1)
    signs = np.where((np.arange(cutoff) // 2) % 2 == 0, 1.0, -1.0)
    return np.sqrt(pmf) * signs


def test_wick_decomposition_matches_two_mode_fock_space_calculation() -> None:
    """Independent check of flux_second_moment_terms against explicit matrices."""

    cutoff = 46
    nbars = np.array([0.30, 0.45])
    rng = np.random.default_rng(7)
    overlap = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))

    a = _ladder(cutoff)
    identity = np.eye(cutoff)
    modes = [np.kron(a, identity), np.kron(identity, a)]
    state = np.kron(_squeezed_vacuum_vector(nbars[0], cutoff), _squeezed_vacuum_vector(nbars[1], cutoff))
    assert np.vdot(state, state).real == pytest.approx(1.0, abs=1e-9)

    flux = sum(overlap[k, l] * modes[k].conj().T @ modes[l] for k in range(2) for l in range(2))
    applied = flux @ state
    exact = float(np.vdot(applied, applied).real)

    terms = flux_second_moment_terms(overlap, nbars)
    assert terms["total"] == pytest.approx(exact, rel=1e-7)
    mean = np.vdot(state, applied)
    assert terms["coherent"] == pytest.approx(abs(mean) ** 2, rel=1e-7)


def test_single_occupied_mode_spectrum_has_a_spontaneous_floor() -> None:
    nbar = 2.0
    c11 = 0.6
    c21 = np.sqrt(1.0 - c11**2)  # completeness: sum_k |c_k1|^2 = 1
    overlap = np.array([[c11, 0.0], [c21, 0.0]], dtype=np.complex128)
    terms = flux_second_moment_terms(overlap, np.array([nbar, 0.0]))
    assert terms["total"] == pytest.approx(c11**2 * (3 * nbar**2 + nbar) + nbar)
    assert terms["spontaneous"] == pytest.approx(nbar)


def test_gaussian_mode_overlap_is_one_at_zero_frequency() -> None:
    assert gaussian_mode_overlap_squared(0.0) == pytest.approx(1.0)
    assert gaussian_mode_overlap_squared(2.0) == pytest.approx(np.exp(-1.0))


def test_classical_noise_sampler_reproduces_bright_limit_cumulants() -> None:
    rng = np.random.default_rng(20261114)
    modes = 3
    samples = sample_classical_noise_amplitudes(nbars=np.full(modes, 1.0), shots=400_000, rng=rng)
    k1, k2, k3, k4 = sample_cumulants(samples)
    assert k1 == pytest.approx(modes, rel=0.01)
    assert k2 == pytest.approx(2.0 * modes, rel=0.02)
    assert k3 == pytest.approx(8.0 * modes, rel=0.05)
    assert k4 == pytest.approx(48.0 * modes, rel=0.12)
    assert np.all(samples >= 0.0)


def test_mode_number_estimators_from_skewness_and_kurtosis_ignore_detection_noise() -> None:
    rng = np.random.default_rng(11)
    modes = 2
    samples = sample_classical_noise_amplitudes(
        nbars=np.full(modes, 1.0), shots=600_000, rng=rng, detection_noise=1.0
    )
    estimates = schmidt_number_estimates(sample_cumulants(samples))
    assert estimates["from_skewness"] == pytest.approx(modes, rel=0.05)
    assert estimates["from_kurtosis"] == pytest.approx(modes, rel=0.08)
    assert estimates["from_variance"] < 0.85 * modes  # biased low by the added noise


def test_husimi_q_mixture_overestimates_thz_energy_by_the_stated_amount() -> None:
    """Approximative phase-space description: Q-weighted coherent drivers.

    A coherent driver |alpha> gives <n^2> = |alpha|^4 + |alpha|^2, so the
    Q-average is 3 nbar^2 + 6 nbar + 3 against the exact 3 nbar^2 + 2 nbar.
    """

    r = 1.2
    nbar = float(np.sinh(r) ** 2)
    rng = np.random.default_rng(5)
    alpha = sample_single_mode_husimi_q(r=r, shots=2_000_000, rng=rng)
    intensity = np.abs(alpha) ** 2
    assert float(np.mean(intensity)) == pytest.approx(nbar + 1.0, rel=5e-3)
    app = float(np.mean(intensity**2 + intensity))
    assert app == pytest.approx(3 * nbar**2 + 6 * nbar + 3, rel=1e-2)
    exact = moments_from_cumulants(squeezed_vacuum_photon_number_cumulants(nbar))[1]
    assert exact == pytest.approx(3 * nbar**2 + 2 * nbar)
    assert app - exact == pytest.approx(4 * nbar + 3, rel=0.08)
