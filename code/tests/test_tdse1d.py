import numpy as np
import pytest

from stochastic_em_theory.tdse1d import (
    SoftCoreGrid,
    TrapezoidPulse,
    acceleration_expectation,
    acceleration_spectrum,
    gaussian_wavepacket,
    normalize_wavefunction,
    soft_core_potential,
    split_operator_step,
    tdse_harmonic_spectrum,
)


def test_soft_core_grid_uses_half_open_fft_domain() -> None:
    grid = SoftCoreGrid.create(x_min=-10.0, x_max=10.0, points=256)

    assert grid.x[0] == -10.0
    assert grid.x[-1] < 10.0
    assert np.isclose(grid.dx, 20.0 / 256.0)


def test_soft_core_potential_is_even_and_negative() -> None:
    x = np.array([-10.0, -2.5, 0.0, 2.5, 10.0], dtype=np.float64)
    potential = soft_core_potential(x, softening=0.8160)

    assert np.all(potential < 0.0)
    assert np.allclose(potential, potential[::-1])


def test_split_operator_conserves_norm_without_field() -> None:
    grid = SoftCoreGrid.create(x_min=-20.0, x_max=20.0, points=512)
    potential = soft_core_potential(grid.x, softening=0.8160)
    psi = gaussian_wavepacket(grid.x, width=2.0)
    psi = normalize_wavefunction(psi, grid.dx)

    for _ in range(20):
        psi = split_operator_step(psi=psi, grid=grid, potential=potential, field_au=0.0, dt_au=0.02)

    norm = np.sum(np.abs(psi) ** 2) * grid.dx
    assert np.isclose(norm, 1.0, atol=2e-10)


def test_even_wavefunction_has_zero_acceleration_without_field() -> None:
    grid = SoftCoreGrid.create(x_min=-20.0, x_max=20.0, points=512)
    potential = soft_core_potential(grid.x, softening=0.8160)
    psi = normalize_wavefunction(gaussian_wavepacket(grid.x, width=2.0), grid.dx)

    acceleration = acceleration_expectation(psi=psi, grid=grid, potential=potential, field_au=0.0)

    assert abs(acceleration) < 1e-12


def test_normalize_wavefunction_rejects_nonpositive_dx() -> None:
    psi = np.array([1.0, 2.0], dtype=np.complex128)

    with pytest.raises(ValueError, match="dx must be positive"):
        normalize_wavefunction(psi, dx=0.0)


def test_acceleration_spectrum_peaks_at_known_angular_frequency() -> None:
    dt_au = 0.05
    points = 256
    expected_bin = 7
    time = np.arange(points, dtype=np.float64) * dt_au
    expected_angular_frequency = 2.0 * np.pi * expected_bin / (points * dt_au)
    acceleration = np.sin(expected_angular_frequency * time)

    angular_frequency, power = acceleration_spectrum(acceleration, dt_au=dt_au)
    peak_index = np.argmax(power[1:]) + 1

    assert np.isclose(angular_frequency[peak_index], expected_angular_frequency)


def test_trapezoid_pulse_has_linear_ramps_and_flat_top() -> None:
    pulse = TrapezoidPulse(
        omega_au=0.5,
        field_amplitude_au=0.2,
        ramp_cycles=1.0,
        flat_cycles=1.0,
        carrier_phase=0.0,
    )
    period = 2.0 * np.pi / 0.5

    assert np.isclose(pulse.envelope(0.0), 0.0)
    assert np.isclose(pulse.envelope(0.5 * period), 0.5)
    assert np.isclose(pulse.envelope(1.25 * period), 1.0)
    assert np.isclose(pulse.envelope(2.5 * period), 0.5)
    assert np.isclose(pulse.envelope(3.0 * period), 0.0)


def test_tdse_harmonic_spectrum_returns_odd_order_dipole_acceleration_power() -> None:
    spectrum = tdse_harmonic_spectrum(
        field_amplitude_au=0.025,
        omega_au=0.4,
        max_order=9,
        x_min=-20.0,
        x_max=20.0,
        grid_points=128,
        softening=0.8160,
        dt_au=0.12,
        ramp_cycles=0.5,
        flat_cycles=0.5,
        ground_state_iterations=30,
        ground_state_dt_au=0.08,
    )

    assert np.array_equal(spectrum.orders, np.array([1.0, 3.0, 5.0, 7.0, 9.0]))
    assert spectrum.intensity.shape == spectrum.orders.shape
    assert np.all(np.isfinite(spectrum.intensity))
    assert np.all(spectrum.intensity >= 0.0)
    assert spectrum.intensity[0] > spectrum.intensity[-1]
    assert spectrum.metadata["spectrum_model"] == "tdse_dipole_acceleration"
