"""Symmetry check: which colour of a two-colour plasma drive carries the BSV.

Same local photocurrent model as notebooks/thz_plasma_bsv_photocurrent.ipynb
(quasi-static tunnelling rate, damped Brunel current, THz source = band-limited
dJ/dt; no propagation). The BSV amplitude is taken in the macroscopic limit: a
real zero-mean Gaussian X on the anti-squeezed quadrature.

  A) coherent 800 nm + BSV 400 nm  : THz field is odd in X  -> zero ensemble mean
  B) BSV 800 nm + coherent 400 nm  : THz field is even in X -> nonzero ensemble mean

Case B follows because X -> -X on the fundamental equals a half-cycle time
shift of the whole two-colour waveform. See
wiki/theory/bsv-even-order-response-moment-scaling.md.

Units: atomic units internally; intensities in W/cm^2; THz field in arbitrary units.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import numpy as np
from scipy.signal import lfilter

from stochastic_em_theory.io import current_git_commit, write_manifest

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "runs" / "20261114-thz-two-color-parity-check"

AU_TIME_FS = 0.0241888432651
AU_FREQ_THZ = 1.0e3 / AU_TIME_FS
AU_INTENSITY_W_CM2 = 3.50944758e16
PARAMS = {
    "seed": 20261114,
    "shots": 4000,
    "lambda_w_nm": 800.0,
    "mean_intensity_w_W_cm2": 1.0e14,
    "intensity_ratio_2w": 0.02,
    "fwhm_fs": 35.0,
    "Ip_au": 0.579,
    "nu_coll_au": 5.0e-4,
    "t_span_fs": 200.0,
    "dt_au": 0.4,
    "thz_cut_THz": 60.0,
}


def _rate(field: np.ndarray, ip: float) -> np.ndarray:
    field = np.maximum(np.abs(field), 1.0e-6)
    kappa3 = (2.0 * ip) ** 1.5
    return 4.0 * (2.0 * ip) ** 2.5 / field * np.exp(-2.0 * kappa3 / (3.0 * field))


def _thz_waveforms(field: np.ndarray, *, dt: float, ip: float, nu: float, cut_thz: float) -> np.ndarray:
    n_e = 1.0 - np.exp(-dt * np.cumsum(_rate(field, ip), axis=0))
    drive = n_e * field
    current = lfilter([dt], [1.0, -np.exp(-nu * dt)], drive, axis=0)
    djdt = drive - nu * current
    freqs_thz = np.fft.rfftfreq(djdt.shape[0], d=dt) * AU_FREQ_THZ
    spectrum = np.fft.rfft(djdt, axis=0) * dt * np.exp(-((freqs_thz / cut_thz) ** 8))[:, None]
    return np.fft.irfft(spectrum, n=djdt.shape[0], axis=0) / dt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    p = PARAMS
    omega = 45.5633525316 / p["lambda_w_nm"]
    dt = p["dt_au"]
    sigma_t = p["fwhm_fs"] / (2.0 * np.sqrt(np.log(2.0))) / AU_TIME_FS
    half_span = 0.5 * p["t_span_fs"] / AU_TIME_FS
    t = np.arange(-half_span, half_span, dt)
    envelope = np.exp(-(t**2) / (2.0 * sigma_t**2))
    rng = np.random.default_rng(p["seed"])
    x = rng.normal(size=p["shots"])  # unit-variance real Gaussian BSV amplitude
    e_w = np.sqrt(p["mean_intensity_w_W_cm2"] / AU_INTENSITY_W_CM2)
    e_2w = e_w * np.sqrt(p["intensity_ratio_2w"])
    fundamental = (envelope * np.cos(omega * t))[:, None]
    second = (envelope * np.sin(2.0 * omega * t))[:, None]
    fields = {
        "A_coherent_w_plus_bsv_2w": e_w * fundamental + e_2w * x[None, :] * second,
        "B_bsv_w_plus_coherent_2w": e_w * x[None, :] * fundamental + e_2w * second,
    }

    results = {}
    for name, field in fields.items():
        waveforms = _thz_waveforms(field, dt=dt, ip=p["Ip_au"], nu=p["nu_coll_au"], cut_thz=p["thz_cut_THz"])
        probe = int(np.argmax(waveforms.std(axis=1)))  # time of largest shot-to-shot spread
        amplitude = waveforms[probe]
        energy = np.sum(waveforms**2, axis=0) * dt
        sem = float(amplitude.std(ddof=1) / np.sqrt(amplitude.size))
        half = amplitude.size // 2
        results[name] = {
            "probe_time_fs": float(t[probe] * AU_TIME_FS),
            "mean_field": float(amplitude.mean()),
            "standard_error": sem,
            "mean_over_standard_error": float(amplitude.mean() / sem),
            "fraction_positive": float(np.mean(amplitude > 0.0)),
            "fraction_negative": float(np.mean(amplitude < 0.0)),
            "split_half_means": [float(amplitude[:half].mean()), float(amplitude[half:].mean())],
            "energy_g2_classical": float(np.mean(energy**2) / np.mean(energy) ** 2),
            "coherent_energy_fraction": float(np.sum(waveforms.mean(axis=1) ** 2) * dt / np.mean(energy)),
        }

    (args.output_dir / "thz_two_color_parity.json").write_text(json.dumps(results, indent=1) + "\n")
    write_manifest(args.output_dir / "parameters.yaml", PARAMS)
    write_manifest(
        args.output_dir / "manifest.yaml",
        {
            "run_id": args.output_dir.name,
            "created": date.today().isoformat(),
            "code_entrypoint": "code/scripts/check_thz_two_color_parity.py",
            "git_commit": current_git_commit(REPO_ROOT),
            "parameter_file": "parameters.yaml",
            "random_seeds": [p["seed"]],
            "observable": "ensemble-mean THz field, its standard error, sign fractions, classical energy g2",
            "units": "atomic units internally; W/cm^2 for intensities; THz field in arbitrary units",
            "notes": (
                "Symmetry check, not a quantitative prediction: local current model, ADK-form rate proxy, "
                "no ionization-saturation or propagation physics, single-quadrature Gaussian BSV amplitude."
            ),
            "outputs": {"results_json": "thz_two_color_parity.json"},
        },
    )
    print(json.dumps(results, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
