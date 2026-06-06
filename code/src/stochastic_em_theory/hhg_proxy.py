from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class HHGProxySpectrum:
    orders: FloatArray
    intensity: FloatArray
    cutoff_energy_au: float
    cutoff_order: float


def ponderomotive_energy_au(*, field_amplitude_au: float, omega_au: float) -> float:
    if field_amplitude_au < 0:
        raise ValueError("field_amplitude_au must be non-negative")
    if omega_au <= 0:
        raise ValueError("omega_au must be positive")
    return float(field_amplitude_au**2 / (4.0 * omega_au**2))


def cutoff_energy_au(*, field_amplitude_au: float, omega_au: float, ionization_potential_au: float) -> float:
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    up = ponderomotive_energy_au(field_amplitude_au=field_amplitude_au, omega_au=omega_au)
    return float(ionization_potential_au + 3.17 * up)


def odd_harmonic_orders(*, max_order: int) -> FloatArray:
    if max_order < 1:
        raise ValueError("max_order must be at least 1")
    return np.arange(1, max_order + 1, 2, dtype=np.float64)


def proxy_hhg_spectrum(
    *,
    field_amplitude_au: float,
    omega_au: float,
    ionization_potential_au: float,
    max_order: int,
    nonlinearity_power: float = 6.0,
) -> HHGProxySpectrum:
    """Fast HHG intensity proxy for ensemble and plotting pipeline tests.

    This is not a TDSE result. It encodes three-step cutoff scaling and a
    smooth plateau-to-cutoff envelope for intensity-level pipeline development.
    """

    if nonlinearity_power <= 0:
        raise ValueError("nonlinearity_power must be positive")
    orders = odd_harmonic_orders(max_order=max_order)
    cutoff_energy = cutoff_energy_au(
        field_amplitude_au=field_amplitude_au,
        omega_au=omega_au,
        ionization_potential_au=ionization_potential_au,
    )
    cutoff_order = cutoff_energy / omega_au
    plateau = np.power(max(field_amplitude_au, 0.0), nonlinearity_power)
    rolloff = np.exp(-np.maximum(orders - cutoff_order, 0.0) / max(cutoff_order, 1.0))
    low_order_suppression = 1.0 - np.exp(-orders / 3.0)
    intensity = plateau * rolloff * low_order_suppression
    return HHGProxySpectrum(
        orders=orders,
        intensity=intensity.astype(np.float64),
        cutoff_energy_au=float(cutoff_energy),
        cutoff_order=float(cutoff_order),
    )
