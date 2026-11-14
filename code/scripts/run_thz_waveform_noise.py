"""Noise of the rectified THz waveform against delay for a multimode BSV pump.

Spec: wiki/simulations/thz-waveform-noise-against-delay.md.
Three pumps with the same total mode number K = 10 (same g2 = 1.2) that
differ in how K splits into spatial and temporal modes. Times in fs; field
and flux in arbitrary units.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from stochastic_em_theory.io import current_git_commit, write_csv, write_json, write_manifest
from stochastic_em_theory.thz_waveform_noise import (
    FWHM_TO_RMS,
    analytic_noise_coefficients,
    exact_variance,
    fit_noise_templates,
    gaussian_schell_covariance,
    model_response_matrix,
    sample_photon_flux,
    temporal_mode_number,
    waveform_noise,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "runs" / "20261114-thz-waveform-noise-against-delay"

SEED = 20261114
SHOTS = 20_000
PUMP_FWHM_FS = 100.0
RESPONSE_RMS_FS = 150.0
DT_PUMP = 4.0
DT_THZ = 10.0
CASES = ((10, 1.0), (5, 2.0), (2, 5.0))  # (spatial modes, temporal modes), K = 10 for all
SNR_AT_MEAN_PEAK = 30.0

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
ORDINAL_BLUE = ("#86b6ef", "#3987e5", "#0d366b")  # temporal modes 1, 2, 5
BAND = "#cde2fb"


def _style(ax: plt.Axes, *, title: str, xlabel: str, ylabel: str) -> None:
    ax.set_facecolor(SURFACE)
    ax.set_title(title, loc="left", fontsize=10.5, color=INK, pad=8)
    ax.set_xlabel(xlabel, fontsize=9, color=INK_SECONDARY)
    ax.set_ylabel(ylabel, fontsize=9, color=INK_SECONDARY)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
    ax.tick_params(colors=INK_MUTED, labelsize=8, length=3)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    out: Path = args.output_dir
    out.mkdir(parents=True, exist_ok=True)

    t_rms = float(PUMP_FWHM_FS * FWHM_TO_RMS)
    t_pump = np.arange(-220.0, 220.0 + 1e-9, DT_PUMP)
    t_thz = np.arange(-800.0, 800.0 + 1e-9, DT_THZ)
    response = model_response_matrix(t_thz, t_pump, response_rms=RESPONSE_RMS_FS)
    rng = np.random.default_rng(SEED)

    rows: list[dict] = []
    summary: dict[str, dict] = {}
    curves: dict[tuple[int, float], dict[str, np.ndarray]] = {}
    centroid_demo: dict[str, np.ndarray] = {}
    for spatial, temporal in CASES:
        covariance = gaussian_schell_covariance(t_pump, rms_duration=t_rms, temporal_modes=temporal)
        flux = sample_photon_flux(covariance, spatial_modes=spatial, shots=SHOTS, rng=rng)
        noise = waveform_noise(flux, response, t_pump)
        exact = exact_variance(response, covariance, dt_pump=DT_PUMP, spatial_modes=spatial)
        a, b = analytic_noise_coefficients(rms_duration=t_rms, temporal_modes=temporal, spatial_modes=spatial)
        a_fit, b_fit, c_fit = fit_noise_templates(
            noise.mean_field, noise.variance, dt_thz=DT_THZ, mean_photon_number=noise.mean_photon_number
        )
        peak = int(np.argmax(np.abs(noise.mean_field)))
        centre = t_thz.size // 2
        node = centre - 8 + int(np.argmin(np.abs(noise.mean_field[centre - 8 : centre + 9])))
        peak_field = float(abs(noise.mean_field[peak]))
        slope = np.gradient(noise.mean_field, DT_THZ)
        rms = np.sqrt(noise.variance)
        number_part = np.sqrt(a) * np.abs(noise.mean_field)
        # Infer the temporal mode number by fitting the exact variance model to the
        # sampled variance, at the total mode number fixed by the amplitude noise.
        total_modes = 2.0 / noise.number_coefficient
        candidates = np.linspace(1.0, 8.0, 141)
        misfit = []
        for candidate in candidates:
            trial = gaussian_schell_covariance(t_pump, rms_duration=t_rms, temporal_modes=float(candidate))
            model = exact_variance(response, trial, dt_pump=DT_PUMP, spatial_modes=total_modes / candidate)
            misfit.append(float(np.sum((model - noise.variance) ** 2)))
        inferred = float(candidates[int(np.argmin(misfit))])
        key = f"Ms{spatial}_Kt{temporal:g}"
        summary[key] = {
            "spatial_modes": spatial,
            "temporal_modes": temporal,
            "temporal_modes_from_discretized_covariance": temporal_mode_number(covariance),
            "A_analytic": a,
            "A_sampled": noise.number_coefficient,
            "A_template_fit": a_fit,
            "B_analytic_fs2": b,
            "B_sampled_fs2": noise.timing_coefficient,
            "B_template_fit_fs2": b_fit,
            "C_template_fit_fs": c_fit,
            "centroid_jitter_fs": float(np.sqrt(noise.timing_coefficient)),
            "rms_at_peak_over_peak_field": float(rms[peak] / peak_field),
            "rms_at_node_over_peak_field": float(rms[node] / peak_field),
            "rms_at_node_over_rms_at_peak": float(rms[node] / rms[peak]),
            "node_delay_fs": float(t_thz[node]),
            "peak_delay_fs": float(t_thz[peak]),
            "temporal_modes_inferred_from_exact_model_fit": inferred,
            "max_relative_deviation_sampled_vs_exact_variance": float(
                np.max(np.abs(noise.variance - exact)[exact > 0.05 * exact.max()] / exact[exact > 0.05 * exact.max()])
            ),
        }
        curves[(spatial, temporal)] = {
            "mean": noise.mean_field / peak_field,
            "rms": rms / peak_field,
            "number_part": number_part / peak_field,
        }
        for i, delay in enumerate(t_thz):
            rows.append(
                {
                    "spatial_modes": spatial,
                    "temporal_modes": temporal,
                    "delay_fs": float(delay),
                    "mean_field_over_peak": float(noise.mean_field[i] / peak_field),
                    "rms_over_peak_field": float(rms[i] / peak_field),
                    "exact_rms_over_peak_field": float(np.sqrt(exact[i]) / peak_field),
                    "number_noise_part_over_peak_field": float(number_part[i] / peak_field),
                }
            )
        if (spatial, temporal) == (5, 2.0):
            fields = flux @ response.T * DT_PUMP
            detection = rng.normal(scale=peak_field / SNR_AT_MEAN_PEAK, size=SHOTS)
            true_centroid = noise.first_moment / noise.photon_number
            estimate = -(fields[:, node] + detection) / (noise.photon_number * slope[node] / noise.mean_photon_number)
            estimate_noiseless = -fields[:, node] / (noise.photon_number * slope[node] / noise.mean_photon_number)
            bright = noise.photon_number > 0.5 * noise.mean_photon_number
            summary[key]["single_shot_centroid"] = {
                "detection_snr_at_mean_peak": SNR_AT_MEAN_PEAK,
                "true_centroid_rms_fs": float(true_centroid.std()),
                "true_centroid_rms_fs_shots_above_half_mean": float(true_centroid[bright].std()),
                "estimate_error_rms_fs_no_detection_noise": float((estimate_noiseless - true_centroid)[bright].std()),
                "estimate_error_rms_fs_with_detection_noise": float((estimate - true_centroid)[bright].std()),
                "correlation_with_detection_noise": float(np.corrcoef(estimate[bright], true_centroid[bright])[0, 1]),
            }
            centroid_demo = {"true": true_centroid[bright][:3000], "estimate": estimate[bright][:3000]}
            shots_demo = fields[:6] / peak_field

    write_csv(out / "waveform_noise_against_delay.csv", rows, list(rows[0].keys()))

    # node noise against temporal mode number, analytic (model waveform), at fixed K = 10
    reference = curves[(5, 2.0)]
    kt_axis = np.linspace(1.0, 8.0, 141)
    covariance_ref = gaussian_schell_covariance(t_pump, rms_duration=t_rms, temporal_modes=2.0)
    mean_ref = response @ np.diag(covariance_ref) * DT_PUMP
    slope_ratio = float(np.max(np.abs(np.gradient(mean_ref, DT_THZ)[t_thz.size // 2 - 3 : t_thz.size // 2 + 4])) / np.max(np.abs(mean_ref)))
    node_curve = np.array(
        [np.sqrt(analytic_noise_coefficients(rms_duration=t_rms, temporal_modes=k, spatial_modes=10.0 / k)[1]) for k in kt_axis]
    ) * slope_ratio
    summary["model_waveform"] = {
        "slope_at_node_over_peak_field_per_fs": slope_ratio,
        "pump_rms_duration_fs": t_rms,
    }
    write_json(out / "waveform_noise_summary.json", summary)

    fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.4), constrained_layout=True)
    fig.patch.set_facecolor(SURFACE)

    ax = axes[0, 0]
    _style(ax, title="(a) Mean THz waveform and shot-to-shot spread",
           xlabel="delay (fs)", ylabel="field / peak of mean")
    ax.text(590, 1.95, "pump: 2 temporal x 5 spatial modes", fontsize=8, color=INK_MUTED, ha="right", va="top")
    ax.fill_between(t_thz, reference["mean"] - reference["rms"], reference["mean"] + reference["rms"], color=BAND,
                    linewidth=0, label="mean ± rms")
    for shot in shots_demo:
        ax.plot(t_thz, shot, color=INK_MUTED, linewidth=0.6, alpha=0.7)
    ax.plot([], [], color=INK_MUTED, linewidth=0.6, label="single shots")
    ax.plot(t_thz, reference["mean"], color=ORDINAL_BLUE[2], linewidth=2.0, label="mean")
    ax.set_xlim(-600, 600)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="upper left")

    ax = axes[0, 1]
    _style(ax, title="(b) Noise against delay; same g2 = 1.2 in all three",
           xlabel="delay (fs)", ylabel="rms field / peak of mean")
    for color, (spatial, temporal) in zip(ORDINAL_BLUE, CASES, strict=True):
        ax.plot(t_thz, curves[(spatial, temporal)]["rms"], color=color, linewidth=2.0,
                label=f"{temporal:g} temporal x {spatial} spatial")
    ax.plot(t_thz, reference["number_part"], color=INK_MUTED, linewidth=1.0, linestyle=(0, (3, 3)))
    ax.text(590, 0.70, "dashed: photon-number noise only,\n0.45 x |mean field|", fontsize=8, color=INK_MUTED,
            va="top", ha="right")
    ax.axvline(0.0, color=AXIS, linewidth=0.8, ymin=0.22, ymax=0.76)
    ax.text(12, 0.535, "zero crossing of the mean", fontsize=8, color=INK_SECONDARY, va="center")
    ax.set_xlim(-600, 600)
    ax.set_ylim(0, 0.72)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="upper left", title="pump modes", title_fontsize=8)

    ax = axes[1, 0]
    _style(ax, title="(c) Noise at the zero crossing against temporal modes (K = 10)",
           xlabel="temporal modes of the pump", ylabel="rms at zero crossing / peak of mean")
    ax.plot(kt_axis, node_curve, color=ORDINAL_BLUE[1], linewidth=2.0, label="second-order formula")
    sim_x = [temporal for _, temporal in CASES]
    sim_y = [summary[f"Ms{s}_Kt{k:g}"]["rms_at_node_over_peak_field"] for s, k in CASES]
    ax.plot(sim_x, sim_y, linestyle="none", marker="o", markersize=8, markerfacecolor=ORDINAL_BLUE[2],
            markeredgecolor=SURFACE, markeredgewidth=2.0, label="simulation, 20,000 shots")
    offsets = {1.0: (0.35, 0.006), 2.0: (0.15, -0.013), 5.0: (0.15, 0.007)}
    for x, y, (s, k) in zip(sim_x, sim_y, CASES, strict=True):
        jitter = summary[f"Ms{s}_Kt{k:g}"]["centroid_jitter_fs"]
        text = "one temporal mode: no jitter" if k == 1.0 else f"{jitter:.0f} fs arrival-time jitter"
        ax.text(x + offsets[k][0], y + offsets[k][1], text, fontsize=8, color=INK_SECONDARY)
    ax.set_xlim(0.8, 8.0)
    ax.set_ylim(0, 0.2)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="lower right")

    ax = axes[1, 1]
    _style(ax, title="(d) Single-shot arrival time from the field at the zero crossing",
           xlabel="true centroid of the photon flux (fs)", ylabel="single-shot estimate (fs)")
    ax.plot(centroid_demo["true"], centroid_demo["estimate"], linestyle="none", marker="o", markersize=2.5,
            markerfacecolor=ORDINAL_BLUE[1], markeredgewidth=0, alpha=0.35)
    ax.plot([-60, 60], [-60, 60], color=INK_MUTED, linewidth=1.0, linestyle=(0, (3, 3)))
    error = summary["Ms5_Kt2"]["single_shot_centroid"]["estimate_error_rms_fs_with_detection_noise"]
    ax.text(-57, 47, f"detection noise = peak field / {SNR_AT_MEAN_PEAK:.0f}\nrms error {error:.1f} fs", fontsize=8,
            color=INK_SECONDARY, va="top")
    ax.set_xlim(-60, 60)
    ax.set_ylim(-60, 60)

    fig.savefig(out / "thz_waveform_noise.png", dpi=200, facecolor=SURFACE)
    plt.close(fig)

    parameters = {
        "seed": SEED,
        "shots": SHOTS,
        "pump_fwhm_fs": PUMP_FWHM_FS,
        "pump_rms_duration_fs": t_rms,
        "response": f"first derivative of a Gaussian, rms {RESPONSE_RMS_FS} fs (model, not a crystal response)",
        "dt_pump_fs": DT_PUMP,
        "dt_thz_fs": DT_THZ,
        "cases_spatial_temporal": [list(case) for case in CASES],
        "single_shot_snr_at_mean_peak": SNR_AT_MEAN_PEAK,
    }
    write_manifest(out / "parameters.yaml", parameters)
    write_manifest(
        out / "manifest.yaml",
        {
            "run_id": out.name,
            "created": date.today().isoformat(),
            "claim_level": "validated_stochastic_simulation",
            "mechanism": "optical_rectification_of_bsv",
            "code_entrypoint": "code/scripts/run_thz_waveform_noise.py",
            "git_commit": current_git_commit(REPO_ROOT),
            "parameter_file": "parameters.yaml",
            "random_seeds": [SEED],
            "observable": "mean and rms THz field against delay; number and timing noise coefficients; single-shot arrival time",
            "units": "fs for times; field and flux in arbitrary units, normalized to the peak of the mean field",
            "notes": (
                "Bright classical-noise limit, Gaussian Schell-model pump, model THz response. "
                "No instrument timing jitter and no technical pump noise."
            ),
            "outputs": {
                "curves_csv": "waveform_noise_against_delay.csv",
                "summary_json": "waveform_noise_summary.json",
                "figure_png": "thz_waveform_noise.png",
            },
        },
    )
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
