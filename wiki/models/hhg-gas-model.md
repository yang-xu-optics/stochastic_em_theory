---
title: HHG Gas Model
type: model
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [hhg, gas, strong-field, squeezed-vacuum]
source_count: 8
confidence: high
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

## Source-Backed Representation Path

The strongest starting point is coherent-response phase-space averaging:

```text
S_HHG^BSV(omega) =
  integral d^2 alpha Q_BSV(alpha) S_HHG^coh(omega; alpha)
```

This structure appears in the Gorlach 2023 supplement, Rasputnyi 2024, and
Heimerl 2025 strong-field analysis. For the gas model, the plan is:

1. Compute `S_HHG^coh(omega; alpha)` with a classical or semiclassical gas
   response for fixed coherent amplitude and phase.
2. Sample `alpha` from the chosen BSV phase-space distribution.
3. Report both the unconditional ensemble spectrum and conditional spectra
   binned by sampled intensity or photon number.

## Gas Baseline From Gorlach 2023 Supplement

A reproducible first single-atom calculation can use the 1D soft-core neon-like
setup in the supplement:

```text
x_min = -100 bohr
x_max = 100 bohr
dx = 0.06 bohr
dt = 0.02 atomic units
V(r) = -(r^2 + a^2)^(-1/2)
a = 0.8160 bohr
I_p = 0.7924 hartree
a(t) = -<psi | grad V(r) + E(t) | psi>
```

The harmonic spectrum is obtained from the Fourier transform of the dipole
acceleration. This is a local single-atom baseline; macroscopic propagation,
phase matching, and ionization depletion come later.

## Conditional Versus Unconditional Observables

Heimerl 2025 shows that BSV-driven strong-field spectra can look very different
after shot averaging versus photon-number post-selection. For this project,
every HHG result should label which object is shown:

- `mean spectrum`: average over all sampled BSV shots,
- `conditional spectrum`: average over a bin of sampled intensity/photon
  number,
- `shot distribution`: histogram or quantiles over individual realizations.

## Quantum Output-State Boundary

Gorlach 2020 and Tzur et al. show that generated harmonic quantum states can
carry nonclassical statistics. An intensity-only stochastic simulation should
not claim to predict emitted harmonic squeezing unless it includes the
appropriate phase-space mapping and measurement model.

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

Additional source-backed risks:

- Rare BSV intensity outliers may dominate the ensemble mean and require many
  Monte Carlo samples.
- A single-mode BSV distribution is only justified with source and detection
  mode selection.
- Strong coherent-plus-BSV experiments are not identical to pure BSV driving.
