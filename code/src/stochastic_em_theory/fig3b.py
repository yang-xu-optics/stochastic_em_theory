from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.fields import sample_single_mode_husimi_q
from stochastic_em_theory.hhg_proxy import odd_harmonic_orders
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest


MECHANISM = "quantum_light_hhg_spectra_proxy"
FIELD_NORMALIZATION = "field_amplitude = base_field_amplitude_au * sqrt(|alpha|^2 / mean(|alpha|^2))"
DRIVER_SAMPLING = "single_mode_husimi_q_fig3b"


class Fig3BDriverState(str, Enum):
    COHERENT = "coherent"
    FOCK = "fock"
    THERMAL = "thermal"
    BSV = "bsv"


@dataclass(frozen=True)
class Fig3BStateStyle:
    label: str
    color: str
    display_offset: float


STATE_STYLES: dict[Fig3BDriverState, Fig3BStateStyle] = {
    Fig3BDriverState.COHERENT: Fig3BStateStyle("Coherent", "#e41a1c", 1.0),
    Fig3BDriverState.FOCK: Fig3BStateStyle("Fock", "#377eb8", 6.0),
    Fig3BDriverState.THERMAL: Fig3BStateStyle("Thermal", "#ff7f00", 30.0),
    Fig3BDriverState.BSV: Fig3BStateStyle("BSV", "#4daf4a", 150.0),
}


def _complex_normal(
    *,
    rng: np.random.Generator,
    shots: int,
    variance_abs2: float,
    center: complex = 0.0j,
) -> np.ndarray:
    if variance_abs2 <= 0:
        raise ValueError("variance_abs2 must be positive")
    std = np.sqrt(variance_abs2 / 2.0)
    real = rng.normal(loc=np.real(center), scale=std, size=shots)
    imag = rng.normal(loc=np.imag(center), scale=std, size=shots)
    return (real + 1j * imag).astype(np.complex128)


def sample_fig3b_driver_alpha(
    state: Fig3BDriverState | str,
    *,
    shots: int,
    rng: np.random.Generator,
    mean_photon_number: float,
    fock_n: int,
    bsv_r: float,
    bsv_phase: float,
) -> np.ndarray:
    """Sample single-mode Husimi-Q coherent amplitudes for the Fig. 3b states."""

    if shots <= 0:
        raise ValueError("shots must be positive")
    if mean_photon_number < 0:
        raise ValueError("mean_photon_number must be non-negative")
    if fock_n < 0:
        raise ValueError("fock_n must be non-negative")

    driver_state = Fig3BDriverState(state)
    if driver_state is Fig3BDriverState.COHERENT:
        return _complex_normal(
            rng=rng,
            shots=shots,
            variance_abs2=1.0,
            center=np.sqrt(mean_photon_number) + 0.0j,
        )
    if driver_state is Fig3BDriverState.FOCK:
        radius_squared = rng.gamma(shape=fock_n + 1.0, scale=1.0, size=shots)
        phase = rng.uniform(0.0, 2.0 * np.pi, size=shots)
        return (np.sqrt(radius_squared) * np.exp(1j * phase)).astype(np.complex128)
    if driver_state is Fig3BDriverState.THERMAL:
        return _complex_normal(rng=rng, shots=shots, variance_abs2=mean_photon_number + 1.0)
    return sample_single_mode_husimi_q(r=bsv_r, phase=bsv_phase, shots=shots, rng=rng)


def _field_amplitudes_from_alpha(*, alpha: np.ndarray, base_field_amplitude_au: float) -> np.ndarray:
    if base_field_amplitude_au <= 0:
        raise ValueError("base_field_amplitude_au must be positive")
    intensity = np.abs(alpha) ** 2
    mean_intensity = float(np.mean(intensity))
    if mean_intensity <= 0:
        raise ValueError("sampled driver intensity mean must be positive")
    return (base_field_amplitude_au * np.sqrt(intensity / mean_intensity)).astype(np.float64)


def _proxy_spectra_matrix(
    *,
    field_amplitudes_au: np.ndarray,
    omega_au: float,
    ionization_potential_au: float,
    max_order: int,
    nonlinearity_power: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if omega_au <= 0:
        raise ValueError("omega_au must be positive")
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    if nonlinearity_power <= 0:
        raise ValueError("nonlinearity_power must be positive")

    orders = odd_harmonic_orders(max_order=max_order)
    up = np.square(field_amplitudes_au) / (4.0 * omega_au**2)
    cutoff_orders = (ionization_potential_au + 3.17 * up) / omega_au
    plateau = np.power(np.maximum(field_amplitudes_au, 0.0), nonlinearity_power)
    rolloff_denominator = np.maximum(cutoff_orders, 1.0)
    rolloff = np.exp(-np.maximum(orders[None, :] - cutoff_orders[:, None], 0.0) / rolloff_denominator[:, None])
    low_order_suppression = 1.0 - np.exp(-orders / 3.0)
    spectra = plateau[:, None] * rolloff * low_order_suppression[None, :]
    return orders, spectra.astype(np.float64), cutoff_orders.astype(np.float64)


def _plot_fig3b_proxy(*, csv_path: Path, output_path: Path) -> Path:
    import csv

    rows_by_state: dict[str, list[dict[str, str]]] = {state.value: [] for state in Fig3BDriverState}
    with csv_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows_by_state[row["driver_state"]].append(row)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.8, 4.4), constrained_layout=True)
    for state in Fig3BDriverState:
        style = STATE_STYLES[state]
        rows = rows_by_state[state.value]
        orders = [float(row["harmonic_order"]) for row in rows]
        display = [float(row["display_intensity"]) for row in rows]
        ax.plot(orders, display, color=style.color, lw=1.4, label=style.label)

    ax.set_yscale("log")
    ax.set_xlim(0, 151)
    ax.set_xlabel("Harmonic order")
    ax.set_ylabel("Proxy emission energy")
    ax.set_title("Gorlach et al. 2023 Fig. 3b proxy reproduction")
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(1.01, 1.0), borderaxespad=0.0)
    ax.grid(alpha=0.2)
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return output_path


def run_gorlach_2023_fig3b_proxy(
    *,
    output_dir: Path,
    shots: int = 50_000,
    seed: int = 20230603,
    base_field_amplitude_au: float = 0.08,
    omega_au: float = 0.057,
    ionization_potential_au: float = 0.7924,
    max_order: int = 151,
    mean_photon_number: float = 100.0,
    fock_n: int = 100,
    bsv_r: float = 2.0,
    bsv_phase: float = 0.0,
    nonlinearity_power: float = 6.0,
) -> RunArtifacts:
    """Run a local stochastic-field proxy reproduction of Nature Fig. 3b."""

    if shots <= 0:
        raise ValueError("shots must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    rows: list[dict[str, object]] = []
    state_summaries: dict[str, dict[str, float]] = {}

    for state in Fig3BDriverState:
        alpha = sample_fig3b_driver_alpha(
            state,
            shots=shots,
            rng=rng,
            mean_photon_number=mean_photon_number,
            fock_n=fock_n,
            bsv_r=bsv_r,
            bsv_phase=bsv_phase,
        )
        sampled_intensity = np.abs(alpha) ** 2
        field_amplitudes = _field_amplitudes_from_alpha(alpha=alpha, base_field_amplitude_au=base_field_amplitude_au)
        orders, spectra, cutoff_orders = _proxy_spectra_matrix(
            field_amplitudes_au=field_amplitudes,
            omega_au=omega_au,
            ionization_potential_au=ionization_potential_au,
            max_order=max_order,
            nonlinearity_power=nonlinearity_power,
        )
        mean_spectrum = np.mean(spectra, axis=0)
        std_spectrum = np.std(spectra, axis=0, ddof=1) if shots > 1 else np.zeros_like(mean_spectrum)
        normalization = max(float(np.max(mean_spectrum)), 1.0e-300)
        style = STATE_STYLES[state]

        state_summaries[state.value] = {
            "mean_alpha_abs2": float(np.mean(sampled_intensity)),
            "normalized_intensity_cv": float(np.std(sampled_intensity / np.mean(sampled_intensity))),
            "mean_field_amplitude_au": float(np.mean(field_amplitudes)),
            "mean_cutoff_order": float(np.mean(cutoff_orders)),
            "std_cutoff_order": float(np.std(cutoff_orders, ddof=1)) if shots > 1 else 0.0,
            "cutoff_order_p95": float(np.quantile(cutoff_orders, 0.95)),
            "cutoff_order_p99": float(np.quantile(cutoff_orders, 0.99)),
            "display_offset": float(style.display_offset),
        }

        for order, mean_value, std_value in zip(orders, mean_spectrum, std_spectrum, strict=True):
            normalized = float(mean_value / normalization)
            rows.append(
                {
                    "driver_state": state.value,
                    "harmonic_order": float(order),
                    "mean_intensity": float(mean_value),
                    "std_intensity": float(std_value),
                    "normalized_intensity": normalized,
                    "display_intensity": float(normalized * style.display_offset),
                    "display_offset": style.display_offset,
                    "mean_cutoff_order": state_summaries[state.value]["mean_cutoff_order"],
                    "normalized_intensity_cv": state_summaries[state.value]["normalized_intensity_cv"],
                    "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
                    "mechanism": MECHANISM,
                }
            )

    csv_path = output_dir / "gorlach_2023_fig3b_proxy_spectra.csv"
    summary_path = output_dir / "gorlach_2023_fig3b_proxy_summary.json"
    figure_path = output_dir / "gorlach_2023_fig3b_proxy.png"
    manifest_path = output_dir / "manifest.yaml"
    fieldnames = [
        "driver_state",
        "harmonic_order",
        "mean_intensity",
        "std_intensity",
        "normalized_intensity",
        "display_intensity",
        "display_offset",
        "mean_cutoff_order",
        "normalized_intensity_cv",
        "claim_level",
        "mechanism",
    ]
    parameters = {
        "shots": int(shots),
        "seed": int(seed),
        "base_field_amplitude_au": float(base_field_amplitude_au),
        "omega_au": float(omega_au),
        "ionization_potential_au": float(ionization_potential_au),
        "max_order": int(max_order),
        "mean_photon_number": float(mean_photon_number),
        "fock_n": int(fock_n),
        "bsv_r": float(bsv_r),
        "bsv_phase": float(bsv_phase),
        "nonlinearity_power": float(nonlinearity_power),
        "driver_sampling": DRIVER_SAMPLING,
        "field_normalization": FIELD_NORMALIZATION,
    }
    source_refs = [
        "Nature Fig. 3b image and source-data link: https://www.nature.com/articles/s41567-023-02127-y",
        "Public source data archive: https://static-content.springer.com/esm/art%3A10.1038%2Fs41567-023-02127-y/MediaObjects/41567_2023_2127_MOESM2_ESM.zip",
        "Local supplement: raw/sources/Gorlach et al. - 2023 - High-harmonic generation driven by quantum light.pdf",
        "Wiki source summary: wiki/sources/gorlach-2023-hhg-driven-quantum-light-supplement.md",
    ]
    notes = (
        "Single-mode Husimi-Q coherent-response HHG proxy for the qualitative "
        "coherent/Fock/thermal/BSV ordering in Gorlach et al. 2023 Fig. 3b; "
        "not a TDSE reproduction of the published source-data curves."
    )

    write_csv(csv_path, rows, fieldnames)
    write_json(
        summary_path,
        {
            "driver_states": [state.value for state in Fig3BDriverState],
            "parameters": parameters,
            "state_summaries": state_summaries,
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mechanism": MECHANISM,
            "source_refs": source_refs,
            "notes": notes,
        },
    )
    _plot_fig3b_proxy(csv_path=csv_path, output_path=figure_path)
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mechanism": MECHANISM,
            "source_model": {
                "representation": "Husimi-Q coherent-state sampling",
                "driver_states": [state.value for state in Fig3BDriverState],
                "field_normalization": FIELD_NORMALIZATION,
            },
            "code_entrypoint": "stochastic_em_theory.fig3b.run_gorlach_2023_fig3b_proxy",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "ensemble_mean_proxy_hhg_spectrum_by_driver_state",
            "units": "atomic units for fields and energies; dimensionless harmonic order",
            "parameters": parameters,
            "source_refs": source_refs,
            "notes": notes,
            "outputs": {
                "spectra_csv": csv_path.name,
                "summary_json": summary_path.name,
                "figure_png": figure_path.name,
            },
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
