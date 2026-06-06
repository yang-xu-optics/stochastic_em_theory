---
title: Raymer And Landes 2023 Classical Model For Broadband Squeezed Vacuum
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, stochastic-fields, squeezed-vacuum, tpa, sfg]
source_count: 1
confidence: high
related:
  - ../theory/stochastic-quantum-optics-correspondence
  - ../models/thz-optical-rectification-model
---

# Raymer And Landes 2023 Classical Model For Broadband Squeezed Vacuum

## Bibliographic Metadata

- Authors: Michael G. Raymer and Tiemo Landes.
- Year: 2023.
- Identifier: arXiv:2309.04845v1.
- Raw source: [2309.04845v1.pdf](../../raw/sources/2309.04845v1.pdf)
- Ingest date: 2026-06-06.

## Core Result

The paper constructs a classical stochastic-field model for broadband squeezed
vacuum in TPA and SFG. After an explicit subtraction of the vacuum-only
contribution, the stochastic model reproduces the quantum-field predictions for
the considered TPA/SFG observables in both high-gain and low-gain regimes.

## Useful Equations Or Model Ingredients

- Classical stochastic field amplitudes use Gaussian random variables with a
  zero-point spectral density:

```text
P_SF(omega) = 1/2
```

- The amplified stochastic field has the same gain functions as the quantum
  Bogoliubov transform:

```text
b(omega) = f(omega) a(omega) + g(omega) a^*(2 omega_0 - omega)
```

- The source term is governed by the same four-frequency structure as the
  quantum calculation after subtracting the `g = 0` vacuum result.

## Assumptions

- The stochastic vacuum background is Gaussian and broadband.
- Vacuum-field contributions to absorption are removed by a prescribed
  subtraction procedure.
- Agreement is claimed for observables expressible through the considered
  four-frequency correlations.

## Limitations And Cautions

- The vacuum subtraction is described as ad hoc, not as a complete derivation
  from a renormalized Hamiltonian.
- The authors explicitly do not claim that this stochastic model reproduces
  every quantum effect, such as Bell violation or teleportation.
- This is closest to a stochastic electrodynamics recipe, but it must be used
  with operator-ordering discipline.

## Relevance To This Project

This is the strongest local source for the paper's first thesis: stochastic
field theory can match selected quantum-optical predictions of squeezed vacuum
when vacuum noise, ordering, and nonlinear response are handled correctly.
It also provides a useful analogy for THz optical rectification as a frequency
conversion process driven by stochastic fields.

