---
title: Stochastic Quantum Optics Correspondence
type: concept
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [theory, stochastic-fields, quantum-optics, ordering]
source_count: 7
confidence: high
related:
  - squeezed-vacuum-g2-proof-plan
  - non-gaussian-output-novelty
  - ../overview
  - ../sources/raymer-landes-2022-broadband-squeezed-vacuum-tpa
  - ../sources/raymer-landes-2023-classical-model-broadband-squeezed-vacuum
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
- Gorlach/Tzur-style HHG papers often use Positive P or Husimi Q coherent-state
  decompositions. Those are phase-space representations of a quantum state,
  not a blanket statement that all output observables are classical.
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
