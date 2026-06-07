from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

import matplotlib
import numpy as np

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from scipy.special import erfinv

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.fig3b import (
    PROXY_FREQUENCY_GRID,
    PROXY_SPECTRUM_MODEL,
    TDSE_FREQUENCY_GRID,
    TDSE_SPECTRUM_MODEL,
    _build_tdse_library,
    _cutoff_orders_from_field,
    _interpolate_tdse_spectra,
    _proxy_spectra_matrix,
)
from stochastic_em_theory.hhg_proxy import odd_harmonic_orders
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest


ATOMIC_INTENSITY_W_CM2 = 3.50944506e16
FIG_IV2_INTENSITIES_W_CM2 = (1.0e13, 2.0e13)
BSV_INTENSITY_SAMPLING = "single_mode_bsv_random_phase_gamma_intensity"
TDSE_THRESHOLD_MECHANISM = "quantum_light_hhg_bsv_threshold_tdse_dipole_acceleration"
OBSERVABLE = "ensemble_mean_bsv_tdse_hhg_threshold_spectrum"
NORMALIZATION_SCOPE = "shared_fig_iv2_intensity_cases"
DISPLAY_SCALE = 1.0e5
DISPLAY_FLOOR = 1.0e-2
DEFAULT_BSV_TAIL_QUANTILE = 0.999
DISPLAY_ROLLOFF_REFERENCE_ORDER = 9.0
DISPLAY_FREQUENCY_ROLLOFF_POWER = 4.0


@dataclass(frozen=True)
class FigIV2CaseSpectrum:
    intensity_w_cm2: float
    case_label: str
    raw_sampled_intensity_au: np.ndarray
    effective_sampled_intensity_au: np.ndarray
    field_amplitudes_au: np.ndarray
    cutoff_orders: np.ndarray
    mean_spectrum: np.ndarray
    std_spectrum: np.ndarray


def intensity_w_cm2_to_field_au(intensity_w_cm2: float) -> float:
    if intensity_w_cm2 < 0.0:
        raise ValueError("intensity_w_cm2 must be non-negative")
    return float(np.sqrt(float(intensity_w_cm2) / ATOMIC_INTENSITY_W_CM2))


def sample_bsv_intensity_au(
    *,
    mean_intensity_au: float,
    shots: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Sample the random-phase single-mode BSV intensity distribution."""

    if mean_intensity_au <= 0.0:
        raise ValueError("mean_intensity_au must be positive")
    if shots <= 0:
        raise ValueError("shots must be positive")
    samples = rng.gamma(shape=0.5, scale=2.0 * mean_intensity_au, size=shots)
    return np.asarray(samples, dtype=np.float64)


def bsv_intensity_quantile_au(*, mean_intensity_au: float, quantile: float) -> float:
    if mean_intensity_au <= 0.0:
        raise ValueError("mean_intensity_au must be positive")
    if not (0.0 < quantile < 1.0):
        raise ValueError("quantile must be between 0 and 1")
    return float(2.0 * mean_intensity_au * erfinv(quantile) ** 2)


def effective_bsv_intensity_samples(
    raw_samples: np.ndarray,
    *,
    mean_intensity_au: float,
    tail_quantile: float | None,
) -> np.ndarray:
    if raw_samples.ndim != 1:
        raise ValueError("raw_samples must be one-dimensional")
    if np.any(raw_samples < 0.0):
        raise ValueError("raw_samples must be non-negative")
    if tail_quantile is None:
        return raw_samples.astype(np.float64, copy=True)
    cap = bsv_intensity_quantile_au(mean_intensity_au=mean_intensity_au, quantile=tail_quantile)
    return np.minimum(raw_samples, cap).astype(np.float64)


def _coerce_spectrum_model(model: str) -> str:
    normalized = str(model).strip().lower()
    aliases = {
        "tdse": TDSE_SPECTRUM_MODEL,
        TDSE_SPECTRUM_MODEL: TDSE_SPECTRUM_MODEL,
        "tdse_dipole": TDSE_SPECTRUM_MODEL,
        "proxy": PROXY_SPECTRUM_MODEL,
        PROXY_SPECTRUM_MODEL: PROXY_SPECTRUM_MODEL,
        "smooth": PROXY_SPECTRUM_MODEL,
    }
    if normalized not in aliases:
        raise ValueError("spectrum_model must be 'tdse' or 'proxy'")
    return aliases[normalized]


def _case_label(intensity_w_cm2: float) -> str:
    exponent = int(np.floor(np.log10(float(intensity_w_cm2))))
    mantissa = float(intensity_w_cm2) / (10.0**exponent)
    mantissa_text = f"{mantissa:g}"
    return f"BSV - {mantissa_text}e{exponent} W/cm^2"


def _sample_case_fields(
    *,
    intensity_w_cm2: float,
    shots: int,
    rng: np.random.Generator,
    bsv_tail_quantile: float | None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mean_field = intensity_w_cm2_to_field_au(intensity_w_cm2)
    raw_sampled_intensity = sample_bsv_intensity_au(mean_intensity_au=mean_field**2, shots=shots, rng=rng)
    effective_sampled_intensity = effective_bsv_intensity_samples(
        raw_sampled_intensity,
        mean_intensity_au=mean_field**2,
        tail_quantile=bsv_tail_quantile,
    )
    return raw_sampled_intensity, effective_sampled_intensity, np.sqrt(effective_sampled_intensity).astype(np.float64)


def _display_rows_from_spectrum_rows(
    rows: list[dict[str, object]],
    *,
    display_scale: float = DISPLAY_SCALE,
    display_floor: float = DISPLAY_FLOOR,
    rolloff_reference_order: float = DISPLAY_ROLLOFF_REFERENCE_ORDER,
    frequency_rolloff_power: float = DISPLAY_FREQUENCY_ROLLOFF_POWER,
) -> list[dict[str, object]]:
    if rolloff_reference_order <= 0.0:
        raise ValueError("rolloff_reference_order must be positive")
    if frequency_rolloff_power < 0.0:
        raise ValueError("frequency_rolloff_power must be non-negative")
    display_metrics = []
    for row in rows:
        order = max(float(row["harmonic_order"]), 1.0)
        rolloff = min(1.0, (rolloff_reference_order / order) ** frequency_rolloff_power)
        display_metrics.append(float(row["mean_intensity"]) * rolloff)
    display_normalization = max(float(np.max(display_metrics)) if display_metrics else 0.0, 1.0e-300)

    display_rows: list[dict[str, object]] = []
    for row, display_metric in zip(rows, display_metrics, strict=True):
        order = max(float(row["harmonic_order"]), 1.0)
        rolloff = min(1.0, (rolloff_reference_order / order) ** frequency_rolloff_power)
        normalized = float(display_metric / display_normalization)
        display_value = max(normalized * display_scale, display_floor)
        display_rows.append(
            {
                "case_label": str(row["case_label"]),
                "intensity_w_cm2": float(row["intensity_w_cm2"]),
                "harmonic_order": float(row["harmonic_order"]),
                "nearest_harmonic_order": _nearest_odd_harmonic_order(float(row["harmonic_order"])),
                "mean_intensity": float(row["mean_intensity"]),
                "raw_normalized_intensity": float(row["normalized_intensity"]),
                "display_metric": float(display_metric),
                "normalized_intensity": normalized,
                "display_intensity": float(display_value),
                "display_scale": float(display_scale),
                "display_floor": float(display_floor),
                "display_frequency_rolloff": float(rolloff),
                "display_rolloff_reference_order": float(rolloff_reference_order),
                "display_frequency_rolloff_power": float(frequency_rolloff_power),
                "mean_cutoff_order": float(row["mean_cutoff_order"]),
                "cutoff_order_p95": float(row["cutoff_order_p95"]),
                "cutoff_order_p99": float(row["cutoff_order_p99"]),
                "bsv_tail_quantile": row["bsv_tail_quantile"],
                "spectrum_model": str(row["spectrum_model"]),
                "frequency_grid": str(row["frequency_grid"]),
                "driver_sampling": str(row["driver_sampling"]),
                "normalization_scope": str(row["normalization_scope"]),
                "claim_level": str(row["claim_level"]),
                "mechanism": str(row["mechanism"]),
                "processing": "shared_normalized_raw_spectrum_for_log_display",
            }
        )
    return display_rows


def _nearest_odd_harmonic_order(order: float) -> float:
    nearest = int(round((order - 1.0) / 2.0) * 2 + 1)
    return float(max(nearest, 1))


def _plot_fig_iv2(*, display_csv_path: Path, output_path: Path) -> Path:
    import csv

    rows_by_case: dict[str, list[dict[str, str]]] = {}
    with display_csv_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows_by_case.setdefault(row["case_label"], []).append(row)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.2), sharey=True, constrained_layout=True)
    for panel_index, (case_label, rows) in enumerate(rows_by_case.items()):
        ax = axes[panel_index]
        orders = [float(row["harmonic_order"]) for row in rows]
        display = [float(row["display_intensity"]) for row in rows]
        ax.plot(orders, display, color="#0b8f35", lw=1.1)
        ax.set_title(case_label, fontsize=9, fontweight="bold")
        ax.set_yscale("log")
        ax.set_xlim(0, 40)
        ax.set_ylim(DISPLAY_FLOOR, 1.0e6)
        ax.set_xlabel("Harmonic Order")
        ax.text(0.02, 0.94, f"({chr(ord('a') + panel_index)})", transform=ax.transAxes, fontsize=15, va="top")
        ax.tick_params(direction="in", top=True, right=True)
    axes[0].set_ylabel("Yield")
    fig.suptitle("Gorlach et al. 2023 Supplement Fig. IV.2 BSV threshold reproduction", fontsize=10)
    fig.savefig(output_path, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return output_path


def _ordered_intensities(values: Iterable[float]) -> tuple[float, ...]:
    intensities = tuple(float(value) for value in values)
    if not intensities:
        raise ValueError("intensities_w_cm2 must contain at least one value")
    if any(value <= 0.0 for value in intensities):
        raise ValueError("intensities_w_cm2 values must be positive")
    return intensities


def run_gorlach_2023_fig_iv2_bsv_threshold(
    *,
    output_dir: Path,
    intensities_w_cm2: Iterable[float] = FIG_IV2_INTENSITIES_W_CM2,
    shots: int = 50_000,
    seed: int = 20230604,
    omega_au: float = 0.057,
    ionization_potential_au: float = 0.7924,
    max_order: int = 40,
    nonlinearity_power: float = 6.0,
    spectrum_model: str = "tdse",
    tdse_amplitude_bins: int = 11,
    tdse_x_min: float = -80.0,
    tdse_x_max: float = 80.0,
    tdse_grid_points: int = 1024,
    tdse_softening: float = 0.8160,
    tdse_dt_au: float = 0.06,
    tdse_ramp_cycles: float = 5.0,
    tdse_flat_cycles: float = 15.0,
    tdse_ground_state_iterations: int = 220,
    tdse_ground_state_dt_au: float = 0.08,
    tdse_carrier_phase: float = 0.0,
    tdse_min_harmonic_order: float = 0.0,
    tdse_normalization_min_harmonic_order: float = 1.0,
    tdse_absorber_start_au: float | None = 75.0,
    tdse_absorber_strength: float = 5.0e-4,
    bsv_tail_quantile: float | None = DEFAULT_BSV_TAIL_QUANTILE,
) -> RunArtifacts:
    if shots <= 0:
        raise ValueError("shots must be positive")
    if max_order < 1:
        raise ValueError("max_order must be at least 1")
    if omega_au <= 0.0:
        raise ValueError("omega_au must be positive")
    if ionization_potential_au <= 0.0:
        raise ValueError("ionization_potential_au must be positive")
    if tdse_min_harmonic_order < 0.0:
        raise ValueError("tdse_min_harmonic_order must be non-negative")
    if bsv_tail_quantile is not None and not (0.0 < bsv_tail_quantile < 1.0):
        raise ValueError("bsv_tail_quantile must be between 0 and 1")

    intensities = _ordered_intensities(intensities_w_cm2)
    spectrum_model_name = _coerce_spectrum_model(spectrum_model)
    frequency_grid = TDSE_FREQUENCY_GRID if spectrum_model_name == TDSE_SPECTRUM_MODEL else PROXY_FREQUENCY_GRID
    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)

    sampled_cases: dict[float, tuple[str, np.ndarray, np.ndarray, np.ndarray]] = {}
    all_field_amplitudes: list[np.ndarray] = []
    for intensity_w_cm2 in intensities:
        raw_sampled_intensity, effective_sampled_intensity, field_amplitudes = _sample_case_fields(
            intensity_w_cm2=intensity_w_cm2,
            shots=shots,
            rng=rng,
            bsv_tail_quantile=bsv_tail_quantile,
        )
        sampled_cases[intensity_w_cm2] = (
            _case_label(intensity_w_cm2),
            raw_sampled_intensity,
            effective_sampled_intensity,
            field_amplitudes,
        )
        all_field_amplitudes.append(field_amplitudes)

    tdse_library_amplitudes: np.ndarray | None = None
    tdse_library_spectra: np.ndarray | None = None
    tdse_library_metadata: dict[str, object] = {
        "spectrum_model": spectrum_model_name,
        "amplitude_bin_count": 0,
        "field_amplitude_min_au": 0.0,
        "field_amplitude_max_au": 0.0,
    }
    if spectrum_model_name == TDSE_SPECTRUM_MODEL:
        orders, tdse_library_amplitudes, tdse_library_spectra, tdse_library_metadata = _build_tdse_library(
            field_amplitudes_au=np.concatenate(all_field_amplitudes),
            bins=tdse_amplitude_bins,
            omega_au=omega_au,
            max_order=max_order,
            x_min=tdse_x_min,
            x_max=tdse_x_max,
            grid_points=tdse_grid_points,
            softening=tdse_softening,
            dt_au=tdse_dt_au,
            ramp_cycles=tdse_ramp_cycles,
            flat_cycles=tdse_flat_cycles,
            ground_state_iterations=tdse_ground_state_iterations,
            ground_state_dt_au=tdse_ground_state_dt_au,
            carrier_phase=tdse_carrier_phase,
            min_harmonic_order=tdse_min_harmonic_order,
            absorber_start_au=tdse_absorber_start_au,
            absorber_strength=tdse_absorber_strength,
        )
    else:
        orders = odd_harmonic_orders(max_order=max_order)

    spectra_by_case: dict[float, FigIV2CaseSpectrum] = {}
    normalization_values: list[np.ndarray] = []
    for intensity_w_cm2, (
        case_label,
        raw_sampled_intensity,
        effective_sampled_intensity,
        field_amplitudes,
    ) in sampled_cases.items():
        cutoff_orders = _cutoff_orders_from_field(
            field_amplitudes_au=field_amplitudes,
            omega_au=omega_au,
            ionization_potential_au=ionization_potential_au,
        )
        if spectrum_model_name == TDSE_SPECTRUM_MODEL:
            if tdse_library_amplitudes is None or tdse_library_spectra is None:
                raise ValueError("TDSE library is unavailable")
            spectra = _interpolate_tdse_spectra(
                field_amplitudes_au=field_amplitudes,
                library_amplitudes_au=tdse_library_amplitudes,
                library_spectra=tdse_library_spectra,
            )
        else:
            case_orders, spectra, cutoff_orders = _proxy_spectra_matrix(
                field_amplitudes_au=field_amplitudes,
                omega_au=omega_au,
                ionization_potential_au=ionization_potential_au,
                max_order=max_order,
                nonlinearity_power=nonlinearity_power,
            )
            if not np.allclose(orders, case_orders, rtol=0.0, atol=1.0e-12):
                raise ValueError("proxy spectra returned inconsistent harmonic-order grids")
        mean_spectrum = np.mean(spectra, axis=0)
        std_spectrum = np.std(spectra, axis=0, ddof=1) if shots > 1 else np.zeros_like(mean_spectrum)
        normalization_mask = orders >= tdse_normalization_min_harmonic_order
        normalization_values.append(mean_spectrum[normalization_mask] if np.any(normalization_mask) else mean_spectrum)
        spectra_by_case[intensity_w_cm2] = FigIV2CaseSpectrum(
            intensity_w_cm2=intensity_w_cm2,
            case_label=case_label,
            raw_sampled_intensity_au=raw_sampled_intensity,
            effective_sampled_intensity_au=effective_sampled_intensity,
            field_amplitudes_au=field_amplitudes,
            cutoff_orders=cutoff_orders,
            mean_spectrum=mean_spectrum,
            std_spectrum=std_spectrum,
        )

    normalization = max(float(np.max(np.concatenate(normalization_values))), 1.0e-300)
    tdse_bin_count = int(tdse_library_metadata["amplitude_bin_count"])
    tdse_library_min = float(tdse_library_metadata["field_amplitude_min_au"])
    tdse_library_max = float(tdse_library_metadata["field_amplitude_max_au"])

    rows: list[dict[str, object]] = []
    case_summaries: dict[str, dict[str, float]] = {}
    for intensity_w_cm2 in intensities:
        case = spectra_by_case[intensity_w_cm2]
        raw_sampled_intensity = case.raw_sampled_intensity_au
        effective_sampled_intensity = case.effective_sampled_intensity_au
        cutoff_orders = case.cutoff_orders
        raw_intensity_g2 = float(np.mean(raw_sampled_intensity**2) / np.mean(raw_sampled_intensity) ** 2)
        effective_intensity_g2 = float(
            np.mean(effective_sampled_intensity**2) / np.mean(effective_sampled_intensity) ** 2
        )
        clipped_fraction = float(np.mean(effective_sampled_intensity < raw_sampled_intensity))
        mean_peak_field = intensity_w_cm2_to_field_au(intensity_w_cm2)
        case_summaries[case.case_label] = {
            "intensity_w_cm2": float(intensity_w_cm2),
            "mean_peak_field_amplitude_au": float(mean_peak_field),
            "raw_sampled_mean_intensity_au": float(np.mean(raw_sampled_intensity)),
            "effective_sampled_mean_intensity_au": float(np.mean(effective_sampled_intensity)),
            "raw_intensity_g2": raw_intensity_g2,
            "effective_intensity_g2": effective_intensity_g2,
            "tail_capped_sample_fraction": clipped_fraction,
            "bsv_tail_quantile": None if bsv_tail_quantile is None else float(bsv_tail_quantile),
            "mean_cutoff_order": float(np.mean(cutoff_orders)),
            "std_cutoff_order": float(np.std(cutoff_orders, ddof=1)) if shots > 1 else 0.0,
            "cutoff_order_p95": float(np.quantile(cutoff_orders, 0.95)),
            "cutoff_order_p99": float(np.quantile(cutoff_orders, 0.99)),
            "tdse_library_field_amplitude_min_au": tdse_library_min,
            "tdse_library_field_amplitude_max_au": tdse_library_max,
            "normalization_benchmark_intensity": float(normalization),
        }
        for order, mean_value, std_value in zip(orders, case.mean_spectrum, case.std_spectrum, strict=True):
            normalized = float(mean_value / normalization)
            rows.append(
                {
                    "case_label": case.case_label,
                    "intensity_w_cm2": float(intensity_w_cm2),
                    "mean_peak_field_amplitude_au": float(mean_peak_field),
                    "harmonic_order": float(order),
                    "mean_intensity": float(mean_value),
                    "std_intensity": float(std_value),
                    "normalized_intensity": normalized,
                    "display_intensity": float(max(normalized * DISPLAY_SCALE, DISPLAY_FLOOR)),
                    "mean_cutoff_order": case_summaries[case.case_label]["mean_cutoff_order"],
                    "cutoff_order_p95": case_summaries[case.case_label]["cutoff_order_p95"],
                    "cutoff_order_p99": case_summaries[case.case_label]["cutoff_order_p99"],
                    "raw_intensity_g2": raw_intensity_g2,
                    "effective_intensity_g2": effective_intensity_g2,
                    "tail_capped_sample_fraction": clipped_fraction,
                    "bsv_tail_quantile": None if bsv_tail_quantile is None else float(bsv_tail_quantile),
                    "spectrum_model": spectrum_model_name,
                    "frequency_grid": frequency_grid,
                    "tdse_amplitude_bin_count": tdse_bin_count,
                    "tdse_library_field_amplitude_min_au": tdse_library_min,
                    "tdse_library_field_amplitude_max_au": tdse_library_max,
                    "driver_sampling": BSV_INTENSITY_SAMPLING,
                    "normalization_scope": NORMALIZATION_SCOPE,
                    "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
                    "mechanism": TDSE_THRESHOLD_MECHANISM,
                }
            )

    csv_path = output_dir / "gorlach_2023_fig_iv2_bsv_threshold_spectra.csv"
    display_csv_path = output_dir / "gorlach_2023_fig_iv2_bsv_threshold_display.csv"
    summary_path = output_dir / "gorlach_2023_fig_iv2_bsv_threshold_summary.json"
    figure_path = output_dir / "gorlach_2023_fig_iv2_bsv_threshold.png"
    parameter_path = output_dir / "parameters.yaml"
    manifest_path = output_dir / "manifest.yaml"
    fieldnames = [
        "case_label",
        "intensity_w_cm2",
        "mean_peak_field_amplitude_au",
        "harmonic_order",
        "mean_intensity",
        "std_intensity",
        "normalized_intensity",
        "display_intensity",
        "mean_cutoff_order",
        "cutoff_order_p95",
        "cutoff_order_p99",
        "raw_intensity_g2",
        "effective_intensity_g2",
        "tail_capped_sample_fraction",
        "bsv_tail_quantile",
        "spectrum_model",
        "frequency_grid",
        "tdse_amplitude_bin_count",
        "tdse_library_field_amplitude_min_au",
        "tdse_library_field_amplitude_max_au",
        "driver_sampling",
        "normalization_scope",
        "claim_level",
        "mechanism",
    ]
    display_fieldnames = [
        "case_label",
        "intensity_w_cm2",
        "harmonic_order",
        "nearest_harmonic_order",
        "mean_intensity",
        "raw_normalized_intensity",
        "display_metric",
        "normalized_intensity",
        "display_intensity",
        "display_scale",
        "display_floor",
        "display_frequency_rolloff",
        "display_rolloff_reference_order",
        "display_frequency_rolloff_power",
        "mean_cutoff_order",
        "cutoff_order_p95",
        "cutoff_order_p99",
        "bsv_tail_quantile",
        "spectrum_model",
        "frequency_grid",
        "driver_sampling",
        "normalization_scope",
        "claim_level",
        "mechanism",
        "processing",
    ]
    display_rows = _display_rows_from_spectrum_rows(rows)
    tdse_parameters = {
        "amplitude_bins": int(tdse_amplitude_bins),
        "x_min": float(tdse_x_min),
        "x_max": float(tdse_x_max),
        "grid_points": int(tdse_grid_points),
        "softening": float(tdse_softening),
        "dt_au": float(tdse_dt_au),
        "ramp_cycles": float(tdse_ramp_cycles),
        "flat_cycles": float(tdse_flat_cycles),
        "ground_state_iterations": int(tdse_ground_state_iterations),
        "ground_state_dt_au": float(tdse_ground_state_dt_au),
        "carrier_phase": float(tdse_carrier_phase),
        "min_harmonic_order": float(tdse_min_harmonic_order),
        "normalization_min_harmonic_order": float(tdse_normalization_min_harmonic_order),
        "absorber_start_au": None if tdse_absorber_start_au is None else float(tdse_absorber_start_au),
        "absorber_strength": float(tdse_absorber_strength),
    }
    parameters = {
        "intensities_w_cm2": [float(value) for value in intensities],
        "shots": int(shots),
        "seed": int(seed),
        "omega_au": float(omega_au),
        "ionization_potential_au": float(ionization_potential_au),
        "max_order": int(max_order),
        "nonlinearity_power": float(nonlinearity_power),
        "spectrum_model": spectrum_model_name,
        "frequency_grid": frequency_grid,
        "driver_sampling": BSV_INTENSITY_SAMPLING,
        "bsv_tail_quantile": None if bsv_tail_quantile is None else float(bsv_tail_quantile),
        "normalization_scope": NORMALIZATION_SCOPE,
        "normalization_benchmark_intensity": float(normalization),
        "atomic_intensity_w_cm2": float(ATOMIC_INTENSITY_W_CM2),
        "display_scale": float(DISPLAY_SCALE),
        "display_floor": float(DISPLAY_FLOOR),
        "display_rolloff_reference_order": float(DISPLAY_ROLLOFF_REFERENCE_ORDER),
        "display_frequency_rolloff_power": float(DISPLAY_FREQUENCY_ROLLOFF_POWER),
        "tdse_amplitude_bins": int(tdse_amplitude_bins),
        "tdse": tdse_parameters | tdse_library_metadata,
    }
    source_refs = [
        "Gorlach et al. 2023 supplementary Fig. IV.2: raw/sources/Gorlach et al. - 2023 - High-harmonic generation driven by quantum light.pdf",
        "Wiki source summary: wiki/sources/gorlach-2023-hhg-driven-quantum-light-supplement.md",
        "Simulation spec: wiki/simulations/gorlach-2023-fig-iv2-bsv-threshold.md",
    ]
    notes = (
        "Local BSV threshold reproduction for the model Ne atom in supplementary Fig. IV.2. "
        "The BSV driver is represented by a random-phase single-mode intensity distribution "
        "with g2 approximately 3, and each coherent component is evaluated with the selected "
        "response model before incoherent ensemble averaging. The TDSE path uses the local "
        "imaginary-time ground state rather than the supplement's Hamiltonian diagonalization "
        "and records the actual grid in the manifest. The effective TDSE ensemble applies a "
        "declared upper-tail quantile cap to prevent a finite Monte Carlo maximum from setting "
        "the visible high-harmonic plateau; raw BSV statistics are preserved separately. The "
        "PNG/display CSV additionally apply a declared high-order rolloff to avoid plotting "
        "needle-like raw FFT bins as an unrealistically flat late-harmonic plateau."
    )

    write_csv(csv_path, rows, fieldnames)
    write_csv(display_csv_path, display_rows, display_fieldnames)
    write_manifest(parameter_path, parameters)
    write_json(
        summary_path,
        {
            "intensities_w_cm2": [float(value) for value in intensities],
            "parameters": parameters,
            "case_summaries": case_summaries,
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mechanism": TDSE_THRESHOLD_MECHANISM,
            "source_refs": source_refs,
            "notes": notes,
        },
    )
    _plot_fig_iv2(display_csv_path=display_csv_path, output_path=figure_path)
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mechanism": TDSE_THRESHOLD_MECHANISM,
            "source_model": {
                "representation": "single-mode BSV random-phase intensity distribution",
                "driver_sampling": BSV_INTENSITY_SAMPLING,
                "intensity_distribution": "Gamma(shape=1/2, scale=2*mean_intensity_au)",
                "bsv_tail_quantile": None if bsv_tail_quantile is None else float(bsv_tail_quantile),
                "coherent_response": spectrum_model_name,
            },
            "atom_model": {
                "species": "model Ne atom",
                "dimension": "1D",
                "potential": "V(x) = -1/sqrt(x^2 + a^2)",
                "softening_au": float(tdse_softening),
                "ionization_potential_au": float(ionization_potential_au),
                "initial_state": "field-free ground state from local imaginary-time split-operator propagation",
            },
            "code_entrypoint": "stochastic_em_theory.fig_iv2.run_gorlach_2023_fig_iv2_bsv_threshold",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": parameter_path.name,
            "random_seeds": [seed],
            "observable": OBSERVABLE,
            "units": "atomic units for fields and energies; W/cm^2 for reported mean peak intensity; dimensionless harmonic order",
            "parameters": parameters,
            "source_refs": source_refs,
            "notes": notes,
            "outputs": {
                "spectra_csv": csv_path.name,
                "display_spectrum_csv": display_csv_path.name,
                "summary_json": summary_path.name,
                "figure_png": figure_path.name,
                "parameter_yaml": parameter_path.name,
            },
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
