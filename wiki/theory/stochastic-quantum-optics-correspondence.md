---
title: Stochastic Quantum Optics Correspondence
type: concept
status: active
created: 2026-06-06
updated: 2026-11-14
tags: [theory, stochastic-fields, quantum-optics, ordering]
source_count: 10
confidence: high
related:
  - quantum-optical-rectification-of-bsv
  - ../sources/gothelf-2026-limitations-of-approximative-phase-space-description
  - squeezed-vacuum-g2-proof-plan
  - non-gaussian-output-novelty
  - ../overview
  - ../sources/raymer-landes-2022-broadband-squeezed-vacuum-tpa
  - ../sources/raymer-landes-2023-classical-model-broadband-squeezed-vacuum
  - ../sources/kulkarni-2022-a-classical-model-of-spontaneous-pdc
  - ../sources/sharapova-2020-properties-of-bsv-at-increasing-brightness
  - ../sources/lyu-2025-photon-statistics-ati
---

# Stochastic Quantum Optics Correspondence

This page tracks how a stochastic electromagnetic description can be compared
to quantum optics observables.

## Core Issue

Squeezed vacuum has a positive Gaussian Wigner function, so field quadratures
can be sampled as classical random variables in that representation. However,
not every quantum observable is obtained by taking the most obvious classical
moment of those samples.

The Wigner representation gives symmetrically ordered operator moments.
Photon-counting diagnostics such as `g^{(2)}(0)` are normally ordered. The
correspondence therefore requires explicit ordering corrections.

## Single-Mode Seed Conventions

Let `a` be the annihilation operator for one optical mode and let `alpha` be the
complex stochastic Wigner amplitude for that mode.

For Wigner sampling:

```text
<a^\dagger a> = <|alpha|^2>_W - 1/2
<a^\dagger a^\dagger a a> = <|alpha|^4>_W - 2 <|alpha|^2>_W + 1/2
```

The second line is the key correction needed before computing photon-counting
`g^{(2)}(0)`.

## Comparison Checklist

For every stochastic/quantum comparison, record:

- field representation,
- quadrature convention,
- mode normalization,
- squeezing parameter and phase,
- displacement, if any,
- loss and detector efficiency,
- temporal and spectral mode definition,
- ensemble size and convergence tolerance,
- whether the observable is symmetric, normal, or time ordered.

## Source-Backed Guardrails

- Raymer and Landes 2022 identify the four-frequency normally ordered
  correlation as the decisive object for nonlinear absorption by broadband
  squeezed vacuum. A stochastic calculation should match that object, not just
  the visual shape of sampled fields.
- Raymer and Landes 2023 show exact agreement for considered TPA/SFG
  predictions only after subtracting the vacuum-only `g = 0` contribution in
  the stochastic-field model. In this project, that step should be called
  "vacuum subtraction" or "renormalization" and treated as an assumption to be
  justified.
- The stochastic zero-point spectral density used there is:

```text
P_SF(omega) = 1/2
```

- Sharapova et al. 2015 make the multimode warning concrete: BSV correlations
  depend on the Schmidt-mode basis and gain-dependent mode weights. A
  single-mode proof is a validation case, not a full BSV characterization.
- Agafonov/Iskhakov/Perez/Sharapova BSV source papers extend that warning:
  realistic BSV can be two-color, superbunched, spatially engineered, spectrally
  tailored, and gain-dependent. The stochastic sampler needs an explicit source
  model before using a single analytic distribution as "the" BSV ensemble.
- Kulkarni 2022 gives a neighboring example of classical stochastic vacuum
  seeding for SPDC. It is useful support for the correspondence strategy, but
  the observable and subtraction/ordering conventions still have to be matched
  case by case.
- Lyu 2025 gives a strong-field version of the same discipline. The qSFA
  observable is a coherent-component average over `P(E_alpha)`, but the paper
  explicitly derives when off-diagonal phase-space terms can be neglected.
  Importing the formula into HHG requires restating that diagonal approximation
  and checking its regime.
- Gorlach/Tzur-style HHG papers often use Positive P or Husimi Q coherent-state
  decompositions. Those are phase-space representations of a quantum state,
  not a blanket statement that all output observables are classical.
- Correction 2026-11-14. The diagonal Husimi-Q form used in practice (and by
  this project's samplers) is not a representation of the same state. It is
  the classical mixture `int d^2 alpha Q(alpha) |alpha><alpha|`, a different
  state whose photon number is `<n> + 1` and whose quadrature variances are
  larger by 1/2. Gothelf 2026 calls it the approximative phase-space
  description and proves that, when a coherent driver gives coherent output,
  it can never yield output squeezing below vacuum, `g2 < 1`, or Wigner
  negativity. Spectra and intensity-type observables are right to relative
  order `1/<n>`; fluctuation observables carry an error that grows with
  emitter number and pulse duration. See
  [[../sources/gothelf-2026-limitations-of-approximative-phase-space-description]].
- For optical rectification the comparison can be done in closed form:
  exact, Husimi-Q mixture, and classical Gaussian noise give THz energies
  `3 nbar^2 + 2 nbar`, `3 nbar^2 + 6 nbar + 3`, and `3 nbar^2`. See
  [[quantum-optical-rectification-of-bsv]].
- Yanagimoto/Jankowski-style mesoscopic nonlinear optics adds a stricter
  boundary: a positive stochastic ensemble can guide Gaussian and intensity
  observables, but Wigner-negative or otherwise quantum non-Gaussian output
  states require a higher-order quantum model, witness, or measurement
  protocol.

## Boundary of the Claim

Matching squeezed-vacuum diagnostics does not by itself prove that every
strong-field nonlinear process has a fully classical stochastic equivalent. It
establishes a controlled input-field representation and an observable-matching
protocol. Later HHG and THz claims need their own assumptions and validation.
