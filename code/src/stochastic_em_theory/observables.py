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


def analytic_single_mode_n(r: float) -> float:
    if r < 0:
        raise ValueError("r must be non-negative")
    return float(np.sinh(r) ** 2)


def analytic_single_mode_g2(r: float) -> float:
    n = analytic_single_mode_n(r)
    if n <= 0:
        raise ValueError("g2 is singular for squeezed vacuum with zero photons")
    return float(3.0 + 1.0 / n)


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
