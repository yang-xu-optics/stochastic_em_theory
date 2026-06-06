---
title: Even Tzur And Cohen 2024 Motion Of Charged Particles In BSV
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, bsv, electron-dynamics, ponderomotive, hhg]
source_count: 1
confidence: high
related:
  - ../models/hhg-gas-model
  - ../models/thz-plasma-emission-model
---

# Even Tzur And Cohen 2024 Motion Of Charged Particles In BSV

## Bibliographic Metadata

- Authors: Matan Even Tzur and Oren Cohen.
- Year: 2024.
- Venue: Light: Science & Applications.
- Raw source: [Even Tzur and Cohen - 2024 - Motion of charged particles in bright squeezed vac.pdf](<../../raw/sources/Even Tzur and Cohen - 2024 - Motion of charged particles in bright squeezed vac.pdf>)
- Ingest date: 2026-06-06.

## Core Result

BSV has zero mean electric field, so it does not drive the mean electron
position like a coherent field. Instead, it drives oscillations in the electron
wavepacket width. The paper identifies a BSV ponderomotive-energy analogue and
connects closed/open width trajectories to HHG and above-threshold ionization
intuition.

## Useful Equations Or Model Ingredients

- Classical ponderomotive energy:

```text
U_p^c = e^2 E_a^2 / (4 m omega_p^2)
```

- BSV quantum ponderomotive scale depends on intensity and frequency, giving an
  equivalent energy scale for equally intense coherent and BSV fields.
- The reduced electron state can be written as an integral over
  coherent-state-driven wavefunctions weighted by a Gaussian BSV distribution.

## Assumptions

- The BSV field is treated through a phase-space ensemble of coherent
  components.
- The electron response is examined through wavepacket width, not only mean
  displacement.

## Limitations And Cautions

- A zero-mean BSV drive can still produce strong dynamics, but the observable
  may be a variance, width, or conditional response rather than mean position.
- Gas HHG simulations must decide whether they predict trajectory displacement,
  wavepacket spreading, emitted spectra, or field-state observables.

## Relevance To This Project

This source gives physical language for why BSV can drive strong-field
electron dynamics even with zero mean field. It is especially useful for the
HHG discussion and for interpreting plasma ionization bursts under stochastic
fields.

