---
title: Yanagimoto Et Al 2022 Non-Gaussian Pulsed Squeezing
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, non-gaussian, pulsed-squeezing, mesoscopic, gaussian-interaction-frame]
source_count: 1
confidence: high
related:
  - ../theory/non-gaussian-output-novelty
  - ../simulations/simulation-roadmap
---

# Yanagimoto Et Al 2022 Non-Gaussian Pulsed Squeezing

## Bibliographic Metadata

- Authors: Ryotatsu Yanagimoto, Edwin Ng, Atsushi Yamamura, Tatsuhiro
  Onodera, Logan G. Wright, Marc Jankowski, M. M. Fejer, Peter L.
  McMahon, and Hideo Mabuchi.
- Year: 2022.
- Venue: Optica 9, 379-390.
- Title: Onset of non-Gaussian quantum physics in pulsed squeezing with
  mesoscopic fields.
- Raw source: [Yanagimoto 2022 raw PDF](<../../raw/sources/Yanagimoto et al. - 2022 - Onset of non-Gaussian quantum physics in pulsed squeezing with mesoscopic fields.pdf>)
- Ingest date: 2026-06-06.

## Core Result

The paper studies pulsed squeezed-light generation when the pump contains only
dozens to hundreds of photons. In this mesoscopic regime, strong squeezing
coexists with significant pump depletion, and the full dynamics are no longer
captured by undepleted-pump Gaussian squeezing theory. The authors introduce a
Gaussian interaction frame (GIF) that factors out mean-field and Gaussian
features, leaving the residual non-Gaussian quantum dynamics to be modeled in a
small set of principal supermodes.

## Useful Equations Or Model Ingredients

- Single-mode `chi^(2)` toy Hamiltonian:

```text
H = (1/2) (a^2 b^\dagger + a^\dagger^2 b) + delta b^\dagger b
```

where `a` is the signal/fundamental mode and `b` is the pump/second-harmonic
mode.

- Gaussian interaction frame:

```text
|phi(t)> = U_G(t) |phi_I(t)>
i d|phi_I>/dt = H_I(t) |phi_I(t)>
H_I(t) = U_G^\dagger H U_G - i U_G^\dagger dU_G/dt
```

`U_G(t)` is chosen to track displacement, squeezing, and pump depletion so that
`|phi_I>` contains the non-Gaussian residual.

- Non-Gaussian output diagnostics emphasized in the paper:

```text
Wigner negativity
excess quadrature noise
mode purity loss
signal-pump entanglement entropy
higher-order correlations beyond Gaussian covariance
```

## Assumptions

- The worked example is pulsed `chi^(2)` squeezing or optical parametric
  generation, not HHG or THz emission.
- Mesoscopic means that the pump is still bright enough to drive strong
  squeezing but depleted enough for photon discreteness to matter.
- Multimode dynamics require supermode truncation to avoid exponential Hilbert
  space growth.

## Limitations And Cautions

- Non-Gaussian effects can degrade useful squeezing through excess noise and
  purity loss, so "more nonlinear" is not automatically better.
- The Wigner negativity can live in hybridized signal-pump supermodes rather
  than in a naive output mode.
- Gaussian operations cannot remove the non-Gaussian corruption caused by
  signal-pump entanglement.

## Relevance To This Project

This is a direct conceptual template for asking what becomes non-Gaussian in
HHG or THz generation with squeezed pump light. It suggests looking beyond
mean spectra toward mode-selective higher moments, emitted-field Wigner
features, pump-output entanglement, and conditional output states.

