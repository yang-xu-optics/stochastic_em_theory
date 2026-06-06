---
title: HHG Gas Model
type: model
status: seed
created: 2026-06-06
updated: 2026-06-06
tags: [hhg, gas, strong-field, squeezed-vacuum]
source_count: 0
confidence: low
related:
  - ../overview
  - ../theory/stochastic-quantum-optics-correspondence
  - ../simulations/simulation-roadmap
---

# HHG Gas Model

This page defines the modeling path for high harmonic generation in gas driven
by stochastic squeezed fields.

## Modeling Objective

Given a stochastic optical field ensemble `E_j(t)`, compute HHG observables such
as single-trajectory dipole acceleration, ensemble-averaged harmonic spectra,
shot-to-shot fluctuations, and macroscopic phase-matched emission.

## Candidate Fidelity Levels

1. Classical electron trajectory model with ionization and recollision gates.
2. Strong-field approximation or Lewenstein-like single-atom response driven by
   sampled fields.
3. Propagation model with gas dispersion, plasma dispersion, absorption, and
   phase matching.

The first implementation should be deliberately minimal and validated before
adding propagation.

## Stochastic-Drive Questions

- Is the drive a displaced squeezed state, a bright squeezed vacuum with zero
  coherent amplitude, or a filtered multimode squeezed field?
- Are observables averaged over field realizations before or after taking
  spectra?
- Do rare high-field events dominate the HHG yield?
- Does the harmonic cutoff follow a stochastic distribution tied to the
  instantaneous ponderomotive energy?
- Which correlations survive ensemble averaging and which are accessible only
  shot by shot?

## Proposed Observables

- Ensemble mean HHG spectrum.
- Spectrum variance and confidence intervals.
- Distribution of cutoff energies.
- Correlation between drive intensity spikes and harmonic yield.
- Comparison against coherent-state and thermal/noise baselines with matched
  mean energy.

## Open Modeling Risks

HHG is highly nonlinear, so matching low-order squeezed-vacuum diagnostics does
not guarantee that a sampled-field classical model captures all quantum optical
features of the generated harmonics. The manuscript should state the model
boundary clearly.

