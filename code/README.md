# Code Workspace

Python package `stochastic_em_theory`: squeezed-field samplers, quantum-optics
validation, a 1D TDSE solver, HHG ensemble runners, and a plasma-THz notebook.

## Setup and tests

With [uv](https://docs.astral.sh/uv/) (uses the committed `uv.lock`):

```bash
cd code
uv sync --extra dev
uv run pytest
```

Or with plain `venv` and `pip`:

```bash
cd code
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
python3 -m pytest
```

Python 3.11 or newer. The suite has 55 tests and runs in about ten seconds.

## What is where

| Module (`src/stochastic_em_theory/`) | Purpose | Fidelity |
| --- | --- | --- |
| `fields.py` | Single-mode and multimode squeezed-vacuum samplers (Wigner, Husimi-Q) | exact for Gaussian states |
| `observables.py` | Wigner-to-normal-ordering moment conversion, analytic `g2` targets | exact |
| `validation.py` | Single-mode and equal-mode `g2` validation runs with standard errors | validated against analytic results |
| `source_models.py` | BSV source-model metadata (single, equal, Schmidt, twin-beam) | bookkeeping only; Schmidt and twin-beam are not sampled yet |
| `tdse1d.py` | 1D soft-core split-operator TDSE, dipole-acceleration spectrum | physics model; see convergence caveats in the run index |
| `fig3b.py`, `fig_iv2.py` | Gorlach 2023 Fig. 3b and supplementary Fig. IV.2 reproductions | TDSE amplitude library plus interpolation; not converged |
| `hhg_proxy.py`, `ensemble.py` | Smooth cutoff-law HHG proxy and labelled ensemble runner | pipeline development only, not physics |
| `ati.py`, `ionization.py` | ADK-like ionization-rate proxy under coherent, thermal, BSV statistics | proxy, not a qSFA solver |
| `emission_environment.py` | Wang 2024 squeezed emitted-mode `mu_k(t)` toy model | toy; result is analytic |
| `claim_ladder.py`, `mechanisms.py`, `shot_records.py`, `io.py`, `plotting.py`, `cli.py` | Labels, per-shot records, manifests, plots, CLI | infrastructure |

## Entry points

| Command (run from `code/`) | Writes to |
| --- | --- |
| `uv run python scripts/run_paper_one_smoke.py` | `results/tmp/paper-one-smoke/` (ignored by git) |
| `uv run python scripts/reproduce_gorlach_2023_fig3b.py --output-dir ../results/runs/<run-id>` | the given run directory |
| `uv run python scripts/reproduce_gorlach_2023_fig_iv2.py --output-dir ../results/runs/<run-id>` | the given run directory |
| `notebooks/thz_plasma_bsv_photocurrent.ipynb` | `results/runs/20260610-thz-plasma-bsv-notebook/` |

Every run writes a `manifest.yaml` with the commit hash, seed, parameters, and
entry point. Add each new run to `../results/runs/README.md`.
