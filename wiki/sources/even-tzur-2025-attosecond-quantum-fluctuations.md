---
title: Even Tzur Et Al 2025 Attosecond-Resolved Quantum Fluctuations
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, hhg, bsv, attosecond, g2, tomography]
source_count: 1
confidence: high
related:
  - ../models/hhg-gas-model
  - ../theory/squeezed-vacuum-g2-proof-plan
---

# Even Tzur Et Al 2025 Attosecond-Resolved Quantum Fluctuations

## Bibliographic Metadata

- Authors: Matan Even Tzur et al.
- Year: 2025.
- Identifier: arXiv:2511.18362v1.
- Raw source: [2511.18362v1.pdf](../../raw/sources/2511.18362v1.pdf)
- Ingest date: 2026-06-06.

## Core Result

The preprint combines a strong coherent 800 nm field with weaker BSV at
1600 nm to perturb HHG. The BSV perturbation generates even and half-integer
harmonics, enabling reconstruction of quantum fluctuations of emitted XUV
harmonics and attosecond-scale electron dynamics.

## Useful Equations Or Model Ingredients

- The perturbing `omega/2` field breaks half-cycle symmetry and produces
  harmonic families. In the small-perturbation limit, half-integer harmonics
  are approximately linear in the BSV perturbation, while even harmonics are
  approximately quadratic.
- Measured harmonic families are modeled with complex phase shifts
  `sigma_j = alpha_j + i beta_j` and symmetry relations such as:

```text
sigma_3 = -sigma_1
sigma_4 = -sigma_2
```

- The reported statistics include superbunching, with half-integer harmonics
  carrying `g^(2)` values close to the BSV input and even harmonics showing
  larger values consistent with a two-BSV-photon process.

## Assumptions

- The drive is a two-color combination: strong coherent 800 nm plus BSV at
  1600 nm.
- Reconstruction uses shot-resolved harmonic intensities and two-color delay as
  a quadrature-like control.

## Limitations And Cautions

- This is not pure BSV-driven HHG; the coherent field is essential.
- The source goes beyond intensity-only modeling by reconstructing Husimi and
  Wigner distributions of emitted channels.

## Relevance To This Project

This source supports a future manuscript extension on emitted harmonic quantum
statistics. It also reinforces the need to distinguish linear and quadratic
response channels to BSV perturbations.

