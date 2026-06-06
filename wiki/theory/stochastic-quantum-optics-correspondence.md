---
title: Stochastic Quantum Optics Correspondence
type: concept
status: seed
created: 2026-06-06
updated: 2026-06-06
tags: [theory, stochastic-fields, quantum-optics, ordering]
source_count: 0
confidence: low
related:
  - squeezed-vacuum-g2-proof-plan
  - ../overview
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

## Boundary of the Claim

Matching squeezed-vacuum diagnostics does not by itself prove that every
strong-field nonlinear process has a fully classical stochastic equivalent. It
establishes a controlled input-field representation and an observable-matching
protocol. Later HHG and THz claims need their own assumptions and validation.

