---
title: Wang Et Al 2024 HHG From Atom In Squeezed-Vacuum Environment
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, hhg, squeezed-vacuum, vacuum-fluctuations, quantum-light]
source_count: 1
confidence: high
related:
  - ../models/hhg-gas-model
  - ../theory/non-gaussian-output-novelty
  - ../simulations/simulation-roadmap
---

# Wang Et Al 2024 HHG From Atom In Squeezed-Vacuum Environment

## Bibliographic Metadata

- Authors: ShiJun Wang, ShaoGang Yu, XuanYang Lai, XiaoJun Liu.
- Year: 2024.
- Venue: Physical Review Research 6, 033010.
- DOI: 10.1103/PhysRevResearch.6.033010.
- Raw source: [PhysRevResearch.6.033010.pdf](<../../raw/sources/PhysRevResearch.6.033010.pdf>)
- Extracted text:
  [physrevresearch-6-033010.txt](<../../results/ingest-2026-06-06-missing-aps/extracted_text/physrevresearch-6-033010.txt>)
- Ingest date: 2026-06-06.

## Core Result

This paper studies HHG from an atom when a selected harmonic emission mode is in
a single-mode squeezed vacuum. It is not simply a BSV pump paper: the squeezed
vacuum modifies the vacuum quantum fluctuations of the emitted harmonic mode.
Within a fully quantum TDSE treatment, the harmonic amplitude of the squeezed
mode can be changed by the squeezing parameter and squeezing angle.

## Useful Equations Or Model Ingredients

The starting Hamiltonian is the atom plus quantized field in the dipole
approximation:

```text
i d|Psi(t)>/dt = [H_0 - r . E_hat + H_f] |Psi(t)>
```

After transforming the harmonic modes from squeezed vacuum to coherent vacuum,
the quantum fluctuation factor for mode `k` is:

```text
mu_k(t) = cosh(r_k) + sinh(r_k) exp[-i(2 omega_k t - theta_k)]
```

The paper's HHG spectral formula is:

```text
P(omega_k) =
  omega_k^4 / (6 pi^2 c^3)
  | integral dt mu_k(t) d_ii(t) exp(i omega_k t) |^2
```

where `d_ii(t)` is the laser-induced dipole matrix element from the classical
driving-field electron dynamics. For modes that are not squeezed, `r_k = 0` and
`mu_k(t) = 1`, recovering the conventional HHG expression.

For time-frequency analysis, the squeezed-vacuum factor multiplies the wavelet
integral:

```text
A(omega_k, t) =
  integral dt' mu_k(t') d_ii(t') sqrt(omega_k) W[omega_k(t' - t)]
```

The authors interpret the effect as a modulation of the electron-transition
probability by vacuum quantum fluctuations of the emitted mode, consistent with
Fermi-golden-rule intuition.

## Assumptions

- Single-mode squeezed vacuum is applied to a selected harmonic mode.
- The squeezed-vacuum parameter is small enough for a first-order expansion in
  the weak quantum fluctuation part.
- The dominant contribution is taken from the conventional `d_ii(t)` dipole
  term; correction terms with `j != i` are not central in the simulations.
- Numerical examples use a one-dimensional soft-Coulomb atom with argon-like
  ionization potential.
- The model controls the quantum environment of the harmonic emission mode; it
  is not a macroscopic gas propagation model.

## Relevance To This Project

This paper supplies a distinct route by which squeezed vacuum affects HHG:
changing the vacuum fluctuations of an emitted harmonic mode rather than
sampling a squeezed pump field. For the manuscript, it is useful as a boundary
case and novelty source:

- It supports the idea that HHG can be sensitive to quantum fluctuations of
  field modes beyond a deterministic classical driver.
- The factor `mu_k(t)` gives a compact way to think about squeezing-parameter
  and squeezing-angle control of a selected harmonic channel.
- It should not be conflated with the coherent-response averaging used for
  BSV-driven HHG in Gorlach/Rasputnyi/Heimerl-style papers.

## Simulation Hooks

- Add a "squeezed emission-mode environment" test separate from "squeezed pump
  drive" simulations.
- Compare three mechanisms:
  coherent pump only, stochastic/BSV pump sampling, and squeezed vacuum in a
  selected emitted harmonic mode.
- Use the `mu_k(t)` factor as an analytic toy model for how squeezed vacuum
  phase can modify harmonic amplitude before attempting a full quantized-field
  HHG model.
- Track whether squeezing modifies only the targeted harmonic mode or creates
  observable correlations between harmonics.

## Limitations And Cautions

- The model is single-atom and single-mode; it does not include gas propagation,
  phase matching, absorption, or macroscopic depletion.
- It treats a squeezed vacuum environment for a harmonic mode, not a
  bright-squeezed-vacuum pump ensemble.
- Because the analytical formula relies on approximations for weak quantum
  fluctuation terms and dominant `d_ii(t)`, it should be used as conceptual
  support unless its assumptions match the planned simulation.

