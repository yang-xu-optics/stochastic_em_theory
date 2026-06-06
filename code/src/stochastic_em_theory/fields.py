from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]
ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class SqueezedMode:
    """Single squeezed optical mode parameters."""

    r: float
    phase: float = 0.0


def _as_generator(rng: np.random.Generator | None) -> np.random.Generator:
    return np.random.default_rng() if rng is None else rng


def sample_single_mode_wigner(
    *,
    r: float,
    phase: float = 0.0,
    shots: int,
    rng: np.random.Generator | None = None,
) -> ComplexArray:
    """Sample a single-mode squeezed-vacuum Wigner distribution.

    The quadrature convention is alpha = (x + i p) / sqrt(2), with vacuum
    Wigner variances Var(x) = Var(p) = 1/2.
    """

    if shots <= 0:
        raise ValueError("shots must be positive")
    if r < 0:
        raise ValueError("r must be non-negative")

    generator = _as_generator(rng)
    x_std = np.sqrt(0.5 * np.exp(-2.0 * r))
    p_std = np.sqrt(0.5 * np.exp(2.0 * r))
    x = generator.normal(loc=0.0, scale=x_std, size=shots)
    p = generator.normal(loc=0.0, scale=p_std, size=shots)
    rotation = np.exp(0.5j * phase)
    return (rotation * (x + 1j * p) / np.sqrt(2.0)).astype(np.complex128)


def sample_single_mode_husimi_q(
    *,
    r: float,
    phase: float = 0.0,
    shots: int,
    rng: np.random.Generator | None = None,
) -> ComplexArray:
    """Sample the single-mode squeezed-vacuum Husimi-Q coherent amplitudes.

    Relative to Wigner sampling, the Q distribution adds heterodyne vacuum
    noise, so a vacuum mode has <|alpha|^2>_Q = 1.
    """

    if shots <= 0:
        raise ValueError("shots must be positive")
    if r < 0:
        raise ValueError("r must be non-negative")

    generator = _as_generator(rng)
    x_std = np.sqrt(0.5 * np.exp(-2.0 * r) + 0.5)
    p_std = np.sqrt(0.5 * np.exp(2.0 * r) + 0.5)
    x = generator.normal(loc=0.0, scale=x_std, size=shots)
    p = generator.normal(loc=0.0, scale=p_std, size=shots)
    rotation = np.exp(0.5j * phase)
    return (rotation * (x + 1j * p) / np.sqrt(2.0)).astype(np.complex128)


def sample_multimode_wigner(
    *,
    r: float | FloatArray,
    modes: int,
    shots: int,
    phase: float = 0.0,
    rng: np.random.Generator | None = None,
) -> ComplexArray:
    """Sample independent squeezed Wigner modes with shape (shots, modes)."""

    if modes <= 0:
        raise ValueError("modes must be positive")
    if shots <= 0:
        raise ValueError("shots must be positive")

    r_values = np.broadcast_to(np.asarray(r, dtype=np.float64), (modes,))
    if np.any(r_values < 0):
        raise ValueError("all squeezing parameters must be non-negative")

    generator = _as_generator(rng)
    samples = np.empty((shots, modes), dtype=np.complex128)
    for mode_index, r_value in enumerate(r_values):
        samples[:, mode_index] = sample_single_mode_wigner(
            r=float(r_value),
            phase=phase,
            shots=shots,
            rng=generator,
        )
    return samples
