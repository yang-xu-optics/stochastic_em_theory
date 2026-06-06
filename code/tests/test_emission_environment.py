import csv

import numpy as np
import yaml

from stochastic_em_theory.emission_environment import modulated_harmonic_amplitude, mu_factor, run_emission_environment_scan
from stochastic_em_theory.mechanisms import MechanismFamily


def test_mu_factor_reduces_to_one_without_squeezing() -> None:
    time_au = np.linspace(0.0, 10.0, 128)

    mu = mu_factor(time_au=time_au, omega_au=0.5, r=0.0, theta=1.7)

    assert np.allclose(mu, np.ones_like(mu))


def test_modulated_amplitude_matches_unmodulated_limit() -> None:
    omega_au = 0.4
    time_au = np.linspace(0.0, 20.0 * np.pi / omega_au, 4096, endpoint=False)
    dipole_au = np.cos(omega_au * time_au)

    baseline = modulated_harmonic_amplitude(
        time_au=time_au,
        dipole_au=dipole_au,
        harmonic_frequency_au=omega_au,
        r=0.0,
        theta=0.0,
    )
    squeezed = modulated_harmonic_amplitude(
        time_au=time_au,
        dipole_au=dipole_au,
        harmonic_frequency_au=omega_au,
        r=0.6,
        theta=0.0,
    )

    assert abs(baseline) > 0.0
    assert abs(squeezed) > abs(baseline)


def test_emission_environment_scan_writes_manifest_and_angle_dependence(tmp_path) -> None:
    result = run_emission_environment_scan(
        harmonic_order=9,
        fundamental_omega_au=0.057,
        r=0.5,
        theta_values=[0.0, np.pi],
        output_dir=tmp_path,
    )

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 2
    assert rows[0]["mechanism"] == MechanismFamily.SQUEEZED_EMISSION_MODE_ENVIRONMENT.value
    assert float(rows[0]["relative_intensity"]) > float(rows[1]["relative_intensity"])

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["mechanism"] == MechanismFamily.SQUEEZED_EMISSION_MODE_ENVIRONMENT.value
