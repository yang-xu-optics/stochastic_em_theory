---
title: Schuh Et Al 2013 THz Emission From Ultrashort Ionization Of Gases
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, thz, plasma, ionization, photocurrent]
source_count: 1
confidence: high
related:
  - ../models/thz-plasma-emission-model
  - ../simulations/simulation-roadmap
---

# Schuh Et Al 2013 THz Emission From Ultrashort Ionization Of Gases

## Bibliographic Metadata

- Authors: K. Schuh, M. Scheller, J. Hader, and J. V. Moloney.
- Year: 2013.
- Venue: Physical Review E 88, 063102.
- Raw source: [Schuh et al. - 2013 - Quantum theory of terahertz emission due to ultrashort pulse ionization of gases.pdf](<../../raw/sources/Schuh et al. - 2013 - Quantum theory of terahertz emission due to ultrashort pulse ionization of gases.pdf>)
- Ingest date: 2026-06-06.

## Core Result

The paper develops a microscopic semiclassical model for THz emission after
one- and two-color ultrashort ionization of atomic gases. Optical Bloch
equations describe ionization and continuum-electron dynamics, while the THz
field is tied to the temporal change in the current.

## Useful Equations Or Model Ingredients

- Current density:

```text
j(t) = (1/V) sum_k f_k(t) e hbar k / m
```

- THz spectral source from current change:

```text
c(nu) = integral dt exp(2 pi i nu t) d j_z(t) / dt
```

- Two-color phase asymmetry can produce strong low-frequency current, while
  one-color symmetric excitation gives much weaker low-THz emission.

## Assumptions

- The optical field is classical and the electrons are treated quantum
  mechanically.
- The plasma is approximated as a point source for emission.
- The model focuses on dilute gases and neglects some collective plasma and
  geometric effects.

## Limitations And Cautions

- A stochastic BSV drive must be tested for symmetry: a zero-mean one-color
  drive may yield zero ensemble-averaged current.
- The model is microscopic and more detailed than the simplest photocurrent
  ODE used in many simulations.

## Relevance To This Project

This is a source-backed starting point for plasma THz emission in gas. It
identifies `dJ/dt` as the emitted-field driver and makes the two-color
symmetry requirement explicit.

