from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.mechanisms import MechanismFamily


FloatArray = NDArray[np.float64]
ComplexArray = NDArray[np.complex128]


def mu_factor(*, time_au: FloatArray, omega_au: float, r: float, theta: float) -> ComplexArray:
    if time_au.ndim != 1 or time_au.size == 0:
        raise ValueError("time_au must be a non-empty one-dimensional array")
    if omega_au <= 0:
        raise ValueError("omega_au must be positive")
    if r < 0:
        raise ValueError("r must be non-negative")
    return (
        np.cosh(r)
        + np.sinh(r) * np.exp(-1j * (2.0 * omega_au * time_au - theta))
    ).astype(np.complex128)


def modulated_harmonic_amplitude(
    *,
    time_au: FloatArray,
    dipole_au: FloatArray,
    harmonic_frequency_au: float,
    r: float,
    theta: float,
) -> complex:
    if time_au.shape != dipole_au.shape:
        raise ValueError("time_au and dipole_au must have matching shape")
    if harmonic_frequency_au <= 0:
        raise ValueError("harmonic_frequency_au must be positive")
    modulation = mu_factor(time_au=time_au, omega_au=harmonic_frequency_au, r=r, theta=theta)
    integrand = modulation * dipole_au * np.exp(1j * harmonic_frequency_au * time_au)
    return complex(np.trapezoid(integrand, x=time_au))


def run_emission_environment_scan(
    *,
    harmonic_order: int,
    fundamental_omega_au: float,
    r: float,
    theta_values: list[float],
    output_dir: Path,
    cycles: int = 12,
    samples_per_cycle: int = 512,
) -> RunArtifacts:
    if harmonic_order <= 0:
        raise ValueError("harmonic_order must be positive")
    if fundamental_omega_au <= 0:
        raise ValueError("fundamental_omega_au must be positive")
    if r < 0:
        raise ValueError("r must be non-negative")
    if not theta_values:
        raise ValueError("theta_values must contain at least one angle")
    if cycles <= 0:
        raise ValueError("cycles must be positive")
    if samples_per_cycle < 32:
        raise ValueError("samples_per_cycle must be at least 32")

    output_dir = ensure_output_dir(output_dir)
    harmonic_frequency = harmonic_order * fundamental_omega_au
    period = 2.0 * np.pi / harmonic_frequency
    sample_count = cycles * samples_per_cycle
    time_au = np.linspace(0.0, cycles * period, sample_count, endpoint=False, dtype=np.float64)
    dipole_au = np.cos(harmonic_frequency * time_au).astype(np.float64)
    reference = modulated_harmonic_amplitude(
        time_au=time_au,
        dipole_au=dipole_au,
        harmonic_frequency_au=harmonic_frequency,
        r=0.0,
        theta=0.0,
    )
    reference_intensity = max(abs(reference) ** 2, 1.0e-30)

    rows: list[dict[str, float | int | str]] = []
    for theta in theta_values:
        amplitude = modulated_harmonic_amplitude(
            time_au=time_au,
            dipole_au=dipole_au,
            harmonic_frequency_au=harmonic_frequency,
            r=r,
            theta=float(theta),
        )
        rows.append(
            {
                "harmonic_order": int(harmonic_order),
                "r": float(r),
                "theta": float(theta),
                "amplitude_real": float(np.real(amplitude)),
                "amplitude_imag": float(np.imag(amplitude)),
                "relative_intensity": float(abs(amplitude) ** 2 / reference_intensity),
                "mechanism": MechanismFamily.SQUEEZED_EMISSION_MODE_ENVIRONMENT.value,
            }
        )

    csv_path = output_dir / "emission_environment_scan.csv"
    summary_path = output_dir / "emission_environment_summary.json"
    manifest_path = output_dir / "manifest.yaml"
    write_csv(
        csv_path,
        rows,
        ["harmonic_order", "r", "theta", "amplitude_real", "amplitude_imag", "relative_intensity", "mechanism"],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "mechanism": MechanismFamily.SQUEEZED_EMISSION_MODE_ENVIRONMENT.value,
            "max_relative_intensity": max(float(row["relative_intensity"]) for row in rows),
            "min_relative_intensity": min(float(row["relative_intensity"]) for row in rows),
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": "hhg_intensity_prediction",
            "mechanism": MechanismFamily.SQUEEZED_EMISSION_MODE_ENVIRONMENT.value,
            "source_model": "selected_harmonic_emission_mode",
            "code_entrypoint": "stochastic_em_theory.emission_environment.run_emission_environment_scan",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [],
            "observable": "selected_harmonic_mu_k_modulation",
            "units": "atomic units for time and angular frequency; relative intensity dimensionless",
            "notes": "Boundary toy model for Wang 2024 emitted-mode squeezed-vacuum modulation, separate from BSV pump sampling.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
