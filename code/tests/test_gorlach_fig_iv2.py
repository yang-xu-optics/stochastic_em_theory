import csv
import json

import numpy as np
import yaml

from stochastic_em_theory.fig_iv2 import (
    ATOMIC_INTENSITY_W_CM2,
    BSV_INTENSITY_SAMPLING,
    FIG_IV2_INTENSITIES_W_CM2,
    TDSE_THRESHOLD_MECHANISM,
    bsv_intensity_quantile_au,
    effective_bsv_intensity_samples,
    intensity_w_cm2_to_field_au,
    run_gorlach_2023_fig_iv2_bsv_threshold,
    sample_bsv_intensity_au,
)


def test_intensity_w_cm2_to_atomic_field_uses_standard_conversion() -> None:
    assert np.isclose(intensity_w_cm2_to_field_au(ATOMIC_INTENSITY_W_CM2), 1.0)
    assert np.isclose(intensity_w_cm2_to_field_au(1.0e13), 0.016880323915389028)
    assert np.isclose(intensity_w_cm2_to_field_au(2.0e13), 0.023872383018394068)


def test_bsv_intensity_sampler_has_mean_and_g2_of_single_mode_bsv() -> None:
    rng = np.random.default_rng(2023)
    mean_intensity_au = intensity_w_cm2_to_field_au(1.0e13) ** 2

    samples = sample_bsv_intensity_au(mean_intensity_au=mean_intensity_au, shots=200_000, rng=rng)

    assert np.isclose(float(np.mean(samples)), mean_intensity_au, rtol=0.02)
    assert np.isclose(float(np.mean(samples**2) / np.mean(samples) ** 2), 3.0, rtol=0.04)


def test_effective_bsv_intensity_samples_can_cap_extreme_tail() -> None:
    mean_intensity_au = intensity_w_cm2_to_field_au(2.0e13) ** 2
    raw_samples = np.array([0.1, 1.0, 10.0, 100.0]) * mean_intensity_au
    cap = bsv_intensity_quantile_au(mean_intensity_au=mean_intensity_au, quantile=0.99)

    effective = effective_bsv_intensity_samples(raw_samples, mean_intensity_au=mean_intensity_au, tail_quantile=0.99)

    assert np.max(effective) <= cap
    assert effective[-1] == cap
    assert effective[0] == raw_samples[0]


def test_gorlach_fig_iv2_runner_writes_two_intensity_outputs(tmp_path) -> None:
    artifacts = run_gorlach_2023_fig_iv2_bsv_threshold(
        output_dir=tmp_path,
        intensities_w_cm2=FIG_IV2_INTENSITIES_W_CM2,
        shots=4096,
        seed=17,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=39,
        spectrum_model="proxy",
        bsv_tail_quantile=0.999,
    )

    figure_path = tmp_path / "gorlach_2023_fig_iv2_bsv_threshold.png"
    display_csv_path = tmp_path / "gorlach_2023_fig_iv2_bsv_threshold_display.csv"
    parameter_path = tmp_path / "parameters.yaml"
    assert artifacts.csv_path == tmp_path / "gorlach_2023_fig_iv2_bsv_threshold_spectra.csv"
    assert artifacts.summary_path == tmp_path / "gorlach_2023_fig_iv2_bsv_threshold_summary.json"
    assert artifacts.manifest_path == tmp_path / "manifest.yaml"
    assert artifacts.csv_path.exists()
    assert artifacts.summary_path.exists()
    assert artifacts.manifest_path.exists()
    assert parameter_path.exists()
    assert display_csv_path.exists()
    assert figure_path.exists()
    assert figure_path.stat().st_size > 1000

    with artifacts.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert {float(row["intensity_w_cm2"]) for row in rows} == set(FIG_IV2_INTENSITIES_W_CM2)
    assert {row["case_label"] for row in rows} == {"BSV - 1e13 W/cm^2", "BSV - 2e13 W/cm^2"}
    assert len(rows) == 2 * 20
    assert all(row["mechanism"] == TDSE_THRESHOLD_MECHANISM for row in rows)
    assert all(row["driver_sampling"] == BSV_INTENSITY_SAMPLING for row in rows)
    assert all(row["normalization_scope"] == "shared_fig_iv2_intensity_cases" for row in rows)
    assert all(row["bsv_tail_quantile"] == "0.999" for row in rows)

    high_order_rows = {float(row["intensity_w_cm2"]): row for row in rows if float(row["harmonic_order"]) == 39.0}
    assert float(high_order_rows[2.0e13]["mean_intensity"]) > float(high_order_rows[1.0e13]["mean_intensity"])

    summary = json.loads(artifacts.summary_path.read_text())
    assert summary["intensities_w_cm2"] == list(FIG_IV2_INTENSITIES_W_CM2)
    assert summary["parameters"]["spectrum_model"] == "smooth_cutoff_proxy"
    assert summary["parameters"]["driver_sampling"] == BSV_INTENSITY_SAMPLING
    assert summary["parameters"]["bsv_tail_quantile"] == 0.999
    assert summary["case_summaries"]["BSV - 2e13 W/cm^2"]["raw_intensity_g2"] > 2.5
    assert (
        summary["case_summaries"]["BSV - 2e13 W/cm^2"]["effective_intensity_g2"]
        < summary["case_summaries"]["BSV - 2e13 W/cm^2"]["raw_intensity_g2"]
    )
    assert summary["case_summaries"]["BSV - 2e13 W/cm^2"]["cutoff_order_p99"] > 30.0
    assert (
        summary["case_summaries"]["BSV - 2e13 W/cm^2"]["cutoff_order_p99"]
        > summary["case_summaries"]["BSV - 1e13 W/cm^2"]["cutoff_order_p99"]
    )

    manifest = yaml.safe_load(artifacts.manifest_path.read_text())
    assert manifest["code_entrypoint"] == "stochastic_em_theory.fig_iv2.run_gorlach_2023_fig_iv2_bsv_threshold"
    assert manifest["random_seeds"] == [17]
    assert manifest["outputs"]["display_spectrum_csv"] == "gorlach_2023_fig_iv2_bsv_threshold_display.csv"
    assert "Fig. IV.2" in manifest["source_refs"][0]
