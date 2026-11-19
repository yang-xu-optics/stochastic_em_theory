"""Figures for the theory note in paper/theory-note/.

Everything is computed from closed forms or from the exact variance formula;
the only sampling is the handful of single shots drawn in Fig. 3(a).
Writes vector PDFs and a manifest next to the manuscript. Times in fs,
frequencies in THz, fields normalized to the peak of the mean waveform.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma, norm

from stochastic_em_theory.io import current_git_commit, write_manifest
from stochastic_em_theory.thz_waveform_noise import (
    FWHM_TO_RMS,
    analytic_noise_coefficients,
    exact_variance,
    gaussian_schell_covariance,
    gaussian_schell_flux_spectrum,
    model_response_matrix,
    sample_photon_flux,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "paper" / "theory-note" / "figures"

SEED = 20261119
PUMP_FWHM_FS = 100.0
RESPONSE_RMS_FS = 150.0
TOTAL_MODES = 10.0
PHOTONS_PER_PULSE = 2.4e13

INK = "#0b0b0b"
MUTED = "#898781"
GRID = "#e1e0d9"
BLUES = ("#86b6ef", "#3987e5", "#0d366b")  # ordinal: validated light-to-dark ramp
CATEGORICAL = ("#2a78d6", "#eb6834", "#1baf7a")  # validated categorical slots 1-3
BAND = "#cde2fb"
COLUMN = 3.375  # inches, single PRA column
DOUBLE = 7.0


def _setup() -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "cm",
            "font.size": 8,
            "axes.labelsize": 8,
            "axes.titlesize": 8,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "legend.fontsize": 7,
            "axes.linewidth": 0.6,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "lines.linewidth": 1.4,
            "pdf.fonttype": 42,
        }
    )


def _panel_label(ax: plt.Axes, text: str, *, x: float = 0.03, y: float = 0.95) -> None:
    ax.text(x, y, text, transform=ax.transAxes, fontsize=8, va="top", ha="left", color=INK)


def figure_statistics(out: Path) -> dict:
    fig, axes = plt.subplots(1, 2, figsize=(DOUBLE, 2.55), constrained_layout=True)

    ax = axes[0]
    w = np.linspace(1e-3, 3.6, 900)
    for color, style, modes in zip(BLUES, ("-", "--", "-"), (1, 2, 10), strict=True):
        ax.plot(w, gamma.pdf(w, a=0.5 * modes, scale=2.0 / modes), color=color, linestyle=style, label=f"$K={modes}$")
    ax.plot(w, norm.pdf(w, loc=1.0, scale=np.sqrt(0.2)), color=MUTED, linestyle=":", linewidth=1.0,
            label="Gaussian, same\nmean and variance\nas $K=10$")
    ax.set_xlim(-0.25, 3.6)
    wn = np.linspace(-0.25, 0.0, 30)
    ax.plot(wn, norm.pdf(wn, loc=1.0, scale=np.sqrt(0.2)), color=MUTED, linestyle=":", linewidth=1.0)
    ax.axvline(0.0, color=GRID, linewidth=0.6)
    ax.set_ylim(0.0, 1.5)
    ax.set_xlabel(r"single-shot THz field $E/\langle E\rangle$")
    ax.set_ylabel("probability density")
    ax.legend(frameon=False, loc="upper right", handlelength=1.8)
    _panel_label(ax, "(a)", x=0.16)

    ax = axes[1]
    nbar = np.logspace(-1, 6, 400)
    exact = 3 * nbar**2 + 2 * nbar
    app = (4 * nbar + 3) / exact
    classical = 2 * nbar / exact
    ax.loglog(nbar, app, color=CATEGORICAL[1], linestyle="-", label="Husimi-$Q$ mixture (too large)")
    ax.loglog(nbar, classical, color=CATEGORICAL[0], linestyle="--", label="classical Gaussian noise (too small)")
    ax.loglog(nbar, 4 / (3 * nbar), color=MUTED, linestyle=":", linewidth=0.9)
    ax.loglog(nbar, 2 / (3 * nbar), color=MUTED, linestyle=":", linewidth=0.9)
    ax.text(2.0e3, 3.0e-3, r"$4/3\bar n$", fontsize=7, color=MUTED)
    ax.text(1.5e2, 4.0e-4, r"$2/3\bar n$", fontsize=7, color=MUTED)
    ax.set_xlim(1e-1, 1e6)
    ax.set_ylim(1e-7, 30)
    ax.set_xlabel(r"mean photon number $\bar n$")
    ax.set_ylabel("relative error of THz energy")
    ax.legend(frameon=False, loc="upper right")
    _panel_label(ax, "(b)", y=0.10)

    fig.savefig(out / "fig_statistics.pdf")
    plt.close(fig)
    return {"panel_a_modes": [1, 2, 10], "panel_b": "exact 3n^2+2n; APP 3n^2+6n+3; classical 3n^2"}


def figure_spectrum(out: Path, t_rms: float) -> dict:
    fig, ax = plt.subplots(figsize=(COLUMN, 2.6), constrained_layout=True)
    nu = np.linspace(0.0, 48.0, 600)
    omega = 2.0 * np.pi * nu * 1.0e-3  # rad/fs
    crossings = {}
    for color, style, temporal in zip(BLUES, ("-", "--", "-"), (1.0, 2.0, 5.0), strict=True):
        parts = gaussian_schell_flux_spectrum(
            omega, rms_duration=t_rms, temporal_modes=temporal, spatial_modes=TOTAL_MODES / temporal,
            mean_photon_number=PHOTONS_PER_PULSE,
        )
        ax.semilogy(nu, parts["fluctuation"] / PHOTONS_PER_PULSE**2, color=color, linestyle=style,
                    label=f"fluctuation, $K_t={temporal:g}$")
        if temporal > 1.0:
            crossings[f"Kt{temporal:g}"] = float(
                np.sqrt(np.log(TOTAL_MODES / 2.0) / (1.0 - 1.0 / temporal**2)) / t_rms / (2.0 * np.pi) * 1.0e3
            )
    ax.semilogy(nu, parts["mean"] / PHOTONS_PER_PULSE**2, color=CATEGORICAL[1], linestyle="-", label="mean field")
    ax.semilogy(nu, parts["shot_noise"] / PHOTONS_PER_PULSE**2, color=MUTED, linestyle=":", label="shot noise")
    ax.set_xlim(0, 48)
    ax.set_ylim(1e-15, 3e5)
    ax.set_xlabel(r"THz frequency $\Omega/2\pi$ (THz)")
    ax.set_ylabel(r"$\langle\hat N^\dagger(\Omega)\hat N(\Omega)\rangle/\bar N^2$")
    ax.legend(frameon=False, loc="upper center", ncol=2, handlelength=2.0, columnspacing=1.0)
    fig.savefig(out / "fig_spectrum.pdf")
    plt.close(fig)
    return {"mean_fluctuation_crossover_THz": crossings, "photons_per_pulse": PHOTONS_PER_PULSE}


def figure_waveform_noise(out: Path, t_rms: float) -> dict:
    t_pump = np.arange(-220.0, 220.0 + 1e-9, 4.0)
    t_thz = np.arange(-800.0, 800.0 + 1e-9, 10.0)
    response = model_response_matrix(t_thz, t_pump, response_rms=RESPONSE_RMS_FS)
    fig, axes = plt.subplots(1, 2, figsize=(DOUBLE, 2.55), constrained_layout=True)
    summary = {}

    ax = axes[0]
    covariance = gaussian_schell_covariance(t_pump, rms_duration=t_rms, temporal_modes=2.0)
    mean = response @ np.diag(covariance) * 4.0
    peak = float(np.max(np.abs(mean)))
    rms = np.sqrt(exact_variance(response, covariance, dt_pump=4.0, spatial_modes=5.0))
    rng = np.random.default_rng(SEED)
    shots = sample_photon_flux(covariance, spatial_modes=5, shots=5, rng=rng) @ response.T * 4.0
    ax.fill_between(t_thz, (mean - rms) / peak, (mean + rms) / peak, color=BAND, linewidth=0, label=r"mean $\pm$ rms")
    for shot in shots:
        ax.plot(t_thz, shot / peak, color=MUTED, linewidth=0.5)
    ax.plot([], [], color=MUTED, linewidth=0.5, label="single shots")
    ax.plot(t_thz, mean / peak, color=BLUES[2], label="mean")
    ax.set_xlim(-600, 600)
    ax.set_xlabel("delay (fs)")
    ax.set_ylabel(r"THz field / peak of mean")
    ax.legend(frameon=False, loc="upper right")
    _panel_label(ax, "(a)")

    ax = axes[1]
    for color, style, temporal in zip(BLUES, ("-", "--", "-"), (1.0, 2.0, 5.0), strict=True):
        covariance = gaussian_schell_covariance(t_pump, rms_duration=t_rms, temporal_modes=temporal)
        rms = np.sqrt(exact_variance(response, covariance, dt_pump=4.0, spatial_modes=TOTAL_MODES / temporal))
        ax.plot(t_thz, rms / peak, color=color, linestyle=style, label=f"$K_t={temporal:g}$")
        centre = t_thz.size // 2
        a, b = analytic_noise_coefficients(rms_duration=t_rms, temporal_modes=temporal, spatial_modes=TOTAL_MODES / temporal)
        summary[f"Kt{temporal:g}"] = {
            "rms_at_zero_crossing_over_peak": float(rms[centre] / peak),
            "rms_at_peak_over_peak": float(rms.max() / peak),
            "A": a,
            "B_fs2": b,
            "arrival_time_jitter_fs": float(np.sqrt(b)),
        }
    ax.set_xlim(-600, 600)
    ax.set_ylim(0, 0.62)
    ax.set_xlabel("delay (fs)")
    ax.set_ylabel("rms THz field / peak of mean")
    ax.legend(frameon=False, loc="upper right", title="temporal modes", title_fontsize=7)
    _panel_label(ax, "(b)")

    fig.savefig(out / "fig_waveform_noise.pdf")
    plt.close(fig)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    out: Path = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    _setup()
    t_rms = float(PUMP_FWHM_FS * FWHM_TO_RMS)
    details = {
        "fig_statistics": figure_statistics(out),
        "fig_spectrum": figure_spectrum(out, t_rms),
        "fig_waveform_noise": figure_waveform_noise(out, t_rms),
    }
    write_manifest(
        out / "manifest.yaml",
        {
            "created": date.today().isoformat(),
            "code_entrypoint": "code/scripts/make_theory_note_figures.py",
            "git_commit": current_git_commit(REPO_ROOT),
            "random_seeds": [SEED],
            "parameters": {
                "pump_fwhm_fs": PUMP_FWHM_FS,
                "pump_rms_duration_fs": t_rms,
                "total_modes": TOTAL_MODES,
                "photons_per_pulse": PHOTONS_PER_PULSE,
                "thz_response": f"first derivative of a Gaussian, rms {RESPONSE_RMS_FS} fs (model, not a crystal response)",
            },
            "units": "fs, THz; fields normalized to the peak of the mean waveform",
            "notes": "Closed forms and the exact variance formula; five sampled shots in fig_waveform_noise (a) only.",
            "values": details,
        },
    )
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
