from __future__ import annotations

import argparse
from pathlib import Path

from stochastic_em_theory.ati import run_ati_statistics_benchmark
from stochastic_em_theory.emission_environment import run_emission_environment_scan
from stochastic_em_theory.ensemble import run_proxy_hhg_ensemble
from stochastic_em_theory.plotting import plot_multimode_g2, plot_proxy_hhg_spectrum, plot_single_mode_g2
from stochastic_em_theory.validation import run_multimode_validation, run_single_mode_validation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=Path("../results/tmp/paper-one-smoke"))
    parser.add_argument("--shots", type=int, default=50_000)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    output_root = args.output_root
    runs_root = output_root / "runs"
    figures_root = output_root / "figures"
    runs_root.mkdir(parents=True, exist_ok=True)
    figures_root.mkdir(parents=True, exist_ok=True)

    single = run_single_mode_validation(
        r_values=[0.4, 0.7, 1.0],
        shots=args.shots,
        seed=1001,
        output_dir=runs_root / "paper-one-smoke-single",
    )
    multi = run_multimode_validation(
        r=0.7,
        mode_counts=[1, 2, 4, 8],
        shots=args.shots,
        seed=1002,
        output_dir=runs_root / "paper-one-smoke-multimode",
    )
    hhg = run_proxy_hhg_ensemble(
        r=0.8,
        phase=0.0,
        shots=max(64, min(args.shots, 5000)),
        seed=1003,
        base_field_amplitude_au=0.035,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=31,
        output_dir=runs_root / "paper-one-smoke-hhg",
    )
    ati = run_ati_statistics_benchmark(
        mean_field_amplitude_au=0.035,
        ionization_potential_au=0.7924,
        shots=max(64, min(args.shots, 5000)),
        seed=1004,
        output_dir=runs_root / "paper-one-smoke-ati",
    )
    emission = run_emission_environment_scan(
        harmonic_order=9,
        fundamental_omega_au=0.057,
        r=0.5,
        theta_values=[0.0, 1.5707963267948966, 3.141592653589793],
        output_dir=runs_root / "paper-one-smoke-emission",
    )

    plot_single_mode_g2(csv_path=single.csv_path, output_path=figures_root / "single_mode_g2.png")
    plot_multimode_g2(csv_path=multi.csv_path, output_path=figures_root / "multimode_g2.png")
    plot_proxy_hhg_spectrum(csv_path=hhg.csv_path, output_path=figures_root / "proxy_hhg_spectrum.png")

    print(output_root / "runs" / "paper-one-smoke-single")
    print(output_root / "runs" / "paper-one-smoke-multimode")
    print(output_root / "runs" / "paper-one-smoke-hhg")
    print(ati.output_dir)
    print(emission.output_dir)
    print(output_root / "figures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
