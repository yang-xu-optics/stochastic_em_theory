import numpy as np

from stochastic_em_theory.tdse1d import (
    SoftCoreGrid,
    acceleration_expectation,
    gaussian_wavepacket,
    normalize_wavefunction,
    soft_core_potential,
    split_operator_step,
)


def test_soft_core_potential_is_even_and_negative() -> None:
    grid = SoftCoreGrid.create(x_min=-10.0, x_max=10.0, points=256)
    potential = soft_core_potential(grid.x, softening=0.8160)

    assert np.all(potential < 0.0)
    assert np.isclose(potential[0], potential[-1], rtol=1e-3)


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
