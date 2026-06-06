---
title: THz Optical Rectification Model
type: model
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [thz, optical-rectification, nonlinear-optics, squeezed-vacuum]
source_count: 2
confidence: medium
related:
  - ../overview
  - ../simulations/simulation-roadmap
  - ../sources/raymer-landes-2023-classical-model-broadband-squeezed-vacuum
  - ../sources/sun-2022-thz-laser-induced-plasma
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

## Source-Backed Notes

- Sun 2022 treats optical rectification as one standard THz source, but most
  plasma THz language in gases is better separated into four-wave
  rectification/mixing and photocurrent mechanisms.
- In two-color plasma literature, a common effective mixing form is:

```text
E_THz(t) proportional to chi^(3) E_2omega(t) E_omega^*(t) E_omega^*(t) cos(phi)
```

This is not the same as true `chi^(2)` optical rectification in a
noncentrosymmetric crystal.
- Raymer and Landes 2023 provide a stochastic-field frequency-conversion
  analogy through SFG. The lesson for OR is to match the relevant nonlinear
  correlation and remove vacuum-only contributions if they appear.

## Source Gap

No ingested paper directly derives squeezed-vacuum-driven `chi^(2)` optical
rectification. Until that source or derivation is added, this branch should be
framed as a proposed stochastic-field calculation, not as an established
source-backed result.

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

For a zero-mean squeezed-vacuum drive, track both:

```text
<P_THz(t)>_ensemble
<|P_THz(omega)|^2>_ensemble
```

A zero mean emitted field with nonzero emitted intensity is a possible outcome,
not a failure.
