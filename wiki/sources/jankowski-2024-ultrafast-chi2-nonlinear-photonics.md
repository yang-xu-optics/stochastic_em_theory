---
title: Jankowski Et Al 2024 Ultrafast Second-Order Nonlinear Photonics
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, chi2, nonlinear-photonics, non-gaussian, tutorial]
source_count: 1
confidence: high
related:
  - ../theory/non-gaussian-output-novelty
  - ../models/thz-optical-rectification-model
---

# Jankowski Et Al 2024 Ultrafast Second-Order Nonlinear Photonics

## Bibliographic Metadata

- Authors: Marc Jankowski, Ryotatsu Yanagimoto, Edwin Ng, Ryan Hamerly,
  Timothy P. McKenna, Hideo Mabuchi, and M. M. Fejer.
- Year: 2024.
- Venue: Advances in Optics and Photonics 16, 347-537.
- Title: Ultrafast second-order nonlinear photonics-from classical physics to
  non-Gaussian quantum dynamics: a tutorial.
- Raw source: [Jankowski 2024 raw PDF](<../../raw/sources/Jankowski et al. - 2024 - Ultrafast second-order nonlinear photonics—from cl.pdf>)
- Ingest date: 2026-06-06.

## Core Result

This tutorial connects classical `chi^(2)` nonlinear optics, Gaussian quantum
optics, mesoscopic non-Gaussian dynamics, and deep-quantum few-photon regimes in
one framework. Its most useful message for this project is that saturated
nonlinear interactions can generate non-Gaussian quantum features even before
one reaches single-photon operation, and that these features should be analyzed
by separating mean-field, Gaussian, and residual non-Gaussian dynamics.

## Useful Equations Or Model Ingredients

- Classical coupled-wave equations can be quantized into Hamiltonian dynamics
  for broadband `chi^(2)` devices.
- The Gaussian interaction frame separates:

```text
field state = mean field + Gaussian covariance + residual non-Gaussian state
```

- A Gaussian split-step Fourier method can propagate mean and covariance while
  staying in the Gaussian approximation.
- Residual non-Gaussian features require extra machinery:

```text
GIF-principal supermodes
higher-order moment or cumulant expansions
matrix-product states
photon-number basis in the deep-quantum limit
```

## Assumptions

- The main platform is ultrafast integrated `chi^(2)` photonics, especially
  waveguides and resonators.
- The framework is designed for multimode pulsed nonlinear optics and is
  transferable in spirit to `chi^(3)` processes.

## Limitations And Cautions

- This is not an HHG or gas-plasma paper.
- The tutorial repeatedly warns that Wigner negativity and other non-Gaussian
  features are experimentally fragile against loss and phase noise.
- A positive Wigner stochastic simulation can capture Gaussian physics but not
  Wigner-negative output states without a more complete quantum model.

## Relevance To This Project

For THz optical rectification, this source gives the strongest language for
turning a classical `chi^(2)` source model into a quantum nonlinear optics
question. For HHG and plasma THz, it provides the broader conceptual hierarchy:
mean spectra are classical-like, covariance and squeezing are Gaussian quantum
features, and higher-order cumulants/Wigner negativity are the high-impact
non-Gaussian frontier.
