---
title: Project Overview
type: synthesis
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [overview, thesis]
source_count: 52
confidence: high
related:
  - research-agenda
  - theory/stochastic-quantum-optics-correspondence
  - simulations/simulation-roadmap
---

# Project Overview

This workspace supports a paper on classical stochastic electromagnetic theory
for strong-field and THz processes driven by squeezed vacuum light.

The central strategy is to first validate the stochastic-field description in a
regime where quantum optics has sharp answers, then reuse the same stochastic
field ensemble as an input to classical or semiclassical nonlinear emission
models.

## Research Thesis

If the stochastic electromagnetic field is interpreted with the correct
phase-space representation and measurement ordering, it should reproduce
squeezed-vacuum characterization observables such as `g^{(2)}(0)`. Once this
correspondence is explicit, the same sampled fields can be used to simulate
nonlinear source terms for:

- high harmonic generation in gas,
- THz optical rectification,
- THz emission from plasma photocurrents.

## Milestones

1. Define the squeezed-vacuum stochastic ensemble and detection model.
2. Prove the `g^{(2)}(0)` correspondence for the simplest single-mode case.
3. Extend the characterization to multimode bright squeezed vacuum.
4. Build a reusable stochastic-field sampler with convergence tests.
5. Drive HHG gas response models with sampled squeezed fields.
6. Drive THz optical rectification models with sampled squeezed fields.
7. Drive plasma THz emission models and identify required symmetry breaking.
8. Assemble manuscript figures, limitations, and comparison baselines.

## Current Source Status

The first source ingest is complete. The strongest source-backed architecture
now looks like this:

- Use Raymer and Landes as the correspondence spine for squeezed-vacuum
  `g^(2)(0)`, four-frequency correlations, and stochastic-field vacuum
  subtraction.
- Use Sharapova et al. as the multimode BSV guardrail: single-mode claims need
  an explicit filtering or detection-mode assumption.
- Use Gorlach 2023, Rasputnyi 2024, Heimerl 2025, and related HHG sources for
  the ensemble-of-coherent-responses strategy:

```text
observable_BSV = integral phase_space_weight * observable_coh
```

- Use Ravi 2014 for classical tilted-pulse-front optical rectification and use
  Schuh 2013, Sun 2022, and Wang 2026 for THz plasma emission, with symmetry
  breaking treated as a central requirement.
- Use Yanagimoto 2022/2024 and Jankowski 2024 to frame high-impact novelty:
  identify whether HHG or THz generation creates only non-Gaussian classical
  shot distributions or genuinely non-Gaussian quantum output states.

The 2026-06-06 literature search expanded the HHG and strong-field branch
substantially: photon bunching, harmonic squeezing, displaced squeezed output,
attosecond synthesis, symmetry breaking, cutoff fluctuations, tunneling, and
ionization under quantum-light driving are now source-backed targets. The same
search strengthened the non-Gaussian branch through pump-depleted PDC,
Kerr-propagated BSV, and MPS/Gaussian-interaction-frame simulation methods.

The optical rectification branch now has a strong classical propagation source,
but still needs a dedicated squeezed-vacuum OR source or an explicit derivation
for stochastic/quantum-light pump statistics. The new search did not close that
gap.
