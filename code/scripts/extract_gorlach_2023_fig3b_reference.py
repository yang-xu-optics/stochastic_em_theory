"""Extract the published Gorlach et al. 2023 Fig. 3b curves from the source-data archive.

The public source-data archive ships the Fig. 3b panel as a MATLAB figure
(`Dot fig files/Figure 3b/Spectra.fig`). This script walks the figure object
tree, pulls out the four line series (coherent, Fock, thermal, squeezed
vacuum), and writes them to a long-format CSV used as the published reference
for local reproduction overlays. The intensities carry the authors' display
offsets between states; only curve shapes and cutoffs are comparable.
"""

from __future__ import annotations

import argparse
import warnings
from datetime import date
from pathlib import Path

import numpy as np
import scipy.io as sio

from stochastic_em_theory.io import current_git_commit, ensure_output_dir, write_csv, write_manifest

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FIG_PATH = (
    REPO_ROOT
    / "raw"
    / "assets"
    / "gorlach-2023-fig3-source-data"
    / "HHG BSV Data - 16 05 2023"
    / "Dot fig files"
    / "Figure 3b"
    / "Spectra.fig"
)
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "gorlach-2023-fig3b-published-reference"


def extract_line_series(fig_path: Path) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        contents = sio.loadmat(fig_path, simplify_cells=True)
    figure_tree = contents["hgS_070000"]
    curves: dict[str, tuple[np.ndarray, np.ndarray]] = {}

    def walk(node: object) -> None:
        if not isinstance(node, dict):
            return
        if node.get("type") == "graph2d.lineseries":
            properties = node["properties"]
            name = str(properties["DisplayName"])
            curves[name] = (
                np.asarray(properties["XData"], dtype=np.float64),
                np.asarray(properties["YData"], dtype=np.float64),
            )
        children = node.get("children")
        if children is not None:
            for child in np.atleast_1d(children):
                walk(child)

    walk(figure_tree)
    if not curves:
        raise ValueError(f"no line series found in {fig_path}")
    return curves


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fig-path", type=Path, default=DEFAULT_FIG_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    curves = extract_line_series(args.fig_path)
    output_dir = ensure_output_dir(args.output_dir)
    csv_path = output_dir / "fig3b_published_curves.csv"
    rows = [
        {"state": name, "harmonic_order": float(x), "intensity": float(y)}
        for name, (xs, ys) in curves.items()
        for x, y in zip(xs, ys, strict=True)
    ]
    write_csv(csv_path, rows, ["state", "harmonic_order", "intensity"])
    write_manifest(
        output_dir / "manifest.yaml",
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "code_entrypoint": "code/scripts/extract_gorlach_2023_fig3b_reference.py",
            "git_commit": current_git_commit(REPO_ROOT),
            "source_fig": str(args.fig_path.relative_to(REPO_ROOT) if args.fig_path.is_relative_to(REPO_ROOT) else args.fig_path),
            "states": sorted(curves),
            "notes": (
                "Published Fig. 3b line series extracted from the authors' MATLAB figure. "
                "Intensities include the authors' per-state display offsets; only curve "
                "shapes, harmonic comb structure, and cutoffs are comparable across states."
            ),
            "outputs": {"curves_csv": csv_path.name},
        },
    )
    print(csv_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
