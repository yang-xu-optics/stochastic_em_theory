from __future__ import annotations

import argparse
from pathlib import Path

from stochastic_em_theory.ensemble import run_proxy_hhg_ensemble
from stochastic_em_theory.plotting import plot_multimode_g2, plot_single_mode_g2
from stochastic_em_theory.validation import run_multimode_validation, run_single_mode_validation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="stochastic-em-theory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    single = subparsers.add_parser("single-mode", help="run single-mode squeezed-vacuum g2 validation")
    single.add_argument("--r-values", nargs="+", type=float, required=True)
    single.add_argument("--shots", type=int, required=True)
    single.add_argument("--seed", type=int, required=True)
    single.add_argument("--output-dir", type=Path, required=True)

    multimode = subparsers.add_parser("multimode", help="run equal-mode squeezed-vacuum g2 validation")
    multimode.add_argument("--r", type=float, required=True)
    multimode.add_argument("--mode-counts", nargs="+", type=int, required=True)
    multimode.add_argument("--shots", type=int, required=True)
    multimode.add_argument("--seed", type=int, required=True)
    multimode.add_argument("--output-dir", type=Path, required=True)

    proxy_hhg = subparsers.add_parser("proxy-hhg", help="run proxy HHG ensemble with squeezed Husimi-Q samples")
    proxy_hhg.add_argument("--r", type=float, required=True)
    proxy_hhg.add_argument("--phase", type=float, default=0.0)
    proxy_hhg.add_argument("--shots", type=int, required=True)
    proxy_hhg.add_argument("--seed", type=int, required=True)
    proxy_hhg.add_argument("--base-field-amplitude-au", type=float, required=True)
    proxy_hhg.add_argument("--omega-au", type=float, default=0.057)
    proxy_hhg.add_argument("--ionization-potential-au", type=float, default=0.7924)
    proxy_hhg.add_argument("--max-order", type=int, default=31)
    proxy_hhg.add_argument("--output-dir", type=Path, required=True)

    plot_single = subparsers.add_parser("plot-single-mode", help="plot single-mode g2 validation CSV")
    plot_single.add_argument("--csv-path", type=Path, required=True)
    plot_single.add_argument("--output-path", type=Path, required=True)

    plot_multi = subparsers.add_parser("plot-multimode", help="plot multimode g2 validation CSV")
    plot_multi.add_argument("--csv-path", type=Path, required=True)
    plot_multi.add_argument("--output-path", type=Path, required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "single-mode":
        artifacts = run_single_mode_validation(
            r_values=args.r_values,
            shots=args.shots,
            seed=args.seed,
            output_dir=args.output_dir,
        )
        print(artifacts.output_dir)
        return 0
    if args.command == "multimode":
        artifacts = run_multimode_validation(
            r=args.r,
            mode_counts=args.mode_counts,
            shots=args.shots,
            seed=args.seed,
            output_dir=args.output_dir,
        )
        print(artifacts.output_dir)
        return 0
    if args.command == "proxy-hhg":
        artifacts = run_proxy_hhg_ensemble(
            r=args.r,
            phase=args.phase,
            shots=args.shots,
            seed=args.seed,
            base_field_amplitude_au=args.base_field_amplitude_au,
            omega_au=args.omega_au,
            ionization_potential_au=args.ionization_potential_au,
            max_order=args.max_order,
            output_dir=args.output_dir,
        )
        print(artifacts.output_dir)
        return 0
    if args.command == "plot-single-mode":
        print(plot_single_mode_g2(csv_path=args.csv_path, output_path=args.output_path))
        return 0
    if args.command == "plot-multimode":
        print(plot_multimode_g2(csv_path=args.csv_path, output_path=args.output_path))
        return 0
    raise ValueError(f"unknown command {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
