---
title: THz Plasma Emission Model
type: model
status: seed
created: 2026-06-06
updated: 2026-06-06
tags: [thz, plasma, photocurrent, ionization, squeezed-vacuum]
source_count: 0
confidence: low
related:
  - ../overview
  - ../simulations/simulation-roadmap
---

# THz Plasma Emission Model

This page defines the plasma-emission path for THz generation driven by
stochastic squeezed optical fields.

## Minimal Photocurrent Picture

A common time-domain model evolves a free-electron current `J(t)` driven by the
optical field and ionization-generated electron density:

```text
dJ/dt + nu J = (q^2/m) n_e(t) E(t) + source_terms
dn_e/dt = W[E(t)] (n_gas - n_e)
E_THz proportional to dJ/dt
```

The exact source terms, ionization rate, and propagation model must be chosen
from sources before implementation.

## Symmetry Check

For a zero-mean stochastic drive, the ensemble-averaged plasma current may
vanish unless a physical asymmetry is present. Candidate asymmetry mechanisms:

- two-color mixing or carrier-envelope asymmetry,
- biased or oriented medium,
- conditioning on high-field events,
- propagation or ionization gating that breaks time-reversal symmetry,
- nonzero coherent displacement of the squeezed field.

The paper should treat a zero-result as scientifically meaningful if symmetry
requires it.

## Proposed Observables

- Ensemble-averaged THz field.
- Ensemble-averaged THz intensity.
- Shot-to-shot THz waveform distribution.
- Correlation of ionization bursts with field quadrature statistics.
- Dependence on squeezing phase and displacement.

## First Simulation Target

Start with a local-current model before macroscopic propagation:

1. sample `E_j(t)`,
2. compute ionization rate `W[E_j(t)]`,
3. evolve `n_e,j(t)` and `J_j(t)`,
4. band-limit `dJ_j/dt` to THz frequencies,
5. compare ensemble mean, variance, and conditional statistics.

