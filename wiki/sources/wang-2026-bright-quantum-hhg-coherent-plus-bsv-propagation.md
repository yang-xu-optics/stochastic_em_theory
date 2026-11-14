---
title: Wang Et Al 2026 Bright Quantum HHG Driven By Coherent Plus BSV Light
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, hhg, bsv, two-color, propagation, phase-matching, husimi-q, experiment]
source_count: 1
confidence: medium
related:
  - ../project-status-review
  - ../models/hhg-gas-model
  - ../theory/bsv-even-order-response-moment-scaling
  - ../theory/stochastic-quantum-optics-correspondence
  - even-tzur-2025-attosecond-quantum-fluctuations
  - rivera-dean-2025-propagation-of-intense-squeezed-vacuum-light-in-non
  - wang-2026-quantum-thz-plasma-bsv
---

# Wang Et Al 2026 Bright Quantum HHG Driven By Coherent Plus BSV Light

## Bibliographic Metadata

- Authors: Wentao Wang, Yaoshun Sun, Liyuan Wang, Lingrui Hu, Dajun Ding,
  Xiangyu Tang, Mingxuan Li, Jianmin Yuan, Sizuo Luo (Jilin University).
- Year: 2026. Identifier: arXiv:2607.20941v1 [quant-ph], 23 Jul 2026. No
  journal reference or DOI in the PDF.
- Not the same paper as [[wang-2026-quantum-thz-plasma-bsv]] (Yi-Ben Wang,
  Zhuang-Wei Ding, Marcelo F. Ciappina, Xue-Bin Bian; Phys. Rev. A 113,
  L021501). The two author lists share no author.
- Raw source: [Wang et al. - 2026 - Generation of bright quantum high-order harmonic driven by combined coherent and bright squeezed vacuum light.pdf](<../../raw/sources/Wang et al. - 2026 - Generation of bright quantum high-order harmonic driven by combined coherent and bright squeezed vacuum light.pdf>)
- Extracted text:
  [wang-2026-bright-quantum-hhg-coherent-plus-bsv-propagation.txt](<../../results/literature/ingest-2026-11-14/extracted_text/wang-2026-bright-quantum-hhg-coherent-plus-bsv-propagation.txt>)
- Ingest date: 2026-11-14. The supplement (SI) is not in `raw/`; not read.

## Core Result

Experiment plus simulation of high harmonic generation (HHG) in krypton
driven by a strong coherent 800 nm field and a weak 1600 nm bright squeezed
vacuum (BSV). The BSV adds half-integer harmonics (one BSV photon absorbed or
emitted) and even harmonics (two BSV photons) to the odd harmonics. The yield
of each family peaks at a different gas pressure (measured, Fig. 2). A
propagation simulation reproduces this and attributes it to a BSV-induced
shift of the action phase of each sub-cycle burst. Simulated, not measured,
shot-to-shot statistics give `g2(0)` near 1.1 for odd, near 2 for
half-integer, and above 4 for even harmonics (Fig. 5).

## Useful Equations Or Model Ingredients

```text
Delta k = Delta k_geo + Delta k_dis + Delta k_ele + Delta k_dip        (1)
Delta k_dip = grad phi_act,   phi_act = phi_coh + sigma
Delta k = Delta k_coh + grad sigma                                     (2)
p_opt = p_coh + Delta p
Delta p * omega_h / (2 eps0 c k_B T)
   * [(1 - eta)(alpha_1 - alpha_q) - eta e^2 / (m_e omega_1^2)]
   = -grad sigma                                                       (3)
Q(alpha) = <alpha| rho |alpha> / pi                 Husimi, Methods
g2(0) = <I^2> / <I>^2                               harmonic intensity
```

SI units, implied by `eps0` and `k_B`: mismatch in rad/m, `p` in Pa,
`omega_h` (harmonic) and `omega_1` (driver) in rad/s, polarizabilities
`alpha_1`, `alpha_q` in C m^2/V, ionization degree `eta` dimensionless.
`sigma` is the BSV-induced part of the action phase; it oscillates with the
relative phase of the two fields and scales with the 1600 nm amplitude
(p. 6; Fig. S5 of the SI, not seen). The four bursts per two cycles of the
800 nm field obey `sigma_3 = -sigma_1`, `sigma_4 = -sigma_2` (p. 7).

Model chain (Methods): one shot is one classical waveform. The 800 nm field
is noiseless; the BSV is an ensemble of 1,000 coherent fields drawn from the
Husimi distribution. For each shot a one-dimensional time-dependent
Schrodinger equation (TDSE), accelerated by machine learning, gives the
polarization, which enters a Maxwell propagation equation with dispersion,
absorption, and phase modulation of the driver by neutrals and plasma.

| Parameter | Value | Where |
| --- | --- | --- |
| Laser and coherent arm | Ti:sapphire, 800 nm, 35 fs, 1 kHz, split 50:50; 1.7e14 W/cm^2; waist 100 um (simulation) | Fig. 1, Methods |
| BSV generation | double pass, 3 mm type-I BBO, cut 19.8 deg | Methods |
| BSV on target | 1600 nm after bandpass; 0.18 uJ (about 1.5e12 photons); 2e11 W/cm^2; waist 25 um (simulation) | Methods, Fig. 1 |
| BSV statistics | measured `g2 = 2.324`; coherent laser 1.003; "single-spatial-mode" | Fig. 1b, p. 3 |
| Target and range | Kr, 3 mm cell, 5 to 60 Torr; entrance 3.5 mm before focus (simulation); H14.5 to H27, about 22.5 to 42 eV | Fig. 2, Methods, p. 4 |

| Harmonic family | BSV photons | Optimum pressure, measured | Optimum, simulated | Simulated `g2(0)` near phase matching |
| --- | --- | --- | --- | --- |
| odd, H(2N+1) | 0 | 20 to 24 Torr | not quoted | about 1.1 |
| H(2N+1/2) | 1 | 27 Torr (H20.5) | about 30 Torr | about 2 |
| H(2N+3/2) | 1 | 13 Torr (H21.5) | lower than H(2N+1/2) | about 2 |
| even, H(2N) | 2 | 30 to 44 Torr | about 40 Torr | above 4 |

## Assumptions

- Each BSV shot has a definite waveform (ref. 46), so coherent-field HHG
  theory applies shot by shot and observables are ensemble averages.
- The BSV is perturbative: the odd harmonics show nearly the same pressure
  dependence with and without it (Fig. S2 of the SI, not seen), so the
  ionization degree and the dispersion terms are taken as unchanged.
- One-dimensional TDSE; fundamental Gaussian spatial modes for both fields.

## Limitations And Cautions

- Harmonic `g2` and photon statistics come from 1,000 simulated shots. No
  harmonic statistics were measured, and no error bars are given.
- The paper calls the output "quantum" because driver fluctuations transfer
  to it. No nonclassicality test is made; the model output is a classical
  mixture over sampled fields.
- The temporal mode number of the BSV is not given. The measured `g2 = 2.324`
  is below the single-mode value 3. Whether the 1,000 Husimi samples
  reproduce it is not stated in the main text (Fig. S3 of the SI, not seen).
- `g2` depends on pressure where a harmonic is phase-mismatched: odd
  harmonics dip between 40 and 50 Torr, and H23.5 rises to about 8 near
  35 Torr (Fig. 5h, read by eye). Propagation alters the statistics.

## Relevance To This Project

- Same method as this project, a Husimi ensemble of classical fields driving
  a TDSE ([[../models/hhg-gas-model]]), plus the propagation step it lacks.
- It illustrates the parity rule of
  [[../theory/bsv-even-order-response-moment-scaling]]. Shots with BSV phase
  0 and pi shift the optimum pressure of a burst in opposite directions, and
  the ensemble average looks like the coherent case (Fig. 4c). Even harmonics
  are second order in the BSV field and have the largest simulated `g2`.
- Caution for the optical-rectification claim: moment ratios such as 35/3
  assume a local response. Here phase mismatch changes the output `g2`, so a
  thick-crystal THz prediction needs a propagation model first.
- The same two-colour scheme at the single-atom level is in
  [[even-tzur-2025-attosecond-quantum-fluctuations]] (the paper's ref. 40);
  ionization loss of BSV in gas is in
  [[rivera-dean-2025-propagation-of-intense-squeezed-vacuum-light-in-non]].
