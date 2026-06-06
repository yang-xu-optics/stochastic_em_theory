---
title: Attosecond pulse synthesis from high-order harmonic generation in intense squeezed light
type: source-summary
status: draft
created: 2026-06-06
updated: 2026-06-06
tags: [source, hhg, quantum-light]
source_count: 1
confidence: medium
related:
  - ../models/hhg-gas-model
  - ../theory/non-gaussian-output-novelty
---

# Attosecond pulse synthesis from high-order harmonic generation in intense squeezed light

## Bibliographic Metadata

- Authors: ShiJun Wang, XuanYang Lai, XiaoJun Liu.
- Year: 2024.
- Venue: arXiv.
- DOI/arXiv: 10.48550/arXiv.2406.10443.
- Raw source: [Wang et al. - 2024 - Attosecond pulse synthesis from high-order harmonic generation in intense squeezed light.pdf](<../../raw/sources/Wang et al. - 2024 - Attosecond pulse synthesis from high-order harmonic generation in intense squeezed light.pdf>)
- Search source: retry_export_arxiv.
- Ingest date: 2026-06-06.

## Core Result

Analyzes HHG-driven attosecond pulse synthesis with intense squeezed light,
relevant to transferring pump quantum statistics into attosecond observables.

## Abstract Signal

HHG provides broad bandwidth for attosecond pulse synthesis, but usual schemes
phase-lock only part of the harmonic spectrum. This paper studies an atom driven
by intense squeezed light and reports phase locking across the full spectrum in
the model, with the synthesized pulse width depending on the squeezing
parameter.

## Relevance To This Project

Supports the HHG branch by identifying which pump-state or output-state
observables should be tracked beyond an averaged harmonic spectrum.

## Simulation Or Manuscript Hooks

- Add to the literature map for squeezed/quantum-light-driven HHG, BSV source
  characterization, or non-Gaussian nonlinear-output mechanisms as tagged
  above.
- Use the source to decide which stochastic ensemble variables must be sampled:
  quadratures, intensity, phase, mode weights, conditioning records, or emitted
  harmonic quadratures.
- If the paper is used in the manuscript, extract its governing equations and
  detection assumptions into the relevant theory/model page before citing it as
  quantitative support.

## Limitations And Cautions

- This is a first-pass ingest from the downloaded source and metadata; extract
equations before using it as a primary derivation source.
- Mode definition, loss, gain, and detection bandwidth must be specified before
quoting g2 or higher cumulants.
