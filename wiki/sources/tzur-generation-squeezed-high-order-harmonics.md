---
title: Tzur Et Al Generation Of Squeezed High-Order Harmonics
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, hhg, squeezed-light, positive-p, harmonic-state]
source_count: 1
confidence: high
related:
  - ../models/hhg-gas-model
  - ../theory/stochastic-quantum-optics-correspondence
---

# Tzur Et Al Generation Of Squeezed High-Order Harmonics

## Bibliographic Metadata

- Authors: Matan Even Tzur, Michael Birk, Alexey Gorlach, Ido Kaminer,
  Michael Kruger, and Oren Cohen.
- Year: not specified in local filename.
- Raw source: [Tzur et al. - Generation of squeezed high-order harmonics.pdf](<../../raw/sources/Tzur et al. - Generation of squeezed high-order harmonics.pdf>)
- Ingest date: 2026-06-06.

## Core Result

The paper derives how the quantum state of high-order harmonics can be obtained
when HHG is driven by arbitrary quantum light. It predicts that moderately
squeezed pump fields can generate squeezed high harmonics, while stronger pump
squeezing can produce squeezed thermal or more intricate harmonic states.

## Useful Equations Or Model Ingredients

- The driving state can be represented with a Positive P distribution and
  propagated through a semiclassical HHG response.
- For squeezed vacuum, the Husimi distribution is Gaussian in quadratures:

```text
Q_SV(alpha) =
  1 / (pi cosh r)
  exp[-2 alpha_y^2 / (1 + exp(2r))
      -2 alpha_x^2 / (1 + exp(-2r))]
```

- The vacuum intensity scale is related to squeezing by:

```text
I_vac = c hbar omega sinh^2(r) / V
```

## Assumptions

- The harmonic state is inferred through a mapping from driving-field
  phase-space variables to the semiclassical nonlinear response.
- Ionization timing relative to the squeezing phase controls squeezing transfer.

## Limitations And Cautions

- The local PDF lacks a year in the filename, so the bibliographic metadata
  should be completed later from a stable external source or BibTeX.
- The framework is more ambitious than intensity-only stochastic simulations;
  it targets generated harmonic quantum states.

## Relevance To This Project

This source is important if the manuscript goes beyond HHG spectra and discusses
generated harmonic squeezing. It also gives a concrete BSV Husimi distribution
for Monte Carlo sampling.
