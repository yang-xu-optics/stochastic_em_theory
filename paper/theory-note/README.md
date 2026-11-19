# Theory Note: Quantum Theory Of Optical Rectification With A Quantized Pump

Draft of 2026-11-19, Physical Review A style (REVTeX 4.2, two columns,
11 pages, 3 figures, 1 table, 30 references). Written at the author's
request as the theory paper that precedes the experimental one; the framing
follows [../theory-paper-outline.md](../theory-paper-outline.md). Derivations
and checks are recorded in
[[wiki/theory/quantum-optical-rectification-of-bsv]].

## Files

| File | Content |
| --- | --- |
| `theory-note.tex` | manuscript source |
| `theory-note.pdf` | compiled draft |
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
  perfect phase matching, the four-term second moment, the cumulants, the
  closed-form spectrum. Not checked numerically: the phase operator for a
  phase mismatch (Appendix A), which is analytic only.
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
  missing). These print "[to be checked]" in the reference list.
- Volume and page missing: Rasputnyi et al. 2024, Heimerl et al. 2025, Racz
  et al. (DOI from arXiv metadata).
- Gothelf et al. 2026 journal reference was supplied with the ingest request
  and not checked against the journal.
- Rivera-Dean et al. 2025 is cited as an arXiv preprint; a web search
  reported a journal version, not verified.

Form:

- Affiliation and acknowledgments are placeholders.
- Section IV C uses `B` for the arrival-time coefficient and Sec. VII uses
  `B_T` for the measurement strength; consider renaming one.

## Corrections Made While Writing

- Pump phase: a first version had `theta = F_in + (Kerr term)`. The correct
  phase at perfect phase matching is `(F_in + F_out)/2`; the flux-dependent
  part is required by energy conservation and confirmed numerically.
- Shots needed to resolve the third cumulant: the estimate used in the wiki
  since 2026-11-14 kept only the Gaussian part of the sampling variance. The
  full expression is Eq. (33) of the note; for `K = 10` at `5 sigma` it is
  900 shots without detection noise, not about 200.
- Photon-number resolution by the THz field is `1/(2 sqrt(B_T))`, not
  `1/sqrt(B_T)`.
- "Two small parameters, `1/nbar` and `B nbar`" was wrong for the THz
  statistics: they are exact in the coupling; `B nbar` controls only the pump
  back-action.
