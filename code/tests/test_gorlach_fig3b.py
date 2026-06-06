import csv
import json

import numpy as np
import yaml

from stochastic_em_theory.fig3b import (
    Fig3BDriverState,
    _tdse_library_field_amplitudes,
    run_gorlach_2023_fig3b_proxy,
    sample_fig3b_driver_alpha,
)


def _normalized_intensity_cv(alpha: np.ndarray) -> float:
    intensity = np.abs(alpha) ** 2
    return float(np.std(intensity / np.mean(intensity)))


def test_tdse_library_amplitudes_focus_high_field_tail() -> None:
    field_amplitudes = np.linspace(0.0, 1.0, 101)

    library = _tdse_library_field_amplitudes(field_amplitudes_au=field_amplitudes, bins=5)

    assert np.isclose(library[0], 0.0)
    assert np.isclose(library[-1], 1.0)
    assert library[1] > 0.25
    assert library[-2] > 0.9


def test_fig3b_husimi_samplers_have_expected_intensity_fluctuation_hierarchy() -> None:
    rng = np.random.default_rng(1234)
    shots = 20_000

    coherent = sample_fig3b_driver_alpha(
        Fig3BDriverState.COHERENT,
        shots=shots,
        rng=rng,
        mean_photon_number=100.0,
        fock_n=100,
        bsv_r=2.0,
        bsv_phase=0.0,
    )
    fock = sample_fig3b_driver_alpha(
        Fig3BDriverState.FOCK,
        shots=shots,
        rng=rng,
        mean_photon_number=100.0,
        fock_n=100,
        bsv_r=2.0,
        bsv_phase=0.0,
    )
    thermal = sample_fig3b_driver_alpha(
        Fig3BDriverState.THERMAL,
        shots=shots,
        rng=rng,
        mean_photon_number=100.0,
        fock_n=100,
        bsv_r=2.0,
        bsv_phase=0.0,
    )
    bsv = sample_fig3b_driver_alpha(
        Fig3BDriverState.BSV,
        shots=shots,
        rng=rng,
        mean_photon_number=100.0,
        fock_n=100,
        bsv_r=2.0,
        bsv_phase=0.0,
    )

    assert _normalized_intensity_cv(fock) < 0.15
    assert _normalized_intensity_cv(coherent) < 0.2
    assert _normalized_intensity_cv(thermal) > 0.9
    assert _normalized_intensity_cv(bsv) > _normalized_intensity_cv(thermal)


def test_gorlach_fig3b_proxy_runner_writes_four_state_outputs(tmp_path) -> None:
    artifacts = run_gorlach_2023_fig3b_proxy(
        output_dir=tmp_path,
        shots=512,
        seed=7,
        base_field_amplitude_au=0.08,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=31,
        mean_photon_number=100.0,
        fock_n=100,
        bsv_r=2.0,
        bsv_phase=0.0,
        spectrum_model="proxy",
    )

    figure_path = tmp_path / "gorlach_2023_fig3b_proxy.png"
    assert artifacts.csv_path == tmp_path / "gorlach_2023_fig3b_proxy_spectra.csv"
    assert artifacts.summary_path == tmp_path / "gorlach_2023_fig3b_proxy_summary.json"
    assert artifacts.manifest_path == tmp_path / "manifest.yaml"
    assert artifacts.csv_path.exists()
    assert artifacts.summary_path.exists()
    assert artifacts.manifest_path.exists()
    assert (tmp_path / "parameters.yaml").exists()
    assert figure_path.exists()
    assert figure_path.stat().st_size > 1000

    with artifacts.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    states = [state.value for state in Fig3BDriverState]
    assert {row["driver_state"] for row in rows} == set(states)
    assert len(rows) == len(states) * 16
    assert all(row["claim_level"] == "hhg_intensity_prediction" for row in rows)
    assert all(row["mechanism"] == "quantum_light_hhg_spectra_proxy" for row in rows)

    high_order_rows = {row["driver_state"]: row for row in rows if float(row["harmonic_order"]) == 31.0}
    assert float(high_order_rows["bsv"]["mean_intensity"]) > float(high_order_rows["thermal"]["mean_intensity"])
    assert float(high_order_rows["thermal"]["mean_intensity"]) > float(high_order_rows["coherent"]["mean_intensity"])

    summary = json.loads(artifacts.summary_path.read_text())
    assert summary["driver_states"] == states
    assert summary["parameters"]["shots"] == 512
    assert summary["parameters"]["driver_sampling"] == "single_mode_husimi_q_fig3b"
    assert summary["state_summaries"]["bsv"]["cutoff_order_p99"] > summary["state_summaries"]["thermal"]["cutoff_order_p99"]
    assert summary["state_summaries"]["thermal"]["cutoff_order_p99"] > summary["state_summaries"]["coherent"]["cutoff_order_p99"]

    manifest = yaml.safe_load(artifacts.manifest_path.read_text())
    assert manifest["code_entrypoint"] == "stochastic_em_theory.fig3b.run_gorlach_2023_fig3b_proxy"
    assert manifest["parameter_file"] == "parameters.yaml"
    assert manifest["random_seeds"] == [7]
    assert "Nature Fig. 3b" in manifest["source_refs"][0]


def test_gorlach_fig3b_tdse_runner_records_dipole_acceleration_model(tmp_path) -> None:
    artifacts = run_gorlach_2023_fig3b_proxy(
        output_dir=tmp_path,
        shots=64,
        seed=11,
        base_field_amplitude_au=0.025,
        omega_au=0.4,
        ionization_potential_au=0.7924,
        max_order=9,
        mean_photon_number=25.0,
        fock_n=25,
        bsv_r=1.0,
        bsv_phase=0.0,
        spectrum_model="tdse",
        tdse_amplitude_bins=3,
        tdse_grid_points=128,
        tdse_x_min=-20.0,
        tdse_x_max=20.0,
        tdse_dt_au=0.12,
        tdse_ramp_cycles=0.5,
        tdse_flat_cycles=0.5,
        tdse_ground_state_iterations=30,
        tdse_ground_state_dt_au=0.08,
    )

    with artifacts.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert {row["driver_state"] for row in rows} == {state.value for state in Fig3BDriverState}
    assert all(row["spectrum_model"] == "tdse_dipole_acceleration" for row in rows)
    assert all(row["mechanism"] == "quantum_light_hhg_tdse_dipole_acceleration" for row in rows)
    assert all(int(row["tdse_amplitude_bin_count"]) == 3 for row in rows)

    summary = json.loads(artifacts.summary_path.read_text())
    assert summary["parameters"]["spectrum_model"] == "tdse_dipole_acceleration"
    assert summary["parameters"]["tdse_amplitude_bins"] == 3
    assert summary["state_summaries"]["bsv"]["tdse_library_field_amplitude_max_au"] > 0.0
    assert "TDSE dipole-acceleration" in summary["notes"]

    manifest = yaml.safe_load(artifacts.manifest_path.read_text())
    assert manifest["mechanism"] == "quantum_light_hhg_tdse_dipole_acceleration"
    assert manifest["observable"] == "ensemble_mean_tdse_hhg_spectrum_by_driver_state"
    assert manifest["parameters"]["tdse"]["grid_points"] == 128
    assert manifest["parameter_file"] == "parameters.yaml"
    parameter_file = yaml.safe_load((tmp_path / "parameters.yaml").read_text())
    assert parameter_file["spectrum_model"] == "tdse_dipole_acceleration"
