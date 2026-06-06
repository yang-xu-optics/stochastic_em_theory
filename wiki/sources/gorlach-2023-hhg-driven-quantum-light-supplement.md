---
title: Gorlach Et Al 2023 HHG Driven By Quantum Light Supplement
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, hhg, bsv, husimi-q, coherent-state-sampling]
source_count: 2
confidence: high
related:
  - ../models/hhg-gas-model
  - ../simulations/simulation-roadmap
---

# Gorlach Et Al 2023 HHG Driven By Quantum Light Supplement

## Bibliographic Metadata

- Authors: Alexey Gorlach, Matan Even Tzur, Mirit Birk, Michael Kruger,
  Nicholas Rivera, Oren Cohen, and Ido Kaminer.
- Year: 2023.
- Work: Supplementary information for "High-harmonic generation driven by
  quantum light".
- Raw source: [41567_2023_2127_MOESM1_ESM.pdf](../../raw/sources/41567_2023_2127_MOESM1_ESM.pdf)
- Duplicate raw file: [Gorlach et al. - 2023 - High-harmonic generation driven by quantum light.pdf](<../../raw/sources/Gorlach et al. - 2023 - High-harmonic generation driven by quantum light.pdf>)
- Ingest date: 2026-06-06.

## Core Result

The supplement gives a practical theory for HHG driven by quantum light by
decomposing the incident field into coherent-state components using phase-space
distributions, then integrating classical or semiclassical HHG responses over
that distribution. It also reports that BSV and thermal light can lower the
apparent HHG threshold because rare high-intensity samples contribute strongly.

## Useful Equations Or Model Ingredients

- The driving-light density matrix can be represented with a positive
  generalized P distribution or related coherent-state distributions.
- For intensity spectra, a useful computational structure is:

```text
S_HHG(omega) = integral d^2 alpha Q(alpha) S_HHG^coh(omega; alpha)
```

- Baseline gas calculation details from the supplement:

```text
x_min = -100 bohr
x_max = 100 bohr
dx = 0.06 bohr
dt = 0.02 atomic units
V(r) = -(r^2 + a^2)^(-1/2)
a = 0.8160 bohr
I_p = 0.7924 hartree
```

- The spectrum is obtained from the Fourier transform of dipole acceleration:

```text
a(t) = -<psi | grad V(r) + E(t) | psi>
```

## Assumptions

- The coherent-state response can be computed independently for each sampled
  field amplitude.
- The final observable considered in the threshold study is an incoherent
  intensity spectrum.
- A 1D soft-core atom is used as a tractable single-atom baseline.

## Limitations And Cautions

- The local files are duplicate copies of the supplementary information, not a
  separate copy of the main article.
- The ensemble-of-coherent-responses method is well suited to intensity
  observables, but generated-field quantum states need additional care.

## Relevance To This Project

This is the most concrete source for the first HHG simulation: reproduce a
1D gas-like single-atom coherent response, then integrate over BSV Husimi
samples and compare conditional and unconditional spectra.

