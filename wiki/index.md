---
title: Wiki Index
type: synthesis
status: active
created: 2026-06-06
updated: 2026-11-14
tags: [index]
source_count: 69
confidence: high
related: []
---

# Wiki Index

This index is the content-oriented entry point for the research wiki. Read this
before answering project questions or changing wiki pages.

## Core

- [[prl-restructuring-plan]]: the current plan. Headline claim (optical
  rectification of BSV), honest assessment of the PRL case, workstreams,
  experiment protocol, timeline with gates, inputs needed. Read this first.
- [[project-status-review]]: 2026-11-14 evaluation of progress, result
  quality, literature position, and publication strategy that led to the
  plan. Still the reference for the state of the HHG and plasma material.
- [[overview]]: project thesis, architecture, and milestone structure.
- [[research-agenda]]: research questions, deliverables, risks, and next steps.
- [[log]]: chronological record of setup, ingests, decisions, and durable
  queries.

## Theory

- [[theory/stochastic-quantum-optics-correspondence]]: representation choices
  and operator-ordering guardrails for matching stochastic EM and quantum
  optics.
- [[theory/squeezed-vacuum-g2-proof-plan]]: derivation plan for reproducing the
  squeezed-vacuum `g^{(2)}(0)` value.
- [[theory/non-gaussian-output-novelty]]: source-backed novelty map for what
  could become non-Gaussian in HHG or THz generation.
- [[theory/quantum-optical-rectification-of-bsv]]: fully quantum description
  of THz generation by optical rectification of BSV. Input-output relation,
  Wick decomposition with the spontaneous term, counting statistics for `K`
  modes, solvable single-mode model, comparison of exact, phase-space, and
  classical-noise descriptions. The theory core of the Letter.
- [[theory/bsv-even-order-response-moment-scaling]]: parity rule for
  ensemble-mean fields under BSV driving, single-mode moment scaling, and the
  plasma two-colour check.

## Physical Models

- [[models/hhg-gas-model]]: HHG in gas driven by stochastic squeezed fields.
- [[models/thz-optical-rectification-model]]: THz generation by optical
  rectification of stochastic optical fields.
- [[models/thz-plasma-emission-model]]: THz generation through plasma
  photocurrent dynamics.

## Simulations

- [[simulations/simulation-roadmap]]: staged numerical implementation plan,
  validation tests, and result conventions.
- [[simulations/paper-one-correspondence-hhg-simulation-spec]]: paper-one
  simulation specification for squeezed-field validation, mode-filtered
  `g^(2)`, HHG intensity observables, ATI photon-statistics validation, and
  squeezed emitted-mode boundary modeling.
- [[simulations/gorlach-2023-fig3b-proxy-reproduction]]: Fig. 3b reproduction
  spec for coherent, Fock, thermal, and BSV HHG spectra using single-mode
  Husimi-Q coherent-response sampling with a local TDSE dipole-acceleration
  spectrum library.
- [[simulations/gorlach-2023-fig-iv2-bsv-threshold]]: supplementary Fig. IV.2
  reproduction spec for the BSV HHG intensity threshold in a 1D model Ne atom
  using a TDSE dipole-acceleration response library.
- [[simulations/thz-plasma-bsv-photocurrent-notebook]]: Stage-5 plasma
  photocurrent notebook spec for coherent-plus-BSV THz generation with
  driving-field `g^(2)(0)` validation, ensemble mean/fluctuation THz
  waveforms, and ensemble-averaged spectra.
- [[simulations/bsv-optical-rectification-thz-statistics]]: spec and first
  run for the optical-rectification THz statistics: exact cumulants, energy
  enhancement and fluctuation ratio, amplitude distributions, spectrum terms.
- [[simulations/machine-learning-integration-roadmap]]: physics-separated ML
  roadmap for response surrogates, tail-aware active learning, and joint
  HHG-THz inference of squeezed-field parameters.

## Manuscript

- [paper/outline.md](../paper/outline.md): outline of the Letter on optical
  rectification of BSV, with the figure plan.
- [paper/companion-outline.md](../paper/companion-outline.md): outline of the
  companion paper on HHG and plasma THz emission (the outline until
  2026-11-14).

## Results

- [results/runs/README.md](../results/runs/README.md): index of simulation
  runs with status and whether each may be used in the manuscript.

## Source Summaries

69 pages for 70 PDFs (one duplicate). 35 are full summaries with equations
(`status: active`), including the 15 added on 2026-11-14. 34 are first-pass
stubs written from metadata (`status: draft`); upgrade a stub before citing
it quantitatively. Two papers found by search are not yet in `raw/`; see
[[prl-restructuring-plan]].

### Quantum Optics And Stochastic Squeezed Vacuum

- [[sources/raymer-landes-2022-broadband-squeezed-vacuum-tpa]]: broadband
  BSV TPA theory, `g^(2)(0)`, dispersion compensation, and four-frequency
  correlations.
- [[sources/raymer-landes-2023-classical-model-broadband-squeezed-vacuum]]:
  stochastic-field TPA/SFG model with vacuum subtraction.
- [[sources/sharapova-2015-schmidt-modes-bsv]]: multimode BSV and gain-dependent
  Schmidt modes.
- [[sources/agafonov-2009-two-color-bsv]]: two-color high-gain BSV and
  multimode direct-detection statistics.
- [[sources/iskhakov-2012-super-bunched-bsv-state]]: superbunched BSV intensity
  fluctuations at very high brightness.
- [[sources/perez-2014-spatially-single-mode-source-of-bsv]]: source engineering
  toward a spatially single-mode BSV limit.
- [[sources/iskhakov-2015-nonlinear-interferometer-for-tailoring-the-frequency-spectrum-of]]:
  nonlinear-interferometer tailoring of the BSV frequency spectrum.
- [[sources/sharapova-2020-properties-of-bsv-at-increasing-brightness]]:
  gain-dependent BSV modal properties and Schmidt-mode behavior.
- [[sources/spasibko-2017-multiphoton-effects-photon-number-fluctuations]]:
  second to fourth harmonics of BSV; enhancement by `g^(n)`, measured 2.86,
  13.6, 71; the `(2n - 1)!!` rule. Closest prior art for the moment scaling.
- [[sources/manceau-2019-indefinite-mean-pareto-photon-distribution]]:
  single-shot photon-number distributions of BSV harmonics and of
  supercontinuum; power-law tails with undefined mean.
- [[sources/racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes]]:
  estimators for heavy-tailed shot statistics with a BSV pump.
- [[sources/kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv]]:
  femtosecond BSV at 1040 nm, about 100 nJ, 27 fs, one spatial mode; random
  pi phase seen shot by shot.
- [[sources/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light]]:
  field-resolved single shots of BSV; time-localized bursts with random
  sign; shot-energy `g2` 2.08 against burst `g2` 2.94.

### Non-Gaussian Quantum Nonlinear Optics

- [[sources/florez-2020-pump-depletion-in-pdc-with-low-pump-energies]]: pump
  depletion in high-gain parametric down-conversion at low pulse energy.
- [[sources/yanagimoto-2021-efficient-simulation-of-ultrafast-quantum-nonlinear-optics-with]]:
  MPS simulation route for ultrafast quantum nonlinear optics.
- [[sources/yanagimoto-2022-nongaussian-pulsed-squeezing]]: pump-depleted
  pulsed squeezing, Gaussian interaction frames, Wigner negativity, and
  signal-pump entanglement.
- [[sources/kulkarni-2022-a-classical-model-of-spontaneous-pdc]]: stochastic
  vacuum-seeded classical model of SPDC.
- [[sources/jankowski-2024-ultrafast-chi2-nonlinear-photonics]]: tutorial
  bridge from classical `chi^(2)` nonlinear optics to mesoscopic
  non-Gaussian quantum dynamics.
- [[sources/vendromin-2024-highly-squeezed-states-in-ring-resonators-beyond-the]]:
  multimode ring-resonator squeezing beyond the undepleted-pump approximation.
- [[sources/yanagimoto-2024-mesoscopic-ultrafast-nonlinear-optics]]: review of
  multimode mesoscopic non-Gaussian physics, quantum-light-driven dynamics,
  and non-Gaussian measurement/sensing.
- [[sources/vendromin-2025-nongaussian-states-via-pump-depleted-spdc]]:
  non-Gaussian state generation through pump-depleted SPDC.
- [[sources/rasputnyi-2025-kerr-induced-nongaussianity-of-ultrafast-bsv]]:
  Kerr-induced non-Gaussianity in ultrafast BSV.

### Electro-Optic Sampling And Quantum THz Fields

- [[sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum]]:
  operator theory of electro-optic sampling: signal operator, response
  function, shot-noise and vacuum terms.
- [[sources/riek-2017-subcycle-quantum-electrodynamics]]: optical
  rectification of a 12 fs coherent pump and subcycle squeezing of the
  mid-infrared vacuum, read by electro-optic sampling; field and noise scales.
- [[sources/kizmann-2019-subcycle-squeezing-time-flow-perspective]]:
  time-domain operator theory of a classical THz drive acting on the quantum
  field in a `chi^(2)` crystal.

### HHG And Strong-Field Quantum Light

- [[sources/gorlach-2020-quantum-optical-nature-hhg]]: quantum-optical HHG
  boundary conditions and emitted-field statistics.
- [[sources/stammer-2022-theory-of-entanglement-and-measurement-in-hhg]]:
  entanglement and measurement framing for HHG.
- [[sources/gorlach-2023-hhg-driven-quantum-light-supplement]]: coherent-state
  phase-space sampling for quantum-light-driven HHG and a 1D gas baseline.
- [[sources/gorlach-2023-hhg-driven-by-quantum-light-main-article]]: the main
  article; scaling limit in which the expansion becomes a Husimi-Q average,
  and the cutoff laws for thermal and BSV drivers.
- [[sources/rasputnyi-2024-hhg-bsv]]: experimental BSV-driven HHG in solids and
  coherent-response averaging.
- [[sources/stammer-2024-entanglement-and-squeezing-of-the-optical-field-modes]]:
  entanglement and squeezing of optical field modes generated by HHG.
- [[sources/lemieux-2024-photon-bunching-in-high-harmonic-emission-controlled-by]]:
  photon bunching in high-harmonic emission controlled by quantum light.
- [[sources/rivera-dean-2024-squeezed-states-of-light-after-hhg-in-excited]]:
  squeezed harmonic output from excited atomic systems.
- [[sources/wang-2024-hhg-atom-squeezed-vacuum-environment]]: HHG from an atom
  in a squeezed-vacuum environment for a selected harmonic emission mode.
- [[sources/wang-2024-attosecond-pulse-synthesis-from-hhg-in-intense-squeezed]]:
  attosecond pulse synthesis with intense squeezed-light-driven HHG.
- [[sources/tzur-generation-squeezed-high-order-harmonics]]: generated harmonic
  quantum states and squeezing transfer.
- [[sources/even-tzur-cohen-2024-motion-charged-particles-bsv]]: electron
  wavepacket width dynamics and BSV ponderomotive scale.
- [[sources/heimerl-2025-quantum-light-metal-needle-tips]]: BSV strong-field
  electron emission and post-selected versus shot-averaged spectra.
- [[sources/mao-2025-benchmarking-atomic-ionization-driven-by-strong-quantum-light]]:
  benchmarking atomic ionization theories under strong quantum light.
- [[sources/lyu-2025-photon-statistics-ati]]: photon-statistics effects of BSV
  and thermal light on above-threshold ionization and electron statistics.
- [[sources/gothelf-2025-hhg-in-a-crystal-driven-by-quantum-light]]: crystal
  HHG under quantum-light driving.
- [[sources/lange-2025-excitonic-enhancement-of-squeezed-light-in-quantum-optical]]:
  excitonic enhancement of squeezed-light generation in Mott-insulator HHG.
- [[sources/theidel-2025-observation-of-a-displaced-squeezed-state-in-hhg]]:
  observation of displaced squeezed-state signatures in HHG.
- [[sources/rivera-dean-2025-propagation-of-intense-squeezed-vacuum-light-in-non]]:
  BSV in an ionizing gas: ionization as loss, maximum medium length, yield
  against a coherent driver; linear loss leaves normalized moments unchanged
  (full summary since 2026-11-14).
- [[sources/wang-2025-quantum-dial-for-hhg]]: tuning HHG with the quantum state
  of the driving field.
- [[sources/ciappina-2025-solid-state-hhg-emerging-frontiers-in-ultrafast-and]]:
  review of solid-state HHG at the ultrafast/quantum-light frontier.
- [[sources/rivera-dean-2025-structured-squeezed-light-allows-for-hhg-in-classical]]:
  structured squeezed-light HHG in classically forbidden geometries.
- [[sources/stammer-2025-theory-of-quantum-optics-and-optical-coherence-in]]:
  optical-coherence and quantum-optics theory for HHG.
- [[sources/kim-2025-tunneling-driven-by-quantum-light-described-via-field]]:
  field-Bohmian trajectory view of tunneling driven by quantum light.
- [[sources/even-tzur-2025-attosecond-quantum-fluctuations]]: BSV-perturbed HHG,
  `g^(2)`, Husimi reconstruction, and Wigner reconstruction.
- [[sources/lange-2026-edge-states-and-quantum-optical-hhg-from-topological]]:
  edge-state effects in quantum-optical HHG from topological insulators.
- [[sources/stammer-2026-fluctuation-induced-symmetry-breaking-in-hhg-for-bicircular]]:
  fluctuation-induced symmetry breaking for bicircular quantum-light HHG.
- [[sources/imai-2026-heralded-ultrafast-generation-of-macroscopic-quantum-states-in]]:
  heralded macroscopic matter-state generation with BSV.
- [[sources/singh-2026-interferometrically-enhanced-asymmetry-in-strong-field-ionization-with]]:
  BSV-enhanced asymmetry in strong-field ionization.
- [[sources/khurelbaatar-2026-nonclassical-cutoff-fluctuations-in-squeezed-light-driven-hhg]]:
  nonclassical cutoff fluctuations in squeezed-light-driven HHG.
- [[sources/jiang-2026-nonlinear-atomic-tunnelling-boosted-by-bsv]]:
  boosted nonlinear atomic tunneling under BSV.
- [[sources/ilin-2026-quantum-optical-signatures-of-band-topology-in-solid]]:
  quantum-optical signatures of band topology in solid-state HHG.
- [[sources/liu-2026-strong-field-ionization-of-atoms-with-bsv-light]]:
  strong-field ionization of atoms driven by BSV light.
- [[sources/stammer-2026-symmetry-breaking-by-quantum-light-in-solid-state]]:
  symmetry breaking by quantum light in solid-state HHG.
- [[sources/gothelf-2026-limitations-of-approximative-phase-space-description]]:
  what the Husimi-Q classical-mixture description gets right and wrong;
  no-go statements for squeezing and antibunching; exactly solvable one-band
  benchmark.
- [[sources/de-la-pena-2026-high-order-correlations-wigner-negativities-bsv-hhg]]:
  two-level emitter with quantized BSV driver and emission modes; driver
  becomes Wigner-negative; semiclassical ensembles reproduce the emitter.
- [[sources/stammer-2026-photon-anti-bunching-in-hhg]]: antibunching of single
  harmonics for a coherent driver; vanishes for many emitters.
- [[sources/stammer-2026-attosecond-metrology-of-bright-quantum-light]]:
  streaking with a quantized infrared field; proposal to read squeezing from
  the delay-dependent width.
- [[sources/rivera-dean-2026-erasing-photons-from-bsv-via-ati]]: photoelectron
  detection heralds cat-like states of BSV; unconditional spectra equal the
  classical-mixture average.
- [[sources/wang-2026-bright-quantum-hhg-coherent-plus-bsv-propagation]]: HHG
  in krypton with coherent 800 nm plus weak BSV; pressure dependence and
  propagation; simulated harmonic statistics.

### THz And Plasma Emission

- [[sources/schuh-2013-thz-ionization-gases]]: microscopic gas-ionization THz
  current model.
- [[sources/sun-2022-thz-laser-induced-plasma]]: review of plasma THz
  mechanisms, photocurrent, and four-wave rectification.
- [[sources/wang-2026-quantum-thz-plasma-bsv]]: coherent-plus-BSV plasma THz
  generation with Husimi sampling.
- [[sources/ravi-2014-thz-generation-optical-rectification]]: tilted-pulse-front
  lithium-niobate optical rectification, cascading, and 2D depleted propagation.

## Duplicate Source Note

`raw/sources/41567_2023_2127_MOESM1_ESM.pdf` and
`raw/sources/Gorlach et al. - 2023 - High-harmonic generation driven by quantum light.pdf`
extract to the same text. They are represented by one source-summary page:
[[sources/gorlach-2023-hhg-driven-quantum-light-supplement]].
