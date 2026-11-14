"""Optical rectification (OR) of bright squeezed vacuum: THz field statistics.

Model (see wiki/theory/quantum-optical-rectification-of-bsv.md). To first
order in the chi^(2) coupling and for an undepleted pump, the THz output
operator is the vacuum input plus a linear response to the pump photon-flux
operator,

    b_out(Omega) = b_in(Omega) - i zeta(Omega) N(Omega),
    N(Omega) = integral d omega  a^dagger(omega) a(omega + Omega).

With the pump in independent squeezed-vacuum Schmidt modes A_k (mean photon
numbers nbar_k), N(Omega) = sum_kl c_kl(Omega) A_k^dagger A_l, and at THz
frequencies well inside the pump-envelope bandwidth N -> total photon number.
The single-shot THz field amplitude is then proportional to the pump photon
number, so its statistics are those of the photon number.

Everything here is dimensionless: photon numbers, and THz field amplitudes in
units of the amplitude emitted per pump photon.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]
ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class THzFieldStatistics:
    """Statistics of the single-shot THz field amplitude, in per-photon units."""

    mean_photon_number: float
    schmidt_number: float
    cumulants: tuple[float, float, float, float]
    moments: tuple[float, float, float, float]
    mean_field: float
    relative_field_fluctuation: float
    skewness: float
    excess_kurtosis: float
    energy_enhancement_over_coherent: float
    energy_g2: float


def squeezed_vacuum_photon_number_cumulants(nbar: float) -> tuple[float, float, float, float]:
    """First four cumulants of the photon number of single-mode squeezed vacuum.

    From the generating function <z^n> = [1 + nbar (1 - z^2)]^(-1/2).
    """

    if nbar < 0:
        raise ValueError("nbar must be non-negative")
    k1 = nbar
    k2 = 2.0 * nbar * (1.0 + nbar)
    k3 = 4.0 * nbar * (1.0 + nbar) * (1.0 + 2.0 * nbar)
    k4 = 8.0 * nbar * (1.0 + nbar) * (1.0 + 6.0 * nbar + 6.0 * nbar**2)
    return float(k1), float(k2), float(k3), float(k4)


def coherent_photon_number_cumulants(nbar: float) -> tuple[float, float, float, float]:
    """Poisson cumulants: all equal to the mean."""

    if nbar < 0:
        raise ValueError("nbar must be non-negative")
    return float(nbar), float(nbar), float(nbar), float(nbar)


def thermal_photon_number_cumulants(nbar: float) -> tuple[float, float, float, float]:
    """First four cumulants of the Bose-Einstein photon-number distribution."""

    if nbar < 0:
        raise ValueError("nbar must be non-negative")
    k1 = nbar
    k2 = nbar * (1.0 + nbar)
    k3 = nbar * (1.0 + nbar) * (1.0 + 2.0 * nbar)
    k4 = nbar * (1.0 + nbar) * (1.0 + 6.0 * nbar + 6.0 * nbar**2)
    return float(k1), float(k2), float(k3), float(k4)


def moments_from_cumulants(cumulants: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
    """Raw moments <N>, <N^2>, <N^3>, <N^4> from the first four cumulants."""

    k1, k2, k3, k4 = cumulants
    m1 = k1
    m2 = k2 + k1**2
    m3 = k3 + 3.0 * k2 * k1 + k1**3
    m4 = k4 + 4.0 * k3 * k1 + 3.0 * k2**2 + 6.0 * k2 * k1**2 + k1**4
    return float(m1), float(m2), float(m3), float(m4)


def squeezed_vacuum_photon_number_pmf(nbar: float, n_max: int) -> FloatArray:
    """P(n) for n = 0..n_max of single-mode squeezed vacuum (odd n have P = 0)."""

    if nbar < 0:
        raise ValueError("nbar must be non-negative")
    if n_max < 0:
        raise ValueError("n_max must be non-negative")
    pmf = np.zeros(n_max + 1, dtype=np.float64)
    tanh2 = nbar / (1.0 + nbar)
    value = 1.0 / np.sqrt(1.0 + nbar)
    pmf[0] = value
    for pair in range(1, n_max // 2 + 1):
        value *= tanh2 * (2.0 * pair - 1.0) / (2.0 * pair)
        pmf[2 * pair] = value
    return pmf


def schmidt_number(nbars: FloatArray) -> float:
    """Effective mode number K = (sum nbar_k)^2 / sum nbar_k^2."""

    values = np.asarray(nbars, dtype=np.float64)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("nbars must be a non-empty one-dimensional array")
    if np.any(values < 0) or float(np.sum(values)) <= 0.0:
        raise ValueError("nbars must be non-negative with a positive sum")
    return float(np.sum(values) ** 2 / np.sum(values**2))


def _statistics_from_cumulants(
    cumulants: tuple[float, float, float, float], *, schmidt: float
) -> THzFieldStatistics:
    k1, k2, k3, k4 = cumulants
    if k1 <= 0 or k2 <= 0:
        raise ValueError("mean and variance of the photon number must be positive")
    moments = moments_from_cumulants(cumulants)
    coherent_second_moment = k1**2 + k1
    return THzFieldStatistics(
        mean_photon_number=float(k1),
        schmidt_number=float(schmidt),
        cumulants=cumulants,
        moments=moments,
        mean_field=float(k1),
        relative_field_fluctuation=float(np.sqrt(k2) / k1),
        skewness=float(k3 / k2**1.5),
        excess_kurtosis=float(k4 / k2**2),
        energy_enhancement_over_coherent=float(moments[1] / coherent_second_moment),
        energy_g2=float(moments[3] / moments[1] ** 2),
    )


def thz_field_statistics(nbars: FloatArray | float) -> THzFieldStatistics:
    """Exact quantum statistics of the THz amplitude for independent squeezed modes.

    Valid for THz frequencies well inside the pump-envelope bandwidth, where the
    THz amplitude is proportional to the total pump photon number. Cumulants of
    independent modes add.
    """

    values = np.atleast_1d(np.asarray(nbars, dtype=np.float64))
    per_mode = np.array([squeezed_vacuum_photon_number_cumulants(float(v)) for v in values])
    summed = per_mode.sum(axis=0)
    cumulants = (float(summed[0]), float(summed[1]), float(summed[2]), float(summed[3]))
    return _statistics_from_cumulants(cumulants, schmidt=schmidt_number(values))


def bright_limit_statistics(schmidt: float) -> dict[str, float]:
    """Classical-noise (macroscopic) limit for K equal modes.

    The normalized intensity W = N / <N> is Gamma distributed with shape K/2 and
    mean 1, so <W^m> = Gamma(K/2 + m) / [Gamma(K/2) (K/2)^m].
    """

    if schmidt <= 0:
        raise ValueError("schmidt must be positive")
    shape = 0.5 * schmidt
    second = (shape + 1.0) / shape
    fourth = (shape + 1.0) * (shape + 2.0) * (shape + 3.0) / shape**3
    return {
        "relative_field_fluctuation": float(np.sqrt(2.0 / schmidt)),
        "skewness": float(2.0 * np.sqrt(2.0 / schmidt)),
        "excess_kurtosis": float(12.0 / schmidt),
        "energy_enhancement_over_coherent": float(second),
        "energy_g2": float(fourth / second**2),
    }


def flux_second_moment_terms(
    overlap: ComplexArray,
    nbars: FloatArray,
    *,
    anomalous: ComplexArray | None = None,
) -> dict[str, float]:
    """Wick decomposition of <N^dagger(Omega) N(Omega)> for Gaussian pump modes.

    ``overlap[k, l] = c_kl(Omega) = integral psi_k^*(omega) psi_l(omega + Omega)``
    over a mode basis that is complete on the relevant band; modes with
    ``nbars[k] = 0`` are vacuum modes that only receive scattered photons.
    ``anomalous[k] = <A_k A_k>``; by default the pure squeezed-vacuum value with a
    common phase, ``sqrt(nbar_k (nbar_k + 1))``.

    Returns the four contributions:

    - ``coherent``: |sum_k c_kk nbar_k|^2, the square of the mean THz field;
    - ``phase_sensitive``: sum_kl conj(c_kl) c_lk conj(m_l) m_k, present only for
      squeezed light;
    - ``bunching``: sum_kl |c_kl|^2 nbar_l nbar_k, as for thermal light;
    - ``spontaneous``: sum_kl |c_kl|^2 nbar_l, linear in the pump (spontaneous
      difference-frequency generation); absent from any classical-noise model.
    """

    c = np.asarray(overlap, dtype=np.complex128)
    n = np.asarray(nbars, dtype=np.float64)
    if c.ndim != 2 or c.shape[0] != c.shape[1] or c.shape[0] != n.size:
        raise ValueError("overlap must be square with one row per mode in nbars")
    if np.any(n < 0):
        raise ValueError("nbars must be non-negative")
    m = np.sqrt(n * (n + 1.0)).astype(np.complex128) if anomalous is None else np.asarray(anomalous, dtype=np.complex128)
    if m.shape != n.shape:
        raise ValueError("anomalous must have one entry per mode")

    coherent = abs(np.sum(np.diag(c) * n)) ** 2
    phase_sensitive = np.real(np.sum(np.conj(c) * c.T * np.outer(m, np.conj(m))))
    weights = np.abs(c) ** 2
    bunching = float(n @ weights @ n)
    spontaneous = float(np.sum(weights @ n))
    return {
        "coherent": float(coherent),
        "phase_sensitive": float(phase_sensitive),
        "bunching": bunching,
        "spontaneous": spontaneous,
        "total": float(coherent + phase_sensitive + bunching + spontaneous),
    }


def gaussian_mode_overlap_squared(omega_over_sigma: FloatArray | float) -> FloatArray:
    """|c(Omega)|^2 for one Gaussian mode with intensity-spectrum rms width sigma.

    psi(omega) ~ exp[-(omega - omega0)^2 / (4 sigma^2)] gives
    c(Omega) = exp[-Omega^2 / (8 sigma^2)].
    """

    x = np.asarray(omega_over_sigma, dtype=np.float64)
    return np.exp(-(x**2) / 4.0)


def sample_classical_noise_amplitudes(
    *,
    nbars: FloatArray | float,
    shots: int,
    rng: np.random.Generator,
    detection_noise: float = 0.0,
) -> FloatArray:
    """Single-shot THz amplitudes from the classical Gaussian amplitude-noise model.

    Each mode has a real Gaussian amplitude X_k with <X_k^2> = nbar_k (macroscopic
    limit of squeezed vacuum; the squeezed quadrature is neglected). The THz
    amplitude is sum_k X_k^2 plus optional Gaussian detection noise with the
    given standard deviation, in the same per-photon units.
    """

    values = np.atleast_1d(np.asarray(nbars, dtype=np.float64))
    if shots <= 0:
        raise ValueError("shots must be positive")
    if np.any(values < 0):
        raise ValueError("nbars must be non-negative")
    if detection_noise < 0:
        raise ValueError("detection_noise must be non-negative")
    amplitudes = rng.normal(size=(shots, values.size)) * np.sqrt(values)[None, :]
    signal = np.sum(amplitudes**2, axis=1)
    if detection_noise > 0:
        signal = signal + rng.normal(scale=detection_noise, size=shots)
    return signal.astype(np.float64)


def sample_cumulants(samples: FloatArray) -> tuple[float, float, float, float]:
    """Plain sample cumulants (k-statistics are not used; fine for large samples)."""

    x = np.asarray(samples, dtype=np.float64)
    if x.ndim != 1 or x.size < 4:
        raise ValueError("samples must be one-dimensional with at least four entries")
    mean = float(np.mean(x))
    centered = x - mean
    m2 = float(np.mean(centered**2))
    m3 = float(np.mean(centered**3))
    m4 = float(np.mean(centered**4))
    return mean, m2, m3, m4 - 3.0 * m2**2


def schmidt_number_estimates(cumulants: tuple[float, float, float, float]) -> dict[str, float]:
    """Mode-number estimates from THz-amplitude cumulants in the bright limit.

    For K equal modes, k2 = 2 k1^2 / K, k3 = 8 k1^3 / K^2, k4 = 48 k1^4 / K^3.
    The k3 and k4 estimators do not depend on additive Gaussian detection noise.
    """

    k1, k2, k3, k4 = cumulants
    return {
        "from_variance": float(2.0 * k1**2 / k2) if k2 > 0 else float("nan"),
        "from_skewness": float(np.sqrt(8.0 * k1**3 / k3)) if k3 > 0 else float("nan"),
        "from_kurtosis": float(np.cbrt(48.0 * k1**4 / k4)) if k4 > 0 else float("nan"),
    }
