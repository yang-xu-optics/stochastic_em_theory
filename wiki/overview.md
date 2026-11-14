---
title: Project Overview
type: synthesis
status: active
created: 2026-06-06
updated: 2026-11-14
tags: [overview, thesis]
source_count: 54
confidence: high
related:
  - prl-restructuring-plan
  - research-agenda
  - project-status-review
  - theory/stochastic-quantum-optics-correspondence
  - simulations/simulation-roadmap
---

# Project Overview

> **Headline claim since 2026-11-14.** Optical rectification turns a
> zero-mean bright squeezed vacuum pulse into a phase-stable THz transient
> whose single-shot field is proportional to the pump photon number, so the
> THz field carries the photon-number statistics of squeezed vacuum. Exact
> quantum model: [[theory/quantum-optical-rectification-of-bsv]]. Plan for a
> Physical Review Letters submission with a measurement on the author's BSV
> source: [[prl-restructuring-plan]]. What follows on this page is the
> original framing. It now describes the companion paper on HHG and plasma
> THz emission, which is frozen until the Letter is submitted.

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

Status as of 2026-11-14; evidence and caveats are in
[[project-status-review]].

1. Define the squeezed-vacuum stochastic ensemble and detection model.
   *Done for one mode; no loss or temporal-gate model.*
2. Prove the `g^{(2)}(0)` correspondence for the simplest single-mode case.
   *Done.*
3. Extend the characterization to multimode bright squeezed vacuum.
   *Partial: equal independent modes only.*
4. Build a reusable stochastic-field sampler with convergence tests.
   *Done for one mode.*
5. Drive HHG gas response models with sampled squeezed fields.
   *Partial: qualitative reproductions of Gorlach 2023; not converged.*
6. Drive THz optical rectification models with sampled squeezed fields.
   *Now the main line: quantum derivation, code, tests, and a first run exist
   ([[simulations/bsv-optical-rectification-thz-statistics]]); crystal
   response, detection model, and measurement are next.*
7. Drive plasma THz emission models and identify required symmetry breaking.
   *Partial: one notebook configuration; parity rule identified.*
8. Assemble manuscript figures, limitations, and comparison baselines.
   *Not started.*

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
The two later-added APS papers close the previous command-line access gap and
add two useful distinctions: squeezed vacuum can modify a selected emitted
harmonic mode as an environment, and BSV photon statistics can reshape ATI
ionization yield, decoherence, and electron-number statistics.

The optical rectification branch now has a strong classical propagation source,
but still needs a dedicated squeezed-vacuum OR source or an explicit derivation
for stochastic/quantum-light pump statistics. The new search did not close that
gap.

Update 2026-11-14: 15 sources were ingested on this date, bringing the total
to 69 summaries for 70 PDFs. They include the 2026 critique of the
coherent-state phase-space approximation
([[sources/gothelf-2026-limitations-of-approximative-phase-space-description]]),
field-resolved measurements of BSV itself, and the earlier experiments on
harmonics of BSV that the new headline claim must be positioned against. Two
papers found by search could not be downloaded; see [[prl-restructuring-plan]].
