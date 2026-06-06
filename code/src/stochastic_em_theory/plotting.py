from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def _read_csv_columns(csv_path: Path) -> dict[str, list[float]]:
    with csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"{csv_path} contains no data rows")
    columns: dict[str, list[float]] = {key: [] for key in rows[0]}
    for row in rows:
        for key, value in row.items():
            try:
                columns[key].append(float(value))
            except ValueError:
                continue
    return columns


def plot_single_mode_g2(*, csv_path: Path, output_path: Path) -> Path:
    columns = _read_csv_columns(csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.0, 4.0), constrained_layout=True)
    ax.plot(columns["r"], columns["analytic_g2"], color="black", label="analytic")
    ax.scatter(columns["r"], columns["g2_corrected"], color="#0072B2", label="corrected Wigner")
    ax.scatter(columns["r"], columns["g2_naive"], color="#D55E00", marker="x", label="naive raw moment")
    ax.set_xlabel("squeezing parameter r")
    ax.set_ylabel("g^(2)(0)")
    ax.set_title("Single-mode squeezed-vacuum photon-counting validation")
    ax.legend(frameon=False)
    ax.grid(alpha=0.25)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def plot_multimode_g2(*, csv_path: Path, output_path: Path) -> Path:
    columns = _read_csv_columns(csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.0, 4.0), constrained_layout=True)
    ax.plot(columns["modes"], columns["analytic_g2"], color="black", label="analytic")
    ax.scatter(columns["modes"], columns["g2_corrected"], color="#009E73", label="corrected Wigner")
    ax.set_xlabel("number of equal detected modes")
    ax.set_ylabel("total g^(2)(0)")
    ax.set_title("Mode-filtered squeezed-vacuum validation")
    ax.legend(frameon=False)
    ax.grid(alpha=0.25)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def plot_proxy_hhg_spectrum(*, csv_path: Path, output_path: Path) -> Path:
    columns = _read_csv_columns(csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.0, 4.0), constrained_layout=True)
    ax.plot(columns["harmonic_order"], columns["mean_intensity"], color="#0072B2", label="ensemble mean")
    ax.plot(columns["harmonic_order"], columns["conditional_low"], color="#999999", linestyle="--", label="low intensity bin")
    ax.plot(columns["harmonic_order"], columns["conditional_high"], color="#D55E00", linestyle="--", label="high intensity bin")
    ax.set_yscale("log")
    ax.set_xlabel("harmonic order")
    ax.set_ylabel("proxy intensity")
    ax.set_title("Squeezed-drive HHG proxy ensemble")
    ax.legend(frameon=False)
    ax.grid(alpha=0.25)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path
