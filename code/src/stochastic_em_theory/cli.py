from __future__ import annotations

import argparse
from pathlib import Path

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
    if args.command == "plot-single-mode":
        print(plot_single_mode_g2(csv_path=args.csv_path, output_path=args.output_path))
        return 0
    if args.command == "plot-multimode":
        print(plot_multimode_g2(csv_path=args.csv_path, output_path=args.output_path))
        return 0
    raise ValueError(f"unknown command {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
