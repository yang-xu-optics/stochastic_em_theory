"""Shot-to-shot noise of a rectified THz waveform as a function of delay.

Spec: wiki/simulations/thz-waveform-noise-against-delay.md.

Bright (classical-noise) limit: the single-shot THz field is a linear filter
of the pump photon flux, E_j(t) = integral g(t - t') I_j(t') dt'. The pump is a
Gaussian Schell-model pulse with M_s independent spatial modes and K_t
temporal modes. Times are in fs; field and flux are in arbitrary units.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]

FWHM_TO_RMS = 1.0 / (2.0 * np.sqrt(2.0 * np.log(2.0)))


def coherence_time_for_temporal_modes(*, rms_duration: float, temporal_modes: float) -> float:
    """tau_c such that K_t = sqrt(1 + 4 T^2 / tau_c^2). Infinite for K_t = 1."""

    if rms_duration <= 0:
        raise ValueError("rms_duration must be positive")
    if temporal_modes < 1:
        raise ValueError("temporal_modes must be at least 1")
    if temporal_modes == 1:
        return float("inf")
    return float(2.0 * rms_duration / np.sqrt(temporal_modes**2 - 1.0))


def gaussian_schell_covariance(t: FloatArray, *, rms_duration: float, temporal_modes: float) -> FloatArray:
    """Field covariance G1(t1, t2) with unit peak mean intensity."""

    tau_c = coherence_time_for_temporal_modes(rms_duration=rms_duration, temporal_modes=temporal_modes)
    envelope = np.exp(-(t**2) / (4.0 * rms_duration**2))
    difference = t[:, None] - t[None, :]
    coherence = np.ones_like(difference) if np.isinf(tau_c) else np.exp(-(difference**2) / (2.0 * tau_c**2))
    return (envelope[:, None] * envelope[None, :] * coherence).astype(np.float64)


def temporal_mode_number(covariance: FloatArray) -> float:
    """K_t = (trace G1)^2 / sum(G1^2): the Schmidt number of the discretized G1."""

    return float(np.trace(covariance) ** 2 / np.sum(covariance**2))


def sample_photon_flux(
    covariance: FloatArray,
    *,
    spatial_modes: int,
    shots: int,
    rng: np.random.Generator,
    statistics: str = "bsv",
) -> FloatArray:
    """Photon flux I_j(t') summed over spatial modes, shape (shots, n_t).

    ``statistics="bsv"``: real Gaussian field per mode (anti-squeezed quadrature),
    flux X^2. ``"thermal"``: circular complex Gaussian field, flux |Z|^2. Both have
    mean flux G1(t, t); the flux covariance is 2 G1^2 / M_s and G1^2 / M_s.
    """

    if spatial_modes < 1:
        raise ValueError("spatial_modes must be at least 1")
    if shots <= 0:
        raise ValueError("shots must be positive")
    if statistics not in ("bsv", "thermal"):
        raise ValueError("statistics must be 'bsv' or 'thermal'")
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    keep = eigenvalues > eigenvalues.max() * 1.0e-12
    factor = eigenvectors[:, keep] * np.sqrt(eigenvalues[keep] / spatial_modes)[None, :]
    flux = np.zeros((shots, covariance.shape[0]), dtype=np.float64)
    for _ in range(spatial_modes):
        if statistics == "bsv":
            field = rng.normal(size=(shots, factor.shape[1])) @ factor.T
            flux += field**2
        else:
            real = rng.normal(size=(shots, factor.shape[1])) @ factor.T
            imag = rng.normal(size=(shots, factor.shape[1])) @ factor.T
            flux += 0.5 * (real**2 + imag**2)
    return flux


def model_response_matrix(t_thz: FloatArray, t_pump: FloatArray, *, response_rms: float = 150.0) -> FloatArray:
    """g(t - t') for a single-cycle model response (first derivative of a Gaussian).

    Normalized to unit peak magnitude. This is a stand-in, not a crystal model.
    """

    if response_rms <= 0:
        raise ValueError("response_rms must be positive")
    lag = t_thz[:, None] - t_pump[None, :]
    return (-(lag / response_rms) * np.exp(0.5 - lag**2 / (2.0 * response_rms**2))).astype(np.float64)


def analytic_noise_coefficients(
    *, rms_duration: float, temporal_modes: float, spatial_modes: float, statistics: str = "bsv"
) -> tuple[float, float]:
    """(A, B) of the moment expansion: Var N / <N>^2 and Var(N t_c) / <N>^2 (fs^2)."""

    prefactor = 2.0 if statistics == "bsv" else 1.0
    a = prefactor / (spatial_modes * temporal_modes)
    b = a * 0.5 * rms_duration**2 * (1.0 - 1.0 / temporal_modes**2)
    return float(a), float(b)


def exact_variance(
    response: FloatArray, covariance: FloatArray, *, dt_pump: float, spatial_modes: float, statistics: str = "bsv"
) -> FloatArray:
    """Var E(t) = (2 / M_s) double-integral g(t-t1) g(t-t2) G1(t1,t2)^2 (1 for thermal)."""

    prefactor = 2.0 if statistics == "bsv" else 1.0
    kernel = covariance**2
    return (prefactor / spatial_modes) * np.einsum("ik,kl,il->i", response, kernel, response) * dt_pump**2


@dataclass(frozen=True)
class WaveformNoise:
    mean_field: FloatArray
    variance: FloatArray
    mean_photon_number: float
    photon_number: FloatArray
    first_moment: FloatArray
    number_coefficient: float
    timing_coefficient: float
    cross_coefficient: float


def waveform_noise(flux: FloatArray, response: FloatArray, t_pump: FloatArray) -> WaveformNoise:
    """Mean and variance of E_j(t) against delay, with the sampled moment coefficients."""

    dt = float(t_pump[1] - t_pump[0])
    fields = flux @ response.T * dt
    photon_number = flux.sum(axis=1) * dt
    first_moment = (flux * t_pump[None, :]).sum(axis=1) * dt
    mean_number = float(photon_number.mean())
    return WaveformNoise(
        mean_field=fields.mean(axis=0),
        variance=fields.var(axis=0),
        mean_photon_number=mean_number,
        photon_number=photon_number,
        first_moment=first_moment,
        number_coefficient=float(photon_number.var() / mean_number**2),
        timing_coefficient=float(first_moment.var() / mean_number**2),
        cross_coefficient=float(-np.cov(photon_number, first_moment)[0, 1] / mean_number**2),
    )


def fit_noise_templates(
    mean_field: FloatArray, variance: FloatArray, *, dt_thz: float, mean_photon_number: float, detection_variance: float = 0.0
) -> tuple[float, float, float]:
    """Least-squares (A, B, C) in Var/<N>^2 = A g^2 + B (g'^2 - g g'') + 2 C g g'.

    ``g = <E>/<N>`` is the measured mean waveform per photon. The combination
    ``g'^2 - g g''`` is what multiplies the timing coefficient at second order in
    (pulse duration / THz period): the ``g g''`` part comes from the covariance of
    the photon number with the second temporal moment of the flux. This is the
    analysis an experiment would run on the measured mean and variance;
    ``detection_variance`` is subtracted first.
    """

    g = mean_field / mean_photon_number
    slope = np.gradient(g, dt_thz)
    curvature = np.gradient(slope, dt_thz)
    design = np.stack([g**2, slope**2 - g * curvature, 2.0 * g * slope], axis=1)
    target = (variance - detection_variance) / mean_photon_number**2
    coefficients, *_ = np.linalg.lstsq(design, target, rcond=None)
    return float(coefficients[0]), float(coefficients[1]), float(coefficients[2])


def gaussian_schell_flux_spectrum(
    omega: FloatArray,
    *,
    rms_duration: float,
    temporal_modes: float,
    spatial_modes: float,
    mean_photon_number: float,
    statistics: str = "bsv",
) -> dict[str, FloatArray]:
    """Closed-form <N^dagger(Omega) N(Omega)> for a Gaussian Schell-model pump.

    ``omega`` in rad/fs. Three parts, all in photons squared:

    - ``mean``: |<N(Omega)>|^2 = Nbar^2 exp(-Omega^2 T^2), the mean waveform;
    - ``fluctuation``: (2 Nbar^2 / K) exp(-Omega^2 T^2 / K_t^2) for BSV (1 in
      place of 2 for thermal light), wider than the mean part by K_t;
    - ``shot_noise``: Nbar, flat: the rectified shot noise of the photon flux
      (spontaneous difference-frequency generation).
    """

    w = np.asarray(omega, dtype=np.float64)
    prefactor = 2.0 if statistics == "bsv" else 1.0
    total_modes = spatial_modes * temporal_modes
    mean = mean_photon_number**2 * np.exp(-(w**2) * rms_duration**2)
    fluctuation = (prefactor * mean_photon_number**2 / total_modes) * np.exp(-(w**2) * rms_duration**2 / temporal_modes**2)
    shot = np.full_like(w, mean_photon_number)
    return {"mean": mean, "fluctuation": fluctuation, "shot_noise": shot, "total": mean + fluctuation + shot}
