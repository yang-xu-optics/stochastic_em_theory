---
title: Research Agenda
type: synthesis
status: active
created: 2026-06-06
updated: 2026-11-14
tags: [agenda, planning]
source_count: 54
confidence: high
related:
  - prl-restructuring-plan
  - overview
  - project-status-review
  - theory/squeezed-vacuum-g2-proof-plan
  - simulations/simulation-roadmap
---

# Research Agenda

## Core Questions

1. Which stochastic representation is meant by "stochastic EM theory" in this
   project: Wigner sampling of the quantized field, stochastic electrodynamics
   with zero-point fields, or a semiclassical Gaussian random process?
2. What observables are required to claim agreement with quantum optics for
   squeezed vacuum: quadrature variance, photon number, `g^{(2)}(0)`,
   higher-order correlations, spectral correlations, or multimode statistics?
3. What is the minimal proof that connects stochastic sampled amplitudes to
   normally ordered photon-counting observables?
4. In HHG, which parts of the model are classical, semiclassical, or quantum:
   electron trajectory, ionization, recombination, propagation, and detection?
5. For THz optical rectification, what low-frequency observable survives
   ensemble averaging over a zero-mean squeezed field?
6. For plasma THz emission, what symmetry-breaking ingredient is needed to
   produce nonzero emitted THz fields from stochastic squeezed-vacuum drive?
7. What, exactly, can become non-Gaussian in HHG or THz generation: the emitted
   field, the residual pump, a conditional postselected state, or only the
   classical shot distribution?

## Deliverables

- A derivation page showing the stochastic/quantum optics match for
  squeezed-vacuum `g^{(2)}(0)`.
- A validated stochastic squeezed-field sampler.
- Numerical convergence plots for quadrature variance, photon number, and
  `g^{(2)}(0)`.
- HHG spectra driven by coherent, thermal/noisy, and squeezed ensembles.
- THz spectra from optical rectification driven by matched ensembles.
- THz plasma spectra with clear symmetry assumptions.
- A non-Gaussian novelty map with candidate witnesses, cumulants, and
  conditioning protocols for HHG and THz output.
- A manuscript outline with figure-to-claim mapping.

## Initial Risk Register

- Operator ordering error: using raw stochastic intensity moments as if they
  were normally ordered photon correlations.
- Mode ambiguity: quoting a squeezed-vacuum `g^{(2)}` value without specifying
  temporal/spectral modes and detection bandwidth.
- Symmetry null result: plasma or optical rectification signal may vanish after
  ensemble averaging unless the model includes a physical asymmetry.
- Overclaiming classicality: Wigner sampling can reproduce some quantum
  moments without making all later nonlinear dynamics fully equivalent to
  quantum electrodynamics.
- Numerical cost: rare high-field events in bright squeezed vacuum may dominate
  nonlinear observables and require many trajectories.
- Non-Gaussian overclaiming: heavy-tailed stochastic spectra are not equivalent
  to Wigner-negative or otherwise quantum non-Gaussian output states.

## Source-Backed Decisions

- D1: The first proof target remains single-mode `g^(2)(0) = 3 + 1/<n>`, but
  the broadband extension must specify temporal mode, dispersion compensation,
  and distinguishability. See
  [[sources/raymer-landes-2022-broadband-squeezed-vacuum-tpa]].
- D2: A stochastic EM comparison is strongest when the observable is expressed
  as a matched quantum/stochastic correlation function and vacuum terms are
  handled explicitly. See
  [[sources/raymer-landes-2023-classical-model-broadband-squeezed-vacuum]].
- D3: BSV-driven HHG and strong-field spectra should be reported both as
  unconditional ensemble averages and as conditional/post-selected observables.
  See [[sources/heimerl-2025-quantum-light-metal-needle-tips]].
- D4: For HHG intensity spectra, begin with coherent-response phase-space
  averaging; for generated harmonic quantum states, keep the claim separate and
  use the Positive P/Husimi reconstruction literature.
- D5: Pure zero-mean BSV plasma or OR emission may vanish at the field level by
  symmetry. Simulations should include a symmetry-breaking scan rather than
  assume a nonzero mean THz waveform.
- D6: Non-Gaussian novelty must be tied to a specific object and witness. Use
  [[theory/non-gaussian-output-novelty]] to separate higher-order classical
  statistics, Gaussian quantum squeezing, and genuine non-Gaussian quantum
  output.
- D7: The 2026-06-06 literature search found many new HHG/strong-field
  quantum-light papers but no direct squeezed-vacuum optical-rectification
  source. Treat HHG as the best-sourced first nonlinear application, and treat
  THz OR as a derivation-led extension until a dedicated source is found.
- D8: Non-Gaussian novelty is now better supported on the pump/output side:
  pump-depleted PDC, Kerr-propagated BSV, displaced/squeezed HHG output,
  cutoff fluctuations, and heralded BSV-matter states all give concrete witness
  targets.
- D9: The newly ingested APS papers split the strong-field problem into two
  validation axes: squeezed emitted-mode vacuum fluctuations can modulate a
  selected harmonic amplitude, while BSV/thermal photon statistics can be
  mapped through qSFA into ATI yield and electron statistics.

## Current Source Gaps

- A dedicated source for optical rectification driven directly by squeezed
  vacuum. None was found in June or in November 2026. The derivation now
  exists in the wiki ([[theory/quantum-optical-rectification-of-bsv]]) but is
  the project's own; Ravi 2014 covers classical tilted-pulse-front OR only.
- A foundational stochastic electrodynamics source beyond the Raymer/Landes
  stochastic-field construction.
- A gas-phase BSV HHG experiment analogous to the solid and metal-tip sources.
- A clear manuscript convention for whether "classical stochastic EM" means
  Wigner sampling, Husimi sampling, Positive P sampling, or SED-like
  zero-point fields in each section.
- Two papers found by search on 2026-11-14 but not obtained: "Theory of
  high-harmonic generation with quantum light" (Phys. Rev. Research) and the
  Nature Communications version of the Rivera-Dean propagation paper.
- For the optical-rectification claim: the cavity electro-optics papers for
  the `n (b + b^dagger)` Hamiltonian, a THz parametric down-conversion
  review for the spontaneous term, and a paper on THz spectroscopy with
  incoherent light as classical precedent.

## Next Actions

The current list is [[prl-restructuring-plan]] (2026-11-14): workstreams,
week-by-week gates, and the inputs needed from the author. In short: crystal
response and detection model for the optical-rectification theory; source
characterization, calibration, averaged trace, and shot-resolved statistics
on the BSV source; Letter drafted in parallel. The HHG and plasma work
(rebuild the drive ensemble, quadrature, comparison with source data) moves
to the companion paper and waits.

## Status Of The June 2026 Action List

1. Turn [[theory/squeezed-vacuum-g2-proof-plan]] into a complete derivation and
   simulation spec. *Done: the page contains the derivation;
   [[simulations/paper-one-correspondence-hhg-simulation-spec]] is the spec.*
2. Implement a single-mode squeezed-vacuum sampler and Monte Carlo validation.
   *Done.*
3. Add a broadband BSV validation matching Raymer/Landes assumptions.
   *Not started.*
4. Decide the first HHG model fidelity level: classical trajectory,
   Lewenstein-like semiclassical response, or propagation-first source model.
   *Decided in practice: 1D soft-core TDSE with an amplitude library.*
5. Build a minimal two-color plasma THz model before testing pure BSV symmetry.
   *Done as a notebook; pure-BSV test not run.*
6. Add a non-Gaussian diagnostics spec: cumulants, mode selection, conditional
   bins, and candidate phase-space witnesses. *Not started.*
7. Prioritize an HHG pilot before THz OR because the HHG literature now offers
   specific stochastic-driver observables: bunching, symmetry leakage, cutoff
   fluctuations, ionization/tunneling distributions, and harmonic quadrature
   reconstruction. *Done as a pilot; see the review for its numerical state.
   The priority argument is reversed in the review: THz OR is now the less
   crowded direction.*
8. Add an ATI/ionization validation notebook before full HHG: compare coherent,
   thermal, and BSV sampled-field ensembles against the qSFA/ADK observables in
   Lyu 2025. *Partial: an ionization-rate proxy exists (`ati.py`); no qSFA
   comparison.*
