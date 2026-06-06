---
title: Wang Et Al 2026 Quantum THz Generation In Laser-Induced Plasmas
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, thz, bsv, plasma, husimi-q, tdse]
source_count: 1
confidence: high
related:
  - ../models/thz-plasma-emission-model
  - ../simulations/simulation-roadmap
---

# Wang Et Al 2026 Quantum THz Generation In Laser-Induced Plasmas

## Bibliographic Metadata

- Authors: Yi-Ben Wang, Zhuang-Wei Ding, Marcelo F. Ciappina, and Xue-Bin
  Bian.
- Year: 2026.
- Venue: Physical Review A 113, L021501.
- Publication date: 2026-02-10.
- Raw source: [Wang et al. - 2026 - Broadband quantum terahertz wave generation in laser-induced plasmas.pdf](<../../raw/sources/Wang et al. - 2026 - Broadband quantum terahertz wave generation in laser-induced plasmas.pdf>)
- Ingest date: 2026-06-06.

## Core Result

The paper proposes broadband quantum THz generation in laser-induced plasmas by
combining a strong classical 800 nm field with a weak 400 nm BSV field. The BSV
enhances bandwidth and yield, and the emitted THz photons are predicted to be
bunched or super-Poissonian with a thermal-like Wigner function.

## Useful Equations Or Model Ingredients

- THz spectral power from sampled current:

```text
S(omega) =
  omega^2 / (6 pi^2 c^3 epsilon_0)
  integral d^2 E_alpha Q(E_alpha) |j_alpha(omega)|^2
```

- For a coherent fundamental plus BSV second harmonic, sample the BSV Husimi
  distribution and solve the TDSE/current response for each realization:

```text
j(t) = <psi | p | psi>
```

then Fourier transform to `j(omega)`.

## Assumptions

- The strong coherent fundamental breaks the symmetry; the BSV is a weaker
  second-harmonic component.
- The calculation samples a positive Husimi Q distribution, making Monte Carlo
  averaging practical.

## Limitations And Cautions

- This is not pure zero-mean BSV plasma emission; a strong coherent driver is
  part of the mechanism.
- The predicted THz state is thermal-like rather than simply squeezed.

## Relevance To This Project

This is the most direct source for the BSV plasma THz simulation. The project
should first reproduce the coherent-plus-BSV setting before claiming anything
about pure BSV plasma emission.
