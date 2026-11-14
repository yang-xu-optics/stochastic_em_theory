# Letter Outline: Optical Rectification Of Bright Squeezed Vacuum

Target: Physical Review Letters. Limits: 3,750 words including captions and
equations, four figures, plus Supplemental Material.

Status (2026-11-14): outline and first theory figure only. No text drafted,
no measurement yet. The plan that gets from here to submission is
[[wiki/prl-restructuring-plan]]. The earlier HHG-plus-plasma outline is now
[companion-outline.md](companion-outline.md).

## The Claim

One sentence:

```text
Optical rectification turns a zero-mean bright squeezed vacuum pulse into a
phase-stable terahertz transient whose single-shot field is proportional to
the pump photon number, so the terahertz field carries the photon-number
statistics of squeezed vacuum.
```

Three supports, each one figure:

1. Theory, exact within first order: the THz field operator is a linear
   filter of the pump photon-flux operator. Consequences: nonzero mean field
   from zero-mean light; THz field statistics equal pump photon-number
   statistics; mean THz energy `1 + 2/K` times the coherent-pump value;
   one-sided Gamma-distributed single-shot field.
2. The classical Gaussian amplitude-noise model of BSV gives the same numbers
   up to `1/<n>` and misses only the spontaneous term. For this process the
   "mixture of classical states" picture is the exact reduced state.
3. Measurement on the BSV source: single-shot electro-optic sampling shows a
   sign-definite THz field linear in the shot energy, with the predicted
   distribution and cumulants.

Candidate titles:

```text
Phase-stable terahertz fields from bright squeezed vacuum
Terahertz fields that follow the photon statistics of squeezed vacuum
Optical rectification of bright squeezed vacuum
```

## What Is New, And What Is Not

State this plainly in the introduction; referees will know the prior work.

- Not new: enhancement of second-order processes by the pump `g2`, and the
  `(2n - 1)!!` factor for `n`-photon processes driven by BSV, measured as
  2.86 +- 0.08 for the second harmonic (Spasibko 2017); single-shot energy
  distributions of the second and third harmonics of BSV (Manceau 2019);
  field-resolved detection of a rectified transient from a coherent pump at
  nanojoule energy (Riek 2017);
  field-resolved measurement of BSV itself with random pi phase flips
  (Gholam-Mirzaei 2026, Kern 2026); plasma THz with a BSV second harmonic,
  predicted to be incoherent (Wang 2026, theory).
- New: (a) THz generation driven by quantum light, observed; (b) a
  phase-stable *field* from a zero-mean driver, and the parity rule that says
  when that happens; (c) field-level statistics: a sign-definite, strongly
  non-Gaussian THz field measured shot by shot; (d) an exact quantum model in
  which the status of the classical-noise description is settled with an
  error bound, in direct contact with the 2026 critique of phase-space
  approximations (Gothelf 2026).

## Section Plan (about 3,750 words)

### Introduction (about 450 words)

Quantum light as a driver of nonlinear emission; all results so far are
energies or photon counts; BSV has no mean field and a random pi phase, so
odd-order emission has no stable phase. Question: can zero-mean quantum light
make a field with a definite phase, and what statistics does that field have?
Answer in one paragraph. Prior work as above.

### Theory (about 900 words, Fig. 1 and Fig. 2)

- Hamiltonian, input-output relation `b_out = b_in - i zeta N(Omega)`.
- Parity rule in one paragraph: the mean field depends on the mean photon
  flux only.
- Counting statistics in the electro-optic-sampling band: field proportional
  to total photon number; cumulants; `K` modes; Gamma distribution.
- Classical-noise limit and what it misses; one sentence on the single-mode
  solvable model (QND structure, back-action strength `B`).
- Wiki: [[wiki/theory/quantum-optical-rectification-of-bsv]],
  [[wiki/theory/bsv-even-order-response-moment-scaling]],
  [[wiki/simulations/bsv-optical-rectification-thz-statistics]].

### Experiment (about 600 words, Fig. 3)

Source (wavelength, energy, duration, repetition rate, measured `g2` and
`K`), rectification crystal, electro-optic sampling with a probe from the
coherent laser, per-shot pump-energy monitor. To be written from the
measurement; parameters to be supplied
([[wiki/prl-restructuring-plan]], "Inputs needed").

### Results (about 1,100 words, Fig. 3 and Fig. 4)

1. Averaged THz waveform from BSV exists and matches the coherent-pump
   waveform in shape and sign.
2. Shot-resolved: THz field versus shot energy is linear through the origin;
   no shot has the opposite sign beyond detection noise.
3. Histogram of the single-shot field against the Gamma prediction with the
   independently measured `K`; cumulant estimates of `K` from skewness and
   kurtosis.
4. Mode-number dependence: all shots against single-peak shots selected from
   per-shot spectra, or a scan over `K`; THz energy enhancement against
   `2/K`, slope one.
5. Recommended: the same statistics from a classical emulator (coherent laser
   with shot-by-shot Gaussian random amplitude), overlaid on the BSV data.
6. Optional: THz field against the per-shot sign of the BSV field.

### Discussion (about 500 words)

- What is quantum here and what is not: quantum in origin (the statistics
  are those of squeezed vacuum), classical in description (positive P
  function), with the size of the corrections stated.
- Contrast with plasma THz and with odd harmonics through the parity rule.
- Outlook: photon-number readout by a THz field, twin-beam correlations, the
  spontaneous term, cascading.

### Supplemental Material

Full derivation; multimode formulas; crystal response and phase matching;
electro-optic-sampling model and noise; estimators for heavy-tailed data;
source characterization; all shot statistics; code and data availability.

## Figure Plan

| # | Figure | Supports | Evidence today |
| --- | --- | --- | --- |
| 1 | Concept: BSV pulse with random sign, rectification crystal, sign-definite THz transient, single-shot sampling; inset with the input-output relation | the claim | not started |
| 2 | Theory: single-shot field distributions for several `K`; energy enhancement and fluctuation ratio versus photon number, exact against bright limit; spectrum with the spontaneous floor | theory, classical-noise limit | draft in `results/runs/20261114-bsv-or-thz-statistics/`; needs the real crystal response and source modes |
| 3 | Measurement: averaged THz waveforms for BSV and coherent pump; a set of single shots; field versus shot energy | phase stability, linearity | no data |
| 4 | Statistics: measured field histogram against the prediction; cumulant estimates of `K`; enhancement against `2/K` | photon-statistics transfer | no data |

## Wiki Pages Used By The Letter

- [[wiki/theory/quantum-optical-rectification-of-bsv]]
- [[wiki/theory/bsv-even-order-response-moment-scaling]]
- [[wiki/models/thz-optical-rectification-model]]
- [[wiki/simulations/bsv-optical-rectification-thz-statistics]]
- [[wiki/prl-restructuring-plan]]
- [[wiki/project-status-review]]
