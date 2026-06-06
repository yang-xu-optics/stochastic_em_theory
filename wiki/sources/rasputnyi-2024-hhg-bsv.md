---
title: Rasputnyi Et Al 2024 HHG By Bright Squeezed Vacuum
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, hhg, bsv, solids, superbunching]
source_count: 1
confidence: high
related:
  - ../models/hhg-gas-model
  - ../simulations/simulation-roadmap
---

# Rasputnyi Et Al 2024 HHG By Bright Squeezed Vacuum

## Bibliographic Metadata

- Authors: Ivan Rasputnyi et al.
- Year: 2024.
- Identifier: arXiv:2403.15337v1.
- Raw source: [Rasputnyi et al. - 2024 - High Harmonic Generation by Bright Squeezed Vacuum.pdf](<../../raw/sources/Rasputnyi et al. - 2024 - High Harmonic Generation by Bright Squeezed Vacuum.pdf>)
- Ingest date: 2026-06-06.

## Core Result

The paper reports nonperturbative HHG in solids driven by BSV and finds more
efficient HHG than coherent light at the same mean intensity. Although the
medium is solid rather than gas, the analysis strongly supports ensemble
weighting of coherent responses by a BSV phase-space distribution.

## Useful Equations Or Model Ingredients

- BSV has even-photon statistics and strong higher moments:

```text
g_BSV^(n) = (2n - 1)!!
g_thermal^(n) = n!
```

- The HHG spectrum is modeled by integrating coherent-driver spectra over the
  BSV Husimi distribution:

```text
S_HHG^BSV(omega, Ebar) =
  integral dE_alpha Q(E_alpha) S_HHG^coh(omega, E_alpha)
```

## Assumptions

- The BSV source is treated as a single spatiotemporal mode for the experiment.
- The key observable is the ensemble-averaged HHG intensity spectrum.

## Limitations And Cautions

- The physical medium is a solid, so gas-phase ionization and recombination
  details are not directly transferable.
- The coherent-response averaging picture does not automatically reconstruct
  the emitted harmonic quantum state.

## Relevance To This Project

This is useful experimental motivation and a practical model template for BSV
HHG. The gas simulation should keep the same ensemble-averaged comparison but
swap in a gas HHG response model.

