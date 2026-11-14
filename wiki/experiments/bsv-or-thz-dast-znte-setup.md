---
title: BSV Optical Rectification THz Setup (DAST, ZnTe)
type: synthesis
status: draft
created: 2026-11-14
updated: 2026-11-14
tags: [experiment, bsv, thz, optical-rectification, dast, znte, electro-optic-sampling]
source_count: 4
confidence: low
related:
  - ../prl-restructuring-plan
  - ../theory/quantum-optical-rectification-of-bsv
  - ../simulations/bsv-optical-rectification-thz-statistics
  - ../sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum
  - ../sources/riek-2017-subcycle-quantum-electrodynamics
  - ../sources/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light
  - ../sources/racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes
---

# BSV Optical Rectification THz Setup (DAST, ZnTe)

The author's source and detection, as stated on 2026-11-14, and what the
theory predicts for them. The parameters are stated values, not records in
`raw/data/`; replace them with measured ones as they become available.
Confidence is low because several numbers below rest on assumptions that are
marked as such.

## Stated Parameters

| Quantity | Value | Status |
| --- | --- | --- |
| BSV centre wavelength | 1600 nm | stated |
| Pulse energy | about 3 microjoules | stated |
| Pulse duration | about 100 fs, possibly shorter | stated |
| Repetition rate | 1 kHz | stated |
| `g2` | about 1.2, source not filtered | stated; confirmed by the author on 2026-11-14 to be the full-beam value |
| THz generation crystal | DAST | stated; thickness not given |
| Sampling crystal | ZnTe | stated; thickness not given |
| Probe | 800 nm, 100 fs | stated |
| Single-shot acquisition | being built | stated |

## Derived Quantities

Representation: bright limit of the quantum model in
[[../theory/quantum-optical-rectification-of-bsv]]; ordering corrections are
dropped and their size is given.

```text
photons per pulse        N = 3e-6 J / (h c / 1.6e-6 m) = 2.4e13
mode number              K = 2 / (g2 - 1) = 10      (degenerate BSV, equal modes)
Gamma shape              a = 1 / (g2 - 1) = 5       (pulse-energy distribution)
photons per mode         2.4e12
ordering corrections     1 / nbar = 4e-13           (negligible)
envelope overlap |c|^2   0.93, 0.75, 0.53 at 1, 2, 3 THz   (100 fs Gaussian)
```

The stated `g2` is the full-beam value (confirmed by the author), so it is
the pulse-energy statistic that matters here: a THz field measured at a focus
is the coherent sum over the emitting area, follows the total pulse energy,
and counts spatial as well as temporal modes. `K = 10` therefore applies at
the crystal, provided the whole beam reaches it. Remaining assumption: the
modes are taken as equal; unequal weights change the higher cumulants (see
below) but not the 45 % fluctuation.

The ZnTe band with a 100 fs probe ends near 3 THz, where the overlap is still
above one half. The detected THz therefore integrates the intensity over the
pulse, and the single-shot field is close to "pulse energy times a fixed
waveform". Shape fluctuations from structure inside the pulse grow toward the
upper band edge and need the multimode calculation listed in the plan.

## Predicted Single-Shot Statistics

For ten equal bright modes. `W` is the THz field at the waveform peak divided
by its mean.

| Quantity | Value |
| --- | --- |
| Sign of the THz field | the same in every shot |
| Mean waveform | that of a coherent pump with the same mean envelope |
| Relative field fluctuation, `sqrt(g2 - 1)` | 0.45 |
| Distribution of `W` | Gamma, shape 5: median 0.93, mode 0.80 |
| Shots with `W < 0.5`; `W > 1.5`; `W > 2`; `W > 3` | 10.9 %; 13.2 %; 2.9 %; 0.09 % |
| Field skewness; excess kurtosis | 0.89; 1.2 |
| Mean THz energy / coherent pump of equal mean energy | 1.2 |
| THz energy fluctuation ratio `<U^2> / <U>^2` | 1.87 |

Things to note.

- These are not the single-mode numbers (3, 35/3, chi-squared). With an
  unfiltered source the effect is a 45 % amplitude fluctuation with a
  moderately skewed, strictly one-sided distribution.
- A Gaussian with the same mean and width would put 1.3 % of shots below
  zero. One-sidedness and skewness are the testable differences.
- The variance fixes only `K`. The third and fourth cumulants depend on how
  the mode weights are distributed: for geometric weights with the same
  `K = 10` the skewness is 1.19 and the excess kurtosis 2.38. In the bright
  limit `k_j / k_1^j = (j - 1)! 2^(j-1) sum_k w_k^j`, with `w_k` the
  normalized Schmidt weights, so the cumulants of the THz field measure the
  power sums of the Schmidt spectrum.
- Skewness of 0.89 is detected at five standard deviations with about 200
  shots when the single-shot signal-to-noise ratio is high, 1,500 when the
  detection noise equals the signal fluctuation.
- Single-mode statistics need filtering or post-selection of single-peak
  shots from per-shot spectra; see [[../prl-restructuring-plan]].

## Feasibility Estimate

Order of magnitude only. The conversion efficiency is an assumption, not a
value from an ingested source or a measurement.

```text
assumed energy efficiency      1e-4 to 1e-3      ->  THz energy 0.3 to 3 nJ
THz photons / pump photons     0.9 % to 9 %      (at 2 THz)
ZnTe retardation               0.073 rad per kV/cm per mm at 800 nm
                               (n = 2.85, r41 = 4 pm/V; before Fresnel loss)
```

A nanojoule of THz focused to a few hundred micrometres is of order 10 kV/cm.
With 1 mm of ZnTe that is a retardation of several tenths of a radian, far
above single-shot balanced-detection noise. Two consequences: single-shot
histograms should be directly measurable, and the detection must be kept
linear up to about three times the mean field, because linearity in the pump
energy is the thing being tested. Use thin ZnTe or attenuate the THz beam so
that the retardation at three times the mean stays below about 0.2 rad, and
verify linearity with the coherent laser.

Measurement strength of the solvable model, for the same assumed THz
energies: `B N` between 0.008 and 0.08, and an ideal photon-number resolution
`1 / sqrt(B)` between 4 and 11 times the pump shot noise. No detection scheme
here reaches that; it says how far the first-order description is from the
regime where back-action matters.

## Measurement Programme For A High-Impact Experimental Paper

Asked by the author on 2026-11-14 with Nature Photonics in mind. Honest
position: that journal is a long shot for this physics, because the
description is classical and the energy statistics are known for harmonics.
The measurements below are the ones that give it a chance; the same data set
supports Optica or Physical Review Letters. Predicted values are bright-limit
results of [[../theory/quantum-optical-rectification-of-bsv]] for equal
modes; `K` is the pump mode number.

Core: the demonstration.

1. Averaged THz waveform from the BSV pump, with the usual controls. Shows a
   fixed-polarity transient from zero-mean light. Needs no single-shot system.
2. Single-shot field at the waveform peak against shot energy from a pickoff.
   Prediction: a straight line through the origin, one sign.
3. Field histogram and cumulants. Prediction for `K = 10`: Gamma shape 5,
   fluctuation 45 %, skewness 0.89; mode number from the THz cumulants equal
   to `2 / (g2 - 1)` from the pump.

What only a field measurement can show.

4. Noise against delay across the waveform. For pure photon-number noise the
   rms follows the mean field, `rms(t) = sqrt(g2 - 1) |<E(t)>|`, and vanishes
   at the zero crossings. Timing jitter of the BSV bursts inside the pump
   envelope adds a term proportional to the slope, `<E'(t)> delta_t`, which is
   largest at the zero crossings: 25 fs of jitter gives 0.31 of the peak field
   at 2 THz, 0.16 at 1 THz. The map separates the two, and the node noise
   measures the arrival-time fluctuation of the quantum light. With a
   single-shot signal-to-noise ratio of 30 the timing resolution per shot is
   about 3 fs at 2 THz.

Control of the statistics.

5. Mode-number scan by spatial filtering, then spectral filtering or
   post-selection on per-shot spectra. Prediction, pump `g2` to THz:

```text
K     pump g2   field fluctuation   THz energy / coherent   <U^2>/<U>^2
10    1.2       0.45                1.2                     1.87
2     2.0       1.00                2.0                     6.0
1     3.0       1.41                3.0                     11.67
```

   Budget: one mode of ten carries a few tenths of a microjoule; the THz
   field falls in proportion and should stay above single-shot noise
   (estimate). Tail shots matter: for `K = 1`, 2.5 % of shots exceed five
   times the mean energy and 0.16 % exceed ten times, so DAST and the ZnTe
   sampling must stay linear that far.
6. Squeezed against thermal statistics from the same source: tune the
   down-conversion off degeneracy and keep one beam. Prediction at the same
   `K`: field fluctuation `sqrt(1/K)` instead of `sqrt(2/K)` (0.32 against
   0.45 for `K = 10`; 1.00 against 1.41 for one mode); energy ratio 6 instead
   of 11.67 for one mode. The difference is the phase-sensitive term (6b) of
   the theory page, the one contribution specific to squeezed vacuum.

Tests of the description.

7. Classical emulator, if a coherent 1.6 micrometre pulse is available (a
   seeded parametric amplifier): impose a programmed random attenuation shot
   by shot with the Gamma distribution of step 3 and repeat steps 2 to 4.
   Prediction: indistinguishable from BSV within error.
8. Twin beams: off degeneracy, send the signal to DAST and record the idler
   energy. Prediction: the THz field is linear in the idler energy, so
   selecting idler energies in a narrow window gives THz pulses of known
   amplitude from a beam that never reached the crystal. The correlation
   demonstrated this way is far above shot noise and is reproducible by
   classically correlated beams; say so.

Use.

9. One measurement that uses the source: sort shots by amplitude to obtain
   the field dependence of a THz response from a single run, starting with
   the sampling nonlinearity itself, or a time-domain spectrum taken with the
   averaged waveform.

Not practical with a 100 fs probe: the spontaneous term, any sub-shot-noise
correlation, and the change of statistics with THz frequency, which needs a
detection band well beyond 3 THz.

## Open Items

- A shot-energy histogram of the BSV, to check the Gamma shape directly and
  to see whether the mode weights are far from equal.
- Whether the source is degenerate and collinear; the spectrum; an estimate
  of the spatial mode number.
- DAST and ZnTe thicknesses; pump spot size on DAST; THz collection optics.
- Measured THz energy or field with the coherent laser at 3 microjoules.
- DAST dispersion and absorption data for the crystal response, and the ZnTe
  response for a 100 fs probe. Not in `raw/sources/` yet.
