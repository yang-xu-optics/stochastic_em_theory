---
title: Wiki Index
type: synthesis
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [index]
source_count: 54
confidence: high
related: []
---

# Wiki Index

This index is the content-oriented entry point for the research wiki. Read this
before answering project questions or changing wiki pages.

## Core

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

## Manuscript

- [paper/outline.md](../paper/outline.md): linear manuscript structure and
  figure plan.

## Source Summaries

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

### HHG And Strong-Field Quantum Light

- [[sources/gorlach-2020-quantum-optical-nature-hhg]]: quantum-optical HHG
  boundary conditions and emitted-field statistics.
- [[sources/stammer-2022-theory-of-entanglement-and-measurement-in-hhg]]:
  entanglement and measurement framing for HHG.
- [[sources/gorlach-2023-hhg-driven-quantum-light-supplement]]: coherent-state
  phase-space sampling for quantum-light-driven HHG and a 1D gas baseline.
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
  propagation of intense BSV through nonlinear media.
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
