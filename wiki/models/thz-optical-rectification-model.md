---
title: THz Optical Rectification Model
type: model
status: active
created: 2026-06-06
updated: 2026-11-14
tags: [thz, optical-rectification, nonlinear-optics, squeezed-vacuum]
source_count: 6
confidence: high
related:
  - ../overview
  - ../theory/non-gaussian-output-novelty
  - ../simulations/simulation-roadmap
  - ../sources/raymer-landes-2023-classical-model-broadband-squeezed-vacuum
  - ../sources/sun-2022-thz-laser-induced-plasma
  - ../sources/ravi-2014-thz-generation-optical-rectification
  - ../sources/jankowski-2024-ultrafast-chi2-nonlinear-photonics
  - ../theory/bsv-even-order-response-moment-scaling
  - ../theory/quantum-optical-rectification-of-bsv
  - ../simulations/bsv-optical-rectification-thz-statistics
  - ../prl-restructuring-plan
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

- Ravi 2014 gives the classical baseline for tilted-pulse-front optical
  rectification in lithium niobate. In the simplest frequency-domain form, OR is
  an intrapulse DFG integral:

```text
P_THz(Omega, z) =
  epsilon_0 chi_eff^(2)
  integral d omega A_op(omega + Omega, z) A_op^*(omega, z)
  exp[-i Delta k(omega, Omega) z]
```

- The tilted-pulse-front phase-matching condition is:

```text
n_THz(Omega) cos(gamma) = n_g,opt(omega_0)
```

For the lithium-niobate parameters considered in the thesis, the tilt is about
63 degrees.
- Ravi 2014 shows why undepleted-pump OR models can overestimate conversion:
  THz generation cascades the pump to lower optical frequencies, broadens the
  pump spectrum, and combines with angular-dispersion GVD to break up the pump
  spatio-temporally. This makes OR self-limiting.
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
rectification. Ravi 2014 supplies the deterministic classical OR propagation
model. The stochastic extension still needs a derivation of which sampled-field
correlation drives `P_THz`, how normally ordered observables map to stochastic
moments, and whether vacuum-only terms must be subtracted.

The 2026-06-06 literature search did not find a direct squeezed-vacuum OR
paper. Generic THz/OR sources appeared, but they did not address the quantum
pump statistics central to this project, so they were not downloaded into the
source set.

## Non-Gaussian Novelty Path

Jankowski 2024 supplies the conceptual bridge from classical `chi^(2)`
frequency conversion to mesoscopic non-Gaussian quantum dynamics. For OR, there
are three distinct novelty levels:

- classical stochastic OR: non-Gaussian shot-to-shot THz energy or waveform
  distributions caused by nonlinear filtering of BSV fluctuations,
- Gaussian quantum OR: squeezed or correlated THz quadratures with a Gaussian
  covariance model,
- non-Gaussian quantum OR: higher cumulants, Wigner-negativity witnesses, or
  conditional THz/residual-pump states caused by pump depletion, cascading, or
  measurement-like conditioning.

The first level is reachable with the current stochastic source model. The last
level requires a quantum OR model or witness beyond positive stochastic
sampling.

## First Simulation Target

Build a 1D frequency-domain or time-domain model:

1. sample stochastic optical waveforms,
2. compute the OR source term `P_THz,j` either as `E_j(t)^2` filtered to THz
   frequencies or as the intrapulse DFG integral,
3. propagate the THz field with absorption and phase mismatch,
4. compare ensemble-averaged field and intensity,
5. benchmark against a coherent pulse with the same mean energy,
6. add pump depletion/cascading only after the undepleted stochastic source is
   validated.

## Classical Propagation Upgrade

After the minimal source model works, follow Ravi 2014 in stages:

- add tilted-pulse-front phase matching and angular-dispersion GVD,
- couple the optical and THz fields to include cascading,
- include SPM and SRS if the optical intensities justify it,
- move from effective 1D to 2D transverse Fourier propagation,
- track spatial chirp and beam quality, not only total conversion efficiency.

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

## Update 2026-11-14: First Answer To The Key Questions

Seed derivation in [[../theory/bsv-even-order-response-moment-scaling]]
(single mode, macroscopic limit, undepleted, not yet source-backed). Optical
rectification is even in the pump amplitude, so the sign randomness of BSV
does not cancel it:

```text
E_THz,j(t) = I_j g(t),    I_j = shot intensity / mean intensity
<E_THz(t)> = g(t)                      (same as a coherent pump)
<U_THz> = 3 U_coherent                 (thermal pump: 2)
<U^2> / <U>^2 = 35/3                   (thermal pump: 6)
```

`g(t)` is the deterministic THz response to the mean intensity envelope, in
field units. The measurable object is therefore both the mean THz field and
its single-shot amplitude distribution (one-sided chi-squared). Multimode
corrections, vacuum-term subtraction for the THz intensity, and depletion are
open. The source gap stated above remains: two web searches on 2026-11-14
found no paper on BSV-pumped optical rectification.

## Update 2026-11-14 (2): Main Result Of The Project

Optical rectification of BSV is now the headline result
([[../prl-restructuring-plan]]). The seed answer above has been replaced by a
fully quantum derivation, [[../theory/quantum-optical-rectification-of-bsv]]:

```text
b_out(Omega) = b_in(Omega) - i zeta(Omega) N(Omega)
N(Omega) = integral domega a^dagger(omega) a(omega + Omega)
```

The THz field operator is the vacuum input plus a linear filter of the pump
photon-flux operator. This answers the "Key Questions" and the "Source Gap"
items as follows.

- Ensemble mean: nonzero for any pulsed pump, for any number of modes.
- Measurable objects: the mean THz waveform, the single-shot field
  distribution (Gamma with shape `K/2` in the bright limit), and its
  cumulants.
- Ordering: THz normally ordered moments are ordinary moments of the pump
  photon number. `N` is normally ordered, so no vacuum subtraction is needed
  in the quantum description; a Wigner sampling of the pump would need it.
- Vacuum-only terms: the spontaneous term, linear in pump photon number, is
  the one contribution a classical-noise model misses.

Implementation and first run:
[[../simulations/bsv-optical-rectification-thz-statistics]]. Still open and
now on the critical path: `zeta(Omega)` for a specific crystal with phase
matching and absorption, depletion and cascading at the planned pump energy,
and the measured Schmidt modes of the source.

