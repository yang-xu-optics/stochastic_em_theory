from __future__ import annotations

import argparse
from pathlib import Path

from stochastic_em_theory.fig_iv2 import (
    DEFAULT_BSV_TAIL_QUANTILE,
    FIG_IV2_INTENSITIES_W_CM2,
    run_gorlach_2023_fig_iv2_bsv_threshold,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "gorlach-2023-fig-iv2-bsv-threshold"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reproduce Gorlach et al. 2023 supplement Fig. IV.2 with BSV sampling and TDSE spectra."
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--intensities-w-cm2", type=float, nargs="+", default=list(FIG_IV2_INTENSITIES_W_CM2))
    parser.add_argument("--shots", type=int, default=50_000)
    parser.add_argument("--seed", type=int, default=20230604)
    parser.add_argument("--omega-au", type=float, default=0.057)
    parser.add_argument("--ionization-potential-au", type=float, default=0.7924)
    parser.add_argument("--max-order", type=int, default=40)
    parser.add_argument("--nonlinearity-power", type=float, default=6.0)
    parser.add_argument("--spectrum-model", choices=["tdse", "proxy"], default="tdse")
    parser.add_argument("--tdse-amplitude-bins", type=int, default=11)
    parser.add_argument("--tdse-x-min", type=float, default=-80.0)
    parser.add_argument("--tdse-x-max", type=float, default=80.0)
    parser.add_argument("--tdse-grid-points", type=int, default=1024)
    parser.add_argument("--tdse-softening", type=float, default=0.8160)
    parser.add_argument("--tdse-dt-au", type=float, default=0.06)
    parser.add_argument("--tdse-ramp-cycles", type=float, default=5.0)
    parser.add_argument("--tdse-flat-cycles", type=float, default=15.0)
    parser.add_argument("--tdse-ground-state-iterations", type=int, default=220)
    parser.add_argument("--tdse-ground-state-dt-au", type=float, default=0.08)
    parser.add_argument("--tdse-carrier-phase", type=float, default=0.0)
    parser.add_argument("--tdse-min-harmonic-order", type=float, default=0.0)
    parser.add_argument("--tdse-normalization-min-harmonic-order", type=float, default=1.0)
    parser.add_argument("--tdse-absorber-start-au", type=float, default=75.0)
    parser.add_argument("--tdse-absorber-strength", type=float, default=5.0e-4)
    parser.add_argument("--bsv-tail-quantile", type=float, default=DEFAULT_BSV_TAIL_QUANTILE)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    artifacts = run_gorlach_2023_fig_iv2_bsv_threshold(
        output_dir=args.output_dir,
        intensities_w_cm2=args.intensities_w_cm2,
        shots=args.shots,
        seed=args.seed,
        omega_au=args.omega_au,
        ionization_potential_au=args.ionization_potential_au,
        max_order=args.max_order,
        nonlinearity_power=args.nonlinearity_power,
        spectrum_model=args.spectrum_model,
        tdse_amplitude_bins=args.tdse_amplitude_bins,
        tdse_x_min=args.tdse_x_min,
        tdse_x_max=args.tdse_x_max,
        tdse_grid_points=args.tdse_grid_points,
        tdse_softening=args.tdse_softening,
        tdse_dt_au=args.tdse_dt_au,
        tdse_ramp_cycles=args.tdse_ramp_cycles,
        tdse_flat_cycles=args.tdse_flat_cycles,
        tdse_ground_state_iterations=args.tdse_ground_state_iterations,
        tdse_ground_state_dt_au=args.tdse_ground_state_dt_au,
        tdse_carrier_phase=args.tdse_carrier_phase,
        tdse_min_harmonic_order=args.tdse_min_harmonic_order,
        tdse_normalization_min_harmonic_order=args.tdse_normalization_min_harmonic_order,
        tdse_absorber_start_au=args.tdse_absorber_start_au,
        tdse_absorber_strength=args.tdse_absorber_strength,
        bsv_tail_quantile=args.bsv_tail_quantile,
    )
    print(artifacts.csv_path)
    print(artifacts.summary_path)
    print(artifacts.output_dir / "gorlach_2023_fig_iv2_bsv_threshold.png")
    print(artifacts.manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
