from __future__ import annotations

import numpy as np


def keldysh_parameter(*, field_amplitude_au: float, omega_au: float, ionization_potential_au: float) -> float:
    if field_amplitude_au <= 0:
        raise ValueError("field_amplitude_au must be positive")
    if omega_au <= 0:
        raise ValueError("omega_au must be positive")
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    return float(omega_au * np.sqrt(2.0 * ionization_potential_au) / field_amplitude_au)


def adk_like_rate_au(*, field_amplitude_au: float, ionization_potential_au: float) -> float:
    """Monotone ADK-like tunneling-rate proxy for per-shot diagnostics.

    This proxy is used to rank and bin shots. It is not a quantitative ADK
    implementation and must not be cited as an ionization model.
    """

    if field_amplitude_au <= 0:
        raise ValueError("field_amplitude_au must be positive")
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    exponent = -2.0 * (2.0 * ionization_potential_au) ** 1.5 / (3.0 * field_amplitude_au)
    prefactor = field_amplitude_au**2
    return float(prefactor * np.exp(exponent))
