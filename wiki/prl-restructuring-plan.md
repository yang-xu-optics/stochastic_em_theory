---
title: PRL Restructuring Plan
type: synthesis
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [plan, prl, optical-rectification, experiment, restructuring]
source_count: 16
confidence: medium
related:
  - project-status-review
  - research-agenda
  - theory/quantum-optical-rectification-of-bsv
  - theory/bsv-even-order-response-moment-scaling
  - simulations/bsv-optical-rectification-thz-statistics
  - models/thz-optical-rectification-model
  - experiments/bsv-or-thz-dast-znte-setup
---

# PRL Restructuring Plan

Decided by the author on 2026-11-14: change the headline claim, make optical
rectification (OR) of bright squeezed vacuum (BSV) the main result, add a
fully quantum description, and use the BSV source that is available for a
measurement. This page is the plan for turning that into a Physical Review
Letters submission. The linear argument is in
[paper/outline.md](../paper/outline.md).

## The Letter In One Paragraph

Optical rectification turns a zero-mean BSV pulse into a phase-stable THz
transient whose single-shot field is proportional to the pump photon number.
A fully quantum model gives this exactly: the THz field operator is a linear
filter of the pump photon-flux operator. The THz field therefore carries the
photon-number statistics of squeezed vacuum: a sign-definite, Gamma-distributed
single-shot field and a mean THz energy `1 + 2/K` times that of a coherent
pump, with `K` the number of pump modes. A classical Gaussian amplitude-noise
model reproduces all of it up to `1/<n>`. Single-shot electro-optic sampling
(EOS) on the BSV source tests it.

## Honest Assessment Of The PRL Case

For:

- No paper on THz generation with a BSV or squeezed pump was found in three
  rounds of searching (web on 2026-11-14; arXiv title and abstract queries on
  2026-11-14 for terahertz with "bright squeezed vacuum", "optical
  rectification" with squeezed or quantum light, and "difference frequency"
  with BSV). Plasma THz with BSV exists as theory only (Wang 2026).
- The subject is active and visible: BSV-driven strong-field work has
  appeared in Nature Physics, Optica, and Nature Communications since 2023.
- The result is a field, measured with its sign, not an energy. In the
  literature ingested here, emission driven by BSV is reported as energies,
  spectra, or counts; the fields that have been resolved are those of the BSV
  itself.
- The quantum model is exact and short, and it answers a live question (what
  the classical-mixture description gets right) for one process with a stated
  error bound.

Against:

- The energy statistics are the second-order case of a known rule, and they
  have been measured for the second harmonic of BSV: yield enhancement
  2.86 +- 0.08 against the ideal 3 and a harmonic `g2` near 12
  ([[sources/spasibko-2017-multiphoton-effects-photon-number-fluctuations]]),
  and single-shot energy distributions of the second and third harmonics
  ([[sources/manceau-2019-indefinite-mean-pareto-photon-distribution]]). A
  THz energy histogram alone would repeat those results in another band.
- A sign-definite THz field from optical rectification is unsurprising once
  stated, and the field of a rectified transient from a coherent pump has
  been measured at nanojoule pump energy
  ([[sources/riek-2017-subcycle-quantum-electrodynamics]]).
- A THz amplitude proportional to the pump photon number reproduces the pump
  histogram. A referee can call the experiment a pump-energy meter.
- The phase stability is not unique to rectification: by the same parity
  argument the second harmonic of BSV is phase-locked to the pump of the
  down-conversion. Electro-optic sampling is what makes the THz case
  measurable as a field.
- Nothing measured in a first experiment is nonclassical. The Letter must say
  so itself.
- Theory alone would not carry a Letter. Without the measurement the right
  venues are Physical Review A (Letter), Optica Quantum, or Physical Review
  Research.

Consequence: the measurement is on the critical path, and the Letter must
lead with what the earlier work does not contain: a field measured with its
sign from a zero-mean driver, single-shot field statistics, and an exact
quantum model with an error bound for the classical description. The factor
3 is supporting evidence, not the headline. Judged soberly, this is a
reasonable PRL attempt with the measurement and a likely rejection without
it; acceptance is not assured either way, and the fallback venues are named
below.

Two additions would raise the odds, because each turns "expected" into a
test of a contested statement:

1. A classical emulator. Drive the same crystal with the coherent laser,
   its amplitude set shot by shot to a zero-mean Gaussian random value
   (random attenuation with a random pi phase). If the THz field statistics
   of BSV and of the emulator agree within error, the Letter demonstrates
   experimentally, not only argues, that this signature of quantum-light
   driving is a classical-noise effect, with the quantum model saying how
   small the difference must be. This speaks directly to the 2026 debate on
   classical-mixture descriptions.
2. The parity rule in one data set. Record the sign of the BSV field per
   shot against a coherent reference (spectral interferometry, as in Kern
   2026) together with the THz field. Shots of opposite optical sign then
   give THz fields of the same sign.

## What Changes In The Project

| Area | Before | After |
| --- | --- | --- |
| Headline | framework reproducing squeezed-vacuum `g2`, HHG, plasma THz | OR of BSV: phase-stable THz field carrying photon-number statistics |
| Theory core | Wigner-to-normal ordering of the input | quantum input-output relation for the THz field; classical-noise limit with error bound |
| Numerics | TDSE amplitude library, Monte Carlo | closed-form statistics; crystal response; detection model |
| Evidence | reproductions of published figures | measurement on the author's BSV source |
| HHG and plasma THz | main results | companion paper; frozen until the Letter is submitted |
| ML roadmap, emitted-mode toy, ATI proxy | side branches | frozen |

## Workstreams

### A. Theory (owner: theory; about two weeks)

Done on 2026-11-14:

- Input-output relation, Wick decomposition, counting statistics, solvable
  single-mode model: [[theory/quantum-optical-rectification-of-bsv]].
- Code and tests: `code/src/stochastic_em_theory/optical_rectification.py`,
  21 tests including a Fock-space cross-check.
- First theory figure: `results/runs/20261114-bsv-or-thz-statistics/`.

To do, in order:

1. Crystal response `zeta(Omega)` and waveform `g(t)` for the crystal that
   will be used: phase matching, absorption, Fresnel losses. New module
   `or_response.py`, spec page first.
2. Detection model: EOS response function and noise, so the prediction is
   for the measured signal, equation (11) of the theory page. New module
   `eos.py`.
3. Mode structure of the real source: Schmidt modes from the measured
   spectrum and coherence, giving `c_kl(Omega)` and the predicted `K`.
   Promote the Schmidt-mode entry in `source_models.py` from metadata to a
   sampler. Add a burst sampler after Gholam-Mirzaei 2026 (time-localized
   bursts, each with single-mode statistics and a random sign) and validate
   it against their numbers: shot-energy `g2` 2.08, burst `g2` 2.94. With it,
   predict the part of the THz spectrum that comes from intensity structure
   inside the pulse, which has no counterpart for a coherent pump of the same
   duration.
4. Second order: depletion, cascading, and the Kerr-like phase at the planned
   pump energy, to state where first order holds.
5. Supplemental-material derivation written out with every assumption.
6. Independent check of the derivation by someone who did not write it. The
   theory page is this project's own algebra; it has numerical checks but no
   published counterpart.

### B. Experiment (owner: the author's laboratory; about four to six weeks)

The design is self-referenced: it does not need a coherent pulse with the
same mode as the BSV.

Per shot, record three numbers: pump pulse energy `W_j` (photodiode on a
pickoff), EOS balanced signal `s_j` at a fixed delay, and a reference (probe
energy). If a single-shot spectrometer is available, record the pump
spectrum of each shot as well. Prediction: `s_j = a W_j + noise`, with `a` fixed in sign. Shots
selected in a narrow window of `W` are the coherent reference, as in
Spasibko 2017; attenuators do not change the normalized statistics, because
linear loss leaves normalized intensity moments unchanged
([[sources/rivera-dean-2025-propagation-of-intense-squeezed-vacuum-light-in-non]],
Eq. B54).

Use a thin rectification crystal first. The statistics transfer is exact for
a local response; phase mismatch in a long medium can change the output
statistics, as simulated for harmonics in
[[sources/wang-2026-bright-quantum-hhg-coherent-plus-bsv-propagation]].

Published numbers to design against (not the author's source):

| Source | Wavelength, rate | Energy per pulse | Modes and statistics |
| --- | --- | --- | --- |
| Kern 2026 | 1040 nm, 1 kHz | about 100 nJ, 27 fs | one spatial mode, 1.62 spectral modes |
| Gholam-Mirzaei 2026 | 1.6 micrometre, 1 kHz | 1.5 nJ | 1.5 bursts per shot; shot-energy `g2` 2.08, burst `g2` 2.94 |
| Spasibko 2017 | 1.6 micrometre, 5 kHz | up to about 25 nJ (2e11 photons) | `g2` 2.97 after a 2.5 to 4.5 nm filter |
| Wang 2026 (harmonics in krypton) | 1.6 micrometre | 0.18 microjoule | measured `g2` 2.32 |

What these sources imply. None is single-mode in time: `K` is about 2, for
which the pulse-energy distribution is exponential, the same as for
single-mode thermal light. With such a source the THz field histogram would
be exponential and the energy enhancement about 2.1. The law specific to
squeezed vacuum (chi-squared with one degree of freedom, enhancement 3)
appears only at `K` near one. Two ways to get there: filter the source, or
record the spectrum of every shot and keep the single-peak shots, as Kern
2026 does (about 6 % of shots). The second gives both histograms from one
data set, all shots against selected shots, which is a strong figure.
Narrowband filtering has a cost that post-selection does not: a 2.5 to 4.5
nm filter at 1.6 micrometres leaves a spectrum 0.3 to 0.5 THz wide, so the
pulse is picoseconds long and the rectified field is confined to a few
tenths of a THz.

Detection scale from Riek 2017: a 3.5 nJ, 12 fs coherent pump in 16
micrometres of GaSe gives a transient of about 1 kV/cm, read by a 5.8 fs
probe with a per-pulse noise of about 84 V/cm (81 shot noise, 24 sampled
vacuum, as computed by those authors). That is a single-shot signal-to-noise
ratio near 12 at nanojoule energy, in a tightly focused multi-THz geometry.
A conventional few-THz setup with 100 fs pulses will be far less sensitive
per shot; step 2 below measures where the author's setup sits.

Measurements, in order, each with a go or no-go:

1. Source characterization: mean energy, shot-energy histogram, `g2`, and
   from it `K = 2 / (g2 - 1)`; spectrum; spatial mode. Go if `K` is below
   about 20, so that the field fluctuation `sqrt(2/K)` exceeds 30 %.
2. Calibration with the coherent laser attenuated to the BSV energy range:
   single-shot EOS signal-to-noise ratio as a function of pulse energy. This
   replaces any estimate from material constants, because the THz field is
   proportional to pulse energy at fixed pulse shape.
3. Averaged EOS trace with the BSV pump. Go if a waveform is seen: this is
   the phase-stability result and needs no single-shot sensitivity.
4. Shot-resolved run at the waveform peak: `s_j` against `W_j`.
   Conditional mean of `s` in bins of `W` is linear through the origin even
   when single shots are noisy.
5. Statistics: histogram of `s`, cumulants, mode-number estimates from
   skewness and kurtosis, comparison with `K` from step 1.
6. Mode-number scan with an iris or spectral filter: THz energy enhancement
   against `2/K`.
7. Controls: pump blocked; probe only; coherent pump at matched mean energy
   (enhancement should be one, histogram narrow); polarization rotated to
   switch off rectification.
8. Recommended: classical emulator run (coherent laser with shot-by-shot
   Gaussian random amplitude), same analysis as steps 4 and 5.
9. Optional: per-shot sign of the BSV field from spectral interferometry,
   recorded with the THz field.

Shots needed for the cumulant test when detection noise dominates: with
`rho` the ratio of signal fluctuation to detection noise (both rms) and `z`
the wanted significance of the third cumulant,

```text
N = 0.75 z^2 K (1 + 1/rho^2)^3
```

For `K = 5`, `z = 5`: 750 shots at `rho = 1`; about 170,000 at `rho = 0.3`.
When the signal dominates, sample moments converge slowly: for one mode the
sample energy ratio `<U^2>/<U>^2` has relative variance `97.5 / N`, so 10 %
needs about 1e4 shots and 3 % about 1e5. All moments are finite here, so
moment ratios are legitimate; also report the empirical tail function
against the predicted one and the usable detector window
([[sources/racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes]]),
with bootstrap intervals.

Data handling: raw shot records go to `raw/data/<date>-<label>/` with a
README of the acquisition settings and are never edited. Analysis runs go to
`results/runs/` with manifests, as for simulations.

### C. Positioning And Literature (about one week, then monthly)

1. Ingested on 2026-11-14: eight 2026 quantum-light papers and seven earlier
   papers the claim must be positioned against (list in [[log]] and
   [[index]]). The closest neighbours of the Letter are Spasibko 2017 and
   Manceau 2019 (energy statistics of BSV harmonics), Gholam-Mirzaei 2026 and
   Kern 2026 (the BSV field itself), Riek 2017 (field-resolved detection of a
   rectified transient and its noise), Wang 2026 (plasma THz with BSV,
   theory), and Gothelf 2026 (limits of the classical-mixture description).
2. Still to obtain by hand (publisher sites are not reachable from the
   agent environment): "Theory of high-harmonic generation with quantum
   light" (Phys. Rev. Research, doi 10.1103/y3gr-tsns); the Nature
   Communications version of the Rivera-Dean propagation paper; Tsang's
   cavity electro-optics papers; one review of THz parametric
   down-conversion; one paper on THz spectroscopy with incoherent light.
3. Scoop watch, monthly until submission: rerun the arXiv queries recorded
   in `results/literature/ingest-2026-11-14/`.

### D. Writing (about three weeks, overlapping B)

1. Figure 2 final after A1 to A3.
2. Introduction and theory sections drafted while the experiment runs.
3. Results and discussion after B5.
4. Supplemental material from the theory page and the analysis runs.
5. Cover letter built on the "for" list above, with the "against" list
   answered in the text.

### E. Repository

Done on 2026-11-14: `AGENTS.md` mission and guardrails updated;
`paper/outline.md` is the Letter and `paper/companion-outline.md` the
companion paper; OR module, tests, spec, and first run added; new sources
ingested.

To do: `or_response.py`, `eos.py`, an `analysis/` entry point for shot
records (binning, cumulants, heavy-tail estimators, bootstrap) with tests on
synthetic data before any real data arrives; move publication figures to
`results/figures/` only after the gates in `results/runs/README.md`. The
setup page exists: [[experiments/bsv-or-thz-dast-znte-setup]].

## Timeline And Gates

| Week | Theory | Experiment | Writing | Gate |
| --- | --- | --- | --- | --- |
| 1 | A1, A2 specs and code | B1 source characterization | title, abstract draft | G1: `K` and energy known; prediction numbers fixed |
| 2 | A3, A4 | B2 calibration | introduction, theory | G2: predicted single-shot signal-to-noise ratio decides the acquisition mode |
| 3 | A5 | B3 averaged trace | Figure 1, Figure 2 | G3: phase-stable THz waveform observed |
| 4 to 5 | A6, analysis code | B4, B5 | results draft | G4: linearity and statistics agree with prediction within stated uncertainty |
| 6 | | B6 to B8 | discussion, supplement | G5: internal review |
| 7 to 8 | | repeats if needed | submission | |

Fallbacks:

- G3 fails (no THz above noise): raise conversion (thicker or organic
  crystal, tighter focus, higher BSV gain) or move to an intensity-only
  measurement with a THz power detector; the paper then becomes an energy
  statistics paper and PRL is unlikely.
- G4 fails by disagreement: that is a result. Check depletion, multimode
  structure, and detector linearity first.
- Scooped on the experiment: submit theory plus data quickly to Physical
  Review A Letters or Optica Quantum.

## Source And Setup, As Stated On 2026-11-14

Recorded with derived numbers in [[experiments/bsv-or-thz-dast-znte-setup]].

| Input | Stated |
| --- | --- |
| BSV source | 1600 nm, about 3 microjoules, about 100 fs or shorter, 1 kHz |
| Mode content | `g2` about 1.2, unfiltered: `K` about 10 |
| THz generation and sampling | DAST; ZnTe with an 800 nm, 100 fs probe |
| Single-shot acquisition | being built |

What this changes in the plan:

- The realistic prediction is not the single-mode one. For `K = 10` the THz
  field fluctuates by 45 % from shot to shot with a one-sided Gamma
  distribution of shape 5 (skewness 0.89), and the mean THz energy is 1.2
  times the coherent-pump value. Gate G1 is passed: `K` is below 20.
- Signal level should not be the problem. At microjoule pump energy on DAST
  the THz field is expected to be far above single-shot detection noise
  (order-of-magnitude estimate, efficiency assumed). The care goes into
  keeping the sampling linear up to three times the mean field.
- The ZnTe band integrates over the 100 fs pulse, so the simple law "field
  equals pulse energy times a fixed waveform" should hold well below 2 THz.
- Skewness is detectable with a few hundred shots. The demanding part is the
  single-mode limit, which needs filtering or per-shot spectra.

Still needed: what the stated `g2` refers to (detector area and bandwidth);
whether the source is degenerate and collinear; crystal thicknesses and pump
spot size; a measured THz energy or field with the coherent laser.

## Option: Theory Paper First

Raised by the author on 2026-11-14 and not yet decided: publish the theory
as its own paper (Physical Review A or similar) ahead of the experimental
paper. Framing, claims, section plan, figure plan, and timing are in
[paper/theory-paper-outline.md](../paper/theory-paper-outline.md). Effects on
this plan if adopted:

- Workstream A becomes the theory paper and gains the multimode waveform
  calculation and the comparison figure; A6 (independent re-derivation)
  moves to before its submission.
- The Letter becomes the experimental paper: observation, emulator
  comparison, parity in one data set. Its theory section shrinks to a
  paragraph and a citation.
- The PRL case for the experimental paper then rests on the observation
  alone. A joint submission of both keeps more of it.
- Publishing the theory early exposes the experiment to being done by
  others. Submit without posting to arXiv, or have the averaged THz trace in
  hand first.

## Risks

| Risk | Likelihood | Response |
| --- | --- | --- |
| BSV energy too low for single-shot EOS | medium | binning by pump energy and cumulant tests work below unit signal-to-noise; formula above |
| Source has two or more temporal modes | high: published sources have `K` near 2 | filter, or post-select single-peak shots from per-shot spectra; use the comparison of all shots against selected shots, or a scan over `K`, as the main figure |
| Referees: "expected from Spasibko 2017" | high | lead with the field result and the exact model; state prior work in the first column |
| Derivation error | low to medium | Fock-space test exists; independent re-derivation (A6) before submission |
| Depletion or cascading at the chosen energy | low at microjoule level | A4; check linearity of `s` against `W` in the coherent calibration |
| Scooped | unknown | monthly watch; the theory and code are ready to submit with partial data |
