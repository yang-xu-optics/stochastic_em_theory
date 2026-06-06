from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class SingleModeMomentEstimate:
    abs2_wigner: float
    abs4_wigner: float
    n_corrected: float
    factorial2_corrected: float
    g2_corrected: float
    g2_naive: float


@dataclass(frozen=True)
class MultiModeMomentEstimate:
    mode_count: int
    n_total_corrected: float
    factorial2_total_corrected: float
    g2_corrected: float


def analytic_single_mode_n(r: float) -> float:
    if r < 0:
        raise ValueError("r must be non-negative")
    return float(np.sinh(r) ** 2)


def analytic_single_mode_g2(r: float) -> float:
    n = analytic_single_mode_n(r)
    if n <= 0:
        raise ValueError("g2 is singular for squeezed vacuum with zero photons")
    return float(3.0 + 1.0 / n)


def analytic_equal_mode_g2(*, r: float, modes: int) -> float:
    if modes <= 0:
        raise ValueError("modes must be positive")
    n_per_mode = analytic_single_mode_n(r)
    if n_per_mode <= 0:
        raise ValueError("g2 is singular for zero photons per mode")
    return float(1.0 + 2.0 / modes + 1.0 / (modes * n_per_mode))


def analytic_single_mode_wigner_abs_moments(r: float) -> tuple[float, float]:
    n = analytic_single_mode_n(r)
    anomalous_abs2 = n * (n + 1.0)
    abs2_w = n + 0.5
    abs4_w = 2.0 * abs2_w**2 + anomalous_abs2
    return float(abs2_w), float(abs4_w)


def normal_moments_from_wigner_abs_moments(abs2_w: float, abs4_w: float) -> tuple[float, float]:
    n = abs2_w - 0.5
    factorial2 = abs4_w - 2.0 * abs2_w + 0.5
    if n <= 0:
        raise ValueError("normal-ordered photon number must be positive")
    return float(n), float(factorial2)


def estimate_single_mode_moments(alpha: ComplexArray) -> SingleModeMomentEstimate:
    if alpha.ndim != 1:
        raise ValueError("alpha must be a one-dimensional array of mode samples")
    if alpha.size == 0:
        raise ValueError("alpha must contain at least one sample")

    intensity = np.abs(alpha) ** 2
    abs2_w = float(np.mean(intensity))
    abs4_w = float(np.mean(intensity**2))
    n, factorial2 = normal_moments_from_wigner_abs_moments(abs2_w, abs4_w)
    return SingleModeMomentEstimate(
        abs2_wigner=abs2_w,
        abs4_wigner=abs4_w,
        n_corrected=n,
        factorial2_corrected=factorial2,
        g2_corrected=float(factorial2 / n**2),
        g2_naive=float(abs4_w / abs2_w**2),
    )


def estimate_total_photon_moments(alpha: ComplexArray) -> MultiModeMomentEstimate:
    if alpha.ndim != 2:
        raise ValueError("alpha must have shape (shots, modes)")
    if alpha.shape[0] == 0 or alpha.shape[1] == 0:
        raise ValueError("alpha must contain at least one shot and one mode")

    abs2 = np.abs(alpha) ** 2
    normal_n_by_mode = abs2 - 0.5
    factorial2_by_mode = abs2**2 - 2.0 * abs2 + 0.5
    total_n_by_shot = np.sum(normal_n_by_mode, axis=1)
    cross_factorial_by_shot = total_n_by_shot**2 - np.sum(normal_n_by_mode**2, axis=1)
    factorial2_total_by_shot = np.sum(factorial2_by_mode, axis=1) + cross_factorial_by_shot
    n_total = float(np.mean(total_n_by_shot))
    factorial2_total = float(np.mean(factorial2_total_by_shot))
    if n_total <= 0:
        raise ValueError("total corrected photon number must be positive")
    return MultiModeMomentEstimate(
        mode_count=int(alpha.shape[1]),
        n_total_corrected=n_total,
        factorial2_total_corrected=factorial2_total,
        g2_corrected=float(factorial2_total / n_total**2),
    )
