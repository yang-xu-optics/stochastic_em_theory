---
title: Simulation Roadmap
type: simulation
status: seed
created: 2026-06-06
updated: 2026-06-06
tags: [simulation, roadmap, validation]
source_count: 0
confidence: low
related:
  - ../theory/squeezed-vacuum-g2-proof-plan
  - ../models/hhg-gas-model
  - ../models/thz-optical-rectification-model
  - ../models/thz-plasma-emission-model
---

# Simulation Roadmap

## Stage 0: Project Conventions

- Choose units: SI for propagation and material response, with explicit
  conversion if atomic units are used for strong-field electron dynamics.
- Define optical field normalization and mode functions.
- Define random seed handling and reproducibility policy.
- Decide where notebooks end and reusable library code begins.

## Stage 1: Squeezed-Field Sampler

Validation observables:

- quadrature variances,
- `<n>`,
- `g^{(2)}(0)` with Wigner-to-normal ordering corrections,
- convergence versus ensemble size,
- loss and finite mode-filter tests.

Expected result for single-mode pure squeezed vacuum:

```text
g^{(2)}(0) = 3 + 1/<n>
```

## Stage 2: Time-Domain Bright Squeezed Vacuum

Construct stochastic waveforms with spectral and temporal mode structure.

Validation observables:

- optical spectrum,
- temporal correlation function,
- intensity distribution,
- mode-resolved photon-number statistics,
- dependence on squeezing phase and bandwidth.

## Stage 3: HHG in Gas

Start with a single-atom or local response model. Add propagation only after
basic ensemble behavior is understood.

Outputs:

- harmonic spectra,
- cutoff distributions,
- shot-to-shot variance,
- comparison against coherent and thermal baselines.

## Stage 4: THz Optical Rectification

Start with a local `chi^(2)` polarization model and THz filtering. Add
dispersion and phase matching after validating the source term.

Outputs:

- ensemble mean THz field,
- ensemble mean THz intensity,
- shot-to-shot waveform distribution,
- dependence on squeezing phase and detection bandwidth.

## Stage 5: THz Plasma Emission

Start with a local photocurrent model. Treat symmetry as a first-class test.

Outputs:

- current and density traces,
- THz spectra,
- ensemble mean and variance,
- conditional statistics for high-field events,
- symmetry-breaking parameter scans.

## Suggested Code Layout

```text
code/
  src/
    stochastic_em_theory/
      fields.py
      observables.py
      hhg.py
      thz_or.py
      thz_plasma.py
  notebooks/
  tests/
```

This layout is a target, not yet implemented.

## Result Manifest Template

Each completed run should include a small manifest:

```yaml
run_id: YYYYMMDD-short-name
created: YYYY-MM-DD
code_entrypoint:
git_commit:
parameter_file:
random_seeds:
observable:
notes:
```

