---
title: Kern Et Al 2026 Single-Shot Pulse Retrieval Of Femtosecond BSV
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, bsv, experiment, source-design, single-shot, phase-flip, g2]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../theory/bsv-even-order-response-moment-scaling
  - ../theory/squeezed-vacuum-g2-proof-plan
  - ../models/thz-optical-rectification-model
  - gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light
  - perez-2014-spatially-single-mode-source-of-bsv
  - rasputnyi-2024-hhg-bsv
---

# Kern Et Al 2026 Single-Shot Pulse Retrieval Of Femtosecond BSV

## Bibliographic Metadata

- Authors: Yuval Kern, Ido Nisim, Michael Birk, Andrei Rasputnyi, Doron Behar,
  Zhaopin Chen, Ido Kaminer, Pavel Sidorenko, Oren Cohen, Michael Krueger.
- Year: 2026 (journal); preprint dated 22 September 2025.
- Venue: Optica 13, 395 (2026). The local PDF is the preprint
  arXiv:2509.17746v1, 5 pages, without the supplement.
- DOI: 10.1364/OPTICA.580767 (supplied with the ingest request; not printed
  in the PDF).
- Raw source: [Kern et al. - 2026 - Single-shot pulse retrieval of femtosecond bright squeezed vacuum.pdf](<../../raw/sources/Kern et al. - 2026 - Single-shot pulse retrieval of femtosecond bright squeezed vacuum.pdf>)
- Extracted text:
  [kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv.txt](<../../results/literature/ingest-2026-11-14/extracted_text/kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv.txt>)
- Ingest date: 2026-11-14.

## Core Result

Experiment. A femtosecond BSV source at 1040 nm with a single spatial mode is
built on a 1 kHz Yb laser, and the spectral amplitude and phase of individual
BSV shots are retrieved by single-shot spectral interferometry against a
characterized coherent reference pulse. For shots in the fundamental spectral
mode, the mean pulse duration is 27.2 fs FWHM with a standard deviation of
5.5 fs, far shorter than the 125 fs pump, and the group delay is consistent
from shot to shot near the centre frequency. The interferograms show directly
that the BSV field takes one of two phases, pi apart, at random per shot.

## Useful Equations Or Model Ingredients

Source parameters. All values are measured or set by the authors.

| Quantity | Value | Where |
| --- | --- | --- |
| Pump | 515 nm second harmonic of a Yb amplifier (1030 nm, 178 fs, 1 kHz); about 125 fs, 121 uJ, collimated | Sec. 2A |
| Crystals | two identical 1 mm BBO, type I, cut at 23.4 degrees, 22.8 cm apart; unseeded, collinear, degenerate | Sec. 2A |
| BSV wavelength | 1040 nm centre | Sec. 2A |
| Mean pulse energy | about 100 nJ, i.e. 5e11 photons on average; no single-shot maximum given | Sec. 2A |
| Gain | not saturated (gain curve in the supplement) | Sec. 2A |
| Spatial modes | single; the number is not quantified in the main text | Sec. 2A |
| Spectral modes | 1.62, unconditional over conditional spectral width | Sec. 2A, Fig. 2f |
| Shot classes | single-peak spectrum (fundamental mode, roughly Gaussian), double-peak (next Hermite-Gaussian mode), mixtures | Fig. 2b, c |
| `g2(0)` versus wavelength | approaches 3 at 1040 nm; about 2 away from the centre | Fig. 2e |
| Pulse duration | mean 27.2 fs FWHM, std 5.5 fs; transform limit 19.3 fs | Sec. 2C, Fig. 4b |
| Sign statistics | 105 : 95 in 200 shots, `p = 0.525 +- 0.035` | Sec. 2B, Fig. 3b |

Single spatial mode: the first crystal emits weak BSV in many spatial modes.
After 22.8 cm only the fundamental Gaussian mode still overlaps the collimated
pump in the second crystal and is amplified; the distance also sets the
pump-BSV phase for constructive gain. The design follows
[[perez-2014-spatially-single-mode-source-of-bsv]].

Shot-resolved statistics (Sec. 2A). `N(lambda)` is the single-shot spectral
intensity in arbitrary units; averages run over 4e4 shots:

```text
g2(0; lambda)  ~  <N(lambda)^2> / <N(lambda)>^2        (large-intensity form)
Cov(l1, l2)    =  <N(l1) N(l2)> - <N(l1)> <N(l2)>
```

Recorded with single-shot spectrometers: a laser-triggered silicon-based one
for `g2` and the interferograms, an InGaAs one for spectra and covariance. The
intensity histogram at 1040 nm is fitted with BSV photon statistics (Fig. 2d).

Single-shot spectral interferometry (Sec. 2B, 2C; equations only in the
supplement, which is not in `raw/sources/`). The reference is 1030 nm laser
light broadened in 4.2 cm of single-mode fibre to 960-1100 nm (45 nJ), with
its spectral phase from a commercial FROG. BSV and reference meet on a 20:80
combiner at a delay of about 3.05 ps. A Fourier transform of each
interferogram separates the DC term (BSV spectrum) from the AC term (phase
relative to the reference). 1,009 single-peak shots out of 16,000 are
reconstructed. Pi phase evidence: the normalized fringes of 200 consecutive
shots share their zero crossings and appear with either sign (Fig. 3b, c).

## Assumptions

- The reference pulse is stable from shot to shot and its FROG phase is right.
- Single-peak spectra are identified with the fundamental spectral mode.
- `g2` is a ratio of spectral intensity moments, with no ordering correction.

## Limitations And Cautions

- The duration statistics describe 6 % of the shots, post-selected for a
  single-peak spectrum. Double-peak and mixed shots are not reconstructed.
- `g2` is reported per wavelength, not for the pulse energy. With 1.62
  spectral modes the pulse-energy `g2` is expected to lie below 3 (project
  inference); the paper gives no value.
- The interferometer delay is not stabilized, which the authors name as the
  limit of the sign-statistics measurement.
- The reference spectrum is slightly narrower than the BSV spectrum. Fine
  structure in the group delay and temporal side peaks are attributed to
  errors in the FROG reconstruction of the reference.
- The retrieved pulse includes the dispersion of the path to the spectrometer.
- Only anti-squeezed (classical) properties are measured. The squeezed
  quadrature is below the dynamic range of the spectrometer.
- The supplement (gain curve, selection criteria) could not be checked.

## Relevance To This Project

- A named, published source for the planned experiment: 1040 nm, 1 kHz, about
  100 nJ (5e11 photons) mean, 27 fs, one spatial mode, 1.62 spectral modes.
  These are the inputs for [[../models/thz-optical-rectification-model]].
- Direct measurement of the shot-to-shot sign randomness behind the parity
  rule of [[../theory/bsv-even-order-response-moment-scaling]]. Optical
  rectification is even in the field and is not affected by it.
- "THz histogram equals photon-number distribution" needs the pulse-energy
  statistics, which here are not single-mode. Project inference:
  `g2 = 1 + 2/M` with `M = 1.62` gives about 2.2, near the 2.08 measured by
  [[gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light]].
- The per-shot spectrum identifies fundamental-mode shots. Recording it with
  each electro-optic trace would allow post-selection, at the cost of most of
  the data.
