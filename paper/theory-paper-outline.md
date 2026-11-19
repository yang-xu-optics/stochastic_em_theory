# Theory Paper Outline: Quantum Theory Of Optical Rectification Of BSV

Option raised by the author on 2026-11-14: publish the theory first, as a
paper that precedes the main experimental paper. Not yet decided. If adopted,
the Letter in [outline.md](outline.md) becomes the experimental paper and
cites this one. Plan context: [[wiki/prl-restructuring-plan]].

Draft written 2026-11-19: [theory-note/README.md](theory-note/README.md)
(`theory-note/theory-note.tex` and PDF). It follows the framing below with
one change that strengthens it: the model turned out to be exactly solvable
for an arbitrary multimode pump, not only for one mode, so the title and
abstract lead with the general solution and treat BSV as its main
application. Sections and figures of the draft differ from the plan below
where noted in that README; this outline is kept as the planning record.

Correction 2026-11-19, after a prior-art search: the solvability mechanism is
not new. It is the one behind the exact quantum theory of self-phase
modulation (1991, 1994) and of continuous-time cross-phase modulation (2007).
The framing below still holds, with one change of emphasis: the paper should
not present "exactly solvable" as its discovery. It should say that optical
rectification belongs to that known class with the emitted THz field as the
oscillators, and put its weight on what follows from that: the exact state of
the emitted field, the BSV statistics, the benchmark of approximate
descriptions, and the predictions. Search record:
`results/literature/prior-art-2026-11-19/README.md`.

## Recommended Framing

Frame it as a quantum-optics theory paper with one model, one benchmark, and
one set of predictions, not as an announcement of an effect.

```text
An exactly solvable quantum model of a nonlinear process driven by bright
squeezed vacuum: optical rectification maps the pump photon-flux operator
onto a terahertz field. The model gives the full statistics of that field
for multimode pumps, shows in closed form how accurate the classical-noise
and phase-space descriptions are, and predicts what single-shot
electro-optic sampling will record for existing sources.
```

Why this framing and not "phase-stable THz from quantum light":

- The effect on its own is expected once stated, and its energy statistics
  repeat known results for harmonics. A theory paper that leads with the
  effect invites "obvious"; one that leads with the solvable model and the
  error bounds offers something a reader cannot get from Spasibko 2017.
- The 2026 debate about classical-mixture descriptions of quantum drivers has
  no exactly solvable case with a BSV driver. This is one.
- It leaves the observation, the emulator comparison, and the parity
  demonstration for the experimental paper, which can then say "as predicted
  in" instead of spending its length on derivations.

## Venue

Recommended: Physical Review A, regular article. The content is operator
theory, counting statistics, and a benchmark of approximations, which is PRA's
core subject, and a regular article has room for the detection model and the
realistic predictions that the experimental paper will cite.

- Physical Review A Letter: possible if cut to the model, the benchmark, and
  one prediction figure. Faster, but the detection model and estimators would
  move to the experimental paper's supplement.
- Physical Review Research: same framing, open access.
- Optica (the flagship): not recommended for the theory alone. Its criteria
  accept theory but ask for broad interest, a title and abstract a general
  optics reader follows, and high impact, and it is highly selective. The
  specialist framing above does not meet that; a broad reframing would lean on
  an effect that is expected once stated, classical in description, and whose
  energy statistics are known for harmonics. Optica is a strong target for
  the experimental paper instead: the single-shot BSV characterization of
  Kern 2026 appeared there.
- Optica Quantum: scope is quantum information science and technology
  enabled by optics. A paper whose message is that a classical-noise
  description suffices is a poor match.
- Optics Letters or JOSA B: the natural Optica Publishing Group homes for
  the theory, as a four-page prediction paper or a full article.
- Applied Physics Letters: a weaker fit. A theory-only prediction about
  photon statistics is outside what APL usually takes. It would need the
  applied framing below and loses the benchmark.

Applied framing, if APL or an optics journal is preferred:

```text
A terahertz source whose waveform and sign are fixed while its amplitude
varies from shot to shot with a known distribution set by the pump mode
number. Uses: the amplitude dependence of a THz response from one data set by
sorting shots; a single-point readout of the mode structure of bright
squeezed vacuum.
```

## Claims

Make:

1. THz field operator equals vacuum plus a linear filter of the pump
   photon-flux operator; the mean field depends only on the mean flux
   (parity rule), for any number of modes.
2. Full counting statistics in the detection band: THz field cumulants are
   photon-number cumulants; for multimode pumps they are power sums of the
   Schmidt spectrum.
3. Rectification integrates over the pulse, so its statistics follow the
   pulse energy (`1 + 2/K`), unlike harmonic generation, which follows the
   instantaneous intensity.
4. Exact, Husimi-Q mixture, and classical Gaussian noise compared in closed
   form, with the error of each; the spontaneous term and where it takes over.
5. The solvable single-mode model: photon-number QND structure, back-action
   strength `B`, and its size for organic crystals.
6. What single-shot electro-optic sampling records, with estimators and shot
   numbers.

Do not make:

- "Nonclassical THz". The first-order THz state has a positive P function.
- The single-mode numbers (3, 35/3) as the headline. They are limits, and the
  available source has `K` near 10.
- "First THz generation from quantum light". That is the experimental
  paper's sentence.
- Any statement that the classical-noise model is exact without the two
  small parameters, `1/nbar` and `B nbar`.

## Section Plan

1. Introduction. Quantum light as a driver; all modelling rests on
   phase-space approximations whose accuracy is under discussion; no THz
   process has been treated with a quantized pump except plasma currents by
   sampling; what an exactly solvable case offers.
2. Model and input-output relation. Hamiltonian, assumptions, equations (1)
   and (2) of the theory page, normal ordering, parity rule.
3. Solvable single-mode limit. Conditional displacement, reduced THz state,
   back-action and the Kerr-like phase, measurement strength.
4. Multimode pumps. Schmidt expansion, Wick decomposition, the four terms,
   spontaneous floor; integrating against instantaneous response; mean
   waveform and waveform covariance for a pulse with structure inside it;
   power sums.
5. Three descriptions compared. Exact, approximative phase-space, classical
   noise; errors; the two small parameters.
6. Detection. Operator model of electro-optic sampling, single-shot signal,
   cumulant estimators, immunity to Gaussian detection noise, shots needed.
7. Predictions for existing sources. A microjoule, 100 fs, 1.6 micrometre
   source with `g2` near 1.2, DAST and ZnTe; the single-mode limit reached by
   filtering or post-selection; published sources as further examples.
8. Discussion. What is quantum and what is classical; relation to harmonics
   of BSV and to plasma THz; proposals for the experiment (classical
   emulator, sign-resolved shots, twin beams).

Wiki pages behind it: [[wiki/theory/quantum-optical-rectification-of-bsv]],
[[wiki/theory/bsv-even-order-response-moment-scaling]],
[[wiki/simulations/bsv-optical-rectification-thz-statistics]],
[[wiki/experiments/bsv-or-thz-dast-znte-setup]],
[[wiki/models/thz-optical-rectification-model]].

## Figure Plan

| # | Figure | Evidence today |
| --- | --- | --- |
| 1 | Scheme and the input-output relation; parity rule in a sketch | not started |
| 2 | Single-shot field distributions against mode number, including `K = 10` and the single-mode limit | draft in `results/runs/20261114-bsv-or-thz-statistics/` |
| 3 | THz spectrum: mean part, fluctuation part, spontaneous floor, for a pulse with structure inside it | single-mode version exists; multimode calculation not done |
| 4 | Error of the phase-space and classical-noise descriptions against photon number | formulas and tests exist; no figure |
| 5 | Predicted sampling histogram with detection noise for the realistic source; convergence of the cumulant estimators | numbers in the setup page; no figure |
| 6 | Measurement strength against conversion efficiency and pump energy | formula only |

## Work Still Needed Before It Can Be Written

1. Crystal response for DAST pumped at 1.6 micrometres and the ZnTe sampling
   response for a 100 fs probe. Needs dispersion and absorption sources.
2. Multimode calculation: mean and covariance of the THz waveform for a pump
   with temporal and spatial structure (Schmidt or burst model).
3. Second order: where depletion and cascading end the first-order model.
4. Independent re-derivation of the theory page.
5. Sources to ingest: cavity electro-optics (for the Hamiltonian), THz
   parametric down-conversion (for the spontaneous term), THz generation
   with incoherent light (classical precedent), DAST and ZnTe material data.

## Timing Against The Experimental Paper

- A public theory paper is also a recipe. The experiment is a few weeks of
  work for any group with a BSV source and a THz setup, and several exist.
- Submitting to the journal without posting to arXiv gives a received date
  while keeping the content private during review; post when the
  experimental paper is ready.
- If both are ready within a few months, a joint submission of the Letter
  and this article keeps the strongest case for the experimental paper.
- The averaged THz trace from BSV needs no single-shot system. Having it in
  hand before the theory becomes public removes most of the risk.
