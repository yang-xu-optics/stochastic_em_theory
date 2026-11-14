---
title: Spasibko Et Al 2017 Multiphoton Effects Enhanced By Photon-Number Fluctuations
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, bsv, harmonics, multiphoton, photon-statistics, experiment, prior-art]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../theory/bsv-even-order-response-moment-scaling
  - ../theory/quantum-optical-rectification-of-bsv
  - manceau-2019-indefinite-mean-pareto-photon-distribution
  - racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes
  - iskhakov-2012-super-bunched-bsv-state
---

# Spasibko Et Al 2017 Multiphoton Effects Enhanced By Photon-Number Fluctuations

## Bibliographic Metadata

- Authors: Kirill Yu. Spasibko, Denis A. Kopylov, Victor L. Krutyanskiy,
  Tatiana V. Murzina, Gerd Leuchs, Maria V. Chekhova.
- Year: 2017. Venue: Phys. Rev. Lett. 119, 223603. Read here as
  arXiv:1705.07159v1 (19 May 2017); the published version was not compared.
- DOI: 10.1103/PhysRevLett.119.223603 (from the journal reference, not the PDF).
- Raw source: [Spasibko et al. - 2017 - Multiphoton effects enhanced due to ultrafast photon-number fluctuations.pdf](<../../raw/sources/Spasibko et al. - 2017 - Multiphoton effects enhanced due to ultrafast photon-number fluctuations.pdf>)
- Extracted text:
  [spasibko-2017-multiphoton-effects-photon-number-fluctuations.txt](<../../results/literature/ingest-2026-11-14/extracted_text/spasibko-2017-multiphoton-effects-photon-number-fluctuations.txt>)
- Ingest date: 2026-11-14.

## Core Result

Experiment. Second, third, and fourth harmonics (SH, TH, FH) are generated
from bright squeezed vacuum (BSV) at 1600 nm on the surface of LiNbO3 without
phase matching. The yield at fixed pump flux scales with the pump correlation
function `g^(n)`. Against a pseudo-coherent reference (post-selected BSV) the
measured enhancements are 2.86, 13.6, and 71 for `n = 2, 3, 4` (Table I). The
harmonics are more bunched than the pump, up to `g2 = 110 +- 20` for the FH.

Every measured quantity is a photon number per pulse. The paper says nothing
about the phase, field, or first-order coherence of the harmonics, nor about
difference-frequency generation, optical rectification, or THz emission.

## Useful Equations Or Model Ingredients

```text
R^(n) ~ g^(n) F^n                                        (1)
xi^(n) = R^(n) / F^n          statistical efficiency     (2)
g^(n) = <: N^n :> / <N>^n,    <: N^n :> = <(a^dag)^n a^n>
g^(n) = 1 (coherent),  n! (thermal),  (2n - 1)!! (degenerate BSV)
g2_{n w} = <: N_{n w}^2 :> / <N_{n w}>^2                 (3)
g2_{n w} = g^(2n)_w / [g^(n)_w]^2                        (4)
```

`F` is in photons per pulse; everything else is dimensionless. Eq. (4) holds
for any pump statistics (p. 3). The last two columns below are Eq. (4)
evaluated here; the paper quotes only 6 and 184 and draws the rest as bars in
Fig. 4. "ps" is the pseudo-coherent reference.

| n | Yield ratio `A_BSV/A_ps` (Table I) | Pump ratio `g_BSV/g_ps` (Table I) | Ideal `(2n-1)!!` | `eta_max = F_nw/F` (Table I) | Harmonic `g2`, thermal pump | Harmonic `g2`, BSV pump |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 2.86 +- 0.08 | 2.94 +- 0.06 | 3 | (3.2 +- 0.3)e-7 % | 6 | 35/3 = 11.7 |
| 3 | 13.6 +- 0.8 | 14.5 +- 0.6 | 15 | (1.38 +- 0.12)e-9 % | 20 | 46.2 |
| 4 | 71 +- 6 | 63 +- 2 | 105 | (4.9 +- 0.7)e-10 % | 70 | 183.9 |

BSV against thermal statistics (wavelength scanned off degeneracy, Fig. 2):
the text states yield factors 2, 2.5, and 4 for `n = 2, 3, 4`; the ideal
ratios `(2n-1)!!/n!` are 1.5, 2.5, 4.4. Measured `g2` of the harmonics
(Hanbury Brown-Twiss coincidences, Fig. 4): only the FH value is given in
the text. Read by eye from the logarithmic axis: SH about 12 (BSV pump) and
6.5 (thermal pump); TH about 50 and 25; FH about 110 and 50.

| Source or setup parameter | Value | Where |
| --- | --- | --- |
| PDC pump and crystal | 800 nm, 1.6 ps, 5 kHz; 10 mm BBO, type-I collinear | Methods |
| BSV spectrum | 1600 nm degenerate, scan 1550 to 1650 nm; 400 nm wide unfiltered; at most 75 nm (9 THz, 80 fs) after 4f filter | Methods, p. 4 |
| Mode selection | slit to one spatial mode; 4f filter of 2.5 to 4.5 nm for `g^(n)`, 3.3 nm for yield curves | Methods, p. 2 |
| Measured pump `g^(2,3,4)` | 2.97 +- 0.06, 14.8 +- 0.6, 108 +- 9, at no more than 4 mW mean power before filtering | Methods, Fig. 6 |
| Reduced `g^(2,3,4)` | BBO tilt: down to 1.55 +- 0.05, 3.5 +- 0.2, 7.1 +- 0.5; post-selection: 1.01 +- 0.002, 1.02 +- 0.003, 1.1 +- 0.007 | Methods, Fig. 5 |
| Flux per pulse | BSV about 3e6 to 2e11 photons (mean power few nW to tens of uW); harmonics about 1e-3 to 0.3 photons | Fig. 1c axes, p. 4 |
| Target | 1 mm LiNbO3 slab, NA 0.68 lens, Rayleigh length 7 um | Methods |

## Assumptions

- Eq. (1) is taken from Mollow 1968 and Agarwal 1970 (refs. 6, 7), not
  derived: an `n`-photon signal scales as the normally ordered `n`-th moment
  of the pump. Implicit: perturbative, undepleted conversion and a response
  faster than the intensity fluctuations (p. 1).
- `g^(n) = (2n-1)!!` is quoted from refs. 21 to 23 for indistinguishable
  signal and idler; signal or idler alone is thermal. No derivation is given.
  Normal ordering is dropped because photon numbers are large.
- The coherent reference is post-selected BSV (0.6 % tap), not a laser.

## Limitations And Cautions

- No mode number is given. Single-mode statistics are approached by the slit
  plus narrowband filtering; without filtering the detection is multimode and
  `g^(n)` drops (Methods). The measured `g2 = 2.97` is the evidence. In
  Fig. 3 the harmonics come from broadband BSV while `g^(n)` is measured in
  2.5 nm, so the linear relation shown there is empirical.
- The highest `g^(n)` exist only at low power, because sum-frequency
  generation in the BBO acts as a nonlinear absorber. The FH data use
  `g^(4) = 69 +- 2`, so the FH enhancement is 71, not 105.
- The stated factor 2 for SH against thermal light does not match the ideal
  1.5; Fig. 2a read by eye (0.67 to 1.0) gives about 1.5. Not resolved here.
- The FH `g2 = 110 +- 20` is below the ideal 184. The paper calls the
  agreement good and gives no prediction for the reduced `g^(4)`.
- Harmonic photon-number distributions are not measured: at well under one
  photon per pulse only coincidences exist, and the "heavy tail" is inferred
  from `g2`. See [[manceau-2019-indefinite-mean-pareto-photon-distribution]].

## Relevance To This Project

- This is the source for the `(2n-1)!!` rule used in
  [[../theory/bsv-even-order-response-moment-scaling]]. Its field exponent
  `k` maps to `n = 2k`. The optical-rectification numbers on that page, mean
  energy factor 3 and energy `g2 = 35/3`, are the `n = 2` entries above. For
  second-harmonic generation they were measured as 2.86 +- 0.08 (Table I)
  and about 12 (Fig. 4, read by eye).
- Not covered here: field-resolved or phase-sensitive detection, a nonzero
  mean field from a zero-mean pump, and single-shot output distributions.
- Multimode behaviour: the mean yield from broadband BSV still follows the
  narrowband `g^(n)` (Fig. 3), because a fast process responds to
  fluctuations inside the pulse (p. 1), while shot-to-shot statistics need a
  single detected mode (Methods).
- Design notes: post-selection gives the coherent reference; `g^(n)` falls
  at high BSV power; a 2.5 to 4.5 nm filter at 1600 nm is 0.3 to 0.5 THz
  wide (project arithmetic), which bounds the rectified bandwidth.
