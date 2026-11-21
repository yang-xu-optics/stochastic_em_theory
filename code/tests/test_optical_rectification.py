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


def _pump_ladder_basis(bins: int, photons: int) -> list[tuple[int, ...]]:
    """All occupation tuples of `photons` photons in `bins` frequency bins."""

    if bins == 1:
        return [(photons,)]
    states: list[tuple[int, ...]] = []
    for first in range(photons + 1):
        states.extend((first, *rest) for rest in _pump_ladder_basis(bins - 1, photons - first))
    return states


@pytest.mark.parametrize(("coupling_time", "bins"), [(0.3, 13), (0.6, 15)])
def test_rectification_is_an_exact_displacement_by_the_flux_operator(coupling_time: float, bins: int) -> None:
    """Beyond first order: b_out = b_in - i zeta N holds exactly.

    Frequency-bin model H = g (b^dagger N + b N^dagger), N = sum_j a_j^dagger a_{j+1},
    two pump photons in a three-bin wave packet at the centre of a ladder of
    frequency bins, evolved with a full matrix exponential. The relation is exact
    while the edge bins stay empty, because [N, N^dagger] = n_first - n_last.
    A scan (9, 13, 17 bins at coupling 0.6) gave residuals 3e-4, 1e-6, 3e-9,
    equal to the edge-bin population times a number of order one and
    independent of the THz cutoff.
    """

    from scipy.linalg import expm

    photons, thz_cutoff = 2, 26
    basis = _pump_ladder_basis(bins, photons)
    index = {state: k for k, state in enumerate(basis)}
    flux = np.zeros((len(basis), len(basis)))
    for state, column in index.items():
        for j in range(bins - 1):
            if state[j + 1] == 0:
                continue
            moved = list(state)
            amplitude = np.sqrt(state[j + 1] * (state[j] + 1))
            moved[j + 1] -= 1
            moved[j] += 1
            flux[index[tuple(moved)], column] += amplitude

    centre = bins // 2
    weights = {centre - 1: 0.5, centre: 1.0, centre + 1: 0.5j}
    pump = np.zeros(len(basis), dtype=np.complex128)
    for state, k in index.items():
        occupied = [j for j, n in enumerate(state) for _ in range(n)]
        if all(j in weights for j in occupied):
            amplitude = weights[occupied[0]] * weights[occupied[1]]
            pump[k] = amplitude * (np.sqrt(2.0) if occupied[0] == occupied[1] else 2.0) / np.sqrt(2.0)
    pump /= np.linalg.norm(pump)

    b = _ladder(thz_cutoff)
    hamiltonian = np.kron(flux, b.T) + np.kron(flux.T, b)
    vacuum = np.zeros(thz_cutoff)
    vacuum[0] = 1.0
    state_out = expm(-1j * coupling_time * hamiltonian) @ np.kron(pump, vacuum)

    b_full = np.kron(np.eye(len(basis)), b)
    flux_full = np.kron(flux, np.eye(thz_cutoff))
    mean_field = np.vdot(state_out, b_full @ state_out)
    thz_photons = np.vdot(state_out, b_full.T @ b_full @ state_out).real
    mean_flux = np.vdot(pump, flux @ pump)
    flux_second = np.vdot(flux @ pump, flux @ pump).real

    assert abs(mean_flux) > 0.3  # the wave packet has a pulsed mean intensity
    # Tolerance 1e-6: the finite ladder leaves residuals below 1e-7 for these
    # sizes. A relation valid only to first order would be off by terms of
    # relative order coupling_time^2, i.e. several percent here.
    assert mean_field == pytest.approx(-1j * coupling_time * mean_flux, abs=1e-6)
    assert thz_photons == pytest.approx(coupling_time**2 * flux_second, rel=1e-6)
    # the flux itself is a constant of the motion
    assert np.vdot(state_out, flux_full @ state_out) == pytest.approx(mean_flux, abs=1e-6)


@pytest.mark.parametrize(("coupling_time", "bins", "tolerance"), [(0.3, 13, 1e-8), (0.6, 15, 1e-6)])
def test_pump_is_phase_modulated_by_the_mean_of_input_and_output_thz_fields(
    coupling_time: float, bins: int, tolerance: float
) -> None:
    """a_out(tau) = exp(-i [F_in(tau) + F_out(tau)] / 2) a_in(tau), same ladder model.

    With F_out - F_in = 2 int dtau' I(tau') S(tau' - tau) and S(x) = (g t)^2 sin x,
    the output coherence of a pump with two photons in the wave packet phi is

        G(t1, t2) = 2 phi*(t1) phi(t2) exp[-i S(t1 - t2)] exp[-(g t)^2 (1 - cos(t1 - t2))]
                    * int dt' |phi(t')|^2 exp{i [S(t' - t1) - S(t' - t2)]}.

    Compared with <a_j^dagger a_k> from the full matrix exponential. Leaving out
    the flux-dependent phase (the int I S term) changes the result by 0.03 and
    0.09 for the two couplings, so the tolerance tests that term.
    """

    from scipy.linalg import expm

    thz_cutoff = 26
    basis = _pump_ladder_basis(bins, 2)
    index = {state: k for k, state in enumerate(basis)}

    def hop(j: int, k: int) -> np.ndarray:
        matrix = np.zeros((len(basis), len(basis)))
        for state, column in index.items():
            if state[k] == 0:
                continue
            moved = list(state)
            amplitude = np.sqrt(moved[k])
            moved[k] -= 1
            amplitude *= np.sqrt(moved[j] + 1)
            moved[j] += 1
            matrix[index[tuple(moved)], column] += amplitude
        return matrix

    flux = sum(hop(j, j + 1) for j in range(bins - 1))
    centre = bins // 2
    weights = {centre - 1: 0.5, centre: 1.0, centre + 1: 0.5j}
    norm = np.sqrt(sum(abs(value) ** 2 for value in weights.values()))
    weights = {j: value / norm for j, value in weights.items()}
    pump = np.zeros(len(basis), dtype=np.complex128)
    for state, k in index.items():
        occupied = [j for j, n in enumerate(state) for _ in range(n)]
        if all(j in weights for j in occupied):
            pump[k] = weights[occupied[0]] * weights[occupied[1]] * (1.0 if occupied[0] == occupied[1] else np.sqrt(2.0))
    assert np.linalg.norm(pump) == pytest.approx(1.0, abs=1e-12)

    b = _ladder(thz_cutoff)
    hamiltonian = np.kron(flux, b.T) + np.kron(flux.T, b)
    vacuum = np.zeros(thz_cutoff)
    vacuum[0] = 1.0
    state_out = expm(-1j * coupling_time * hamiltonian) @ np.kron(pump, vacuum)
    identity = np.eye(thz_cutoff)
    exact = np.array(
        [[np.vdot(state_out, np.kron(hop(j, k), identity) @ state_out) for k in range(bins)] for j in range(bins)]
    )

    points = 256
    tau = 2.0 * np.pi * np.arange(points) / points
    dtau = 2.0 * np.pi / points
    phi = sum(value * np.exp(-1j * j * tau) for j, value in weights.items()) / np.sqrt(2.0 * np.pi)
    lag = tau[:, None] - tau[None, :]  # t1 - t2, also used as t - t'
    back_action = np.exp(-1j * coupling_time**2 * np.sin(lag))  # exp[i S(t' - t)] as a matrix in (t, t')
    inner = (back_action * np.abs(phi)[None, :] ** 2) @ back_action.conj().T * dtau
    coherence = (
        2.0
        * np.conj(phi)[:, None]
        * phi[None, :]
        * inner
        * np.exp(-1j * coupling_time**2 * np.sin(lag))
        * np.exp(-(coupling_time**2) * (1.0 - np.cos(lag)))
    )
    mode = np.arange(bins)[:, None] * tau[None, :]
    predicted = (np.exp(-1j * mode) @ coherence @ np.exp(1j * mode).T) * dtau**2 / (2.0 * np.pi)

    assert np.abs(exact - predicted).max() < tolerance
    # photon number is conserved and the mean frequency drops by one bin per THz photon
    assert np.trace(exact).real == pytest.approx(2.0, abs=1e-9)
    thz_photons = np.vdot(state_out, np.kron(np.eye(len(basis)), b.T @ b) @ state_out).real
    shift = float(np.sum(np.arange(bins) * np.diag(exact).real)) - float(
        np.sum([j * 2.0 * abs(value) ** 2 for j, value in weights.items()])
    )
    assert shift == pytest.approx(-thz_photons, abs=1e-9)


def test_evolution_with_phase_mismatch_is_displacement_times_flux_phase() -> None:
    """U = exp(i Phi) D for a z-dependent generator, same ladder model.

    G(z) = g (exp(-i dk z) b^dagger N + h.c.); the z-ordered evolution is
    computed exactly as exp(i H0 L) exp(-i (H0 + V) L) with H0 = -dk b^dagger b.
    Prediction: D = exp{-i (zeta b^dagger N + h.c.)},
    zeta = g L exp(-i dk L / 2) sinc(dk L / 2), and Phi = -phi N^dagger N,
    phi = g^2 (dk L - sin dk L) / dk^2. The state-vector distance is 2e-5 for
    15 bins (1e-4 for 13, 4e-6 for 17: the ladder edge again) and 0.30 when
    the flux phase Phi is left out.
    """

    from scipy.linalg import expm

    coupling, length, mismatch, bins, thz_cutoff = 1.0, 0.6, 4.0, 15, 26
    basis = _pump_ladder_basis(bins, 2)
    index = {state: k for k, state in enumerate(basis)}
    flux = np.zeros((len(basis), len(basis)))
    for state, column in index.items():
        for j in range(bins - 1):
            if state[j + 1] == 0:
                continue
            moved = list(state)
            amplitude = np.sqrt(state[j + 1] * (state[j] + 1))
            moved[j + 1] -= 1
            moved[j] += 1
            flux[index[tuple(moved)], column] += amplitude

    centre = bins // 2
    weights = {centre - 1: 0.5, centre: 1.0, centre + 1: 0.5j}
    pump = np.zeros(len(basis), dtype=np.complex128)
    for state, k in index.items():
        occupied = [j for j, n in enumerate(state) for _ in range(n)]
        if all(j in weights for j in occupied):
            pump[k] = weights[occupied[0]] * weights[occupied[1]] * (1.0 if occupied[0] == occupied[1] else np.sqrt(2.0))
    pump /= np.linalg.norm(pump)

    b = _ladder(thz_cutoff)
    interaction = coupling * (np.kron(flux, b.T) + np.kron(flux.T, b))
    free = -mismatch * np.kron(np.eye(len(basis)), b.T @ b)
    vacuum = np.zeros(thz_cutoff)
    vacuum[0] = 1.0
    state_in = np.kron(pump, vacuum)
    exact = expm(1j * free * length) @ (expm(-1j * (free + interaction) * length) @ state_in)

    half = 0.5 * mismatch * length
    zeta = coupling * length * np.exp(-1j * half) * np.sin(half) / half
    phi = coupling**2 * (mismatch * length - np.sin(mismatch * length)) / mismatch**2
    displaced = expm(-1j * (zeta * np.kron(flux, b.T) + np.conj(zeta) * np.kron(flux.T, b))) @ state_in
    flux_phase = expm(-1j * phi * np.kron(flux.T @ flux, np.eye(thz_cutoff)))

    assert np.linalg.norm(exact - flux_phase @ displaced) < 1e-4
    assert np.linalg.norm(exact - displaced) > 0.1


def test_off_shell_phase_reduces_to_the_propagation_form_plus_a_kerr_term() -> None:
    """Frequency-domain form of the flux phase (paper/theory-note/derivation-frequency-domain).

    Phi = int dOmega' N^dagger N C(Omega'), with
    C(Omega') = 2 pi P int_0^inf dOmega |g(Omega, Omega')|^2 / (Omega - Omega')  (+ the Omega' < 0 term),
    |g|^2 = kappa^2 (L / 2 pi)^2 sinc^2(delta L / 2), delta = k_T(Omega) - Omega' / v_g.

    (1) With kappa^2 on the energy shell the principal value is elementary:
        P int du sinc^2((u + dk) L / 2) / u = -(2 pi / L^2) (dk L - sin dk L) / dk^2,
        which gives C = -phi, the phase of the propagation picture.
    (2) With kappa^2 = Omega and a dispersionless THz index (units n_T / c = 1,
        1 / v_g = 1 - eps), the full coefficient is -phi + L: the extra term is
        the instantaneous Kerr-type phase. Units: frequency 1, length c / n_T.
    """

    def sinc_squared(x: np.ndarray | float) -> np.ndarray | float:
        return np.sinc(np.asarray(x) / np.pi) ** 2

    for length, mismatch in [(2.0, 1.3), (5.0, -0.4)]:
        # symmetric midpoint grid without a point at u = 0: the principal value by symmetry
        step = 2.0e-3 / length
        u = (np.arange(-200_000, 200_000) + 0.5) * step
        principal_value = float(np.sum(sinc_squared((u + mismatch) * length / 2.0) / u) * step)
        closed_form = -(2.0 * np.pi / length**2) * (mismatch * length - np.sin(mismatch * length)) / mismatch**2
        assert principal_value == pytest.approx(closed_form, abs=2e-4)

    length, eps, shell = 100.0, 0.05, 1.0
    omega = np.linspace(0.0, shell + 8000.0 / length, 1_000_001)
    coupling = omega * (length / (2.0 * np.pi)) ** 2 * sinc_squared((omega - shell * (1.0 - eps)) * length / 2.0)
    on_shell = shell * (length / (2.0 * np.pi)) ** 2 * float(sinc_squared(shell * eps * length / 2.0))
    detuning = omega - shell
    with np.errstate(divide="ignore", invalid="ignore"):
        regular = np.where(np.abs(detuning) > 1e-12, (coupling - on_shell) / detuning, 0.0)
    pole = int(np.argmin(np.abs(detuning)))
    regular[pole] = 0.5 * (regular[pole - 1] + regular[pole + 1])
    rotating = 2.0 * np.pi * (np.trapezoid(regular, omega) + on_shell * np.log((omega[-1] - shell) / shell))
    counter = omega * (length / (2.0 * np.pi)) ** 2 * sinc_squared((omega + shell * (1.0 - eps)) * length / 2.0)
    counter_rotating = 2.0 * np.pi * np.trapezoid(counter / (omega + shell), omega)

    dk = eps * shell
    phi = shell * (dk * length - np.sin(dk * length)) / dk**2
    assert rotating + counter_rotating == pytest.approx(-phi + length, abs=0.05)
    assert abs(counter_rotating) < 0.5  # does not grow with the crystal length
    assert abs(rotating - (-phi)) > 50.0  # the Kerr-type term is not small in absolute size
