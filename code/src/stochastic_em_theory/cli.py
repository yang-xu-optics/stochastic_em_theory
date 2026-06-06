from __future__ import annotations

import argparse
from pathlib import Path

from stochastic_em_theory.validation import run_single_mode_validation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="stochastic-em-theory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    single = subparsers.add_parser("single-mode", help="run single-mode squeezed-vacuum g2 validation")
    single.add_argument("--r-values", nargs="+", type=float, required=True)
    single.add_argument("--shots", type=int, required=True)
    single.add_argument("--seed", type=int, required=True)
    single.add_argument("--output-dir", type=Path, required=True)

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
    raise ValueError(f"unknown command {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
