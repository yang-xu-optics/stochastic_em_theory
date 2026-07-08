---
title: Non-Gaussian Output Novelty
type: synthesis
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [non-gaussian, novelty, hhg, thz, squeezed-vacuum]
source_count: 20
confidence: medium
related:
  - ../models/hhg-gas-model
  - ../models/thz-optical-rectification-model
  - ../models/thz-plasma-emission-model
  - ../sources/yanagimoto-2022-nongaussian-pulsed-squeezing
  - ../sources/jankowski-2024-ultrafast-chi2-nonlinear-photonics
  - ../sources/yanagimoto-2024-mesoscopic-ultrafast-nonlinear-optics
  - ../sources/even-tzur-2025-attosecond-quantum-fluctuations
  - ../sources/wang-2026-quantum-thz-plasma-bsv
  - ../sources/tzur-generation-squeezed-high-order-harmonics
  - ../sources/florez-2020-pump-depletion-in-pdc-with-low-pump-energies
  - ../sources/yanagimoto-2021-efficient-simulation-of-ultrafast-quantum-nonlinear-optics-with
  - ../sources/kulkarni-2022-a-classical-model-of-spontaneous-pdc
  - ../sources/vendromin-2024-highly-squeezed-states-in-ring-resonators-beyond-the
  - ../sources/vendromin-2025-nongaussian-states-via-pump-depleted-spdc
  - ../sources/rasputnyi-2025-kerr-induced-nongaussianity-of-ultrafast-bsv
  - ../sources/imai-2026-heralded-ultrafast-generation-of-macroscopic-quantum-states-in
  - ../sources/wang-2024-hhg-atom-squeezed-vacuum-environment
  - ../sources/lyu-2025-photon-statistics-ati
---

# Non-Gaussian Output Novelty

## Core Distinction

For this project, "non-Gaussian" needs to be used precisely. A classical
shot-to-shot distribution with a long tail is not automatically a non-Gaussian
quantum state. The source-backed hierarchy is:

```text
mean-field feature:
  ensemble mean field, mean spectrum, cutoff location

Gaussian quantum feature:
  covariance matrix, squeezing, Gaussian entanglement, positive Gaussian Wigner

non-Gaussian quantum feature:
  nonzero higher-order cumulants beyond covariance,
  Wigner negativity,
  non-Gaussian witnesses,
  photon-number features not reducible to Gaussian moments,
  conditional states that cannot be represented as Gaussian states
```

## Bunching Is Not A Standalone Nonclassicality Witness

Photon bunching or superbunching in HHG, THz emission, ATI yields, or other
strong-field observables should not be treated as a uniquely quantum-mechanical
output signature by itself. Classical thermal light, positive phase-space
representations of squeezed or bright squeezed vacuum, detector-mode averaging,
and nonlinear filtering of shot-to-shot intensity fluctuations can all produce
`g^(2) > 1`.

This does not make bunching uninteresting. It makes bunching a baseline problem:
one must first ask how much of the observed correlation is already explained by
the input BSV statistics and the nonlinear response function. The stochastic
field model is therefore useful as a null model and calibration layer. Any
claim of genuinely nonclassical emitted radiation should then go beyond
bunching alone, for example through antibunching, entanglement, squeezing with
a specified mode basis, Wigner negativity, a non-Gaussian witness, or a
conditional-state measurement.

## Mechanisms That Could Create Non-Gaussian HHG Or THz Output

1. Pump depletion and backaction:
   Strong conversion can entangle the squeezed pump with generated harmonics or
   THz modes. Yanagimoto 2022 shows this can cause purity loss, excess
   quadrature noise, and Wigner negativity in pulsed squeezing.

2. Nonlinear measurement or conditioning:
   HHG, ionization, or THz emission can act as a nonlinear measurement of the
   pump field. Conditioning on emitted harmonics, electron yield, ionization
   bursts, or THz energy could project the residual optical field or emitted
   mode into a non-Gaussian state.

3. Mode-selective output structure:
   Non-Gaussian features may live in principal supermodes or hybridized
   pump-output modes, not in a naive spectral bin. The measurement basis is part
   of the claim.

4. Higher-order nonlinear response:
   HHG is an extreme nonlinear process, and plasma THz generation depends on
   ionization gating and current acceleration. These mechanisms can amplify
   higher-order pump statistics, but that only proves quantum non-Gaussianity if
   an emitted-state or conditional-state witness is defined.

5. Nonlinear propagation of the pump before the target:
   The new literature search adds two pump-side mechanisms that should not be
   folded into a static Gaussian BSV sampler without thought. Pump-depleted PDC
   and ring-resonator squeezing beyond the undepleted approximation can make
   the generated squeezed field non-Gaussian before HHG or THz conversion.
   Kerr propagation of ultrafast BSV is another direct route to bright
   non-Gaussian pump states.

6. Heralding and post-interaction measurement:
   BSV followed by quadrature measurement can condition matter or optical modes
   into macroscopic quantum states. For this project, any postselected HHG or
   THz proposal must record the conditioning variable as part of the output
   state definition.

## Candidate Observables

- Higher-order cumulants of emitted harmonic/THz quadratures.
- Normally ordered photon-number cumulants beyond `g^(2)`.
- Mode-resolved Wigner or Husimi reconstruction for selected harmonic/THz
  modes.
- Wigner-negativity witness or operational non-Gaussian witness.
- Conditional output distributions after postselecting on pump photon number,
  electron yield, ionization bursts, or THz energy.
- Residual pump purity and pump-output entanglement indicators.

## HHG Novelty Hypotheses

- Half-integer or even harmonic channels generated by a BSV perturbation may be
  the best near-term place to look because Even Tzur 2025 already reports
  quantum-state reconstruction language for emitted channels.
- Quantum-light HHG papers from 2024-2026 add several sharper targets:
  photon bunching in emitted harmonics, squeezed or displaced-squeezed harmonic
  output, nonclassical cutoff fluctuations, and fluctuation-induced symmetry
  breaking under structured or bicircular quantum light.
- Wang 2024 adds a different mechanism: squeezed vacuum can act as the quantum
  environment of a selected emitted harmonic mode, changing harmonic amplitude
  through vacuum-fluctuation control rather than through pump-shot statistics.
- Lyu 2025 shows that BSV photon statistics can transfer to ATI electron
  statistics. This is valuable but should be described as electron/yield
  statistics unless a quantum non-Gaussian electron or optical output witness is
  specified.
- A pure intensity-spectrum calculation can motivate where nonlinear gain is
  largest, but it cannot certify non-Gaussian emitted light.
- A stronger claim would be: "BSV-driven HHG creates mode-selective
  non-Gaussian harmonic states due to pump-output entanglement and nonlinear
  conditioning." This requires an output-state model or a measurement witness.

## THz Novelty Hypotheses

- In optical rectification, use the `chi^(2)` source as a frequency-conversion
  analogue. If THz generation depletes or measures the squeezed pump, the THz
  mode or residual pump may acquire non-Gaussian features.
- In plasma THz emission, ionization gating is a nonlinear measurement-like
  process. Conditional THz waveforms binned by ionization history or BSV
  amplitude may expose non-Gaussian output statistics.
- Wang 2026 predicts thermal-like THz states for coherent-plus-BSV plasma THz.
  A high-impact extension would ask when the THz state is not merely thermal
  or Gaussian but has nonzero higher cumulants or a non-Gaussian witness.

## Simulation Implications

1. Start with stochastic classical outputs to identify candidate modes and
   conditional bins.
2. Add Gaussian quantum diagnostics: covariance matrix, squeezing, purity proxy,
   and mode decomposition.
3. Only claim non-Gaussian quantum output after adding a higher-cumulant,
   witness, or phase-space reconstruction layer.
4. Track pump depletion/backaction explicitly whenever possible; a frozen pump
   approximation can erase the mechanism that creates non-Gaussianity.

## Caution

The current stochastic electrodynamics framing can reproduce selected Gaussian
and normally ordered diagnostics, but Wigner-negative output states cannot be
represented by a positive classical stochastic ensemble alone. The paper can use
classical stochastic simulations as a discovery and baseline tool, while
separating any quantum non-Gaussian output claims into a higher-level model or
measurement proposal.
