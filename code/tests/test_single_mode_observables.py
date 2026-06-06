import numpy as np

from stochastic_em_theory.fields import sample_single_mode_husimi_q, sample_single_mode_wigner
from stochastic_em_theory.observables import (
    analytic_single_mode_g2,
    analytic_single_mode_wigner_abs_moments,
    estimate_single_mode_moments,
    normal_moments_from_wigner_abs_moments,
)


def test_ordering_correction_recovers_exact_g2_from_analytic_wigner_moments() -> None:
    r = 0.8
    abs2_w, abs4_w = analytic_single_mode_wigner_abs_moments(r)

    n_est, factorial2_est = normal_moments_from_wigner_abs_moments(abs2_w, abs4_w)

    expected_n = np.sinh(r) ** 2
    expected_g2 = analytic_single_mode_g2(r)
    assert np.isclose(n_est, expected_n)
    assert np.isclose(factorial2_est / n_est**2, expected_g2)


def test_wigner_sampler_reproducible_statistics() -> None:
    rng = np.random.default_rng(12345)
    r = 0.7
    alpha = sample_single_mode_wigner(r=r, phase=0.25, shots=250_000, rng=rng)

    estimate = estimate_single_mode_moments(alpha)

    assert np.isclose(estimate.n_corrected, np.sinh(r) ** 2, rtol=0.035, atol=0.01)
    assert np.isclose(estimate.g2_corrected, analytic_single_mode_g2(r), rtol=0.08)
    assert abs(estimate.g2_naive - estimate.g2_corrected) > 0.2


def test_husimi_q_sampler_has_one_vacuum_photon_of_heterodyne_noise() -> None:
    rng = np.random.default_rng(7)
    alpha = sample_single_mode_husimi_q(r=0.0, phase=0.0, shots=100_000, rng=rng)

    assert np.isclose(np.mean(np.abs(alpha) ** 2), 1.0, rtol=0.025)
