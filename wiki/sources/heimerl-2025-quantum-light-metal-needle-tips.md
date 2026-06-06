---
title: Heimerl Et Al 2025 Quantum Light Drives Electrons At Metal Needle Tips
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, bsv, strong-field, postselection, coherent-state-sampling]
source_count: 1
confidence: high
related:
  - ../models/hhg-gas-model
  - ../simulations/simulation-roadmap
---

# Heimerl Et Al 2025 Quantum Light Drives Electrons At Metal Needle Tips

## Bibliographic Metadata

- Authors: Jonas Heimerl et al.
- Year: 2025.
- Venue: Nature Physics.
- Raw source: [s41567-025-03087-1.pdf](../../raw/sources/s41567-025-03087-1.pdf)
- Ingest date: 2026-06-06.

## Core Result

The experiment shows strong-field electron spectra from metal needle tips
driven by BSV. Plateau and cutoff signatures appear only after post-selecting
spectra on the photon number of individual BSV pulses. Shot-averaged spectra
are broad and lack a clear plateau.

## Useful Equations Or Model Ingredients

- BSV intensity Husimi distribution:

```text
Q_BSV(I_alpha, <I_BSV>) =
  1 / sqrt(2 pi <I_BSV> I_alpha)
  exp[-I_alpha / (2 <I_BSV>)]
```

- Shot-averaged response as an incoherent integral over coherent-driver
  spectra:

```text
S_BSV(E, <I_BSV>) =
  integral dI_alpha S_coh(E, I_alpha) Q_BSV(I_alpha, <I_BSV>)
```

## Assumptions

- The experiment uses a single-mode BSV source near 1600 nm.
- Photon-number post-selection acts like sorting by coherent-state amplitude.

## Limitations And Cautions

- The platform is metal-tip electron emission, not gas HHG.
- Averaging and post-selection answer different physical questions; the
  manuscript must keep unconditional and conditional observables separate.

## Relevance To This Project

This is a crucial experimental guardrail. For HHG and THz simulations, report
both shot-averaged spectra and conditional spectra binned by sampled intensity
or photon number.

