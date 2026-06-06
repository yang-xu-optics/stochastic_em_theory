import numpy as np

from stochastic_em_theory.hhg_proxy import cutoff_energy_au, odd_harmonic_orders, proxy_hhg_spectrum


def test_cutoff_energy_increases_with_field_amplitude() -> None:
    weak = cutoff_energy_au(field_amplitude_au=0.03, omega_au=0.057, ionization_potential_au=0.7924)
    strong = cutoff_energy_au(field_amplitude_au=0.06, omega_au=0.057, ionization_potential_au=0.7924)

    assert strong > weak


def test_odd_harmonic_orders_are_odd() -> None:
    orders = odd_harmonic_orders(max_order=15)

    assert orders.tolist() == [1, 3, 5, 7, 9, 11, 13, 15]


def test_proxy_spectrum_has_expected_shape_and_nonnegative_intensity() -> None:
    spectrum = proxy_hhg_spectrum(
        field_amplitude_au=0.05,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=31,
    )

    assert spectrum.orders.shape == spectrum.intensity.shape
    assert np.all(spectrum.intensity >= 0.0)
    assert spectrum.cutoff_order > 0.0
