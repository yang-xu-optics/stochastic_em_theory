---
title: Riek Et Al 2017 Subcycle Quantum Electrodynamics
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, experiment, electro-optic-sampling, optical-rectification, squeezed-vacuum, mid-infrared, chi2]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../models/thz-optical-rectification-model
  - ../sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum
  - ../sources/kizmann-2019-subcycle-squeezing-time-flow-perspective
---

# Riek Et Al 2017 Subcycle Quantum Electrodynamics

## Bibliographic Metadata

- Authors: C. Riek, P. Sulzer, M. Seeger, A. S. Moskalenko, G. Burkard,
  D. V. Seletskiy, A. Leitenstorfer (University of Konstanz).
- Year: 2017 (manuscript file dated 2016).
- Identifier: arXiv:1611.06773v1 (id from the ingest request; the PDF has no
  arXiv stamp). Journal version: Nature 541, 376-379 (2017), as cited in
  ref. 10 of Kizmann 2019; not printed in this PDF.
- DOI: not printed in the PDF.
- Raw source:
  [Riek et al. - 2017 - Subcycle quantum electrodynamics.pdf](<../../raw/sources/Riek et al. - 2017 - Subcycle quantum electrodynamics.pdf>)
- Extracted text:
  [riek-2017-subcycle-quantum-electrodynamics.txt](<../../results/literature/ingest-2026-11-14/extracted_text/riek-2017-subcycle-quantum-electrodynamics.txt>)
- Ingest date: 2026-11-14.

## Core Result

Experiment with a model-based interpretation. A 12 fs near-infrared pump in a
16 um GaSe crystal produces, by optical rectification (OR), a mid-infrared
transient with fixed carrier-envelope phase and mean frequency 44 THz. In the
same crystal this coherent transient squeezes the co-propagating mid-infrared
vacuum through the electro-optic effect: two successive `chi^(2)` steps.
Electro-optic sampling (EOS) with a 5.8 fs probe in AgGaS2 records the
coherent field and the rms noise at each delay relative to bare vacuum (RDN).
At 3.5 nJ pump energy the RDN extrema are about -0.9e-2 and +2.2e-2 (read
from Fig. 4); -0.04 would mean complete removal of the sampled vacuum noise.

## Useful Equations Or Model Ingredients

Notation: `DE` rms field amplitude (V/cm); `qE` fluctuation operator
`delta E_THz`; `E_THz` classical OR transient; `(M)` unnumbered Methods line.

```text
(1)  DE_rms(t) = exp[f(t)] DE_vac,   f(t) = (d l / (n c)) dE_THz(t)/dt
(2)  DE_rms(t_min) DE_rms(t_max) = DE_vac^2 = hbar / (eps0 Dx Dy Dz Dt)
     Dx Dy = pi w_probe^2;  Dz Dt set by the probe intensity envelope
(3)  RDN(t_D) = [sqrt(DE_SN^2 + DE_rms(t_D)^2) - sqrt(DE_SN^2 + DE_vac^2)]
                / sqrt(DE_SN^2 + DE_vac^2)
             ~ [DE_rms(t_D) - DE_vac] DE_vac / DE_SN^2
(M)  P^(2) = -eps0 d E_tot E_tot,   E_tot = E_THz + qE          [C/m^2]
(4)  d qE(z, W)/dz = -i (W d / (n c)) int dW' E_THz^*(z, W' - W) qE(z, W')
(5)  d qE'/dz' = (d / (n c)) [(dE'_THz/dt') qE' + E'_THz dqE'/dt']
(6)  qE_out(t) = exp[f(t)] qE_in(t - n l / c)
(9)  f(t) = -(l / c) dn/dt,   Dn = r n^3 E_THz,   r = -d / n^4
```

- The OR step is described in words only (Methods): difference-frequency
  mixing within the pump spectrum, with the same carrier-envelope phase for
  every pulse. The paper states that `E_THz` is proportional to pump energy.
- Eq. (6) follows from Eq. (5) with its second term dropped. Only terms linear
  in `qE` are kept; the correction to the classical field is omitted.
- Noise maxima sit at the most negative slope of `E_THz(t_D)`, minima near the
  most positive slope (Fig. 2). The RDN is nearly symmetric at 0.8 and 1.5 nJ
  and skewed towards excess noise at 2.5 and 3.5 nJ (Fig. 3).
- Statistics: the probe train acts as two interleaved sub-trains, one with the
  pump present, one sampling bare vacuum. Both are read at once in two
  orthogonal lock-in channels; their rms noise levels are subtracted (Eq. 3).

| Quantity | Value | Status |
| --- | --- | --- |
| Pump | 12 fs, centre 200 THz, 0.8 to 3.5 nJ, spot radius 3.6 um | set |
| Generation crystal; filter | GaSe, 16 um, uncoated; GaSb, 70 um, Brewster's angle | set |
| Probe; detection crystal | 5.8 fs, spot radius 3.6 um; AgGaS2, 24 um, uncoated | set |
| Coherent transient | mean 44 THz (6.8 um); peak about 1 kV/cm at 3.5 nJ (read from Fig. 2a) | measured |
| Repetition rate | probe 40 MHz; pump 20 MHz (every second pulse removed) | set |
| Readout | field: lock-in at 20 MHz; noise: two channels locked to 10 MHz | set |
| Pump-probe timing jitter | 1 as | cited (ref. 32) |
| `DE_vac`; `DE_SN` | 24 V/cm; 81 V/cm | computed by authors |
| Vacuum share of total rms | 4 %, so full removal gives RDN = -0.04 | computed |
| Squeezing inside crystal | `1 - exp f(t_min)` close to 50 % at 3.5 nJ | fit of Eq. (2) |

## Assumptions

- Model (Eqs. 1, 4-9): plane waves and a single transverse mode, justified by
  crystal thicknesses below the mid-infrared Rayleigh range.
- Dispersionless `n` and `chi^(2)`; negligible pump depletion; bare vacuum or
  fully coherent input.
- `E'_THz dqE'/dt'` in Eq. (5) dropped: moderate deviation from vacuum, or
  small `E_THz`. Technical noise taken as negligible.

## Limitations And Cautions

- The number of pulses per data point, the integration time and the lock-in
  bandwidth are not stated. No measured field histogram is shown (Fig. 1b is
  a sketch); only second moments are compared.
- Eq. (1) is offered as a qualitative explanation. Kizmann 2019 notes that it
  holds for weak squeezing or selected times and ignores the probe duration.
- `DE_vac` and `DE_SN` are computed from ref. 15 (Riek et al., Science 350,
  420, 2015), not in `raw/sources/`. Probe photons per pulse are not given.
- Reflections at uncoated crystal faces and imperfect mode matching admix
  vacuum; the 50 % figure refers to the field inside the crystal.
- With `f` proportional to `+d dE_THz/dt` and excess noise at negative slope,
  `d` is negative in the authors' convention (ingest reading).

## Relevance To This Project

- Closest experimental precedent for the measurement proposed in
  [[../project-status-review]]: OR in a thin `chi^(2)` crystal gives a
  phase-stable transient that EOS reads with shot-noise-limited statistics.
  The pump here is coherent, not bright squeezed vacuum.
- Field scales: the OR transient reaches about 1 kV/cm from 3.5 nJ; the noise
  per sample is `sqrt(81^2 + 24^2)`, about 84 V/cm (ingest arithmetic).
  Project inference: fluctuations of order 100 % of such a field exceed the
  floor roughly twelvefold; 10 % fluctuations (100 V/cm) are comparable to it.
- `E_THz` proportional to pump energy supports "single-shot THz amplitude
  proportional to pump photon number" at the classical level only.
- Caution for the claim: the OR field also rescales the THz vacuum noise by
  `exp[f(t)]`; with a fluctuating pump, `f` would vary from shot to shot. Not
  covered by [[../models/thz-optical-rectification-model]].
- Interleaved pump-on and pump-off sampling is a template for calibrating a
  THz histogram against vacuum and shot noise. Detection operator:
  [[../sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum]].
