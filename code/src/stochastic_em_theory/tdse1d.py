from __future__ import annotations

from dataclasses import dataclass
from typing import Any

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
        x = np.linspace(x_min, x_max, points, endpoint=False, dtype=np.float64)
        dx = float(x[1] - x[0])
        k = 2.0 * np.pi * np.fft.fftfreq(points, d=dx)
        return cls(x=x, k=k.astype(np.float64), dx=dx)


@dataclass(frozen=True)
class TrapezoidPulse:
    omega_au: float
    field_amplitude_au: float
    ramp_cycles: float
    flat_cycles: float
    carrier_phase: float = 0.0

    def __post_init__(self) -> None:
        if self.omega_au <= 0:
            raise ValueError("omega_au must be positive")
        if self.field_amplitude_au < 0:
            raise ValueError("field_amplitude_au must be non-negative")
        if self.ramp_cycles <= 0:
            raise ValueError("ramp_cycles must be positive")
        if self.flat_cycles < 0:
            raise ValueError("flat_cycles must be non-negative")

    @property
    def period_au(self) -> float:
        return float(2.0 * np.pi / self.omega_au)

    @property
    def ramp_time_au(self) -> float:
        return float(self.ramp_cycles * self.period_au)

    @property
    def flat_time_au(self) -> float:
        return float(self.flat_cycles * self.period_au)

    @property
    def total_time_au(self) -> float:
        return float((2.0 * self.ramp_cycles + self.flat_cycles) * self.period_au)

    def envelope(self, time_au: float | FloatArray) -> float | FloatArray:
        t = np.asarray(time_au, dtype=np.float64)
        env = np.zeros_like(t, dtype=np.float64)
        ramp = self.ramp_time_au
        flat_end = ramp + self.flat_time_au
        total = self.total_time_au

        rising = (t >= 0.0) & (t < ramp)
        flat = (t >= ramp) & (t <= flat_end)
        falling = (t > flat_end) & (t <= total)

        env[rising] = t[rising] / ramp
        env[flat] = 1.0
        env[falling] = (total - t[falling]) / ramp
        env = np.clip(env, 0.0, 1.0)
        if np.isscalar(time_au):
            return float(env)
        return env.astype(np.float64)

    def field(self, time_au: float | FloatArray) -> float | FloatArray:
        value = self.field_amplitude_au * self.envelope(time_au) * np.sin(self.omega_au * time_au + self.carrier_phase)
        if np.isscalar(time_au):
            return float(value)
        return np.asarray(value, dtype=np.float64)


@dataclass(frozen=True)
class TDSEHarmonicSpectrum:
    orders: FloatArray
    intensity: FloatArray
    angular_frequency: FloatArray
    raw_power: FloatArray
    metadata: dict[str, Any]


def soft_core_potential(x: FloatArray, *, softening: float) -> FloatArray:
    if softening <= 0:
        raise ValueError("softening must be positive")
    return (-1.0 / np.sqrt(x**2 + softening**2)).astype(np.float64)


def complex_absorbing_potential(
    x: FloatArray,
    *,
    absorption_start_au: float,
    strength: float = 5.0e-4,
) -> ComplexArray:
    if absorption_start_au <= 0:
        raise ValueError("absorption_start_au must be positive")
    if strength < 0:
        raise ValueError("strength must be non-negative")
    distance = np.maximum(np.abs(x) - absorption_start_au, 0.0)
    return (-1j * strength * distance**3).astype(np.complex128)


def gaussian_wavepacket(x: FloatArray, *, width: float) -> ComplexArray:
    if width <= 0:
        raise ValueError("width must be positive")
    return np.exp(-0.5 * (x / width) ** 2).astype(np.complex128)


def normalize_wavefunction(psi: ComplexArray, dx: float) -> ComplexArray:
    if dx <= 0:
        raise ValueError("dx must be positive")
    norm = np.sqrt(float(np.sum(np.abs(psi) ** 2) * dx))
    if norm <= 0:
        raise ValueError("wavefunction norm must be positive")
    return (psi / norm).astype(np.complex128)


def imaginary_time_ground_state(
    *,
    grid: SoftCoreGrid,
    potential: FloatArray,
    steps: int,
    dt_au: float,
    initial_width: float = 2.0,
) -> ComplexArray:
    if steps <= 0:
        raise ValueError("steps must be positive")
    if dt_au <= 0:
        raise ValueError("dt_au must be positive")
    if potential.shape != grid.x.shape:
        raise ValueError("potential and grid.x must have matching shape")

    psi = normalize_wavefunction(gaussian_wavepacket(grid.x, width=initial_width), grid.dx)
    half_potential_decay = np.exp(-0.5 * potential * dt_au)
    kinetic_decay = np.exp(-0.5 * grid.k**2 * dt_au)
    for _ in range(steps):
        psi = half_potential_decay * psi
        psi_k = np.fft.fft(psi)
        psi = np.fft.ifft(kinetic_decay * psi_k)
        psi = half_potential_decay * psi
        psi = normalize_wavefunction(psi.astype(np.complex128), grid.dx)
    return psi.astype(np.complex128)


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


def tdse_acceleration_trace(
    *,
    field_amplitude_au: float,
    omega_au: float,
    x_min: float,
    x_max: float,
    grid_points: int,
    softening: float,
    dt_au: float,
    ramp_cycles: float,
    flat_cycles: float,
    ground_state_iterations: int,
    ground_state_dt_au: float,
    carrier_phase: float = 0.0,
    absorber_start_au: float | None = 75.0,
    absorber_strength: float = 5.0e-4,
) -> tuple[FloatArray, FloatArray, dict[str, Any]]:
    if field_amplitude_au < 0:
        raise ValueError("field_amplitude_au must be non-negative")

    grid = SoftCoreGrid.create(x_min=x_min, x_max=x_max, points=grid_points)
    potential = soft_core_potential(grid.x, softening=softening)
    absorber = (
        complex_absorbing_potential(
            grid.x,
            absorption_start_au=absorber_start_au,
            strength=absorber_strength,
        )
        if absorber_start_au is not None
        else np.zeros_like(grid.x, dtype=np.complex128)
    )
    propagation_potential = potential.astype(np.complex128) + absorber
    psi = imaginary_time_ground_state(
        grid=grid,
        potential=potential,
        steps=ground_state_iterations,
        dt_au=ground_state_dt_au,
    )
    pulse = TrapezoidPulse(
        omega_au=omega_au,
        field_amplitude_au=field_amplitude_au,
        ramp_cycles=ramp_cycles,
        flat_cycles=flat_cycles,
        carrier_phase=carrier_phase,
    )

    steps = int(np.ceil(pulse.total_time_au / dt_au)) + 1
    time = (np.arange(steps, dtype=np.float64) * dt_au).astype(np.float64)
    acceleration = np.empty(steps, dtype=np.float64)
    for index, t_au in enumerate(time):
        field_au = pulse.field(float(t_au))
        acceleration[index] = acceleration_expectation(
            psi=psi,
            grid=grid,
            potential=potential,
            field_au=field_au,
        )
        psi = split_operator_step(
            psi=psi,
            grid=grid,
            potential=propagation_potential,
            field_au=field_au,
            dt_au=dt_au,
        )

    metadata = {
        "spectrum_model": "tdse_dipole_acceleration",
        "field_amplitude_au": float(field_amplitude_au),
        "omega_au": float(omega_au),
        "x_min": float(x_min),
        "x_max": float(x_max),
        "grid_points": int(grid_points),
        "dx_au": float(grid.dx),
        "softening": float(softening),
        "dt_au": float(dt_au),
        "ramp_cycles": float(ramp_cycles),
        "flat_cycles": float(flat_cycles),
        "total_time_au": float(pulse.total_time_au),
        "time_steps": int(steps),
        "ground_state_iterations": int(ground_state_iterations),
        "ground_state_dt_au": float(ground_state_dt_au),
        "carrier_phase": float(carrier_phase),
        "absorber_start_au": None if absorber_start_au is None else float(absorber_start_au),
        "absorber_strength": float(absorber_strength),
    }
    return time, acceleration.astype(np.float64), metadata


def tdse_harmonic_spectrum(
    *,
    field_amplitude_au: float,
    omega_au: float,
    max_order: int,
    x_min: float = -100.0,
    x_max: float = 100.0,
    grid_points: int = 1024,
    softening: float = 0.8160,
    dt_au: float = 0.08,
    ramp_cycles: float = 1.0,
    flat_cycles: float = 2.0,
    ground_state_iterations: int = 160,
    ground_state_dt_au: float = 0.08,
    carrier_phase: float = 0.0,
    absorber_start_au: float | None = 75.0,
    absorber_strength: float = 5.0e-4,
) -> TDSEHarmonicSpectrum:
    if max_order < 1:
        raise ValueError("max_order must be at least 1")
    if omega_au <= 0:
        raise ValueError("omega_au must be positive")

    _, acceleration, metadata = tdse_acceleration_trace(
        field_amplitude_au=field_amplitude_au,
        omega_au=omega_au,
        x_min=x_min,
        x_max=x_max,
        grid_points=grid_points,
        softening=softening,
        dt_au=dt_au,
        ramp_cycles=ramp_cycles,
        flat_cycles=flat_cycles,
        ground_state_iterations=ground_state_iterations,
        ground_state_dt_au=ground_state_dt_au,
        carrier_phase=carrier_phase,
        absorber_start_au=absorber_start_au,
        absorber_strength=absorber_strength,
    )
    angular_frequency, raw_power = acceleration_spectrum(acceleration, dt_au=dt_au)
    raw_orders = angular_frequency / omega_au
    orders = np.arange(1, max_order + 1, 2, dtype=np.float64)
    intensity = np.interp(orders, raw_orders, raw_power, left=0.0, right=0.0)
    return TDSEHarmonicSpectrum(
        orders=orders.astype(np.float64),
        intensity=intensity.astype(np.float64),
        angular_frequency=angular_frequency.astype(np.float64),
        raw_power=raw_power.astype(np.float64),
        metadata=metadata,
    )
