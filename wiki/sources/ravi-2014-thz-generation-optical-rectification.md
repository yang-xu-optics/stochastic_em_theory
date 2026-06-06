---
title: Ravi 2014 THz Generation By Optical Rectification
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, thesis, thz, optical-rectification, tilted-pulse-fronts]
source_count: 1
confidence: high
related:
  - ../models/thz-optical-rectification-model
  - ../simulations/simulation-roadmap
---

# Ravi 2014 THz Generation By Optical Rectification

## Bibliographic Metadata

- Author: Koustuban Ravi.
- Year: 2014.
- Institution: Massachusetts Institute of Technology.
- Degree: Master of Science in Electrical Engineering and Computer Science.
- Title: Theory of Terahertz Generation by Optical Rectification.
- Supervisors: Franz X. Kartner and Erich P. Ippen.
- Raw source: [900736523-MIT.pdf](../../raw/sources/900736523-MIT.pdf)
- Ingest date: 2026-06-06.

## Core Result

The thesis reformulates high-field THz generation by optical rectification in
tilted-pulse-front lithium niobate by including effects omitted in simpler
undepleted models: spatio-temporal distortions, nonlinear coupling between
optical and THz fields, self-phase modulation, stimulated Raman scattering,
absorption, and crystal geometry. The main conclusion is that THz generation
itself cascades and broadens the optical pump spectrum, which causes rapid
spatio-temporal breakup of the pump and limits further coherent THz buildup.

## Useful Equations Or Model Ingredients

- Optical rectification is treated as the aggregate of all intrapulse
  difference-frequency processes:

```text
P_THz(Omega, z) =
  epsilon_0 chi_eff^(2)
  integral d omega A_op(omega + Omega, z) A_op^*(omega, z)
  exp[-i Delta k(omega, Omega) z]
```

- In the undepleted tilted-pulse-front model, phase matching is:

```text
n_THz(Omega) cos(gamma) = n_g,opt(omega_0)
```

For lithium niobate, the phase-matching tilt is approximately 63 degrees near
the parameters considered.

- A depleted 1D model evolves both `A_THz(Omega,z)` and `A_op(omega,z)`. The THz
  equation contains absorption plus the OR polarization; the optical equation
  contains cascaded down-conversion, THz-plus-optical SFG, SPM, and SRS.
- The 2D model uses:

```text
P_THz(Omega, x, z) =
  epsilon_0 chi_eff^(2)(x,z)
  integral_0^infty d omega
    E_op(omega + Omega, x, z) E_op^*(omega, x, z)
```

and solves coupled nonlinear wave equations with spatial Fourier decomposition
in transverse momentum `k_x`.

## Assumptions

- The optical pump is a classical ultrafast pulse.
- The nonlinear medium is lithium niobate in a tilted-pulse-front geometry.
- THz generation is modeled through `chi^(2)` optical rectification, with
  material dispersion, absorption, and geometry included.
- The stochastic or quantum nature of the pump is not considered.

## Limitations And Cautions

- This is not a squeezed-vacuum source. It is a classical OR propagation thesis
  that supplies the baseline nonlinear optics model.
- Undepleted models can overestimate conversion efficiency because they miss
  pump reshaping and cascading.
- Optimizing conversion efficiency alone can degrade THz beam quality through
  spatial chirp and spatio-temporal distortions.
- Scaling beam size at fixed intensity does not preserve efficiency in the 2D
  tilted-pulse-front geometry.

## Relevance To This Project

This thesis closes part of the optical-rectification source gap by giving a
source-backed classical OR model. For squeezed-vacuum-driven OR, the project can
reuse the nonlinear polarization structure by replacing deterministic optical
fields with stochastic sampled fields, but it still needs a derivation of the
correct ensemble average, ordering rule, and vacuum subtraction.

