from __future__ import annotations

import argparse
from pathlib import Path

from stochastic_em_theory.fig3b import run_gorlach_2023_fig3b_proxy


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "gorlach-2023-fig3b-proxy"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reproduce Gorlach et al. 2023 Fig. 3b with the local stochastic-field HHG proxy."
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--shots", type=int, default=50_000)
    parser.add_argument("--seed", type=int, default=20230603)
    parser.add_argument("--base-field-amplitude-au", type=float, default=0.08)
    parser.add_argument("--omega-au", type=float, default=0.057)
    parser.add_argument("--ionization-potential-au", type=float, default=0.7924)
    parser.add_argument("--max-order", type=int, default=151)
    parser.add_argument("--mean-photon-number", type=float, default=100.0)
    parser.add_argument("--fock-n", type=int, default=100)
    parser.add_argument("--bsv-r", type=float, default=2.0)
    parser.add_argument("--bsv-phase", type=float, default=0.0)
    parser.add_argument("--nonlinearity-power", type=float, default=6.0)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    artifacts = run_gorlach_2023_fig3b_proxy(
        output_dir=args.output_dir,
        shots=args.shots,
        seed=args.seed,
        base_field_amplitude_au=args.base_field_amplitude_au,
        omega_au=args.omega_au,
        ionization_potential_au=args.ionization_potential_au,
        max_order=args.max_order,
        mean_photon_number=args.mean_photon_number,
        fock_n=args.fock_n,
        bsv_r=args.bsv_r,
        bsv_phase=args.bsv_phase,
        nonlinearity_power=args.nonlinearity_power,
    )
    print(artifacts.csv_path)
    print(artifacts.summary_path)
    print(artifacts.output_dir / "gorlach_2023_fig3b_proxy.png")
    print(artifacts.manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
