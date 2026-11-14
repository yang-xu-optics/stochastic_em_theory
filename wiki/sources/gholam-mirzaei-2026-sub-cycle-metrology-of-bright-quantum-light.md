---
title: Gholam-Mirzaei Et Al 2026 Sub-Cycle Metrology Of Bright Quantum Light
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, bsv, experiment, tiptoe, temporal-modes, phase-flip, g2]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../theory/bsv-even-order-response-moment-scaling
  - ../models/thz-optical-rectification-model
  - kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv
  - perez-2014-spatially-single-mode-source-of-bsv
---

# Gholam-Mirzaei Et Al 2026 Sub-Cycle Metrology Of Bright Quantum Light

## Bibliographic Metadata

- Authors: S. Gholam-Mirzaei and M. T. Weil (equal contribution),
  D. N. Purschke, K. M. Kowalczyk, A. Staudte, D. M. Villeneuve, P. B. Corkum,
  J. S. Lundeen, T. J. Hammond, G. Vampa.
- Year: 2026. Preprint; 33 of 55 pages are Supplementary Information (SI).
- Identifier: arXiv:2608.16027v1 (from the ingest manifest; no stamp in PDF).
- Raw source: [Gholam-Mirzaei et al. - 2026 - Sub-cycle metrology of bright quantum light.pdf](<../../raw/sources/Gholam-Mirzaei et al. - 2026 - Sub-cycle metrology of bright quantum light.pdf>)
- Extracted text:
  [gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light.txt](<../../results/literature/ingest-2026-11-14/extracted_text/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light.txt>)
- Ingest date: 2026-11-14.

## Core Result

Experiment. The field of single femtosecond BSV pulses at 1.6 micrometre is
recorded shot by shot with solid-state TIPTOE: the weak BSV perturbs the
nonlinear photoexcitation of a silicon CMOS sensor by a 16 fs coherent gate,
and a crossing angle maps delay onto position. Findings from 10,000 shots:

- A shot is not one temporal mode but one or more time-localized bursts: 52 %
  of shots have one, 41 % two, 7 % three or more (about 1.5 on average).
- Burst energies have single-mode statistics (`g2 = 2.94`); shot energies do
  not (`g2 = 2.08`), because independent bursts average.
- Each burst is phase-locked to the pump up to a sign. Adjacent bursts in one
  shot differ in phase by one of two values, pi apart, with equal probability.
- Two-time coherence functions match a superposition of time-limited
  (Whittaker-Shannon) modes instead of delocalized Schmidt modes (Fig. 4).

## Useful Equations Or Model Ingredients

Source and detection parameters. M = measured, F = from the burst fit, S = set.

| Quantity | Value | Where |
| --- | --- | --- |
| Pump and crystals | 800 nm, 50 fs, 1 kHz, about 30 uJ, 0.5 mm beam; two 2 mm uncoated BBO, type I, about 20 cm apart (S) | Methods |
| BSV carrier | 1.6 micrometre; fitted `omega_0 = 1.27 +- 0.02 rad/fs` (F) | SI p. 6 |
| Mean pulse energy | 1.5 nJ; 0.42 MW/cm^2 averaged over 1,000 shots (M) | main p. 3 |
| Photon number | order 1e10 per pulse; `<n> = 0.8e10` per burst, from 1 nJ (M) | SI p. 12, 17 |
| Energy `g2` | shots 2.08 (M); bursts 2.94 (F) | Figs. 1b, 2f |
| Bursts per shot | 5,163 / 4,097 / 740 shots with 1 / 2 / 3 or more (F) | SI p. 5 |
| Burst duration, spacing | median 17 fs intensity FWHM (10 fs expected from bandwidth); median separation 26 fs (F) | main p. 4, Figs. S5b, 2e |
| Two-time coherence | `g2(t,t)` is 3 at pulse centre, 2 in the wings, never below 2: at most two bursts overlap; `abs(g1)` width about 40 fs FWHM (M) | Fig. 4a, c |
| Burst phase difference | 4,569 values near 2.2 rad and 2.2 + pi rad; 2,241 zeros, 2,328 ones, `p1 = 0.51 +- 0.01`; seven NIST tests passed (F) | Fig. 3a, SI p. 19 |
| Gate | 16 fs; BSV about 1 % of intensity; window about 12 fs (2.25 cycles); absorption as `I^1.7`; gate `g2 = 1.01` (M) | main p. 3, Methods |

Burst fit, measured coherence functions, and the time-limited-mode model
(`t` in fs, phases in rad; left: SI equation number, or main-text page 7):

```text
1-2  Re E(t) = sum_i A_i exp[-ln2 (t - t0_i)^2 / sigma_i^2]
               * cos(omega_0 t + C t^2 + phi_i)
p.7  g1(t1,t2) = <E*(t1) E(t2)> / sqrt(<I(t1)> <I(t2)>)
     g2(t1,t2) = <I(t1) I(t2)> / (<I(t1)> <I(t2)>)          (shot averages)
15   |Psi> = exp[(beta/2) int dt1 dt2 gamma(t1,t2) a+(t1) a+(t2) - H.c.] |vac>
17   chi_n(t) = tau^(-1/2) sinc[pi (t - n tau) / tau],     tau = 2 pi / Omega
19   G1(t1,t2) = chi^dag(t1) sinh^2(P) chi(t2)
20   G2(t1,t2) = |chi^T(t1) U sinh(P) cosh(P) chi(t2)|^2
                 + G1(t1,t1) G1(t2,t2) + |G1(t1,t2)|^2
21   G1(t,t) = sum_n Gamma_n^2 |rho_n(t)|^2
29   JSA(w_s,w_i) ~ sinc(Dk L / 2) exp[-Dw^2 / (2 Omega_p^2)]
                    * sin[(Dk L + Dk_air L_air) / 2] * (phase factors)
```

`sigma_i` is the field HWHM (intensity FWHM `sqrt(2) sigma_i`); `omega_0` and
`C = -1e-5 fs^-2` are fixed. `gamma` is the joint temporal amplitude (Fourier
transform of the JSA) and `Omega` its band limit; `P` and `U` come from the
left polar decomposition of `beta_nm = beta tau gamma(n tau, m tau)`; `rho_n`
are localized "packets"; `g1`, `g2` are `G1`, `G2` normalized by `G1(t,t)`.
Inputs: `L = 2 mm`, `L_air = 19 cm`, 50 fs pump, `Omega = 0.81 rad/fs`, hence
`tau = 7.8 fs` and mode FWHM 9.4 fs; `beta = 24.15`, tuned to 1e10 photons.
Output: five packets exceed 10 % of the leading weight (Fig. S9b); mean packet
width 15.77 fs, against 17 fs measured.

## Assumptions

- The TIPTOE signal is linear in the BSV field, convolved with the gate.
- Bursts are Gaussian with one fixed carrier frequency and chirp. A burst is
  added only if it lowers the mean fit error by more than 0.5 %.
- Model: plane-wave collinear PDC, Gaussian pump, air gap as a pure phase, and
  correlation formulas that the authors say rest on the low-gain Hamiltonian.

## Limitations And Cautions

- The sign of the field from shot to shot is not measured: path jitter is
  tracked with 800 nm light, which fixes the BSV phase only modulo pi. Only
  the relative phase of bursts inside one shot is an observable here.
- No absolute field calibration. Photon numbers are retrieved intensities
  rescaled to a separately measured mean energy.
- The 12 fs gate is comparable to the burst duration. In the authors'
  simulated test 10 % of two-burst shots are classified as single-burst.
- Phase clusters sit near 2.2 and 2.2 + pi rad, not 0 and pi; unexplained.
- No spatial mode number (only "partial mode filtering" by the second
  crystal), Schmidt number, or gain-saturation check is given.
- Project note: each `g2` is a classical intensity-moment ratio (no ordering).

## Relevance To This Project

- A real two-crystal BSV source with a 50 fs pump is multimode in time. An
  optical-rectification amplitude follows the pulse energy, so here the THz
  histogram would follow Fig. 1b (`g2 = 2.08`), not the single-mode law of
  [[../theory/bsv-even-order-response-moment-scaling]]. Project inference:
  the equal-mode formula `g2 = 1 + 2/M` gives `M = 1.9`.
- Sign flips between bursts do not cancel a response even in the field; they
  reshape the envelope only where bursts overlap (project inference).
- A concrete multimode sampler for that theory page: Gaussian bursts of about
  17 fs spaced by about 26 fs, each with single-mode statistics and a random
  sign. Targets: shot `g2 = 2.08`, burst `g2 = 2.94`, `g2(t,t)` from 3 to 2.
- Energy scale: 1.5 nJ. The 100 nJ source of
  [[kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv]] is the better
  starting point. Data were taken at 1 kHz, one camera frame per shot, with a
  jitter reference: a template for single-shot electro-optic sampling.
