# Paper-One Squeezed-Field Simulation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the reproducible simulation layer for the correspondence-first HHG paper: squeezed-field sampling, ordering-corrected validation, source-model-aware mode validation, ATI/photon-statistics validation, squeezed-emission-mode boundary modeling, paper-one figures, per-shot HHG records, and an HHG intensity-observable pipeline.

**Architecture:** Implement a small Python package under `code/src/stochastic_em_theory/` with focused modules for field sampling, BSV source-model metadata, observable estimators, validation runs, plotting, HHG response models, ATI statistics, squeezed emitted-mode modulation, per-shot records, ionization/cutoff proxies, and result manifests. Keep source code deterministic and testable; write generated outputs under `results/runs/` and `results/figures/` with manifests that identify mechanism family, source-model family, claim-ladder level, and random seeds.

**Tech Stack:** Python 3.11+, NumPy, SciPy, Matplotlib, PyYAML, pytest.

---

## Scope Check

This plan implements the simulation layer for paper one. It does not write the manuscript, certify non-Gaussian quantum output states, implement THz models, or implement macroscopic HHG propagation. It creates working, testable software for:

- exact single-mode squeezed-vacuum input validation,
- source-model-aware mode-filtered squeezed-vacuum validation,
- figures that expose the ordering correction and mode-count effects,
- a lightweight HHG intensity-observable pipeline with per-shot records,
- ionization/tunneling and cutoff proxies that support the new HHG literature targets,
- an ATI/photon-statistics benchmark for coherent, thermal, and BSV ensembles,
- a squeezed-emission-mode toy model for Wang 2024's selected-harmonic mechanism,
- tested utilities for the later 1D soft-core gas baseline.

## File Structure

- `wiki/simulations/paper-one-correspondence-hhg-simulation-spec.md`: simulation spec required before numerical work.
- `wiki/index.md`: add the new simulation spec link.
- `wiki/log.md`: append one simulation planning entry.
- `code/pyproject.toml`: package metadata and test dependencies.
- `code/src/stochastic_em_theory/__init__.py`: package version.
- `code/src/stochastic_em_theory/fields.py`: Wigner and Husimi squeezed-field samplers.
- `code/src/stochastic_em_theory/source_models.py`: explicit BSV source-model catalog and mode weights.
- `code/src/stochastic_em_theory/mechanisms.py`: explicit mechanism-family labels.
- `code/src/stochastic_em_theory/observables.py`: analytic targets and ordering-corrected estimators.
- `code/src/stochastic_em_theory/io.py`: run directory, CSV, JSON, and YAML manifest helpers.
- `code/src/stochastic_em_theory/validation.py`: single-mode and mode-filtered validation runners.
- `code/src/stochastic_em_theory/plotting.py`: deterministic figure builders for validation and HHG outputs.
- `code/src/stochastic_em_theory/hhg_proxy.py`: fast HHG intensity proxy for ensemble-pipeline development.
- `code/src/stochastic_em_theory/ionization.py`: Keldysh and ADK-like ionization/tunneling proxies.
- `code/src/stochastic_em_theory/ati.py`: ATI/photon-statistics benchmark for coherent, thermal, and BSV ensembles.
- `code/src/stochastic_em_theory/emission_environment.py`: squeezed emitted-mode `mu_k(t)` toy model.
- `code/src/stochastic_em_theory/tdse1d.py`: tested 1D split-operator utilities for the soft-core gas baseline.
- `code/src/stochastic_em_theory/claim_ladder.py`: explicit result claim-level labels.
- `code/src/stochastic_em_theory/shot_records.py`: per-shot driver and HHG diagnostic records.
- `code/src/stochastic_em_theory/ensemble.py`: HHG ensemble runner and conditional binning.
- `code/src/stochastic_em_theory/cli.py`: command-line entry points.
- `code/scripts/run_paper_one_smoke.py`: small end-to-end run that creates validation data and figures.
- `code/tests/`: focused pytest files for every module above.

---

### Task 1: Add The Paper-One Simulation Spec

**Files:**
- Create: `wiki/simulations/paper-one-correspondence-hhg-simulation-spec.md`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [ ] **Step 1: Create the simulation spec page**

Create `wiki/simulations/paper-one-correspondence-hhg-simulation-spec.md` with this exact content:

````markdown
---
title: Paper One Correspondence HHG Simulation Spec
type: simulation
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [paper-one, squeezed-vacuum, validation, hhg]
source_count: 54
confidence: high
related:
  - ../theory/stochastic-quantum-optics-correspondence
  - ../theory/squeezed-vacuum-g2-proof-plan
  - ../theory/non-gaussian-output-novelty
  - ../models/hhg-gas-model
  - simulation-roadmap
---

# Paper One Correspondence HHG Simulation Spec

## Goal

Produce reproducible simulations for the correspondence-first HHG paper:

1. validate squeezed-vacuum stochastic sampling against exact input-field quantum optics diagnostics,
2. show why Wigner-to-normal ordering corrections are required for photon-counting `g^(2)(0)`,
3. add a mode-filtered validation that makes mode definition explicit,
4. record the BSV source-model family used to generate each ensemble,
5. drive HHG intensity-level observables with the validated stochastic ensemble,
6. retain per-shot HHG metadata for ionization, cutoff, bunching, and symmetry diagnostics,
7. add a pre-HHG ATI/photon-statistics validation branch for coherent, thermal, and BSV ensembles,
8. add a separate squeezed-emission-mode boundary model for selected harmonic channels,
9. label every output with the mechanism family and claim-ladder level it supports.

## Units

- Single-mode and mode-filtered validation use dimensionless oscillator units.
- HHG proxy outputs use atomic units for field amplitude, angular frequency, ionization potential, and cutoff energy.
- Result manifests must state the units used by each run.

## Random Seed Strategy

- Every validation or ensemble run accepts an integer seed.
- Every result directory stores the seed in `manifest.yaml`.
- Tests use fixed seeds and broad statistical tolerances; paper runs use larger sample counts and record Monte Carlo uncertainty.

## Stage A: Single-Mode Validation

Observable targets:

```text
<n> = sinh^2(r)
g^(2)(0) = 3 + 1/<n>
```

Wigner estimators:

```text
<a^dagger a> = <|alpha|^2>_W - 1/2
<a^dagger a^dagger a a> =
  <|alpha|^4>_W - 2 <|alpha|^2>_W + 1/2
```

Outputs:

- CSV with `r`, analytic `<n>`, estimated `<n>`, corrected `g2`, naive `g2`, standard errors.
- Figure showing corrected and naive `g2` against analytic target.
- Manifest with claim level `exact_input_correspondence`.

## Stage B: Mode-Filtered Validation

Use independent equal squeezed modes as a controlled mode-filtered validation. For `M` equal modes with per-mode mean photon number `n`, the total photon-counting target is:

```text
g_total^(2)(0) = 1 + 2/M + 1/(M n)
```

Record the source-model family for each run:

```text
single_mode
equal_mode
schmidt_mode
two_color_twin_beam
propagated_nongaussian_frontier
```

Outputs:

- CSV with `M`, per-mode `r`, analytic total `g2`, estimated total `g2`, and standard error.
- Figure showing the transition from single-mode superbunching toward the multimode limit.
- Manifest with claim level `exact_input_correspondence`.
- Source-model summary with effective mode count and source references.

## Stage C: HHG Intensity Pipeline

Use the validated ensemble to drive intensity-level HHG observables. The first implementation uses a fast cutoff-weighted HHG proxy to test ensemble averaging, conditional spectra, per-shot records, result manifests, and figure generation. The 1D soft-core split-operator utilities are implemented and tested as the first physics-fidelity upgrade.

Supported paper-one observables:

- ensemble mean HHG spectrum,
- conditional spectra binned by sampled drive intensity,
- ionization/tunneling proxy distributions,
- cutoff distribution,
- shot-to-shot variance,
- per-shot driver quadratures, intensity, phase, ionization proxy, cutoff proxy,
  harmonic amplitudes, and harmonic phases,
- convergence versus ensemble size.

## Stage D: ATI/Photon-Statistics Validation

Before full HHG recombination modeling, validate the upstream ionization step
using coherent, thermal, and BSV photon-statistics ensembles. This branch is
inspired by Lyu 2025 and uses diagonal coherent-component averaging:

```text
W(p) = integral dE_alpha P(E_alpha) |M_alpha(p)|^2
```

The first implementation uses ionization-rate and electron-number proxies, not
a quantitative qSFA momentum solver.

Outputs:

- CSV comparing coherent, thermal, and BSV sampled ensembles at matched mean
  intensity.
- Estimated `g2` hierarchy:

```text
g2_coherent = 1
g2_thermal = 2
g2_BSV = 3
```

- Ionization-yield enhancement and electron-number bunching proxies.
- Manifest with mechanism family `ati_photon_statistics`.

## Stage E: Squeezed Emission-Mode Environment Boundary Model

Model Wang 2024 as a separate mechanism from BSV pump sampling. For a selected
harmonic mode, use:

```text
mu_k(t) = cosh(r_k) + sinh(r_k) exp[-i(2 omega_k t - theta_k)]
```

and compare the targeted-channel amplitude with and without `mu_k(t)`.

Outputs:

- CSV over squeezing angle for one selected harmonic order.
- Figure or summary showing modulation of the targeted harmonic amplitude.
- Manifest with mechanism family `squeezed_emission_mode_environment`.

Unsupported paper-one claims:

- emitted harmonic Wigner negativity,
- full harmonic quantum-state reconstruction,
- macroscopic propagation,
- non-Gaussian quantum-output certification.

## Result Manifest Fields

Each run writes:

```yaml
run_id: YYYYMMDD-short-name
created: YYYY-MM-DD
claim_level: exact_input_correspondence | hhg_intensity_prediction
mechanism:
source_model:
code_entrypoint:
git_commit:
parameter_file:
random_seeds:
observable:
units:
notes:
```
````

- [ ] **Step 2: Add the simulation spec to the wiki index**

Modify the `## Simulations` section of `wiki/index.md` so it contains this extra bullet immediately after `[[simulations/simulation-roadmap]]`:

```markdown
- [[simulations/paper-one-correspondence-hhg-simulation-spec]]: paper-one
  simulation specification for squeezed-field validation, mode-filtered
  `g^(2)`, and HHG intensity observables.
```

- [ ] **Step 3: Append the planning entry to the wiki log**

Append this entry to `wiki/log.md`:

```markdown

## [2026-06-06] simulation | Paper One Correspondence HHG Spec

- Added [[simulations/paper-one-correspondence-hhg-simulation-spec]] as the
  implementation-facing simulation spec for the correspondence-first HHG paper.
- Scoped paper-one simulations to exact input-field validation, mode-filtered
  `g^(2)`, source-model-aware BSV ensembles, HHG intensity-level observables,
  ATI/photon-statistics validation, squeezed-emission-mode boundary modeling,
  per-shot metadata records, and explicit claim-ladder labels.
- Kept non-Gaussian output certification, THz models, and macroscopic HHG
  propagation outside the first simulation implementation.
```

- [ ] **Step 4: Verify the documentation diff**

Run:

```bash
git diff -- wiki/simulations/paper-one-correspondence-hhg-simulation-spec.md wiki/index.md wiki/log.md
```

Expected: diff shows the new simulation page, one new index bullet, and one new log entry.

- [ ] **Step 5: Commit**

Run:

```bash
git add wiki/simulations/paper-one-correspondence-hhg-simulation-spec.md wiki/index.md wiki/log.md
git commit -m "docs: add paper one simulation spec"
```

Expected: commit succeeds.

---

### Task 2: Create The Python Package Scaffold

**Files:**
- Create: `code/pyproject.toml`
- Create: `code/src/stochastic_em_theory/__init__.py`
- Create: `code/tests/test_imports.py`
- Modify: `code/README.md`

- [ ] **Step 1: Write the failing import test**

Create `code/tests/test_imports.py`:

```python
from stochastic_em_theory import __version__


def test_version_is_string() -> None:
    assert isinstance(__version__, str)
    assert __version__
```

- [ ] **Step 2: Run the import test and verify it fails**

Run:

```bash
cd code
PYTHONPATH=src python -m pytest tests/test_imports.py -q
```

Expected: FAIL with `ModuleNotFoundError: No module named 'stochastic_em_theory'`.

- [ ] **Step 3: Add package metadata and the package initializer**

Create `code/pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "stochastic-em-theory"
version = "0.1.0"
description = "Stochastic squeezed-field simulations for HHG and THz research"
requires-python = ">=3.11"
dependencies = [
  "matplotlib>=3.8",
  "numpy>=1.26",
  "pyyaml>=6.0",
  "scipy>=1.12",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.0",
]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
addopts = "-ra"
```

Create `code/src/stochastic_em_theory/__init__.py`:

```python
"""Simulation tools for stochastic squeezed-field HHG and THz research."""

__version__ = "0.1.0"
```

- [ ] **Step 4: Update the code README with local setup commands**

Replace `code/README.md` with:

````markdown
# Code Workspace

Implementation code for stochastic-field samplers, validation tests, HHG
models, and THz emission simulations belongs here.

## Local Setup

```bash
cd code
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
```

Generated run outputs belong under `../results/runs/`. Paper-ready figures
belong under `../results/figures/`.
````

- [ ] **Step 5: Install the package in editable mode**

Run:

```bash
cd code
python -m pip install -e ".[dev]"
```

Expected: command exits with status 0 and installs `stochastic-em-theory`.

- [ ] **Step 6: Run the import test and verify it passes**

Run:

```bash
cd code
python -m pytest tests/test_imports.py -q
```

Expected: `1 passed`.

- [ ] **Step 7: Commit**

Run:

```bash
git add code/pyproject.toml code/src/stochastic_em_theory/__init__.py code/tests/test_imports.py code/README.md
git commit -m "test: scaffold simulation package"
```

Expected: commit succeeds.

---

### Task 3: Implement Single-Mode Squeezed-Field Sampling And Ordering-Corrected Observables

**Files:**
- Create: `code/src/stochastic_em_theory/fields.py`
- Create: `code/src/stochastic_em_theory/observables.py`
- Create: `code/tests/test_single_mode_observables.py`

- [ ] **Step 1: Write failing tests for the single-mode formulas**

Create `code/tests/test_single_mode_observables.py`:

```python
import numpy as np

from stochastic_em_theory.fields import sample_single_mode_husimi_q, sample_single_mode_wigner
from stochastic_em_theory.observables import (
    analytic_single_mode_g2,
    analytic_single_mode_wigner_abs_moments,
    estimate_single_mode_moments,
    normal_moments_from_wigner_abs_moments,
)


def test_ordering_correction_recovers_exact_g2_from_analytic_wigner_moments() -> None:
    r = 0.8
    abs2_w, abs4_w = analytic_single_mode_wigner_abs_moments(r)

    n_est, factorial2_est = normal_moments_from_wigner_abs_moments(abs2_w, abs4_w)

    expected_n = np.sinh(r) ** 2
    expected_g2 = analytic_single_mode_g2(r)
    assert np.isclose(n_est, expected_n)
    assert np.isclose(factorial2_est / n_est**2, expected_g2)


def test_wigner_sampler_reproducible_statistics() -> None:
    rng = np.random.default_rng(12345)
    r = 0.7
    alpha = sample_single_mode_wigner(r=r, phase=0.25, shots=250_000, rng=rng)

    estimate = estimate_single_mode_moments(alpha)

    assert np.isclose(estimate.n_corrected, np.sinh(r) ** 2, rtol=0.035, atol=0.01)
    assert np.isclose(estimate.g2_corrected, analytic_single_mode_g2(r), rtol=0.08)
    assert abs(estimate.g2_naive - estimate.g2_corrected) > 0.2


def test_husimi_q_sampler_has_one_vacuum_photon_of_heterodyne_noise() -> None:
    rng = np.random.default_rng(7)
    alpha = sample_single_mode_husimi_q(r=0.0, phase=0.0, shots=100_000, rng=rng)

    assert np.isclose(np.mean(np.abs(alpha) ** 2), 1.0, rtol=0.025)
```

- [ ] **Step 2: Run the tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_single_mode_observables.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.fields`.

- [ ] **Step 3: Implement field samplers**

Create `code/src/stochastic_em_theory/fields.py`:

```python
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]
ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class SqueezedMode:
    """Single squeezed optical mode parameters."""

    r: float
    phase: float = 0.0


def _as_generator(rng: np.random.Generator | None) -> np.random.Generator:
    return np.random.default_rng() if rng is None else rng


def sample_single_mode_wigner(
    *,
    r: float,
    phase: float = 0.0,
    shots: int,
    rng: np.random.Generator | None = None,
) -> ComplexArray:
    """Sample a single-mode squeezed-vacuum Wigner distribution.

    The quadrature convention is alpha = (x + i p) / sqrt(2), with vacuum
    Wigner variances Var(x) = Var(p) = 1/2.
    """

    if shots <= 0:
        raise ValueError("shots must be positive")
    if r < 0:
        raise ValueError("r must be non-negative")

    generator = _as_generator(rng)
    x_std = np.sqrt(0.5 * np.exp(-2.0 * r))
    p_std = np.sqrt(0.5 * np.exp(2.0 * r))
    x = generator.normal(loc=0.0, scale=x_std, size=shots)
    p = generator.normal(loc=0.0, scale=p_std, size=shots)
    rotation = np.exp(0.5j * phase)
    return (rotation * (x + 1j * p) / np.sqrt(2.0)).astype(np.complex128)


def sample_single_mode_husimi_q(
    *,
    r: float,
    phase: float = 0.0,
    shots: int,
    rng: np.random.Generator | None = None,
) -> ComplexArray:
    """Sample the single-mode squeezed-vacuum Husimi-Q coherent amplitudes.

    Relative to Wigner sampling, the Q distribution adds heterodyne vacuum
    noise, so a vacuum mode has <|alpha|^2>_Q = 1.
    """

    if shots <= 0:
        raise ValueError("shots must be positive")
    if r < 0:
        raise ValueError("r must be non-negative")

    generator = _as_generator(rng)
    x_std = np.sqrt(0.5 * np.exp(-2.0 * r) + 0.5)
    p_std = np.sqrt(0.5 * np.exp(2.0 * r) + 0.5)
    x = generator.normal(loc=0.0, scale=x_std, size=shots)
    p = generator.normal(loc=0.0, scale=p_std, size=shots)
    rotation = np.exp(0.5j * phase)
    return (rotation * (x + 1j * p) / np.sqrt(2.0)).astype(np.complex128)
```

- [ ] **Step 4: Implement analytic targets and estimators**

Create `code/src/stochastic_em_theory/observables.py`:

```python
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class SingleModeMomentEstimate:
    abs2_wigner: float
    abs4_wigner: float
    n_corrected: float
    factorial2_corrected: float
    g2_corrected: float
    g2_naive: float


def analytic_single_mode_n(r: float) -> float:
    if r < 0:
        raise ValueError("r must be non-negative")
    return float(np.sinh(r) ** 2)


def analytic_single_mode_g2(r: float) -> float:
    n = analytic_single_mode_n(r)
    if n <= 0:
        raise ValueError("g2 is singular for squeezed vacuum with zero photons")
    return float(3.0 + 1.0 / n)


def analytic_single_mode_wigner_abs_moments(r: float) -> tuple[float, float]:
    n = analytic_single_mode_n(r)
    anomalous_abs2 = n * (n + 1.0)
    abs2_w = n + 0.5
    abs4_w = 2.0 * abs2_w**2 + anomalous_abs2
    return float(abs2_w), float(abs4_w)


def normal_moments_from_wigner_abs_moments(abs2_w: float, abs4_w: float) -> tuple[float, float]:
    n = abs2_w - 0.5
    factorial2 = abs4_w - 2.0 * abs2_w + 0.5
    if n <= 0:
        raise ValueError("normal-ordered photon number must be positive")
    return float(n), float(factorial2)


def estimate_single_mode_moments(alpha: ComplexArray) -> SingleModeMomentEstimate:
    if alpha.ndim != 1:
        raise ValueError("alpha must be a one-dimensional array of mode samples")
    if alpha.size == 0:
        raise ValueError("alpha must contain at least one sample")

    intensity = np.abs(alpha) ** 2
    abs2_w = float(np.mean(intensity))
    abs4_w = float(np.mean(intensity**2))
    n, factorial2 = normal_moments_from_wigner_abs_moments(abs2_w, abs4_w)
    return SingleModeMomentEstimate(
        abs2_wigner=abs2_w,
        abs4_wigner=abs4_w,
        n_corrected=n,
        factorial2_corrected=factorial2,
        g2_corrected=float(factorial2 / n**2),
        g2_naive=float(abs4_w / abs2_w**2),
    )
```

- [ ] **Step 5: Run the single-mode tests**

Run:

```bash
cd code
python -m pytest tests/test_single_mode_observables.py -q
```

Expected: `3 passed`.

- [ ] **Step 6: Run the full test suite**

Run:

```bash
cd code
python -m pytest -q
```

Expected: all tests pass.

- [ ] **Step 7: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/fields.py code/src/stochastic_em_theory/observables.py code/tests/test_single_mode_observables.py
git commit -m "feat: add single mode squeezed validation primitives"
```

Expected: commit succeeds.

---

### Task 4: Add Single-Mode Validation Runs And Manifests

**Files:**
- Create: `code/src/stochastic_em_theory/io.py`
- Create: `code/src/stochastic_em_theory/validation.py`
- Create: `code/src/stochastic_em_theory/cli.py`
- Create: `code/tests/test_single_mode_validation.py`

- [ ] **Step 1: Write failing tests for validation outputs**

Create `code/tests/test_single_mode_validation.py`:

```python
import csv
import json

import yaml

from stochastic_em_theory.validation import run_single_mode_validation


def test_single_mode_validation_writes_csv_summary_and_manifest(tmp_path) -> None:
    result = run_single_mode_validation(
        r_values=[0.4, 0.8],
        shots=60_000,
        seed=123,
        output_dir=tmp_path,
    )

    assert result.csv_path.exists()
    assert result.summary_path.exists()
    assert result.manifest_path.exists()

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert [float(row["r"]) for row in rows] == [0.4, 0.8]
    assert all(float(row["g2_corrected"]) > 3.0 for row in rows)
    assert any(abs(float(row["g2_naive"]) - float(row["g2_corrected"])) > 0.15 for row in rows)

    summary = json.loads(result.summary_path.read_text())
    assert summary["rows"] == 2
    assert summary["claim_level"] == "exact_input_correspondence"

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["random_seeds"] == [123]
    assert manifest["observable"] == "single_mode_squeezed_vacuum_g2"
    assert manifest["claim_level"] == "exact_input_correspondence"
```

- [ ] **Step 2: Run the test and verify it fails**

Run:

```bash
cd code
python -m pytest tests/test_single_mode_validation.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.validation`.

- [ ] **Step 3: Implement run-output helpers**

Create `code/src/stochastic_em_theory/io.py`:

```python
from __future__ import annotations

import csv
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class RunArtifacts:
    output_dir: Path
    csv_path: Path
    summary_path: Path
    manifest_path: Path


def current_git_commit(repo_root: Path | None = None) -> str:
    cwd = repo_root if repo_root is not None else Path.cwd()
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"
    return completed.stdout.strip()


def ensure_output_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def write_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(payload, sort_keys=False))
```

- [ ] **Step 4: Implement the single-mode validation runner**

Create `code/src/stochastic_em_theory/validation.py`:

```python
from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np

from stochastic_em_theory.fields import sample_single_mode_wigner
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.observables import (
    analytic_single_mode_g2,
    analytic_single_mode_n,
    estimate_single_mode_moments,
)


def run_single_mode_validation(
    *,
    r_values: list[float],
    shots: int,
    seed: int,
    output_dir: Path,
) -> RunArtifacts:
    if not r_values:
        raise ValueError("r_values must contain at least one squeezing parameter")
    if shots <= 0:
        raise ValueError("shots must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    rows: list[dict[str, float | int]] = []

    for r in r_values:
        alpha = sample_single_mode_wigner(r=r, shots=shots, rng=rng)
        estimate = estimate_single_mode_moments(alpha)
        rows.append(
            {
                "r": float(r),
                "shots": int(shots),
                "analytic_n": analytic_single_mode_n(r),
                "estimated_n": estimate.n_corrected,
                "analytic_g2": analytic_single_mode_g2(r),
                "g2_corrected": estimate.g2_corrected,
                "g2_naive": estimate.g2_naive,
                "abs2_wigner": estimate.abs2_wigner,
                "abs4_wigner": estimate.abs4_wigner,
            }
        )

    csv_path = output_dir / "single_mode_g2.csv"
    summary_path = output_dir / "single_mode_summary.json"
    manifest_path = output_dir / "manifest.yaml"

    write_csv(
        csv_path,
        rows,
        [
            "r",
            "shots",
            "analytic_n",
            "estimated_n",
            "analytic_g2",
            "g2_corrected",
            "g2_naive",
            "abs2_wigner",
            "abs4_wigner",
        ],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "claim_level": "exact_input_correspondence",
            "max_abs_g2_error": max(abs(float(row["g2_corrected"]) - float(row["analytic_g2"])) for row in rows),
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": "exact_input_correspondence",
            "code_entrypoint": "stochastic_em_theory.validation.run_single_mode_validation",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "single_mode_squeezed_vacuum_g2",
            "units": "dimensionless oscillator units",
            "notes": "Wigner samples converted to normally ordered photon-counting observables.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
```

- [ ] **Step 5: Implement the CLI entry point**

Create `code/src/stochastic_em_theory/cli.py`:

```python
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
```

- [ ] **Step 6: Run validation tests**

Run:

```bash
cd code
python -m pytest tests/test_single_mode_validation.py -q
```

Expected: `1 passed`.

- [ ] **Step 7: Run a CLI smoke validation**

Run:

```bash
cd code
python -m stochastic_em_theory.cli single-mode --r-values 0.4 0.8 --shots 50000 --seed 123 --output-dir ../results/tmp/single-mode-smoke
```

Expected: command prints `../results/tmp/single-mode-smoke` or the normalized path, and `../results/tmp/single-mode-smoke/single_mode_g2.csv` exists.

- [ ] **Step 8: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/io.py code/src/stochastic_em_theory/validation.py code/src/stochastic_em_theory/cli.py code/tests/test_single_mode_validation.py
git commit -m "feat: add single mode validation runs"
```

Expected: commit succeeds.

---

### Task 5: Add Mode-Filtered Multimode Validation

**Files:**
- Modify: `code/src/stochastic_em_theory/fields.py`
- Modify: `code/src/stochastic_em_theory/observables.py`
- Modify: `code/src/stochastic_em_theory/validation.py`
- Modify: `code/src/stochastic_em_theory/cli.py`
- Create: `code/tests/test_multimode_validation.py`

- [ ] **Step 1: Write failing tests for mode-filtered validation**

Create `code/tests/test_multimode_validation.py`:

```python
import csv

import numpy as np

from stochastic_em_theory.fields import sample_multimode_wigner
from stochastic_em_theory.observables import analytic_equal_mode_g2, estimate_total_photon_moments
from stochastic_em_theory.validation import run_multimode_validation


def test_equal_mode_g2_formula_matches_single_mode_limit() -> None:
    r = 0.9
    assert np.isclose(analytic_equal_mode_g2(r=r, modes=1), 3.0 + 1.0 / (np.sinh(r) ** 2))


def test_multimode_estimator_matches_equal_mode_target() -> None:
    rng = np.random.default_rng(99)
    r = 0.75
    modes = 4
    alpha = sample_multimode_wigner(r=r, modes=modes, shots=180_000, rng=rng)

    estimate = estimate_total_photon_moments(alpha)

    assert np.isclose(estimate.g2_corrected, analytic_equal_mode_g2(r=r, modes=modes), rtol=0.08)
    assert estimate.mode_count == modes


def test_multimode_validation_writes_mode_count_csv(tmp_path) -> None:
    result = run_multimode_validation(
        r=0.7,
        mode_counts=[1, 2, 5],
        shots=70_000,
        seed=321,
        output_dir=tmp_path,
    )

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert [int(row["modes"]) for row in rows] == [1, 2, 5]
    assert float(rows[0]["analytic_g2"]) > float(rows[-1]["analytic_g2"])
```

- [ ] **Step 2: Run the tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_multimode_validation.py -q
```

Expected: FAIL with `ImportError` for `sample_multimode_wigner`.

- [ ] **Step 3: Add multimode Wigner sampling**

Append this function to `code/src/stochastic_em_theory/fields.py`:

```python

def sample_multimode_wigner(
    *,
    r: float | FloatArray,
    modes: int,
    shots: int,
    phase: float = 0.0,
    rng: np.random.Generator | None = None,
) -> ComplexArray:
    """Sample independent squeezed Wigner modes with shape (shots, modes)."""

    if modes <= 0:
        raise ValueError("modes must be positive")
    if shots <= 0:
        raise ValueError("shots must be positive")

    r_values = np.broadcast_to(np.asarray(r, dtype=np.float64), (modes,))
    if np.any(r_values < 0):
        raise ValueError("all squeezing parameters must be non-negative")

    generator = _as_generator(rng)
    samples = np.empty((shots, modes), dtype=np.complex128)
    for mode_index, r_value in enumerate(r_values):
        samples[:, mode_index] = sample_single_mode_wigner(
            r=float(r_value),
            phase=phase,
            shots=shots,
            rng=generator,
        )
    return samples
```

- [ ] **Step 4: Add multimode photon-counting estimators**

Append this code to `code/src/stochastic_em_theory/observables.py`:

```python

@dataclass(frozen=True)
class MultiModeMomentEstimate:
    mode_count: int
    n_total_corrected: float
    factorial2_total_corrected: float
    g2_corrected: float


def analytic_equal_mode_g2(*, r: float, modes: int) -> float:
    if modes <= 0:
        raise ValueError("modes must be positive")
    n_per_mode = analytic_single_mode_n(r)
    if n_per_mode <= 0:
        raise ValueError("g2 is singular for zero photons per mode")
    return float(1.0 + 2.0 / modes + 1.0 / (modes * n_per_mode))


def estimate_total_photon_moments(alpha: ComplexArray) -> MultiModeMomentEstimate:
    if alpha.ndim != 2:
        raise ValueError("alpha must have shape (shots, modes)")
    if alpha.shape[0] == 0 or alpha.shape[1] == 0:
        raise ValueError("alpha must contain at least one shot and one mode")

    abs2 = np.abs(alpha) ** 2
    normal_n_by_mode = abs2 - 0.5
    factorial2_by_mode = abs2**2 - 2.0 * abs2 + 0.5
    total_n_by_shot = np.sum(normal_n_by_mode, axis=1)
    cross_factorial_by_shot = total_n_by_shot**2 - np.sum(normal_n_by_mode**2, axis=1)
    factorial2_total_by_shot = np.sum(factorial2_by_mode, axis=1) + cross_factorial_by_shot
    n_total = float(np.mean(total_n_by_shot))
    factorial2_total = float(np.mean(factorial2_total_by_shot))
    if n_total <= 0:
        raise ValueError("total corrected photon number must be positive")
    return MultiModeMomentEstimate(
        mode_count=int(alpha.shape[1]),
        n_total_corrected=n_total,
        factorial2_total_corrected=factorial2_total,
        g2_corrected=float(factorial2_total / n_total**2),
    )
```

- [ ] **Step 5: Add the multimode validation runner**

Append this import to the existing import block in `code/src/stochastic_em_theory/validation.py`:

```python
from stochastic_em_theory.fields import sample_multimode_wigner
from stochastic_em_theory.observables import analytic_equal_mode_g2, estimate_total_photon_moments
```

Append this function to `code/src/stochastic_em_theory/validation.py`:

```python

def run_multimode_validation(
    *,
    r: float,
    mode_counts: list[int],
    shots: int,
    seed: int,
    output_dir: Path,
) -> RunArtifacts:
    if not mode_counts:
        raise ValueError("mode_counts must contain at least one mode count")
    if shots <= 0:
        raise ValueError("shots must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    rows: list[dict[str, float | int]] = []

    for modes in mode_counts:
        alpha = sample_multimode_wigner(r=r, modes=modes, shots=shots, rng=rng)
        estimate = estimate_total_photon_moments(alpha)
        rows.append(
            {
                "r": float(r),
                "modes": int(modes),
                "shots": int(shots),
                "analytic_g2": analytic_equal_mode_g2(r=r, modes=modes),
                "g2_corrected": estimate.g2_corrected,
                "n_total_corrected": estimate.n_total_corrected,
            }
        )

    csv_path = output_dir / "multimode_g2.csv"
    summary_path = output_dir / "multimode_summary.json"
    manifest_path = output_dir / "manifest.yaml"

    write_csv(
        csv_path,
        rows,
        ["r", "modes", "shots", "analytic_g2", "g2_corrected", "n_total_corrected"],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "claim_level": "exact_input_correspondence",
            "max_abs_g2_error": max(abs(float(row["g2_corrected"]) - float(row["analytic_g2"])) for row in rows),
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": "exact_input_correspondence",
            "code_entrypoint": "stochastic_em_theory.validation.run_multimode_validation",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "mode_filtered_squeezed_vacuum_g2",
            "units": "dimensionless oscillator units",
            "notes": "Independent equal squeezed modes with normally ordered total photon-counting estimator.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
```

- [ ] **Step 6: Add the multimode CLI subcommand**

Modify `code/src/stochastic_em_theory/cli.py` so its imports include:

```python
from stochastic_em_theory.validation import run_multimode_validation, run_single_mode_validation
```

Add this parser block after the `single` parser block:

```python
    multimode = subparsers.add_parser("multimode", help="run equal-mode squeezed-vacuum g2 validation")
    multimode.add_argument("--r", type=float, required=True)
    multimode.add_argument("--mode-counts", nargs="+", type=int, required=True)
    multimode.add_argument("--shots", type=int, required=True)
    multimode.add_argument("--seed", type=int, required=True)
    multimode.add_argument("--output-dir", type=Path, required=True)
```

Add this branch before the unknown-command `ValueError`:

```python
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
```

- [ ] **Step 7: Run multimode tests**

Run:

```bash
cd code
python -m pytest tests/test_multimode_validation.py -q
```

Expected: `3 passed`.

- [ ] **Step 8: Run a multimode CLI smoke validation**

Run:

```bash
cd code
python -m stochastic_em_theory.cli multimode --r 0.7 --mode-counts 1 2 5 --shots 50000 --seed 321 --output-dir ../results/tmp/multimode-smoke
```

Expected: `../results/tmp/multimode-smoke/multimode_g2.csv` exists.

- [ ] **Step 9: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/fields.py code/src/stochastic_em_theory/observables.py code/src/stochastic_em_theory/validation.py code/src/stochastic_em_theory/cli.py code/tests/test_multimode_validation.py
git commit -m "feat: add mode filtered squeezed validation"
```

Expected: commit succeeds.

---

### Task 5A: Add The BSV Source-Model Catalog

**Files:**
- Create: `code/src/stochastic_em_theory/source_models.py`
- Create: `code/tests/test_source_models.py`

- [ ] **Step 1: Write failing tests for source-model metadata**

Create `code/tests/test_source_models.py`:

```python
import numpy as np

from stochastic_em_theory.source_models import (
    SourceModelKind,
    effective_mode_count,
    equal_mode_source,
    schmidt_mode_source,
    single_mode_source,
    two_color_twin_beam_source,
)


def test_single_mode_source_has_unit_effective_mode_count() -> None:
    source = single_mode_source(r=0.8)

    assert source.kind == SourceModelKind.SINGLE_MODE
    assert np.isclose(effective_mode_count(source), 1.0)
    assert source.mode_weights[0].label == "mode_0"


def test_equal_mode_source_has_expected_effective_mode_count() -> None:
    source = equal_mode_source(r=0.7, modes=4)

    assert source.kind == SourceModelKind.EQUAL_MODE
    assert np.isclose(effective_mode_count(source), 4.0)
    assert len(source.mode_weights) == 4


def test_schmidt_mode_source_normalizes_brightness_weights() -> None:
    source = schmidt_mode_source(gain=1.2, eigenvalues=[0.7, 0.2, 0.1])

    assert source.kind == SourceModelKind.SCHMIDT_MODE
    assert np.isclose(sum(mode.weight for mode in source.mode_weights), 1.0)
    assert effective_mode_count(source) < 3.0


def test_two_color_source_records_signal_and_idler_modes() -> None:
    source = two_color_twin_beam_source(r=0.9, signal_label="signal", idler_label="idler")

    assert source.kind == SourceModelKind.TWO_COLOR_TWIN_BEAM
    assert [mode.label for mode in source.mode_weights] == ["signal", "idler"]
    assert np.isclose(sum(mode.weight for mode in source.mode_weights), 1.0)
```

- [ ] **Step 2: Run source-model tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_source_models.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.source_models`.

- [ ] **Step 3: Implement the source-model catalog**

Create `code/src/stochastic_em_theory/source_models.py`:

```python
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np


class SourceModelKind(str, Enum):
    SINGLE_MODE = "single_mode"
    EQUAL_MODE = "equal_mode"
    SCHMIDT_MODE = "schmidt_mode"
    TWO_COLOR_TWIN_BEAM = "two_color_twin_beam"
    PROPAGATED_NONGAUSSIAN_FRONTIER = "propagated_nongaussian_frontier"


@dataclass(frozen=True)
class SourceModeWeight:
    label: str
    nbar: float
    weight: float


@dataclass(frozen=True)
class SourceModelSpec:
    kind: SourceModelKind
    label: str
    mode_weights: tuple[SourceModeWeight, ...]
    source_refs: tuple[str, ...]
    notes: str


def _nbar_from_r(r: float) -> float:
    if r < 0:
        raise ValueError("r must be non-negative")
    return float(np.sinh(r) ** 2)


def _normalize_brightness(labels: list[str], nbars: list[float]) -> tuple[SourceModeWeight, ...]:
    if not labels:
        raise ValueError("at least one mode is required")
    if len(labels) != len(nbars):
        raise ValueError("labels and nbars must have the same length")
    if any(nbar < 0 for nbar in nbars):
        raise ValueError("mode brightness values must be non-negative")
    total = float(sum(nbars))
    if total <= 0:
        weights = [1.0 / len(nbars)] * len(nbars)
    else:
        weights = [nbar / total for nbar in nbars]
    return tuple(
        SourceModeWeight(label=label, nbar=float(nbar), weight=float(weight))
        for label, nbar, weight in zip(labels, nbars, weights, strict=True)
    )


def single_mode_source(*, r: float, label: str = "single_mode") -> SourceModelSpec:
    nbar = _nbar_from_r(r)
    return SourceModelSpec(
        kind=SourceModelKind.SINGLE_MODE,
        label=label,
        mode_weights=_normalize_brightness(["mode_0"], [nbar]),
        source_refs=("Raymer/Landes 2022", "Perez 2014"),
        notes="Ideal single detected mode used for exact input-correspondence validation.",
    )


def equal_mode_source(*, r: float, modes: int, label: str = "equal_mode") -> SourceModelSpec:
    if modes <= 0:
        raise ValueError("modes must be positive")
    nbar = _nbar_from_r(r)
    labels = [f"mode_{index}" for index in range(modes)]
    return SourceModelSpec(
        kind=SourceModelKind.EQUAL_MODE,
        label=label,
        mode_weights=_normalize_brightness(labels, [nbar] * modes),
        source_refs=("Sharapova 2015", "Sharapova 2020"),
        notes="Controlled equal-mode model used to test detection-mode dependence.",
    )


def schmidt_mode_source(*, gain: float, eigenvalues: list[float], label: str = "schmidt_mode") -> SourceModelSpec:
    if gain < 0:
        raise ValueError("gain must be non-negative")
    eigenvalue_array = np.asarray(eigenvalues, dtype=np.float64)
    if eigenvalue_array.ndim != 1 or eigenvalue_array.size == 0:
        raise ValueError("eigenvalues must be a non-empty one-dimensional list")
    if np.any(eigenvalue_array < 0):
        raise ValueError("eigenvalues must be non-negative")
    if float(np.sum(eigenvalue_array)) <= 0:
        raise ValueError("at least one eigenvalue must be positive")

    normalized = eigenvalue_array / np.sum(eigenvalue_array)
    nbars = [float(np.sinh(gain * np.sqrt(value)) ** 2) for value in normalized]
    labels = [f"schmidt_{index}" for index in range(len(nbars))]
    return SourceModelSpec(
        kind=SourceModelKind.SCHMIDT_MODE,
        label=label,
        mode_weights=_normalize_brightness(labels, nbars),
        source_refs=("Sharapova 2015", "Sharapova 2020"),
        notes="Gain-dependent Schmidt-mode brightness model for realistic BSV source studies.",
    )


def two_color_twin_beam_source(
    *,
    r: float,
    signal_label: str = "signal",
    idler_label: str = "idler",
    label: str = "two_color_twin_beam",
) -> SourceModelSpec:
    nbar = _nbar_from_r(r)
    return SourceModelSpec(
        kind=SourceModelKind.TWO_COLOR_TWIN_BEAM,
        label=label,
        mode_weights=_normalize_brightness([signal_label, idler_label], [nbar, nbar]),
        source_refs=("Agafonov 2009", "Iskhakov 2012"),
        notes="Two-color or twin-beam BSV model for paired-mode source bookkeeping.",
    )


def effective_mode_count(source: SourceModelSpec) -> float:
    weights = np.asarray([mode.weight for mode in source.mode_weights], dtype=np.float64)
    return float(1.0 / np.sum(weights**2))
```

- [ ] **Step 4: Run source-model tests**

Run:

```bash
cd code
python -m pytest tests/test_source_models.py -q
```

Expected: `4 passed`.

- [ ] **Step 5: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/source_models.py code/tests/test_source_models.py
git commit -m "feat: add bsv source model catalog"
```

Expected: commit succeeds.

---

### Task 5B: Add Mechanism-Family Labels

**Files:**
- Create: `code/src/stochastic_em_theory/mechanisms.py`
- Create: `code/tests/test_mechanisms.py`

- [ ] **Step 1: Write failing tests for mechanism labels**

Create `code/tests/test_mechanisms.py`:

```python
from stochastic_em_theory.mechanisms import MechanismFamily, mechanism_manifest_value


def test_mechanism_values_are_manifest_strings() -> None:
    assert MechanismFamily.BSV_PUMP_ENSEMBLE.value == "bsv_pump_ensemble"
    assert MechanismFamily.ATI_PHOTON_STATISTICS.value == "ati_photon_statistics"
    assert MechanismFamily.SQUEEZED_EMISSION_MODE_ENVIRONMENT.value == "squeezed_emission_mode_environment"


def test_mechanism_manifest_value_accepts_enum_or_string() -> None:
    assert mechanism_manifest_value(MechanismFamily.BSV_PUMP_ENSEMBLE) == "bsv_pump_ensemble"
    assert mechanism_manifest_value("custom_boundary_check") == "custom_boundary_check"
```

- [ ] **Step 2: Run mechanism-label tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_mechanisms.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.mechanisms`.

- [ ] **Step 3: Implement mechanism-family labels**

Create `code/src/stochastic_em_theory/mechanisms.py`:

```python
from __future__ import annotations

from enum import Enum


class MechanismFamily(str, Enum):
    BSV_PUMP_ENSEMBLE = "bsv_pump_ensemble"
    ATI_PHOTON_STATISTICS = "ati_photon_statistics"
    SQUEEZED_EMISSION_MODE_ENVIRONMENT = "squeezed_emission_mode_environment"


def mechanism_manifest_value(mechanism: MechanismFamily | str) -> str:
    if isinstance(mechanism, MechanismFamily):
        return mechanism.value
    if not mechanism:
        raise ValueError("mechanism must be a non-empty string")
    return mechanism
```

- [ ] **Step 4: Run mechanism-label tests**

Run:

```bash
cd code
python -m pytest tests/test_mechanisms.py -q
```

Expected: `2 passed`.

- [ ] **Step 5: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/mechanisms.py code/tests/test_mechanisms.py
git commit -m "feat: add mechanism family labels"
```

Expected: commit succeeds.

---

### Task 6: Add Plotting For Validation Figures

**Files:**
- Create: `code/src/stochastic_em_theory/plotting.py`
- Create: `code/tests/test_plotting.py`
- Modify: `code/src/stochastic_em_theory/cli.py`

- [ ] **Step 1: Write failing plotting tests**

Create `code/tests/test_plotting.py`:

```python
import csv

from stochastic_em_theory.plotting import plot_multimode_g2, plot_single_mode_g2


def test_single_mode_plot_writes_png(tmp_path) -> None:
    csv_path = tmp_path / "single_mode_g2.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "r",
                "shots",
                "analytic_n",
                "estimated_n",
                "analytic_g2",
                "g2_corrected",
                "g2_naive",
                "abs2_wigner",
                "abs4_wigner",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "r": 0.5,
                "shots": 1000,
                "analytic_n": 0.27,
                "estimated_n": 0.27,
                "analytic_g2": 6.7,
                "g2_corrected": 6.8,
                "g2_naive": 2.2,
                "abs2_wigner": 0.77,
                "abs4_wigner": 1.3,
            }
        )

    output_path = plot_single_mode_g2(csv_path=csv_path, output_path=tmp_path / "single.png")

    assert output_path.exists()
    assert output_path.stat().st_size > 1000


def test_multimode_plot_writes_png(tmp_path) -> None:
    csv_path = tmp_path / "multimode_g2.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["r", "modes", "shots", "analytic_g2", "g2_corrected", "n_total_corrected"],
        )
        writer.writeheader()
        writer.writerow({"r": 0.7, "modes": 1, "shots": 1000, "analytic_g2": 4.2, "g2_corrected": 4.1, "n_total_corrected": 0.5})
        writer.writerow({"r": 0.7, "modes": 4, "shots": 1000, "analytic_g2": 1.8, "g2_corrected": 1.9, "n_total_corrected": 2.0})

    output_path = plot_multimode_g2(csv_path=csv_path, output_path=tmp_path / "multi.png")

    assert output_path.exists()
    assert output_path.stat().st_size > 1000
```

- [ ] **Step 2: Run the plotting tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_plotting.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.plotting`.

- [ ] **Step 3: Implement plotting functions**

Create `code/src/stochastic_em_theory/plotting.py`:

```python
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def _read_csv_columns(csv_path: Path) -> dict[str, list[float]]:
    with csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"{csv_path} contains no data rows")
    columns: dict[str, list[float]] = {key: [] for key in rows[0]}
    for row in rows:
        for key, value in row.items():
            columns[key].append(float(value))
    return columns


def plot_single_mode_g2(*, csv_path: Path, output_path: Path) -> Path:
    columns = _read_csv_columns(csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.0, 4.0), constrained_layout=True)
    ax.plot(columns["r"], columns["analytic_g2"], color="black", label="analytic")
    ax.scatter(columns["r"], columns["g2_corrected"], color="#0072B2", label="corrected Wigner")
    ax.scatter(columns["r"], columns["g2_naive"], color="#D55E00", marker="x", label="naive raw moment")
    ax.set_xlabel("squeezing parameter r")
    ax.set_ylabel("g^(2)(0)")
    ax.set_title("Single-mode squeezed-vacuum photon-counting validation")
    ax.legend(frameon=False)
    ax.grid(alpha=0.25)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def plot_multimode_g2(*, csv_path: Path, output_path: Path) -> Path:
    columns = _read_csv_columns(csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.0, 4.0), constrained_layout=True)
    ax.plot(columns["modes"], columns["analytic_g2"], color="black", label="analytic")
    ax.scatter(columns["modes"], columns["g2_corrected"], color="#009E73", label="corrected Wigner")
    ax.set_xlabel("number of equal detected modes")
    ax.set_ylabel("total g^(2)(0)")
    ax.set_title("Mode-filtered squeezed-vacuum validation")
    ax.legend(frameon=False)
    ax.grid(alpha=0.25)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path
```

- [ ] **Step 4: Add the plotting CLI subcommands**

Modify imports in `code/src/stochastic_em_theory/cli.py`:

```python
from stochastic_em_theory.plotting import plot_multimode_g2, plot_single_mode_g2
```

Add these parser blocks after the validation parser blocks:

```python
    plot_single = subparsers.add_parser("plot-single-mode", help="plot single-mode g2 validation CSV")
    plot_single.add_argument("--csv-path", type=Path, required=True)
    plot_single.add_argument("--output-path", type=Path, required=True)

    plot_multi = subparsers.add_parser("plot-multimode", help="plot multimode g2 validation CSV")
    plot_multi.add_argument("--csv-path", type=Path, required=True)
    plot_multi.add_argument("--output-path", type=Path, required=True)
```

Add these branches before the unknown-command `ValueError`:

```python
    if args.command == "plot-single-mode":
        print(plot_single_mode_g2(csv_path=args.csv_path, output_path=args.output_path))
        return 0
    if args.command == "plot-multimode":
        print(plot_multimode_g2(csv_path=args.csv_path, output_path=args.output_path))
        return 0
```

- [ ] **Step 5: Run plotting tests**

Run:

```bash
cd code
python -m pytest tests/test_plotting.py -q
```

Expected: `2 passed`.

- [ ] **Step 6: Run the full test suite**

Run:

```bash
cd code
python -m pytest -q
```

Expected: all tests pass.

- [ ] **Step 7: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/plotting.py code/src/stochastic_em_theory/cli.py code/tests/test_plotting.py
git commit -m "feat: add validation plotting"
```

Expected: commit succeeds.

---

### Task 7: Add A Fast HHG Intensity Proxy

**Files:**
- Create: `code/src/stochastic_em_theory/hhg_proxy.py`
- Create: `code/tests/test_hhg_proxy.py`

- [ ] **Step 1: Write failing tests for the HHG proxy**

Create `code/tests/test_hhg_proxy.py`:

```python
import numpy as np

from stochastic_em_theory.hhg_proxy import cutoff_energy_au, odd_harmonic_orders, proxy_hhg_spectrum


def test_cutoff_energy_increases_with_field_amplitude() -> None:
    weak = cutoff_energy_au(field_amplitude_au=0.03, omega_au=0.057, ionization_potential_au=0.7924)
    strong = cutoff_energy_au(field_amplitude_au=0.06, omega_au=0.057, ionization_potential_au=0.7924)

    assert strong > weak


def test_odd_harmonic_orders_are_odd() -> None:
    orders = odd_harmonic_orders(max_order=15)

    assert orders.tolist() == [1, 3, 5, 7, 9, 11, 13, 15]


def test_proxy_spectrum_has_expected_shape_and_nonnegative_intensity() -> None:
    spectrum = proxy_hhg_spectrum(
        field_amplitude_au=0.05,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=31,
    )

    assert spectrum.orders.shape == spectrum.intensity.shape
    assert np.all(spectrum.intensity >= 0.0)
    assert spectrum.cutoff_order > 0.0
```

- [ ] **Step 2: Run the tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_hhg_proxy.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.hhg_proxy`.

- [ ] **Step 3: Implement the HHG proxy**

Create `code/src/stochastic_em_theory/hhg_proxy.py`:

```python
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class HHGProxySpectrum:
    orders: FloatArray
    intensity: FloatArray
    cutoff_energy_au: float
    cutoff_order: float


def ponderomotive_energy_au(*, field_amplitude_au: float, omega_au: float) -> float:
    if field_amplitude_au < 0:
        raise ValueError("field_amplitude_au must be non-negative")
    if omega_au <= 0:
        raise ValueError("omega_au must be positive")
    return float(field_amplitude_au**2 / (4.0 * omega_au**2))


def cutoff_energy_au(*, field_amplitude_au: float, omega_au: float, ionization_potential_au: float) -> float:
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    up = ponderomotive_energy_au(field_amplitude_au=field_amplitude_au, omega_au=omega_au)
    return float(ionization_potential_au + 3.17 * up)


def odd_harmonic_orders(*, max_order: int) -> FloatArray:
    if max_order < 1:
        raise ValueError("max_order must be at least 1")
    return np.arange(1, max_order + 1, 2, dtype=np.float64)


def proxy_hhg_spectrum(
    *,
    field_amplitude_au: float,
    omega_au: float,
    ionization_potential_au: float,
    max_order: int,
    nonlinearity_power: float = 6.0,
) -> HHGProxySpectrum:
    """Fast HHG intensity proxy for ensemble and plotting pipeline tests.

    This is not a TDSE result. It encodes three-step cutoff scaling and a
    smooth plateau-to-cutoff envelope for intensity-level pipeline development.
    """

    if nonlinearity_power <= 0:
        raise ValueError("nonlinearity_power must be positive")
    orders = odd_harmonic_orders(max_order=max_order)
    cutoff_energy = cutoff_energy_au(
        field_amplitude_au=field_amplitude_au,
        omega_au=omega_au,
        ionization_potential_au=ionization_potential_au,
    )
    cutoff_order = cutoff_energy / omega_au
    plateau = np.power(max(field_amplitude_au, 0.0), nonlinearity_power)
    rolloff = np.exp(-np.maximum(orders - cutoff_order, 0.0) / max(cutoff_order, 1.0))
    low_order_suppression = 1.0 - np.exp(-orders / 3.0)
    intensity = plateau * rolloff * low_order_suppression
    return HHGProxySpectrum(
        orders=orders,
        intensity=intensity.astype(np.float64),
        cutoff_energy_au=float(cutoff_energy),
        cutoff_order=float(cutoff_order),
    )
```

- [ ] **Step 4: Run HHG proxy tests**

Run:

```bash
cd code
python -m pytest tests/test_hhg_proxy.py -q
```

Expected: `3 passed`.

- [ ] **Step 5: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/hhg_proxy.py code/tests/test_hhg_proxy.py
git commit -m "feat: add hhg intensity proxy"
```

Expected: commit succeeds.

---

### Task 7A: Add Ionization Proxies And Per-Shot Records

**Files:**
- Create: `code/src/stochastic_em_theory/ionization.py`
- Create: `code/src/stochastic_em_theory/shot_records.py`
- Create: `code/tests/test_ionization_and_records.py`

- [ ] **Step 1: Write failing tests for ionization proxies and shot records**

Create `code/tests/test_ionization_and_records.py`:

```python
import numpy as np

from stochastic_em_theory.ionization import adk_like_rate_au, keldysh_parameter
from stochastic_em_theory.shot_records import HHGShotRecord, shot_records_to_rows


def test_keldysh_parameter_decreases_with_field_strength() -> None:
    weak = keldysh_parameter(field_amplitude_au=0.03, omega_au=0.057, ionization_potential_au=0.7924)
    strong = keldysh_parameter(field_amplitude_au=0.06, omega_au=0.057, ionization_potential_au=0.7924)

    assert strong < weak


def test_adk_like_rate_increases_with_field_strength() -> None:
    weak = adk_like_rate_au(field_amplitude_au=0.03, ionization_potential_au=0.7924)
    strong = adk_like_rate_au(field_amplitude_au=0.06, ionization_potential_au=0.7924)

    assert strong > weak
    assert weak > 0.0


def test_shot_records_convert_to_csv_rows() -> None:
    records = [
        HHGShotRecord(
            shot_index=0,
            source_model_kind="single_mode",
            source_model_label="paper_one",
            driver_x=0.1,
            driver_p=-0.2,
            driver_intensity=0.05,
            driver_phase=-1.1,
            field_amplitude_au=0.04,
            ionization_rate_proxy=1.0e-4,
            cutoff_order=21.0,
            harmonic_phase_proxy=0.3,
        )
    ]

    rows = shot_records_to_rows(records)

    assert rows[0]["source_model_kind"] == "single_mode"
    assert np.isclose(float(rows[0]["cutoff_order"]), 21.0)
```

- [ ] **Step 2: Run tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_ionization_and_records.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.ionization`.

- [ ] **Step 3: Implement ionization proxy functions**

Create `code/src/stochastic_em_theory/ionization.py`:

```python
from __future__ import annotations

import numpy as np


def keldysh_parameter(*, field_amplitude_au: float, omega_au: float, ionization_potential_au: float) -> float:
    if field_amplitude_au <= 0:
        raise ValueError("field_amplitude_au must be positive")
    if omega_au <= 0:
        raise ValueError("omega_au must be positive")
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    return float(omega_au * np.sqrt(2.0 * ionization_potential_au) / field_amplitude_au)


def adk_like_rate_au(*, field_amplitude_au: float, ionization_potential_au: float) -> float:
    """Monotone ADK-like tunneling-rate proxy for per-shot diagnostics.

    This proxy is used to rank and bin shots. It is not a quantitative ADK
    implementation and must not be cited as an ionization model.
    """

    if field_amplitude_au <= 0:
        raise ValueError("field_amplitude_au must be positive")
    if ionization_potential_au <= 0:
        raise ValueError("ionization_potential_au must be positive")
    exponent = -2.0 * (2.0 * ionization_potential_au) ** 1.5 / (3.0 * field_amplitude_au)
    prefactor = field_amplitude_au**2
    return float(prefactor * np.exp(exponent))
```

- [ ] **Step 4: Implement per-shot record serialization**

Create `code/src/stochastic_em_theory/shot_records.py`:

```python
from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class HHGShotRecord:
    shot_index: int
    source_model_kind: str
    source_model_label: str
    driver_x: float
    driver_p: float
    driver_intensity: float
    driver_phase: float
    field_amplitude_au: float
    ionization_rate_proxy: float
    cutoff_order: float
    harmonic_phase_proxy: float


def shot_records_to_rows(records: list[HHGShotRecord]) -> list[dict[str, int | float | str]]:
    return [asdict(record) for record in records]
```

- [ ] **Step 5: Run ionization and record tests**

Run:

```bash
cd code
python -m pytest tests/test_ionization_and_records.py -q
```

Expected: `3 passed`.

- [ ] **Step 6: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/ionization.py code/src/stochastic_em_theory/shot_records.py code/tests/test_ionization_and_records.py
git commit -m "feat: add ionization proxies and shot records"
```

Expected: commit succeeds.

---

### Task 8: Add Tested 1D Soft-Core TDSE Utilities

**Files:**
- Create: `code/src/stochastic_em_theory/tdse1d.py`
- Create: `code/tests/test_tdse1d.py`

- [ ] **Step 1: Write failing tests for split-operator utilities**

Create `code/tests/test_tdse1d.py`:

```python
import numpy as np

from stochastic_em_theory.tdse1d import (
    SoftCoreGrid,
    acceleration_expectation,
    gaussian_wavepacket,
    normalize_wavefunction,
    soft_core_potential,
    split_operator_step,
)


def test_soft_core_potential_is_even_and_negative() -> None:
    grid = SoftCoreGrid.create(x_min=-10.0, x_max=10.0, points=256)
    potential = soft_core_potential(grid.x, softening=0.8160)

    assert np.all(potential < 0.0)
    assert np.isclose(potential[0], potential[-1], rtol=1e-3)


def test_split_operator_conserves_norm_without_field() -> None:
    grid = SoftCoreGrid.create(x_min=-20.0, x_max=20.0, points=512)
    potential = soft_core_potential(grid.x, softening=0.8160)
    psi = gaussian_wavepacket(grid.x, width=2.0)
    psi = normalize_wavefunction(psi, grid.dx)

    for _ in range(20):
        psi = split_operator_step(psi=psi, grid=grid, potential=potential, field_au=0.0, dt_au=0.02)

    norm = np.sum(np.abs(psi) ** 2) * grid.dx
    assert np.isclose(norm, 1.0, atol=2e-10)


def test_even_wavefunction_has_zero_acceleration_without_field() -> None:
    grid = SoftCoreGrid.create(x_min=-20.0, x_max=20.0, points=512)
    potential = soft_core_potential(grid.x, softening=0.8160)
    psi = normalize_wavefunction(gaussian_wavepacket(grid.x, width=2.0), grid.dx)

    acceleration = acceleration_expectation(psi=psi, grid=grid, potential=potential, field_au=0.0)

    assert abs(acceleration) < 1e-12
```

- [ ] **Step 2: Run TDSE tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_tdse1d.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.tdse1d`.

- [ ] **Step 3: Implement split-operator utilities**

Create `code/src/stochastic_em_theory/tdse1d.py`:

```python
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]
ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class SoftCoreGrid:
    x: FloatArray
    k: FloatArray
    dx: float

    @classmethod
    def create(cls, *, x_min: float, x_max: float, points: int) -> "SoftCoreGrid":
        if points < 8:
            raise ValueError("points must be at least 8")
        if x_max <= x_min:
            raise ValueError("x_max must be greater than x_min")
        x = np.linspace(x_min, x_max, points, endpoint=False, dtype=np.float64)
        dx = float(x[1] - x[0])
        k = 2.0 * np.pi * np.fft.fftfreq(points, d=dx)
        return cls(x=x, k=k.astype(np.float64), dx=dx)


def soft_core_potential(x: FloatArray, *, softening: float) -> FloatArray:
    if softening <= 0:
        raise ValueError("softening must be positive")
    return (-1.0 / np.sqrt(x**2 + softening**2)).astype(np.float64)


def gaussian_wavepacket(x: FloatArray, *, width: float) -> ComplexArray:
    if width <= 0:
        raise ValueError("width must be positive")
    return np.exp(-0.5 * (x / width) ** 2).astype(np.complex128)


def normalize_wavefunction(psi: ComplexArray, dx: float) -> ComplexArray:
    norm = np.sqrt(float(np.sum(np.abs(psi) ** 2) * dx))
    if norm <= 0:
        raise ValueError("wavefunction norm must be positive")
    return (psi / norm).astype(np.complex128)


def split_operator_step(
    *,
    psi: ComplexArray,
    grid: SoftCoreGrid,
    potential: FloatArray,
    field_au: float,
    dt_au: float,
) -> ComplexArray:
    if dt_au <= 0:
        raise ValueError("dt_au must be positive")
    if psi.shape != grid.x.shape or potential.shape != grid.x.shape:
        raise ValueError("psi, potential, and grid.x must have matching shape")

    interaction = potential + grid.x * field_au
    half_potential_phase = np.exp(-0.5j * interaction * dt_au)
    kinetic_phase = np.exp(-0.5j * grid.k**2 * dt_au)
    psi_half = half_potential_phase * psi
    psi_k = np.fft.fft(psi_half)
    psi_after_k = np.fft.ifft(kinetic_phase * psi_k)
    return (half_potential_phase * psi_after_k).astype(np.complex128)


def acceleration_expectation(
    *,
    psi: ComplexArray,
    grid: SoftCoreGrid,
    potential: FloatArray,
    field_au: float,
) -> float:
    if psi.shape != grid.x.shape or potential.shape != grid.x.shape:
        raise ValueError("psi, potential, and grid.x must have matching shape")
    density = np.abs(psi) ** 2
    d_v_dx = np.gradient(potential, grid.dx, edge_order=2)
    acceleration_density = -(d_v_dx + field_au) * density
    return float(np.sum(acceleration_density) * grid.dx)


def acceleration_spectrum(acceleration: FloatArray, *, dt_au: float) -> tuple[FloatArray, FloatArray]:
    if acceleration.ndim != 1:
        raise ValueError("acceleration must be one-dimensional")
    if dt_au <= 0:
        raise ValueError("dt_au must be positive")
    window = np.hanning(acceleration.size)
    spectrum = np.fft.rfft(acceleration * window)
    angular_frequency = 2.0 * np.pi * np.fft.rfftfreq(acceleration.size, d=dt_au)
    return angular_frequency.astype(np.float64), (np.abs(spectrum) ** 2).astype(np.float64)
```

- [ ] **Step 4: Run TDSE tests**

Run:

```bash
cd code
python -m pytest tests/test_tdse1d.py -q
```

Expected: `3 passed`.

- [ ] **Step 5: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/tdse1d.py code/tests/test_tdse1d.py
git commit -m "feat: add soft core tdse utilities"
```

Expected: commit succeeds.

---

### Task 9: Add HHG Ensemble Runner With Claim Labels

**Files:**
- Create: `code/src/stochastic_em_theory/claim_ladder.py`
- Create: `code/src/stochastic_em_theory/ensemble.py`
- Modify: `code/src/stochastic_em_theory/cli.py`
- Create: `code/tests/test_hhg_ensemble.py`

- [ ] **Step 1: Write failing HHG ensemble tests**

Create `code/tests/test_hhg_ensemble.py`:

```python
import csv

import yaml

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.ensemble import run_proxy_hhg_ensemble


def test_proxy_hhg_ensemble_writes_labeled_outputs(tmp_path) -> None:
    result = run_proxy_hhg_ensemble(
        r=0.8,
        phase=0.0,
        shots=64,
        seed=42,
        base_field_amplitude_au=0.035,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=21,
        output_dir=tmp_path,
    )

    assert result.csv_path.exists()
    assert result.summary_path.exists()
    assert result.manifest_path.exists()

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 11
    assert all(float(row["mean_intensity"]) >= 0.0 for row in rows)
    assert all(row["claim_level"] == ClaimLevel.HHG_INTENSITY_PREDICTION.value for row in rows)

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["claim_level"] == ClaimLevel.HHG_INTENSITY_PREDICTION.value
    assert manifest["random_seeds"] == [42]
```

- [ ] **Step 2: Run ensemble tests and verify they fail**

Run:

```bash
cd code
python -m pytest tests/test_hhg_ensemble.py -q
```

Expected: FAIL with `ModuleNotFoundError` for `stochastic_em_theory.claim_ladder`.

- [ ] **Step 3: Implement claim labels**

Create `code/src/stochastic_em_theory/claim_ladder.py`:

```python
from __future__ import annotations

from enum import Enum


class ClaimLevel(str, Enum):
    EXACT_INPUT_CORRESPONDENCE = "exact_input_correspondence"
    VALIDATED_STOCHASTIC_SIMULATION = "validated_stochastic_simulation"
    HHG_INTENSITY_PREDICTION = "hhg_intensity_prediction"
    GAUSSIAN_OUTPUT_DIAGNOSTIC = "gaussian_output_diagnostic"
    NON_GAUSSIAN_FRONTIER = "non_gaussian_frontier"
```

- [ ] **Step 4: Implement HHG ensemble aggregation**

Create `code/src/stochastic_em_theory/ensemble.py`:

```python
from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.fields import sample_single_mode_husimi_q
from stochastic_em_theory.hhg_proxy import proxy_hhg_spectrum
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest


def _conditional_means(values: np.ndarray, spectra: np.ndarray) -> dict[str, np.ndarray]:
    quantiles = np.quantile(values, [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    bins: dict[str, np.ndarray] = {}
    labels = ["low", "middle", "high"]
    for index, label in enumerate(labels):
        left = quantiles[index]
        right = quantiles[index + 1]
        if index == len(labels) - 1:
            mask = (values >= left) & (values <= right)
        else:
            mask = (values >= left) & (values < right)
        if not np.any(mask):
            bins[label] = np.zeros(spectra.shape[1], dtype=np.float64)
        else:
            bins[label] = np.mean(spectra[mask], axis=0)
    return bins


def run_proxy_hhg_ensemble(
    *,
    r: float,
    phase: float,
    shots: int,
    seed: int,
    base_field_amplitude_au: float,
    omega_au: float,
    ionization_potential_au: float,
    max_order: int,
    output_dir: Path,
) -> RunArtifacts:
    if shots <= 0:
        raise ValueError("shots must be positive")
    if base_field_amplitude_au <= 0:
        raise ValueError("base_field_amplitude_au must be positive")

    output_dir = ensure_output_dir(output_dir)
    rng = np.random.default_rng(seed)
    alpha = sample_single_mode_husimi_q(r=r, phase=phase, shots=shots, rng=rng)
    sampled_intensity = np.abs(alpha) ** 2
    normalized_amplitude = np.sqrt(sampled_intensity / max(float(np.mean(sampled_intensity)), 1e-12))
    field_amplitudes = base_field_amplitude_au * normalized_amplitude

    spectra = []
    cutoff_orders = []
    orders = None
    for field_amplitude in field_amplitudes:
        spectrum = proxy_hhg_spectrum(
            field_amplitude_au=float(field_amplitude),
            omega_au=omega_au,
            ionization_potential_au=ionization_potential_au,
            max_order=max_order,
        )
        orders = spectrum.orders
        spectra.append(spectrum.intensity)
        cutoff_orders.append(spectrum.cutoff_order)

    if orders is None:
        raise ValueError("no spectra were generated")

    spectra_array = np.vstack(spectra)
    conditional = _conditional_means(sampled_intensity, spectra_array)
    mean_spectrum = np.mean(spectra_array, axis=0)
    std_spectrum = np.std(spectra_array, axis=0, ddof=1) if shots > 1 else np.zeros_like(mean_spectrum)

    rows = []
    for index, order in enumerate(orders):
        rows.append(
            {
                "harmonic_order": float(order),
                "mean_intensity": float(mean_spectrum[index]),
                "std_intensity": float(std_spectrum[index]),
                "conditional_low": float(conditional["low"][index]),
                "conditional_middle": float(conditional["middle"][index]),
                "conditional_high": float(conditional["high"][index]),
                "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            }
        )

    csv_path = output_dir / "proxy_hhg_spectrum.csv"
    summary_path = output_dir / "proxy_hhg_summary.json"
    manifest_path = output_dir / "manifest.yaml"
    write_csv(
        csv_path,
        rows,
        [
            "harmonic_order",
            "mean_intensity",
            "std_intensity",
            "conditional_low",
            "conditional_middle",
            "conditional_high",
            "claim_level",
        ],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "mean_cutoff_order": float(np.mean(cutoff_orders)),
            "std_cutoff_order": float(np.std(cutoff_orders, ddof=1)) if shots > 1 else 0.0,
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "code_entrypoint": "stochastic_em_theory.ensemble.run_proxy_hhg_ensemble",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "proxy_hhg_intensity_spectrum",
            "units": "atomic units for fields and energies; dimensionless harmonic order",
            "notes": "Fast cutoff-weighted HHG proxy used for ensemble-pipeline development, not TDSE publication result.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
```

- [ ] **Step 5: Add the proxy-HHG CLI subcommand**

Modify `code/src/stochastic_em_theory/cli.py` imports:

```python
from stochastic_em_theory.ensemble import run_proxy_hhg_ensemble
```

Add this parser block:

```python
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
```

Add this branch:

```python
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
```

- [ ] **Step 6: Run HHG ensemble tests**

Run:

```bash
cd code
python -m pytest tests/test_hhg_ensemble.py -q
```

Expected: `1 passed`.

- [ ] **Step 7: Run a proxy-HHG CLI smoke run**

Run:

```bash
cd code
python -m stochastic_em_theory.cli proxy-hhg --r 0.8 --shots 128 --seed 42 --base-field-amplitude-au 0.035 --max-order 21 --output-dir ../results/tmp/proxy-hhg-smoke
```

Expected: `../results/tmp/proxy-hhg-smoke/proxy_hhg_spectrum.csv` exists.

- [ ] **Step 8: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/claim_ladder.py code/src/stochastic_em_theory/ensemble.py code/src/stochastic_em_theory/cli.py code/tests/test_hhg_ensemble.py
git commit -m "feat: add labeled hhg ensemble runner"
```

Expected: commit succeeds.

---

### Task 9A: Upgrade HHG Ensemble Outputs With Source Metadata And Shot Records

**Files:**
- Modify: `code/src/stochastic_em_theory/ensemble.py`
- Modify: `code/tests/test_hhg_ensemble.py`

- [ ] **Step 1: Extend the HHG ensemble test for shot records**

Replace `code/tests/test_hhg_ensemble.py` with:

```python
import csv

import yaml

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.ensemble import run_proxy_hhg_ensemble
from stochastic_em_theory.source_models import single_mode_source


def test_proxy_hhg_ensemble_writes_labeled_outputs_and_shot_records(tmp_path) -> None:
    source_model = single_mode_source(r=0.8, label="test_single_mode")
    result = run_proxy_hhg_ensemble(
        r=0.8,
        phase=0.0,
        shots=64,
        seed=42,
        base_field_amplitude_au=0.035,
        omega_au=0.057,
        ionization_potential_au=0.7924,
        max_order=21,
        output_dir=tmp_path,
        source_model=source_model,
    )

    shot_records_path = tmp_path / "shot_records.csv"
    assert result.csv_path.exists()
    assert result.summary_path.exists()
    assert result.manifest_path.exists()
    assert shot_records_path.exists()

    with result.csv_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 11
    assert all(float(row["mean_intensity"]) >= 0.0 for row in rows)
    assert all(row["claim_level"] == ClaimLevel.HHG_INTENSITY_PREDICTION.value for row in rows)

    with shot_records_path.open(newline="") as handle:
        shot_rows = list(csv.DictReader(handle))

    assert len(shot_rows) == 64
    assert shot_rows[0]["source_model_kind"] == "single_mode"
    assert shot_rows[0]["source_model_label"] == "test_single_mode"
    assert float(shot_rows[0]["ionization_rate_proxy"]) >= 0.0

    manifest = yaml.safe_load(result.manifest_path.read_text())
    assert manifest["claim_level"] == ClaimLevel.HHG_INTENSITY_PREDICTION.value
    assert manifest["random_seeds"] == [42]
    assert manifest["source_model"]["kind"] == "single_mode"
    assert manifest["source_model"]["label"] == "test_single_mode"
```

- [ ] **Step 2: Run the upgraded ensemble test and verify it fails**

Run:

```bash
cd code
python -m pytest tests/test_hhg_ensemble.py -q
```

Expected: FAIL because `run_proxy_hhg_ensemble` does not accept `source_model`.

- [ ] **Step 3: Replace the ensemble implementation with source-aware shot records**

Replace `code/src/stochastic_em_theory/ensemble.py` with:

```python
from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np

from stochastic_em_theory.claim_ladder import ClaimLevel
from stochastic_em_theory.fields import sample_single_mode_husimi_q
from stochastic_em_theory.hhg_proxy import proxy_hhg_spectrum
from stochastic_em_theory.ionization import adk_like_rate_au
from stochastic_em_theory.io import RunArtifacts, current_git_commit, ensure_output_dir, write_csv, write_json, write_manifest
from stochastic_em_theory.shot_records import HHGShotRecord, shot_records_to_rows
from stochastic_em_theory.source_models import SourceModelSpec, single_mode_source


def _conditional_means(values: np.ndarray, spectra: np.ndarray) -> dict[str, np.ndarray]:
    quantiles = np.quantile(values, [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    bins: dict[str, np.ndarray] = {}
    labels = ["low", "middle", "high"]
    for index, label in enumerate(labels):
        left = quantiles[index]
        right = quantiles[index + 1]
        if index == len(labels) - 1:
            mask = (values >= left) & (values <= right)
        else:
            mask = (values >= left) & (values < right)
        if not np.any(mask):
            bins[label] = np.zeros(spectra.shape[1], dtype=np.float64)
        else:
            bins[label] = np.mean(spectra[mask], axis=0)
    return bins


def _source_model_manifest(source_model: SourceModelSpec) -> dict[str, object]:
    return {
        "kind": source_model.kind.value,
        "label": source_model.label,
        "mode_weights": [
            {"label": mode.label, "nbar": mode.nbar, "weight": mode.weight}
            for mode in source_model.mode_weights
        ],
        "source_refs": list(source_model.source_refs),
        "notes": source_model.notes,
    }


def run_proxy_hhg_ensemble(
    *,
    r: float,
    phase: float,
    shots: int,
    seed: int,
    base_field_amplitude_au: float,
    omega_au: float,
    ionization_potential_au: float,
    max_order: int,
    output_dir: Path,
    source_model: SourceModelSpec | None = None,
) -> RunArtifacts:
    if shots <= 0:
        raise ValueError("shots must be positive")
    if base_field_amplitude_au <= 0:
        raise ValueError("base_field_amplitude_au must be positive")

    output_dir = ensure_output_dir(output_dir)
    source_model = source_model if source_model is not None else single_mode_source(r=r, label="default_single_mode")
    rng = np.random.default_rng(seed)
    alpha = sample_single_mode_husimi_q(r=r, phase=phase, shots=shots, rng=rng)
    sampled_intensity = np.abs(alpha) ** 2
    normalized_amplitude = np.sqrt(sampled_intensity / max(float(np.mean(sampled_intensity)), 1e-12))
    field_amplitudes = base_field_amplitude_au * normalized_amplitude

    spectra = []
    cutoff_orders = []
    shot_records: list[HHGShotRecord] = []
    orders = None
    for shot_index, (field_amplitude, alpha_value, intensity_value) in enumerate(zip(field_amplitudes, alpha, sampled_intensity, strict=True)):
        spectrum = proxy_hhg_spectrum(
            field_amplitude_au=float(field_amplitude),
            omega_au=omega_au,
            ionization_potential_au=ionization_potential_au,
            max_order=max_order,
        )
        orders = spectrum.orders
        spectra.append(spectrum.intensity)
        cutoff_orders.append(spectrum.cutoff_order)
        shot_records.append(
            HHGShotRecord(
                shot_index=shot_index,
                source_model_kind=source_model.kind.value,
                source_model_label=source_model.label,
                driver_x=float(np.sqrt(2.0) * np.real(alpha_value)),
                driver_p=float(np.sqrt(2.0) * np.imag(alpha_value)),
                driver_intensity=float(intensity_value),
                driver_phase=float(np.angle(alpha_value)),
                field_amplitude_au=float(field_amplitude),
                ionization_rate_proxy=adk_like_rate_au(
                    field_amplitude_au=max(float(field_amplitude), 1.0e-12),
                    ionization_potential_au=ionization_potential_au,
                ),
                cutoff_order=float(spectrum.cutoff_order),
                harmonic_phase_proxy=float(np.angle(alpha_value)),
            )
        )

    if orders is None:
        raise ValueError("no spectra were generated")

    spectra_array = np.vstack(spectra)
    conditional = _conditional_means(sampled_intensity, spectra_array)
    mean_spectrum = np.mean(spectra_array, axis=0)
    std_spectrum = np.std(spectra_array, axis=0, ddof=1) if shots > 1 else np.zeros_like(mean_spectrum)

    rows = []
    for index, order in enumerate(orders):
        rows.append(
            {
                "harmonic_order": float(order),
                "mean_intensity": float(mean_spectrum[index]),
                "std_intensity": float(std_spectrum[index]),
                "conditional_low": float(conditional["low"][index]),
                "conditional_middle": float(conditional["middle"][index]),
                "conditional_high": float(conditional["high"][index]),
                "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            }
        )

    csv_path = output_dir / "proxy_hhg_spectrum.csv"
    shot_records_path = output_dir / "shot_records.csv"
    summary_path = output_dir / "proxy_hhg_summary.json"
    manifest_path = output_dir / "manifest.yaml"
    write_csv(
        csv_path,
        rows,
        [
            "harmonic_order",
            "mean_intensity",
            "std_intensity",
            "conditional_low",
            "conditional_middle",
            "conditional_high",
            "claim_level",
        ],
    )
    write_csv(
        shot_records_path,
        shot_records_to_rows(shot_records),
        [
            "shot_index",
            "source_model_kind",
            "source_model_label",
            "driver_x",
            "driver_p",
            "driver_intensity",
            "driver_phase",
            "field_amplitude_au",
            "ionization_rate_proxy",
            "cutoff_order",
            "harmonic_phase_proxy",
        ],
    )
    write_json(
        summary_path,
        {
            "rows": len(rows),
            "shots": len(shot_records),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "source_model": _source_model_manifest(source_model),
            "mean_cutoff_order": float(np.mean(cutoff_orders)),
            "std_cutoff_order": float(np.std(cutoff_orders, ddof=1)) if shots > 1 else 0.0,
            "mean_ionization_rate_proxy": float(np.mean([record.ionization_rate_proxy for record in shot_records])),
        },
    )
    write_manifest(
        manifest_path,
        {
            "run_id": output_dir.name,
            "created": date.today().isoformat(),
            "claim_level": ClaimLevel.HHG_INTENSITY_PREDICTION.value,
            "source_model": _source_model_manifest(source_model),
            "code_entrypoint": "stochastic_em_theory.ensemble.run_proxy_hhg_ensemble",
            "git_commit": current_git_commit(Path(__file__).resolve().parents[3]),
            "parameter_file": None,
            "random_seeds": [seed],
            "observable": "proxy_hhg_intensity_spectrum_with_shot_records",
            "units": "atomic units for fields and energies; dimensionless harmonic order",
            "notes": "Fast cutoff-weighted HHG proxy used for ensemble-pipeline development, not TDSE publication result.",
        },
    )
    return RunArtifacts(output_dir=output_dir, csv_path=csv_path, summary_path=summary_path, manifest_path=manifest_path)
```

- [ ] **Step 4: Run upgraded ensemble tests**

Run:

```bash
cd code
python -m pytest tests/test_hhg_ensemble.py -q
```

Expected: `1 passed`.

- [ ] **Step 5: Commit**

Run:

```bash
git add code/src/stochastic_em_theory/ensemble.py code/tests/test_hhg_ensemble.py
git commit -m "feat: add source aware hhg shot records"
```

Expected: commit succeeds.

---

### Task 10: Add End-To-End Paper-One Smoke Pipeline

**Files:**
- Create: `code/scripts/run_paper_one_smoke.py`
- Modify: `code/src/stochastic_em_theory/plotting.py`
- Create: `code/tests/test_paper_one_smoke.py`

- [ ] **Step 1: Write failing test for the smoke pipeline**

Create `code/tests/test_paper_one_smoke.py`:

```python
import subprocess
import sys
from pathlib import Path


def test_paper_one_smoke_script_creates_expected_outputs(tmp_path) -> None:
    script = Path("scripts/run_paper_one_smoke.py")
    completed = subprocess.run(
        [sys.executable, str(script), "--output-root", str(tmp_path), "--shots", "2000"],
        cwd=Path(__file__).resolve().parents[1],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "paper-one-smoke" in completed.stdout
    assert (tmp_path / "runs" / "paper-one-smoke-single" / "single_mode_g2.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-multimode" / "multimode_g2.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-hhg" / "proxy_hhg_spectrum.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-hhg" / "shot_records.csv").exists()
    assert (tmp_path / "figures" / "single_mode_g2.png").exists()
    assert (tmp_path / "figures" / "multimode_g2.png").exists()
    assert (tmp_path / "figures" / "proxy_hhg_spectrum.png").exists()
```

- [ ] **Step 2: Run the smoke-pipeline test and verify it fails**

Run:

```bash
cd code
python -m pytest tests/test_paper_one_smoke.py -q
```

Expected: FAIL because `scripts/run_paper_one_smoke.py` does not exist.

- [ ] **Step 3: Add proxy-HHG plotting**

Append this function to `code/src/stochastic_em_theory/plotting.py`:

```python

def plot_proxy_hhg_spectrum(*, csv_path: Path, output_path: Path) -> Path:
    columns = _read_csv_columns(csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.0, 4.0), constrained_layout=True)
    ax.plot(columns["harmonic_order"], columns["mean_intensity"], color="#0072B2", label="ensemble mean")
    ax.plot(columns["harmonic_order"], columns["conditional_low"], color="#999999", linestyle="--", label="low intensity bin")
    ax.plot(columns["harmonic_order"], columns["conditional_high"], color="#D55E00", linestyle="--", label="high intensity bin")
    ax.set_yscale("log")
    ax.set_xlabel("harmonic order")
    ax.set_ylabel("proxy intensity")
    ax.set_title("Squeezed-drive HHG proxy ensemble")
    ax.legend(frameon=False)
    ax.grid(alpha=0.25)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path
```

- [ ] **Step 4: Add the smoke script**

Create `code/scripts/run_paper_one_smoke.py`:

```python
from __future__ import annotations

import argparse
from pathlib import Path

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

    plot_single_mode_g2(csv_path=single.csv_path, output_path=figures_root / "single_mode_g2.png")
    plot_multimode_g2(csv_path=multi.csv_path, output_path=figures_root / "multimode_g2.png")
    plot_proxy_hhg_spectrum(csv_path=hhg.csv_path, output_path=figures_root / "proxy_hhg_spectrum.png")

    print(output_root / "runs" / "paper-one-smoke-single")
    print(output_root / "runs" / "paper-one-smoke-multimode")
    print(output_root / "runs" / "paper-one-smoke-hhg")
    print(output_root / "figures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run the smoke-pipeline test**

Run:

```bash
cd code
python -m pytest tests/test_paper_one_smoke.py -q
```

Expected: `1 passed`.

- [ ] **Step 6: Run the smoke pipeline into ignored temporary results**

Run:

```bash
cd code
python scripts/run_paper_one_smoke.py --output-root ../results/tmp/paper-one-smoke --shots 10000
```

Expected: command prints four paths and creates:

```text
results/tmp/paper-one-smoke/runs/paper-one-smoke-single/single_mode_g2.csv
results/tmp/paper-one-smoke/runs/paper-one-smoke-multimode/multimode_g2.csv
results/tmp/paper-one-smoke/runs/paper-one-smoke-hhg/proxy_hhg_spectrum.csv
results/tmp/paper-one-smoke/runs/paper-one-smoke-hhg/shot_records.csv
results/tmp/paper-one-smoke/figures/single_mode_g2.png
results/tmp/paper-one-smoke/figures/multimode_g2.png
results/tmp/paper-one-smoke/figures/proxy_hhg_spectrum.png
```

- [ ] **Step 7: Run the full test suite**

Run:

```bash
cd code
python -m pytest -q
```

Expected: all tests pass.

- [ ] **Step 8: Commit**

Run:

```bash
git add code/scripts/run_paper_one_smoke.py code/src/stochastic_em_theory/plotting.py code/tests/test_paper_one_smoke.py
git commit -m "feat: add paper one smoke pipeline"
```

Expected: commit succeeds.

---

### Task 11: Final Verification And Wiki Log Update

**Files:**
- Modify: `wiki/log.md`

- [ ] **Step 1: Run the complete verification suite**

Run:

```bash
cd code
python -m pytest -q
python scripts/run_paper_one_smoke.py --output-root ../results/tmp/paper-one-final-smoke --shots 20000
```

Expected:

```text
pytest exits with status 0
single-mode, multimode, proxy-HHG, shot-record, and figure outputs exist under results/tmp/paper-one-final-smoke
```

- [ ] **Step 2: Append the simulation implementation log entry**

Append this entry to `wiki/log.md`:

```markdown

## [2026-06-06] simulation | Paper One Simulation Pipeline

- Implemented the paper-one Python simulation package under `code/`.
- Added single-mode squeezed-vacuum Wigner validation with normally ordered
  `g^(2)` correction and naive-estimator comparison.
- Added mode-filtered equal-mode squeezed-vacuum validation.
- Added BSV source-model metadata and HHG intensity-level ensemble pipeline
  with explicit claim-ladder labels.
- Added per-shot driver, ionization-proxy, cutoff-proxy, and harmonic-phase
  records for later bunching, cutoff-fluctuation, and symmetry diagnostics.
- Verified the package with `python -m pytest -q` and the paper-one smoke run
  writing temporary outputs under `results/tmp/paper-one-final-smoke`.
```

- [ ] **Step 3: Check for accidental committed outputs**

Run:

```bash
git status --short
```

Expected: no tracked files under `results/tmp/`. If `results/tmp/` files appear as untracked, leave them uncommitted because `.gitignore` excludes `results/tmp/`.

- [ ] **Step 4: Commit the final log update**

Run:

```bash
git add wiki/log.md
git commit -m "docs: record paper one simulation pipeline"
```

Expected: commit succeeds.

---

## Self-Review Notes

- Spec coverage: Task 1 covers the required simulation spec. Tasks 3-5 cover exact squeezed-input correspondence, ordering correction, and mode-filtered validation. Task 5A adds the BSV source-model ladder required by the 52-source ingest. Tasks 6 and 10 cover paper-one validation figures. Tasks 7-9 cover the HHG intensity-level demonstration and claim labels. Task 7A and Task 9A add ionization proxies, source metadata, and per-shot records for cutoff, bunching, and symmetry diagnostics. Task 8 creates the tested bridge toward the source-backed 1D soft-core gas baseline.
- Scope control: THz, non-Gaussian output certification, macroscopic propagation, and emitted harmonic quantum-state reconstruction remain outside this implementation plan.
- Type consistency: all later tasks use the same names introduced earlier: `RunArtifacts`, `SourceModelSpec`, `sample_single_mode_wigner`, `sample_single_mode_husimi_q`, `sample_multimode_wigner`, `estimate_single_mode_moments`, `estimate_total_photon_moments`, `run_single_mode_validation`, `run_multimode_validation`, `HHGShotRecord`, and `run_proxy_hhg_ensemble`.
