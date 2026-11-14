---
title: De-la-Pena Et Al 2026 High-Order Correlations And Wigner Negativities
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, hhg, bsv, two-level-system, qed, wigner-negativity, back-action]
source_count: 1
confidence: medium
related:
  - ../project-status-review
  - ../theory/non-gaussian-output-novelty
  - ../theory/stochastic-quantum-optics-correspondence
  - even-tzur-cohen-2024-motion-charged-particles-bsv
  - gothelf-2026-limitations-of-approximative-phase-space-description
  - gorlach-2023-hhg-driven-by-quantum-light-main-article
---

# De-la-Pena Et Al 2026 High-Order Correlations And Wigner Negativities

## Bibliographic Metadata

- Authors: S. de-la-Pena, H. Appel, M. F. Ciappina, O. Neufeld, A. Rubio.
- Year: 2026. Identifier: arXiv:2609.20559v1 [physics.optics], 17 Sep 2026.
  Preprint; no journal reference or DOI in the PDF.
- Raw source: [de-la-Pena et al. - 2026 - High-order correlations and ultrafast Wigner negativities in bright-squeezed-vacuum-driven high-harmonic generation.pdf](<../../raw/sources/de-la-Pena et al. - 2026 - High-order correlations and ultrafast Wigner negativities in bright-squeezed-vacuum-driven high-harmonic generation.pdf>)
- Extracted text: [de-la-pena-2026-high-order-correlations-and-wigner-negativities-bsv-hhg.txt](<../../results/literature/ingest-2026-11-14/extracted_text/de-la-pena-2026-high-order-correlations-and-wigner-negativities-bsv-hhg.txt>)
- Ingest date: 2026-11-14.

## Core Result

State-vector propagation of a two-level system (TLS) coupled to one quantized
driver mode in squeezed vacuum `S(xi)|0>` and to a discretized continuum of
emission modes in vacuum, in a squeezed picture that moves `xi` into `H`.

- In the joint limit `dw -> 0`, `|xi| -> inf`, the driver coupling depends
  only on `Omega_R = kappa e^{|xi|}` (Eq. 5).
- BSV-driven spectra lack the Floquet oscillations of coherent driving and
  show a stronger cutoff dependence on `Omega_R` (Fig. 2; `Delta/w_L = 1, 5`).
- Second- and third-order correlation maps of the emission modes are shown
  for `Omega_R/w_L = 2`, three-cycle pulses (Figs. 3, 4, S4). They are
  unnormalized: the paper reports no `g2` or `g3` value.
- Back-action is quantified by the Wigner function of the reduced driver
  state and its negativity volume (Eq. 10), which grows from 0 to about 1.3
  within four cycles, with local maxima every half cycle (Figs. 5-7).
- App. E: semiclassical ensembles (Wigner or Husimi sampling, with or without
  mean-field back-action) give one excited-state population `p_e(t)`, which
  coincides with the QED curve (Figs. S2, S3; `Omega_R/w_L = 3`).

## Useful Equations Or Model Ingredients

Representation: full state vector in a Fock basis (squeezed-Fock for the
driver); Wigner function of the reduced driver state; Wigner- and
Husimi-sampled classical fields for comparison. Interaction picture;
frequencies in units of `w_L`; `g` dimensionless; units of `S`, `C` not stated.

```text
H_QED = H_TLS + H_driv + H_cont,   H_TLS = (1 - sigma_z) Delta              (1)
H_driv = sigma_x lambda sqrt(w_L/2) [a_L e^{-i w_L t} + h.c.]               (2)
H_cont = sigma_x sum_{eta in D} lambda sqrt(w_eta/2)
         [a_eta e^{-i w_eta t} + h.c.],   w_eta = eta w_L                   (3)
lambda = g sqrt(dw),  g = 2 mu sqrt(alpha_fs/A_eff) ~ 5e-4
```

Squeezed picture `|Psi_s> = S^dag(xi)|Psi>`, `kappa = lambda sqrt(w_L/2)`:

```text
H_driv_s = kappa sigma_x [(a_L cosh|xi| - e^{i phi} a_L^dag sinh|xi|)
           e^{-i w_L t} + h.c.]                                             (4)
  -> (Omega_R/2) sigma_x [(a_L - e^{i phi} a_L^dag) e^{-i w_L t} + h.c.]    (5)
Omega_R = 2 kappa sqrt(<a_L^dag a_L>) = 2 kappa sinh|xi| -> kappa e^{|xi|} (B3,B5)
```

Observables and the semiclassical reference (`kappa -> 0`, field fixed):

```text
dS/dw = w_eta <a_eta^dag a_eta>/dw                                          (6)
C2(w1,w2) ~ <a1^dag a2^dag a1 a2>/dw^2                                      (7)
C3(w1,w2,w3) ~ <a1^dag a2^dag a3^dag a1 a2 a3>/dw^3                         (8)
V_-(t) = - int_{W<0} W(q_L, p_L; t) dq_L dp_L                              (10)
i d|psi_j>/dt = [H_TLS + sigma_x |E_j| cos(w_L t - phi_j)] |psi_j>         (E3)
```

What "converged multimode Hilbert space" amounts to in the text:

- Multimode means the emission continuum on a grid `dw/w_L = 0.05` (0.1 in
  the check of Fig. S1), kept only in unit-width windows around the harmonics
  of interest (Apps. A, C): about 20 modes per window (our arithmetic).
- The driver is one mode; its squeezed-Fock truncation is said to depend only
  on `Omega_R`. No basis size, emission-mode photon cutoff, or time
  integrator is given.
- No finite `|xi|` is quoted. Simulations use Eq. (4). The only number is
  `kappa/w_L < 1e-7` at `Omega_R/w_L = 3` (App. E), which with
  `Omega_R = kappa e^{|xi|}` implies `|xi| > 17` (our arithmetic).

## Assumptions

- TLS emitter (minimal two-band or NV-centre model); one-dimensional
  waveguide coupling with `A_eff ~ 320 nm^2`, `mu ~ 0.053 nm`.
- One pure squeezed-vacuum driver mode, `phi = 0`; single emitter; no loss,
  no propagation; emission modes limited to harmonic windows.

## Limitations And Cautions

- Convergence evidence is one visual comparison of two mode spacings
  (Fig. S1); "converged" cannot be checked from the PDF.
- QED and semiclassical results are compared only for `p_e(t)`. The paper
  does not show that spectra or correlation maps differ from a
  classical-ensemble calculation.
- The Wigner function is shown only in the squeezed picture (`V_-` is
  invariant under the squeezing map, App. F). Pulse envelope not specified.
- Colour scales of the coherent and BSV panels of Fig. 2 differ by about seven
  orders of magnitude, without comment. `kappa` is `lambda sqrt(w_L/2)` in
  Sec. II but `lambda sqrt(w_L)` in App. E. A cited "SI" movie is not included.

## Relevance To This Project

- [[../project-status-review]] (R6) lists this as a quantum benchmark: usable
  for populations and spectra, but no `g2`/`g3` numbers or basis sizes.
- For the headline claim: Figs. S2-S3 show that in the bright limit Wigner
  and Husimi sampling coincide and reproduce the exact emitter dynamics. What
  a classical mixture misses is the driver mode itself, which becomes
  Wigner-negative; compare
  [[gothelf-2026-limitations-of-approximative-phase-space-description]].
- Project note, not a statement of the paper: Eq. (5) contains the driver
  only through `(a_L e^{-i phi/2} - h.c.) sin(w_L t - phi/2)`. This quadrature
  commutes with the limiting Hamiltonian, so emitter and emission-mode
  observables, `C2` and `C3` included, would equal those of a classical
  Gaussian-amplitude ensemble exactly; the terms dropped from Eq. (4) are
  smaller by `e^{-2|xi|} ~ 1/(4<n>)`. Verify before relying on it.
