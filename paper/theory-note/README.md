# Theory Note: Quantum Theory Of Optical Rectification With A Quantized Pump

Draft of 2026-11-19, Physical Review A style (REVTeX 4.2, two columns,
13 pages, 3 figures, 1 table, 37 references). Written at the author's
request as the theory paper that precedes the experimental one; the framing
follows [../theory-paper-outline.md](../theory-paper-outline.md). Derivations
and checks are recorded in
[[wiki/theory/quantum-optical-rectification-of-bsv]].

## Files

| File | Content |
| --- | --- |
| `theory-note.tex` | manuscript source |
| `theory-note.pdf` | compiled draft |
| `derivation.tex`, `derivation.pdf` | step-by-step derivation of the exact solution from the Hamiltonian (10 pages, one column): fields, interaction Hamiltonian with the explicit coupling constant, the two commutators, input-output relation, evolution operator, pump transformation, THz state, check against the classical formula, list of assumptions and checks |
| `derivation-exact-solution.tex`, `derivation-exact-solution.pdf` | detailed derivation of the exact solution, Sec. II B of the note, in the order Hamiltonian, Heisenberg equations of motion, their solution, evolution operator (15 pages, one column), all in the time domain. Target equations carry the note's numbers of 2026-11-21, (8) to (19); a table maps them to the numbers of 2026-11-20 and 2026-11-19, when the file was called `derivation-eq7-14`. Adds checks that are not in the note: commutators of the output operators, energy balance, one pump photon |
| `derivation-frequency-domain.tex`, `derivation-frequency-domain.pdf` | the same solution derived starting in the frequency domain (9 pages): three-wave-mixing Hamiltonian with a coupling function, solvability as a one-line condition on that function, THz mode as a driven oscillator with `zeta = 2 pi g` on the energy shell, evolution operator as on-shell displacement plus off-shell phase (principal-value integral). The pump is handed to the time-domain derivation, where it is simpler. Sec. II of the note follows this document up to the THz output |
| `refs.bib` | bibliography |
| `figures/` | three vector figures and `manifest.yaml` (commit, seed, parameters, quoted values) |

Build, from this folder:

```bash
pdflatex theory-note && bibtex theory-note && pdflatex theory-note && pdflatex theory-note
```

Figures, from `code/`:

```bash
uv run python scripts/make_theory_note_figures.py
```

## What The Note Claims

1. For a coupling that is flat across the pump band and negligible pump
   dispersion, optical rectification is exactly solvable for any pump state:
   `b_out = b_in - i zeta N`, the photon flux is conserved, and the pump is
   only phase modulated.
2. The THz state is a mixture of coherent states weighted by the distribution
   of photon arrival times in the pump. It is classical for every pump state,
   and its mean field depends on the mean photon flux only.
3. For bright squeezed vacuum: single-shot field proportional to the pump
   photon number in the detection band; exact cumulants; gamma distribution
   of shape `K/2`; cumulants measure the power sums of the Schmidt spectrum.
4. Closed-form spectrum (mean field, fluctuation, rectified shot noise) and
   the delay dependence of the noise, which measures the temporal mode number.
5. Errors of the classical Gaussian-noise model and of the Husimi-weighted
   description: `-2/(3 nbar)` and `+4/(3 nbar)` in the THz energy of one mode.
6. Numbers for a 1.6 micrometre, 3 microjoule, 100 fs source with `g2 = 1.2`.

It does not claim that the THz field is nonclassical, and it states that the
single-mode Hamiltonian and the `g2` enhancement of second-order yields are
known. Section II D (added 2026-11-19) states how the model differs from the
quantum theory of difference- and sum-frequency generation: same Hamiltonian,
both sidebands coupled with equal weight, hence no gain and a conserved
source operator.

## Open Items Before Submission

Physics:

- The derivation is this project's own and has not been re-derived
  independently. Checked numerically: the input-output relation and flux
  conservation beyond first order, the pump phase-modulation relation at
  perfect phase matching, the evolution operator with a phase mismatch
  (added 2026-11-19 with the derivation), the four-term second moment, the
  cumulants, the closed-form spectrum. The coupling constant is checked
  analytically against the classical rectification formula. The numerical
  model has one THz mode, so integrals over the THz frequency are not tested.
- Frequency-domain result of 2026-11-21: the propagation picture (ordering in
  `z`) is the approximation in which the coupling strength is evaluated on
  the energy shell; the instantaneous Kerr-type term comes from the variation
  of `kappa^2` across the phase-matching width, not from the terms that do
  not conserve energy. Checked numerically for a dispersionless THz index
  (in the test suite). This replaces "analytic only" in the next item.
- Ordering: the Hamiltonian ordered in time and the generator ordered in `z`
  give the same displacement operator and differ in the kernel of the flux
  phase by a term local in time (an instantaneous Kerr-type phase). Shown
  analytically for a dispersionless THz index only; see `derivation.pdf`,
  Sec. VI B. It affects the pump phase, not the THz field.
- The field normalization is evaluated at the carrier frequency; keeping its
  frequency dependence gives corrections of relative order `Omega/omega_0`
  to the commutation of the flux, about one percent.
- The THz response `g(t)` in Fig. 3 is a model (derivative of a Gaussian,
  rms 150 fs), not a DAST generation response or a ZnTe detection response.
  Section VI gives statistics in units of the mean field for that reason; no
  absolute field strength is predicted.
- The THz energy of 1 nJ used for the measurement-strength estimate in
  Sec. VII is assumed, not measured or calculated.
- Pump group-velocity dispersion, pump absorption, and transverse modes are
  outside the model. A quantitative statement of where the flat-coupling
  assumption fails in DAST at 1.6 micrometres is missing.
- A novelty search on arXiv found no paper on THz generation with a BSV pump
  or on rectification of squeezed light (2026-11-14). Publisher databases
  were not searched. Repeat before submission.

References:

- Entered from memory, not checked against the publication: Blow et al. 1990,
  Blanes et al. 2009, Rice 1944, Iskhakov et al. 2012 (journal reference
  missing). These print "[to be checked]" in the reference list. In
  `derivation.pdf` all five references are from memory and marked so
  (Blow 1990, Quesada and Sipe 2017, Blanes 2009, Glauber 1963, Caumes 2002).
- Volume and page missing: Rasputnyi et al. 2024, Heimerl et al. 2025, Racz
  et al. (DOI from arXiv metadata).
- Gothelf et al. 2026 journal reference was supplied with the ingest request
  and not checked against the journal.
- Blow et al. 1991 and Boivin et al. 1994 are cited for the solvability
  mechanism on the basis of their abstracts and index records only. Their
  full texts must be read before submission, both to confirm the comparison
  and to check whether they state anything about the oscillator side of the
  solution. The author list of Boivin et al. is from memory.
- Guedes et al. 2022 is cited as an arXiv preprint; a journal version may
  exist.
- Rivera-Dean et al. 2025 is cited as an arXiv preprint; a web search
  reported a journal version, not verified.

Form:

- Affiliation and acknowledgments are placeholders.
- Section IV C uses `B` for the arrival-time coefficient and Sec. VII uses
  `B_T` for the measurement strength; consider renaming one.

## Corrections Made While Writing

- Presentation of Sec. II (2026-11-21, agreed with the author): hybrid.
  Sec. II A states the three-wave-mixing Hamiltonian in the frequency domain
  with its coupling function, and the flat-coupling assumption as one line.
  Sec. II B derives the conservation of `N(Omega)` and the THz output in the
  frequency domain (driven oscillator, amplitude on the energy shell), then
  changes to the time domain for the pump phase; the evolution operator is
  described as on-shell displacement plus off-shell phase. Sec. II C (THz
  state) stays in the time domain. Appendix A gives the time-domain
  Hamiltonian, the sideband ladder of the pump, the principal-value form of
  the flux phase, and the propagation picture as its on-shell approximation.
  Equation numbers moved again: the solution block is now (8) to (19), and
  everything after Sec. II B moved up by four. The two companion derivations
  were retagged.

- Order of the derivation (2026-11-20, on the author's advice): Sec. II of
  the note and the detailed derivation now start from the Hamiltonian,
  construct the Heisenberg equations of motion of the flux, the THz operator
  and the pump operator, and solve them; the evolution operator comes last.
  Before, they started from the generator of propagation in `z` and the
  Magnus expansion. Equation numbers changed: the block that was (7) to (14)
  is now (6) to (15); everything after Sec. II B moved up by one.
- Consequence of working with the time-ordered Hamiltonian: the pump phase is
  the THz field integrated along the path of the slice, and the
  flux-dependent remainder has the kernel `W` (time ordering) in place of
  `V` (ordering in `z`). The statement "for perfect phase matching the phase
  is the average of the input and output fields" now carries the qualifier
  "up to an instantaneous Kerr-type term that the model does not determine".
  The THz field and the flux are unaffected.

- Novelty of the exact solution (2026-11-19, after a prior-art search): the
  first draft presented the exact solvability as new and credited only the
  single-mode optomechanical model. The mechanism is known from the quantum
  theory of self-phase modulation (Blow, Loudon, Phoenix 1991; Boivin,
  Kaertner, Haus 1994) and of cross-phase modulation (Shapiro and Razavi
  2007). The introduction now says so and states what is added. Search
  record: `results/literature/prior-art-2026-11-19/README.md`.

- Pump phase: a first version had `theta = F_in + (Kerr term)`. The correct
  phase at perfect phase matching is `(F_in + F_out)/2`; the flux-dependent
  part is required by energy conservation and confirmed numerically.
- Shots needed to resolve the third cumulant: the estimate used in the wiki
  since 2026-11-14 kept only the Gaussian part of the sampling variance. The
  full expression is Eq. (39) of the note; for `K = 10` at `5 sigma` it is
  900 shots without detection noise, not about 200.
- Photon-number resolution by the THz field is `1/(2 sqrt(B_T))`, not
  `1/sqrt(B_T)`.
- "Two small parameters, `1/nbar` and `B nbar`" was wrong for the THz
  statistics: they are exact in the coupling; `B nbar` controls only the pump
  back-action.
