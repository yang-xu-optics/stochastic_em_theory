---
title: Research Agenda
type: synthesis
status: seed
created: 2026-06-06
updated: 2026-06-06
tags: [agenda, planning]
source_count: 0
confidence: low
related:
  - overview
  - theory/squeezed-vacuum-g2-proof-plan
  - simulations/simulation-roadmap
---

# Research Agenda

## Core Questions

1. Which stochastic representation is meant by "stochastic EM theory" in this
   project: Wigner sampling of the quantized field, stochastic electrodynamics
   with zero-point fields, or a semiclassical Gaussian random process?
2. What observables are required to claim agreement with quantum optics for
   squeezed vacuum: quadrature variance, photon number, `g^{(2)}(0)`,
   higher-order correlations, spectral correlations, or multimode statistics?
3. What is the minimal proof that connects stochastic sampled amplitudes to
   normally ordered photon-counting observables?
4. In HHG, which parts of the model are classical, semiclassical, or quantum:
   electron trajectory, ionization, recombination, propagation, and detection?
5. For THz optical rectification, what low-frequency observable survives
   ensemble averaging over a zero-mean squeezed field?
6. For plasma THz emission, what symmetry-breaking ingredient is needed to
   produce nonzero emitted THz fields from stochastic squeezed-vacuum drive?

## Deliverables

- A derivation page showing the stochastic/quantum optics match for
  squeezed-vacuum `g^{(2)}(0)`.
- A validated stochastic squeezed-field sampler.
- Numerical convergence plots for quadrature variance, photon number, and
  `g^{(2)}(0)`.
- HHG spectra driven by coherent, thermal/noisy, and squeezed ensembles.
- THz spectra from optical rectification driven by matched ensembles.
- THz plasma spectra with clear symmetry assumptions.
- A manuscript outline with figure-to-claim mapping.

## Initial Risk Register

- Operator ordering error: using raw stochastic intensity moments as if they
  were normally ordered photon correlations.
- Mode ambiguity: quoting a squeezed-vacuum `g^{(2)}` value without specifying
  temporal/spectral modes and detection bandwidth.
- Symmetry null result: plasma or optical rectification signal may vanish after
  ensemble averaging unless the model includes a physical asymmetry.
- Overclaiming classicality: Wigner sampling can reproduce some quantum
  moments without making all later nonlinear dynamics fully equivalent to
  quantum electrodynamics.
- Numerical cost: rare high-field events in bright squeezed vacuum may dominate
  nonlinear observables and require many trajectories.

## Next Actions

1. Ingest foundational quantum optics sources for squeezed vacuum correlations.
2. Ingest sources on stochastic electrodynamics and Wigner/phase-space sampling.
3. Turn [[theory/squeezed-vacuum-g2-proof-plan]] into a complete derivation.
4. Implement a single-mode squeezed-vacuum sampler and Monte Carlo validation.
5. Decide the first HHG model fidelity level: classical trajectory,
   Lewenstein-like semiclassical response, or propagation-first source model.

