# Code Workspace

Python package `stochastic_em_theory`: optical-rectification THz statistics for
bright squeezed vacuum (the Letter), plus squeezed-field samplers,
quantum-optics validation, a 1D TDSE solver, HHG ensemble runners, and a
plasma-THz notebook (the companion paper).

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

Python 3.11 or newer. The suite has 96 tests and runs in about a minute and a
half; most of that is four matrix-exponential checks of the
optical-rectification model.

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
| `optical_rectification.py` | THz field statistics for optical rectification of BSV: exact photon-number cumulants, Wick decomposition of the photon-flux spectrum, bright-limit formulas, classical-noise sampler | exact for flat coupling and no pump dispersion (all orders in the coupling); Fock-space and matrix-exponential cross-checks in the tests |
| `thz_waveform_noise.py` | Shot-to-shot noise of the rectified THz waveform against delay for a multimode pump: Gaussian Schell-model sampler, exact variance, moment coefficients, template fit, closed-form flux spectrum | exact formula checked against sampling; model THz response |
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
| `uv run python scripts/run_or_thz_statistics.py` | `results/runs/20261114-bsv-or-thz-statistics/` (optical-rectification theory tables and figure) |
| `uv run python scripts/run_thz_waveform_noise.py` | `results/runs/20261114-thz-waveform-noise-against-delay/` |
| `uv run python scripts/audit_fig_iv2_library_convergence.py` | `results/runs/20261114-fig-iv2-library-convergence-audit/` (about seven minutes on four cores) |
| `uv run python scripts/check_thz_two_color_parity.py` | `results/runs/20261114-thz-two-color-parity-check/` |
| `uv run python scripts/make_theory_note_figures.py` | `paper/theory-note/figures/` (three figures of the theory note and their manifest) |

Every run writes a `manifest.yaml` with the commit hash, seed, parameters, and
entry point. Add each new run to `../results/runs/README.md`.
