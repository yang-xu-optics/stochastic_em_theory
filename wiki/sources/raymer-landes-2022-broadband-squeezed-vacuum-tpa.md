---
title: Raymer And Landes 2022 Broadband Squeezed Vacuum TPA
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, squeezed-vacuum, g2, tpa, broadband]
source_count: 1
confidence: high
related:
  - ../theory/squeezed-vacuum-g2-proof-plan
  - ../theory/stochastic-quantum-optics-correspondence
---

# Raymer And Landes 2022 Broadband Squeezed Vacuum TPA

## Bibliographic Metadata

- Authors: Michael G. Raymer and Tiemo Landes.
- Year: 2022.
- Venue: Physical Review A 106, 013717.
- Raw source: [Raymer and Landes - 2022 - Theory of two-photon absorption with broadband squ.pdf](<../../raw/sources/Raymer and Landes - 2022 - Theory of two-photon absorption with broadband squ.pdf>)
- Ingest date: 2026-06-06.

## Core Result

The paper gives a quantum-field theory of nonresonant two-photon absorption
driven by broadband squeezed vacuum, including low-gain SPDC and high-gain BSV.
For broad final-state linewidths, the TPA rate is proportional to
`g^(2)(0)`. For a compensated broadband squeezed field in the indistinguishable
collinear case, the ideal result is recovered:

```text
g^(2)(0) = 3 + 1/nbar
```

where `nbar` is the mean photon number per effective mode.

## Useful Equations Or Model Ingredients

- Broadband squeezing is represented by a Bogoliubov transform:

```text
b(omega) = f(omega) a(omega) + g(omega) a^\dagger(2 omega_0 - omega)
```

- The nonlinear absorption probability is controlled by a four-frequency
  normally ordered correlation:

```text
C^(4) = <c^\dagger c^\dagger c c>
```

- With indistinguishability parameter `xi`, the compensated broadband result
  is:

```text
g^(2)(0) = (2 + xi) + 1/nbar
```

and for collinear type-0/type-I photons, `xi = 1`.

## Assumptions

- The squeezed field is spectrally broadband and effectively stationary before
  time gating.
- The relevant detection or molecular response defines the temporal mode.
- Dispersion compensation is needed to recover maximal intensity fluctuations.

## Limitations And Cautions

- Without dispersion compensation, broadband `g^(2)(0)` can fall below the
  ideal compensated curve in intermediate regimes.
- The result is source- and detection-model dependent; it should not be quoted
  for "multimode BSV" without a mode definition.

## Relevance To This Project

This is the main source for extending the single-mode `g^(2)` proof target to
realistic broadband BSV. It also establishes the four-frequency correlation as
the object to match before using stochastic fields in nonlinear absorption or
frequency-conversion calculations.

