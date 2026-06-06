---
title: Lyu Et Al 2025 Photon Quantum Statistics In Above-Threshold Ionization
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, strong-field, ati, bsv, photon-statistics, ionization]
source_count: 1
confidence: high
related:
  - ../models/hhg-gas-model
  - ../theory/stochastic-quantum-optics-correspondence
  - ../simulations/simulation-roadmap
---

# Lyu Et Al 2025 Photon Quantum Statistics In Above-Threshold Ionization

## Bibliographic Metadata

- Authors: Zijian Lyu, Fengxiao Sun, Yiqi Fang, Qiongyi He, Yunquan Liu.
- Year: 2025.
- Venue: Physical Review Research 7, L012072.
- DOI: 10.1103/PhysRevResearch.7.L012072.
- Raw source: [PhysRevResearch.7.L012072.pdf](<../../raw/sources/PhysRevResearch.7.L012072.pdf>)
- Extracted text:
  [physrevresearch-7-l012072.txt](<../../results/ingest-2026-06-06-missing-aps/extracted_text/physrevresearch-7-l012072.txt>)
- Ingest date: 2026-06-06.

## Core Result

This paper studies above-threshold ionization (ATI) driven by coherent,
thermal, and bright squeezed vacuum light using quantum strong-field
approximation theory. Broad photon-number statistics in BSV and thermal light
modify electron momentum spectra, enhance ionization, smear ATI interference
patterns, and transfer photon bunching into electron-number statistics.

## Useful Equations Or Model Ingredients

The central qSFA observable is an incoherent phase-space average over coherent
field amplitudes:

```text
W(p) = integral dE_alpha P(E_alpha) |M_alpha(p)|^2
```

where `M_alpha(p)` is the photoelectron amplitude for a coherent field with
amplitude `E_alpha`, and `P(E_alpha)` encodes the quantum-light statistics. The
paper compares BSV, thermal, and coherent-state field distributions.

The photon bunching enhancement is framed with normally ordered correlations:

```text
g^(n) = < : N^n : > / <N>^n
```

For the considered ideal statistics:

```text
g_BSV^(n) = (2n - 1)!!
g_thermal^(n) = n!
g_coherent^(n) = 1
```

For `n = 2`, this gives the familiar hierarchy:

```text
g_BSV^(2) = 3
g_thermal^(2) = 2
g_coherent^(2) = 1
```

The appendix derives the qSFA averaging formula by starting from the
Glauber-P representation and arguing that, in the large coherent-amplitude
limit for a fixed classical field amplitude, the off-diagonal phase-space
terms localize onto diagonal contributions.

## Assumptions

- Hydrogen is used as the benchmark atomic target.
- The qSFA calculation keeps the diagonal/incoherent coherent-amplitude average
  and neglects off-diagonal interference terms under a stated limiting
  argument.
- The compared optical states are idealized coherent, thermal, and BSV states
  with matched field-strength scale.
- Ionization-rate interpretation uses ADK/tunneling intuition for parts of the
  electron-number distribution analysis.

## Relevance To This Project

This paper is highly useful for the gas-HHG plan because ATI is the upstream
strong-field ionization step that also controls HHG trajectories. It supplies a
direct source-backed formula for replacing a single classical field by a
quantum-light statistics average while keeping the atomic response calculation
classical or semiclassical for each coherent component.

It also supports a practical validation target: before running full HHG, the
stochastic BSV sampler should reproduce the predicted ordering of ionization
yield and momentum-pattern decoherence for coherent, thermal, and BSV
statistics at matched field scale.

## Simulation Hooks

- Implement a qSFA/ADK-style ionization benchmark with sampled coherent
  amplitudes drawn from coherent, thermal, and BSV distributions.
- Store photoelectron yield, energy/momentum spectra, and electron-number
  statistics as driver-validation observables before HHG recollision modeling.
- Test whether BSV heavy tails dominate ionization and therefore HHG yield,
  convergence, and cutoff statistics.
- Use `g^(n)` enhancement factors to connect the project's squeezed-vacuum
  `g^(2)` proof to multiphoton and nonperturbative ionization observables.

## Limitations And Cautions

- ATI is not HHG; it validates the ionization part of the strong-field
  mechanism but not recombination emission or harmonic output statistics.
- The diagonal phase-space averaging is an approximation whose regime should be
  checked before importing it into a full HHG model.
- Electron-number heavy tails are classical or measurement statistics until a
  specific quantum electron or light-output non-Gaussian witness is defined.

