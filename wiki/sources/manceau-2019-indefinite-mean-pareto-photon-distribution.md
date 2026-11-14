---
title: Manceau Et Al 2019 Indefinite-Mean Pareto Photon Distribution From Amplified Quantum Noise
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, bsv, harmonics, supercontinuum, heavy-tails, photon-statistics, experiment, prior-art]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../theory/bsv-even-order-response-moment-scaling
  - ../theory/quantum-optical-rectification-of-bsv
  - spasibko-2017-multiphoton-effects-photon-number-fluctuations
  - racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes
---

# Manceau Et Al 2019 Indefinite-Mean Pareto Photon Distribution From Amplified Quantum Noise

## Bibliographic Metadata

- Authors: Mathieu Manceau, Kirill Yu. Spasibko, Gerd Leuchs, Radim Filip,
  Maria V. Chekhova.
- Year: 2019. Venue: Phys. Rev. Lett. 123, 123606. Read here as
  arXiv:1807.11784v4 (31 May 2019), which includes the supplement.
- DOI: 10.1103/PhysRevLett.123.123606 (from the journal reference, not the PDF).
- Raw source: [Manceau et al. - 2019 - Indefinite-mean Pareto photon distribution from amplified quantum noise.pdf](<../../raw/sources/Manceau et al. - 2019 - Indefinite-mean Pareto photon distribution from amplified quantum noise.pdf>)
- Extracted text:
  [manceau-2019-indefinite-mean-pareto-photon-distribution.txt](<../../results/literature/ingest-2026-11-14/extracted_text/manceau-2019-indefinite-mean-pareto-photon-distribution.txt>)
- Ingest date: 2026-11-14.

## Core Result

Experiment with a transformation-of-variables model. Single-shot photon-number
distributions are recorded for bright squeezed vacuum (BSV), for its second
and third harmonics, and for supercontinuum (SC) pumped by BSV. The harmonic
distributions are heavy-tailed but keep all moments finite. The SC
distribution is a power law `P(N) ~ N^-(1+k)` with measured `k` of 0.31,
0.49, and 0.64, all below 1, so the mean is not defined. The mechanism is an
output that depends exponentially on an already broadly distributed pump.

## Useful Equations Or Model Ingredients

```text
P_B(N_B) = exp(-N_B / (2 <N_B>)) / sqrt(2 pi <N_B> N_B)              (1)
N_{n w} = K N_w^n                                                    (2)
P_{n w}(N) = P_w((N/K)^(1/n)) / (n K^(1/n) N^(1 - 1/n))              (3)
P_{n w}(N) = [(2n-1)!!]^(1/2n) exp(-(1/2) [(2n-1)!! N/<N>]^(1/n))
             / (n sqrt(2 pi) <N>^(1/2n) N^(1 - 1/2n))                (4)
N_SC = sinh^2(kappa N_B)
P_SC(N) = exp(-arcsinh(sqrt N) / (2 kappa <N_B>))
          / sqrt(8 pi kappa <N_B> N (1 + N) arcsinh(sqrt N))         (5)
P(N) ~ N^-(1+k) for large N                                          (6)
Cbar_{n w}(N) = Erfc([(2n-1)!! N/<N>]^(1/2n) / sqrt 2)              (10)
P_{B,M}(N_B) = N_B^(M/2-1) (M / (2 <N_B>))^(M/2)
               exp(-M N_B / (2 <N_B>)) / Gamma(M/2)                 (12)
k = M / (4 kappa <N_B>)                                             (14)
```

`N` are photon numbers per pulse, `n` the harmonic order, `M` the number of
BSV modes, `kappa` in inverse photons. In Eqs. (4) and (10), `N` and `<N>`
refer to the harmonic. `Cbar` is the complementary cumulative distribution
(CCDF), Eq. (8); the SC analogue is Eq. (11). Eq. (12) with `M = 2` is the
exponential (thermal) law, so a BSV pump reaches `k < 1` at half the mean
photon number a thermal pump needs.

| Quantity | Harmonics experiment | SC experiment | Where |
| --- | --- | --- | --- |
| PDC pump and crystal | 800 nm, 1.6 ps, 5 kHz, up to 0.5 mJ; 10 mm BBO, type-I collinear | 400 nm, up to 0.2 mJ, same laser; two 3 mm BBO, type-I collinear | Supplement |
| BSV | 1600 nm; width over 35 THz; gain `G` up to 15.3 +- 0.5 | 800 nm; 80 nm wide, filtered to 10 or 3 nm; 0.2 to 48 nJ | p. 2, Fig. 1, Fig. 3 |
| Mode selection | slit and 4f monochromator, "down to a single mode" | bandpass filter, "few-mode"; `M = 5 +- 1` (10 nm), `2 +- 0.2` (3 nm) | Supplement |
| Nonlinear medium | surface of 1 mm LiNbO3, no phase matching | 5 m single-mode fused silica fibre | Supplement |
| Detection | charge-integrating visible detector, noise 270 photons/pulse | same detector after 1 nm monochromator at 770 nm; CCD for single-pulse spectra | Supplement |

- BSV photon-number histogram follows Eq. (1) (Fig. 1c); infrared detector
  linear to 1e6 photons/pulse, noise 1600 photons/pulse.
- Second- and third-harmonic histograms span about 1e2 to 1e6 photons/pulse
  (Fig. 2 axis) and match Eq. (4) convolved with Gaussian detector noise,
  with no fitting parameter (Fig. 2b,c; supplement). Single pulses exceed the
  mean by more than 200 (SH) and 650 (TH) times. No harmonic `g2` is quoted.
- SC tail exponents from CCDF fits (Table S1). Maximum likelihood gives
  `k = 0.53` for the first row (Fig. S1b); theory values carry 25 % error.

| BSV energy, bandwidth | `k` measured | `k` from Eq. (14) | `kappa <N_B>` | Truncated mean, photons/pulse |
| --- | --- | --- | --- | --- |
| 48 nJ, 10 nm | 0.49 +- 0.02 | 0.31 | 4 +- 0.5 | 1.18e4 |
| 30 nJ, 10 nm | 0.64 +- 0.02 | 0.5 | 2.5 +- 0.5 | 6.5e3 |
| 30 nJ, 3 nm | 0.31 +- 0.02 | 0.2 | 2.5 +- 0.5 | 5.6e3 |

- SC `g2(lambda, lambda')` from single-pulse spectra reaches 170 on the
  diagonal at 40 nJ (Fig. 4d); the paper calls this a lower bound that grows
  with observation time. Subtracting one photon raises the SC mean photon
  number up to 140 times (Fig. 5b).

## Assumptions

- The output photon number is a deterministic, monotonic function of the pump
  photon number in the same shot, so distributions map by change of variables.
- Eq. (1) is the envelope of the BSV photon-number distribution after
  narrowband filtering, taken from refs. 23 and 24 (p. 2).
- SC model: the blue side is Raman-free high-gain four-wave mixing (p. 3).
  `M` is inferred from `g2` of 3 pJ BSV after the fibre (supplement).

## Limitations And Cautions

- The number of recorded pulses is not stated. Histogram floors near 1e-6
  suggest about 1e6 pulses (inference from Figs. 2 and 3, not a quoted value).
- The power law holds over a finite window. The detector saturates above 1e6
  photons/pulse, and below 3e4 photons the Fig. 3e data are exponential
  (note 25). The quoted means exist only because of this truncation.
- Measured `k` exceeds the model `k` in all three rows.
- With `k < 1` the sample mean grows with sample size `s` as `s^(1/k - 1)`,
  and `g2` likewise depends on the record length (p. 4).
- Photon numbers only; no field or phase measurement.

## Relevance To This Project

- Optical rectification in the single-mode limit of
  [[../theory/bsv-even-order-response-moment-scaling]] maps onto these
  formulas: the THz field amplitude follows Eq. (1), and the THz energy
  follows Eq. (4) with `n = 2`, with CCDF `Erfc((3 U/<U>)^(1/4) / sqrt 2)`.
- The `n = 2` single-shot energy distribution was therefore already measured
  here for the second harmonic; a THz energy histogram would repeat it in
  another band. Moments are in
  [[spasibko-2017-multiphoton-effects-photon-number-fluctuations]].
- For a power-law process the mean and `g2` are not usable observables; for
  harmonics and rectification they are finite. Estimators are in
  [[racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes]].
- Detector noise and saturation set the usable window; model them the same
  way for a THz detector.
