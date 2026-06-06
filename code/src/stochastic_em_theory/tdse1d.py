from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]
ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class SoftCoreGrid:
    x: FloatArray
    k: FloatArray
    dx: float

    @classmethod
    def create(cls, *, x_min: float, x_max: float, points: int) -> "SoftCoreGrid":
        if points < 8:
            raise ValueError("points must be at least 8")
        if x_max <= x_min:
            raise ValueError("x_max must be greater than x_min")
        x = np.linspace(x_min, x_max, points, dtype=np.float64)
        dx = float(x[1] - x[0])
        k = 2.0 * np.pi * np.fft.fftfreq(points, d=dx)
        return cls(x=x, k=k.astype(np.float64), dx=dx)


def soft_core_potential(x: FloatArray, *, softening: float) -> FloatArray:
    if softening <= 0:
        raise ValueError("softening must be positive")
    return (-1.0 / np.sqrt(x**2 + softening**2)).astype(np.float64)


def gaussian_wavepacket(x: FloatArray, *, width: float) -> ComplexArray:
    if width <= 0:
        raise ValueError("width must be positive")
    return np.exp(-0.5 * (x / width) ** 2).astype(np.complex128)


def normalize_wavefunction(psi: ComplexArray, dx: float) -> ComplexArray:
    norm = np.sqrt(float(np.sum(np.abs(psi) ** 2) * dx))
    if norm <= 0:
        raise ValueError("wavefunction norm must be positive")
    return (psi / norm).astype(np.complex128)


def split_operator_step(
    *,
    psi: ComplexArray,
    grid: SoftCoreGrid,
    potential: FloatArray,
    field_au: float,
    dt_au: float,
) -> ComplexArray:
    if dt_au <= 0:
        raise ValueError("dt_au must be positive")
    if psi.shape != grid.x.shape or potential.shape != grid.x.shape:
        raise ValueError("psi, potential, and grid.x must have matching shape")

    interaction = potential + grid.x * field_au
    half_potential_phase = np.exp(-0.5j * interaction * dt_au)
    kinetic_phase = np.exp(-0.5j * grid.k**2 * dt_au)
    psi_half = half_potential_phase * psi
    psi_k = np.fft.fft(psi_half)
    psi_after_k = np.fft.ifft(kinetic_phase * psi_k)
    return (half_potential_phase * psi_after_k).astype(np.complex128)


def acceleration_expectation(
    *,
    psi: ComplexArray,
    grid: SoftCoreGrid,
    potential: FloatArray,
    field_au: float,
) -> float:
    if psi.shape != grid.x.shape or potential.shape != grid.x.shape:
        raise ValueError("psi, potential, and grid.x must have matching shape")
    density = np.abs(psi) ** 2
    d_v_dx = np.gradient(potential, grid.dx, edge_order=2)
    acceleration_density = -(d_v_dx + field_au) * density
    return float(np.sum(acceleration_density) * grid.dx)


def acceleration_spectrum(acceleration: FloatArray, *, dt_au: float) -> tuple[FloatArray, FloatArray]:
    if acceleration.ndim != 1:
        raise ValueError("acceleration must be one-dimensional")
    if dt_au <= 0:
        raise ValueError("dt_au must be positive")
    window = np.hanning(acceleration.size)
    spectrum = np.fft.rfft(acceleration * window)
    angular_frequency = 2.0 * np.pi * np.fft.rfftfreq(acceleration.size, d=dt_au)
    return angular_frequency.astype(np.float64), (np.abs(spectrum) ** 2).astype(np.float64)
