import numpy as np
import pytest

from stochastic_em_theory.tdse1d import (
    SoftCoreGrid,
    acceleration_expectation,
    acceleration_spectrum,
    gaussian_wavepacket,
    normalize_wavefunction,
    soft_core_potential,
    split_operator_step,
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
