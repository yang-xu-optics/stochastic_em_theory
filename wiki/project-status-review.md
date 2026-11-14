---
title: Project Status Review
type: synthesis
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [review, status, quality, publication-strategy]
source_count: 54
confidence: medium
related:
  - prl-restructuring-plan
  - overview
  - research-agenda
  - simulations/simulation-roadmap
  - theory/bsv-even-order-response-moment-scaling
  - theory/stochastic-quantum-optics-correspondence
---

# Project Status Review

> **Follow-up, same day.** The author accepted the main recommendations with
> one change: optical rectification of BSV is the main result, with a fully
> quantum description and a measurement on the author's BSV source, aimed at
> Physical Review Letters. The plan is [[prl-restructuring-plan]]. Since this
> review was written: 15 sources were ingested (the 2026 papers in the table
> below that are on arXiv, the main Gorlach 2023 article, and the prior work
> on BSV harmonics and on electro-optic sampling); the quantum derivation is
> [[theory/quantum-optical-rectification-of-bsv]]; the first Letter run is
> `results/runs/20261114-bsv-or-thz-statistics/`. Corrections to this review
> that came out of reading the papers are marked "Correction" below. The rest
> of the page is the review as written and still describes the HHG and plasma
> material, which is now the companion paper.

Review date: 2026-11-14. Scope: everything in the repository at commit
`f8a5065`, plus two checks run during the review. Statements about papers
published after 2026-06-06 come from web-search snippets, not from reading the
papers; they are marked as such.

## Verdict

The project has a careful scaffold and a correct input-field validation, but
it has not yet produced a result that is new, and its two physics results
(HHG spectra, plasma THz) are not numerically ready for a paper. All physics
work dates from 2026-06-06 to 2026-06-10. The field has moved since, and one
2026 paper now criticizes the exact approximation this project is built on.
The most valuable next step is to choose one sharp claim and rebuild the
numerics around it, not to add breadth.

## Aims As Understood

Three linked claims ([[overview]]):

1. A stochastic (phase-space sampled) field reproduces squeezed-vacuum
   quantum-optics diagnostics when representation, operator ordering, and
   detection model are matched. Proof target: `g2(0) = 3 + 1/<n>`.
2. The same sampled field can drive classical or semiclassical HHG in gas.
3. The framework extends to THz emission through optical rectification and
   plasma photocurrents.

Interpretive aim added on 2026-06-18: use the stochastic model as a null
model, to separate what follows from input intensity statistics from what
would need a genuinely quantum output state.

## Progress Against Milestones

| # | Milestone ([[overview]]) | Status | Evidence |
| --- | --- | --- | --- |
| 1 | Squeezed-vacuum ensemble and detection model | Done for one mode; partial otherwise | `fields.py` (Wigner, Husimi-Q), `observables.py`. Detection model is total photon counting only: no loss, no temporal gate |
| 2 | Single-mode `g2` correspondence | Done | derivation in [[theory/squeezed-vacuum-g2-proof-plan]]; `validation.py`; tests pass |
| 3 | Multimode BSV characterization | Partial | equal independent modes only. Schmidt-mode and twin-beam models are metadata in `source_models.py`, not samplers. Broadband Raymer and Landes validation (roadmap Stage 1B) not started |
| 4 | Reusable sampler with convergence tests | Done for one mode | batched standard errors in `validation.py` |
| 5 | HHG driven by sampled fields | Partial | 1D TDSE plus amplitude library; qualitative reproductions of Gorlach 2023 Fig. 3b and Fig. IV.2. Not converged, not compared with the published source data |
| 6 | THz optical rectification | Not started | no code. First derivation: [[theory/bsv-even-order-response-moment-scaling]] (seed) |
| 7 | Plasma THz and symmetry | Partial | one notebook, one configuration, 400 shots. Angle, intensity, and post-selection scans not done |
| 8 | Manuscript figures and text | Not started | outline only; `paper/figures/` and `results/figures/` are empty |

Timeline from git and [[log]]: 43 of 50 commits are dated 2026-06-06. The THz
notebook is from 2026-06-10, the paper framing from 2026-06-18, the ML roadmap
from 2026-08-26. The last commit (2026-09-22) added an unrelated note.

## What Is Solid

- The ordering algebra and samplers are correct. Checked by hand:
  `<|alpha|^2>_W = n + 1/2`, `<|alpha|^2>_Q = n + 1`, the Wigner-to-normal
  conversion, and the equal-mode formula `1 + 2/M + 1/(M n)`.
- 55 tests pass in about ten seconds on a clean environment.
- The wiki is structurally clean: 70 pages at review time, no broken links, no
  orphans, every PDF in `raw/sources/` has a summary page.
- Every committed run has a manifest with commit hash, seed, and parameters.
- Claims are labelled honestly throughout: proxies are called proxies, the THz
  energy ratio is called a classical statistic, and non-Gaussian output claims
  are kept out.
- The ground state used by the TDSE runs is converged: energy `-0.79253`
  hartree after the production 220 imaginary-time steps, unchanged after
  2,000, against the target `-0.7924`.

## Problems, Ranked By Threat To Publication

### 1. No new result yet

Each of the three claims is already in the literature the project cites:

- Claim 1 is a textbook property of Wigner sampling of Gaussian states. The
  broadband stochastic version is Raymer and Landes 2023.
- Claim 2 is the method of Gorlach 2023 (phase-space averaging of
  coherent-state responses), used by most later quantum-light HHG papers. The
  two HHG runs here are reproductions of that paper's figures.
- Claim 3 for plasma is Wang 2026 (PRA 113, L021501). The notebook reproduces
  its setting qualitatively.

The null-model argument (bunching is not a nonclassicality witness) is a real
contribution in spirit, but it is currently prose, not a theorem or a test.

### 2. The benchmark and the applications are in different regimes

The ordering correction is `1/<n>`. It matters at `<n> ~ 1`. The strong-field
applications need enormous photon numbers: a 35 fs, 800 nm pulse at
`1e14 W/cm^2` in a 30 micrometre focus carries about `4e14` photons, and a 2 %
second-harmonic arm about `4e12`, which corresponds to `r ~ 15`. There the
correction is of order `1e-13` and the Wigner, Husimi-Q, and P distributions of
the scaled field coincide. So the headline benchmark does not validate
anything that the applications use.

It also causes concrete artifacts, because the application runs sample
finite-photon-number Husimi-Q distributions and then rescale them to strong
fields:

- Fig. 3b runs use `nbar = 100`, `fock_n = 100`, `bsv_r = 2`. The coherent
  and Fock drivers then carry shot-to-shot intensity noise of 14.0 % and
  9.9 % (`normalized_intensity_cv` in the run summaries). At real photon
  numbers this noise is zero. HHG is nonlinear enough for it to matter.
- The THz notebook uses `r = 1` (`<n> = 1.38`). Its Q-function has an
  anti-squeezed to squeezed variance ratio of 7.4, so the squeezed quadrature
  carries 12 % of the sampled intensity. That part is pure vacuum noise of the
  Q representation. At `r ~ 15` it is absent.
- The Fig. IV.2 runs do use the macroscopic-limit distribution
  (`I ~ Gamma(1/2, 2)`). The three application runs are therefore not driven
  by the same ensemble definition.

### 3. The HHG spectra are not converged

Check run during this review:
`results/runs/20261114-fig-iv2-library-convergence-audit/`
(`code/scripts/audit_fig_iv2_library_convergence.py`). Same seed, shots,
grid, and pulse as the committed Fig. IV.2 run; only the number of TDSE
amplitude-library nodes changes (13, 25, 49, 97, nested).

| Compared with 97 nodes, harmonics 7 to 39 | `1e13 W/cm^2` | `2e13 W/cm^2` |
| --- | --- | --- |
| 13 nodes (the committed run): median deviation factor | 1.8 | 2.2 |
| 13 nodes: largest deviation factor | 38 | 12 |
| 49 nodes: median deviation factor | 1.3 | 1.3 |
| 49 nodes: largest deviation factor | 6.9 | 2.5 |

So individual harmonic yields in the committed figures are uncertain by a
typical factor of two and by more than a factor of ten in places, and the
result is still moving between 49 and 97 nodes. The cause is linear
interpolation of `log S` between widely spaced amplitudes for a response that
turns on sharply with field strength; the last two nodes of the 13-node
library are at 0.060 and 0.111 a.u., exactly where the yield is concentrated.

The same check shows how much the tail matters. At `1e13 W/cm^2`, capping the
top 0.1 % of shots (the `bsv_tail_quantile = 0.999` option) removes between
14 % and 80 % of the yield of harmonics 7 to 31 and essentially all of it
from order 33 up. For most plateau harmonics, more than half the yield comes
from about 50 of 50,000 shots. Monte Carlo sampling is the wrong tool for this
integral.

Further convergence gaps, from the manifests:

- Fig. 3b library amplitudes reach 0.256 and 0.341 a.u.
  (`2.3e15` and `4.1e15 W/cm^2`). The quiver radius `E / omega^2` is then 79
  and 105 bohr on a grid of half-width 80 bohr with the absorber starting at
  75. Those nodes are outside the range the grid can represent, and the BSV and
  thermal curves, which run flat to order 150, are dominated by them.
- Grid spacing 0.10 to 0.21 bohr and time step 0.05 to 0.10 a.u., against 0.06
  bohr and 0.02 a.u. in the source. No grid or time-step convergence run
  exists.
- No uncertainty band on any spectrum.

### 4. Display processing that changes the physics

`results/runs/gorlach-2023-fig-iv2-bsv-threshold-tailcap-20260606/` multiplies
the plotted spectrum by `min(1, (9/q)^4)` (a factor 0.007 at order 31) and
caps the BSV intensity tail, in order to make the plot resemble the published
figure. Both steps are declared in the manifest, which is to the project's
credit, but neither has a physical justification, and item 3 shows the cap
alone changes yields by factors of two to five. This run must not be used as
evidence. The Fig. 3b "cleaned peak-window" display (background subtraction
plus a display floor) is less severe but also should not be a paper figure.

### 5. No quantitative comparison with reference data

The published Fig. 3b source data has been in
`raw/assets/gorlach-2023-fig3-source-data/` since 2026-06-06 and has never
been loaded. "Reproduction" currently means visual resemblance. The wiki
notes the main Gorlach 2023 article is not in `raw/sources/`: the two Gorlach
2023 PDFs are byte-identical copies of the supplement. (Correction: the main
article was added on 2026-11-14;
[[sources/gorlach-2023-hhg-driven-by-quantum-light-main-article]].)

### 6. The plasma THz result is one unconverged configuration

- 400 shots. The energy ratio `g2_THz = 20.2` has a bootstrap interval of 10.4
  to 28.1. A 4,000-shot run in the macroscopic-limit ensemble gave 44.1
  (`results/runs/20261114-thz-two-color-parity-check/`). The number depends on
  the ensemble definition and is not established.
- The headline symmetry result (zero mean THz field) follows in one line from
  `alpha -> -alpha` and holds only because the BSV is on the second harmonic.
  See [[theory/bsv-even-order-response-moment-scaling]].
- ADK-form rate without saturation physics, an arbitrary damping rate, no
  propagation.

### 7. The literature layer is broad but shallow, and five months old

- 35 of 54 source summaries are first-pass stubs written from metadata, with
  no equations (`status: draft`). This includes papers central to the
  positioning, for example Rivera-Dean 2025 on propagation.
- Nothing has been ingested since 2026-06-06. Web searches on 2026-11-14
  surfaced the following, none of which is in `raw/sources/`. Read and ingest
  them before trusting the summaries given here:

| Paper (as returned by search) | Why it matters |
| --- | --- |
| Gothelf, Madsen, Lange, "Limitations of an approximative phase-space description in strong-field quantum optics", arXiv:2602.04370, now in Phys. Rev. A | Says the coherent-state phase-space approximation turns the driver into an incoherent mixture of classical states and cannot capture sub-Poissonian statistics or squeezing of the emitted light. This is the limitation side of this project's own thesis |
| "Theory of high-harmonic generation with quantum light", Phys. Rev. Research | Full quantum theory for arbitrary quantum drivers; the natural reference calculation |
| "Propagation effects in high harmonic generation media driven by bright squeezed vacuum light", Nature Communications 2026 | Macroscopic propagation with BSV; probably the published version of the Rivera-Dean 2025 preprint |
| arXiv:2607.20941, "Generation of bright quantum high-order harmonic driven by combined coherent and bright squeezed vacuum light" | Phase matching and pressure dependence with coherent plus BSV drive |
| arXiv:2609.20559, "High-order correlations and ultrafast Wigner negativities in bright-squeezed-vacuum-driven high-harmonic generation" | Converged multimode quantum calculation; a benchmark the stochastic model could be tested against |
| arXiv:2605.31160, "Erasing photons from bright squeezed vacuum light via above-threshold ionization" | Correction: not dynamical back-action, which the paper neglects. It is conditioning: detecting the photoelectron heralds a cat-like state of the light. Unconditional spectra equal the classical-mixture average |
| arXiv:2607.06395 and arXiv:2608.16027, attosecond and sub-cycle metrology of bright quantum light | Describe the random pi phase flips of BSV, the basis of the parity rule. Correction: only 2608.16027 (an experiment) does; 2607.06395 is a streaking theory and does not discuss the flips |

- Two searches found no paper on optical rectification or THz generation with
  a BSV pump. That direction still looks open. (Later the same day: arXiv
  title and abstract queries also found none. But the energy statistics of
  second-order processes driven by BSV were measured for the second harmonic
  in 2017 and 2019, so the open part is the field-level result; see
  [[prl-restructuring-plan]].)

### 8. Manuscript and scope

- `paper/outline.md` held two overlapping section lists and three figure
  lists after the framing changed twice on 2026-06-18. Consolidated on
  2026-11-14 without removing content.
- Side branches consume attention without feeding a figure: the ML roadmap,
  the emitted-mode toy model (whose scan result is the closed form
  `|cosh r + sinh r exp(i theta)|^2`), and the ATI rate proxy.
- The working title says "classical stochastic electrodynamics". That term
  names a specific and contested programme (classical electrodynamics with a
  real zero-point field as a replacement for quantum mechanics). What the code
  does is phase-space sampling of a quantum state. The agenda has listed this
  as open question 1 since June. The title invites the wrong referee.

## Recommendations

### R1. Refresh the literature, then commit to one headline claim

One to two days: ingest the papers in the table above, with equations, and
upgrade the stubs for the ten or so papers the manuscript will actually lean
on. Then choose. Recommended headline, in one sentence:

> In the macroscopic limit, BSV-driven strong-field and THz emission is
> exactly that of a classical Gaussian amplitude-noise field; we give the
> error bound, the parity rule that decides which emissions are phase-stable,
> and a THz prediction that tests it.

This turns the existing null-model idea into a constructive result and makes
the 2026 "limitations" paper a foil instead of a pre-emption. It has three
parts, in order of effort:

1. Equivalence with an error bound. State the scaling limit precisely, show
   the three phase-space distributions coincide, bound the corrections in
   `1/<n>` and in emitter density and pulse length (the quantities the
   limitations paper identifies), and list what the classical model can never
   give: antibunching, sub-vacuum squeezing, sub-shot-noise pump-harmonic
   correlations.
2. Parity rule and moment scaling
   ([[theory/bsv-even-order-response-moment-scaling]]): odd-order responses
   have zero mean field; even-order responses are phase-stable with
   closed-form statistics.
3. One experiment-facing prediction (R4).

### R2. Rebuild the drive ensemble in the macroscopic limit

Use one ensemble everywhere: a real Gaussian amplitude on the anti-squeezed
quadrature, with the multimode generalization from a Schmidt decomposition.
Keep the `3 + 1/<n>` benchmark as a unit test and an appendix, not as the
first result. Reserve the ordering machinery for where photon numbers are
small: the emitted harmonic or THz mode.

### R3. Replace Monte Carlo plus interpolation with quadrature, and gate every figure on convergence

- The integral is one-dimensional over a Gaussian amplitude. Use
  Gauss-Hermite or adaptive quadrature on a dense amplitude grid, refined
  where the response turns on. A few hundred TDSE solves take well under an
  hour on four cores at the current grid (16 s each) and a few hours at the
  source grid.
- Treat the tail explicitly: report the share of each harmonic's yield coming
  from above a given intensity, and stop the integration where the atom is
  fully ionized or the grid cannot hold the quiver motion, with that limit
  stated.
- Required before a run may be copied to `results/figures/`: node-count,
  grid, and time-step convergence shown; uncertainty band shown; no display
  transform other than a stated normalization.
- Delete the `(9/q)^4` rolloff and the tail-cap default from `fig_iv2.py`.

### R4. Give experimentalists one number to measure

Candidates, from the parity rule:

- THz by optical rectification of BSV: the mean THz waveform equals the
  coherent-pump waveform at the same mean energy, the mean THz energy is three
  times larger, the single-shot field histogram is one-sided chi-squared, and
  the energy `g2` is 35/3. All closed-form for one mode; the multimode
  correction is a short calculation. Measurable with single-shot electro-optic
  sampling. No strong-field intensity is needed, which suits nanophotonic and
  thin-film lithium niobate BSV sources.
- Swapped two-colour plasma: the mean THz field vanishes with BSV on the
  second harmonic (Wang 2026) and is nonzero with BSV on the fundamental. The
  check run shows the sign asymmetry (79 % of shots one sign, 1 % the other).
  This needs BSV near `1e14 W/cm^2`, so it is a harder experiment.

Pick one, compute it for a named, published BSV source, and approach a group
that has that source.

### R5. Benchmark against data that is already on disk

Load `SourceData_3b.mat` and the Fig. 5 files, define a per-harmonic
log-ratio metric, and report it. Do the same against Wang 2026 for THz. Add
the main Gorlach 2023 article to `raw/sources/`.

### R6. Test the model against a full quantum calculation where one exists

The claim "classical model with known error" needs at least one case where
the error is measured. arXiv:2609.20559 (two-level emitter, converged
multimode quantum treatment) and the Phys. Rev. Research quantum-light theory
are candidates. (Correction after reading it: that paper gives no basis
sizes and no `g2` or `g3` values, only unnormalized correlation maps; its
appendix shows semiclassical ensembles reproducing the exact emitter
population, and the one demonstrated failure of a classical mixture is the
driver's own Wigner negativity. For optical rectification the cross-check
now exists in closed form, [[theory/quantum-optical-rectification-of-bsv]].) Agreement on intensity observables plus a clear failure on a
nonclassical observable would be the strongest figure in the paper.

### R7. Publication mechanics

- Format: one Letter on the R1 claim with the R4 prediction, and one longer
  companion (Physical Review A or Research) with derivations, convergence
  studies, and code. The current combined HHG-plus-THz framework paper, as
  outlined, is a Physical Review A regular article at best and would be
  refereed as incremental.
- Change the title away from "stochastic electrodynamics". Suggested vocabulary:
  "classical-noise model", "phase-space", "stochastic field".
- Release code and data with a DOI at submission. The manifests and tests
  make this cheap.
- Freeze the ML roadmap, the emitted-mode toy model, and the ATI proxy until
  the Letter is submitted.

### Suggested order of work

| Step | Output | Gate |
| --- | --- | --- |
| 1. Literature refresh and claim decision | updated source pages, one-sentence claim in `paper/outline.md` | is the claim still unpublished? |
| 2. Macroscopic-limit ensemble and quadrature | new sampler, convergence figure | spectra stable to 10 % under node, grid, time-step refinement |
| 3. Reference-data comparison | log-ratio figure against Gorlach source data | agreement, or an understood reason for disagreement |
| 4. Parity rule and OR derivation, multimode included | theory page promoted from seed | checked against the multiphoton literature |
| 5. Quantum cross-check | one agreement panel, one failure panel | error bound confirmed |
| 6. Draft Letter | text and four figures | experimental partner identified |

## Open Decisions For The Author

1. Headline claim: keep the framework framing, or adopt R1.
2. Whether optical rectification moves from outlook to main result (R4).
3. Title vocabulary.
4. Whether in-house or partner BSV sources make the R4 measurement feasible.

## Repository Cleanup Done In This Review

- Simulation runs moved from `results/` to `results/runs/`; run index added
  at `results/runs/README.md` with a usable-for-paper column.
- Literature artifacts moved to `results/literature/`.
- `docs/superpowers/` and the unrelated root note `Untitled.md` moved to
  `archive/`.
- `AGENTS.md` made the single schema; `CLAUDE.md` now imports it.
- Build metadata (`*.egg-info`) and Obsidian's `workspace.json` removed from
  version control and ignored.
- `paper/outline.md` consolidated; READMEs rewritten; stale status statements
  in [[overview]], [[research-agenda]], and
  [[simulations/simulation-roadmap]] updated.
- `raw/` was not touched. Its seven opaquely named PDFs (for example
  `900736523-MIT.pdf`) and the duplicate Gorlach supplement are left as they
  are; the source-summary pages map each file to its citation.
