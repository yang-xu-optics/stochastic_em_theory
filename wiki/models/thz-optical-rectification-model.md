---
title: THz Optical Rectification Model
type: model
status: seed
created: 2026-06-06
updated: 2026-06-06
tags: [thz, optical-rectification, nonlinear-optics, squeezed-vacuum]
source_count: 0
confidence: low
related:
  - ../overview
  - ../simulations/simulation-roadmap
---

# THz Optical Rectification Model

This page defines the optical rectification path for THz emission driven by
stochastic squeezed optical fields.

## Minimal Source Model

For a medium with second-order susceptibility, the low-frequency nonlinear
polarization can be modeled from the stochastic optical field as:

```text
P_THz(t) = epsilon_0 chi^(2) [E(t)^2]_{THz}
```

where `[ ]_{THz}` denotes extraction of the low-frequency component after
filtering or propagation.

## Key Questions

- Does the squeezed-vacuum ensemble have a nonzero rectified polarization after
  ensemble averaging?
- Is the measurable object the ensemble-averaged THz field, the THz intensity,
  or conditional emission in individual shots?
- How do squeezing phase, optical bandwidth, and temporal-mode correlations
  change the low-frequency component of `E(t)^2`?
- How should dispersion, phase matching, and absorption be included?

## First Simulation Target

Build a 1D time-domain model:

1. sample stochastic optical waveforms,
2. compute `E_j(t)^2`,
3. apply a THz bandpass filter,
4. compare ensemble-averaged field and intensity,
5. benchmark against a coherent pulse with the same mean energy.

## Symmetry Note

Optical rectification requires a medium or effective process without inversion
symmetry. If the medium has no `chi^(2)`, any effective rectification mechanism
must be stated explicitly.

