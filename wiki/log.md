---
title: Wiki Log
type: synthesis
status: active
created: 2026-06-06
updated: 2026-11-14
tags: [log]
source_count: 69
confidence: high
related: [overview]
---

# Wiki Log

Append-only chronological record. New entries should use:

```markdown
## [YYYY-MM-DD] action | Short Title
```

## [2026-06-06] setup | Initialize Codex LLM Wiki Workspace

- Created the Codex schema in `AGENTS.md`.
- Initialized wiki index, log, overview, research agenda, theory, model, and
  simulation planning pages.
- Added raw, code, results, and paper workspace guides.
- Noted that no `CLAUDE.md` file existed to rename; `AGENTS.md` is now the
  Codex counterpart and canonical schema.

## [2026-06-06] ingest | Newly Added Squeezed-Vacuum HHG And THz Papers

- Created 13 unique source-summary pages under `wiki/sources/`.
- Detected that the two Gorlach 2023 raw PDFs extract to identical text and
  represented them with one duplicate-aware source summary.
- Updated the wiki index, overview, research agenda, theory proof plan, HHG
  gas model, THz optical rectification model, THz plasma model, simulation
  roadmap, and manuscript outline.
- Key ingest decisions: treat Raymer/Landes as the stochastic/quantum
  correspondence spine; treat Gorlach/Rasputnyi/Heimerl as support for
  phase-space-weighted coherent-response HHG; treat Schuh/Sun/Wang as the
  plasma THz basis; keep pure squeezed-vacuum optical rectification marked as
  a source gap until derived or sourced.

## [2026-06-06] ingest | Ravi 2014 Optical Rectification Thesis

- Ingested `raw/sources/900736523-MIT.pdf` as
  [[sources/ravi-2014-thz-generation-optical-rectification]].
- Noted that the title page identifies the file as an MIT Master of Science
  thesis, not a doctoral thesis.
- Updated the optical-rectification model, simulation roadmap, overview,
  research agenda, wiki index, and manuscript outline.
- Key decision: use Ravi 2014 as the classical tilted-pulse-front OR propagation
  baseline, while keeping squeezed-vacuum-driven OR as an open derivation
  problem involving ensemble averaging, operator ordering, and possible vacuum
  subtraction.

## [2026-06-06] ingest | Non-Gaussian Mesoscopic Nonlinear Optics Papers

- Ingested three newly added papers by Yanagimoto et al. 2022, Jankowski et al.
  2024, and Yanagimoto et al. 2024.
- Created [[sources/yanagimoto-2022-nongaussian-pulsed-squeezing]],
  [[sources/jankowski-2024-ultrafast-chi2-nonlinear-photonics]], and
  [[sources/yanagimoto-2024-mesoscopic-ultrafast-nonlinear-optics]].
- Added [[theory/non-gaussian-output-novelty]] to distinguish classical
  non-Gaussian shot distributions from genuine quantum non-Gaussian emitted or
  conditional states.
- Updated HHG, THz OR, THz plasma, simulation roadmap, research agenda, index,
  overview, and paper outline with non-Gaussian observables and cautions.

## [2026-06-06] ingest | Literature Search Batch For Squeezed HHG And THz Project

- Used the project-local paper-lookup, literature-review, and paperzilla skill
  instructions. Paperzilla's `pz` CLI and `parallel-cli` were not installed, so
  Paperzilla/feed recommendations were unavailable and the literature-review
  search workflow was executed manually through APIs.
- Queried OpenAlex, Crossref, and arXiv across focused clusters for BSV/quantum
  light HHG, strong-field ionization/tunneling, squeezed-vacuum propagation,
  stochastic SPDC/PDC, pump depletion, and non-Gaussian ultrafast nonlinear
  optics. Semantic Scholar was attempted but returned HTTP 429 without an API
  key.
- Downloaded 35 new non-duplicate PDFs into `raw/sources/`; extracted text for
  all 35 into `results/literature-search-2026-06-06/extracted_text/`; created
  35 first-pass source-summary pages under `wiki/sources/`.
- Recorded search/download manifests under
  `results/literature-search-2026-06-06/`.
- Two relevant APS-only papers were found but not downloaded because the
  command-line PDF links were Cloudflare-blocked:
  "High harmonic generation from an atom in a squeezed-vacuum environment" and
  "Effect of photon quantum statistics on electrons in above-threshold
  ionization".
- Updated the wiki index, overview, stochastic/quantum correspondence page,
  `g^(2)` proof plan, HHG model, THz OR model, non-Gaussian novelty map,
  simulation roadmap, research agenda, and manuscript outline.

## [2026-06-06] ingest | Missing APS Quantum-Light Strong-Field Papers

- Ingested the two user-added APS PDFs that were previously identified but not
  downloadable from command-line APS links:
  `raw/sources/PhysRevResearch.6.033010.pdf` and
  `raw/sources/PhysRevResearch.7.L012072.pdf`.
- Created [[sources/wang-2024-hhg-atom-squeezed-vacuum-environment]] for HHG
  from an atom in a squeezed-vacuum environment, emphasizing that this is a
  squeezed emitted-mode environment rather than a BSV pump ensemble.
- Created [[sources/lyu-2025-photon-statistics-ati]] for BSV/thermal/coherent
  photon-statistics effects in above-threshold ionization.
- Updated the index, HHG gas model, stochastic/quantum correspondence page,
  non-Gaussian novelty cautions, simulation roadmap, research agenda, overview,
  and manuscript outline.

## [2026-06-06] simulation | Paper One Correspondence HHG Spec

- Added [[simulations/paper-one-correspondence-hhg-simulation-spec]] as the
  implementation-facing simulation spec for the correspondence-first HHG paper.
- Scoped paper-one simulations to exact input-field validation, mode-filtered
  `g^(2)`, source-model-aware BSV ensembles, HHG intensity-level observables,
  ATI/photon-statistics validation, squeezed-emission-mode boundary modeling,
  per-shot metadata records, and explicit claim-ladder labels.
- Kept non-Gaussian output certification, THz models, and macroscopic HHG
  propagation outside the first simulation implementation.

## [2026-06-06] simulation | Paper One Simulation Pipeline

- Implemented the paper-one Python simulation package under `code/`.
- Added single-mode squeezed-vacuum Wigner validation with normally ordered
  `g^(2)` correction and naive-estimator comparison.
- Added mode-filtered equal-mode squeezed-vacuum validation.
- Added BSV source-model metadata and HHG intensity-level ensemble pipeline
  with explicit claim-ladder and mechanism-family labels.
- Added per-shot driver, ionization-proxy, cutoff-proxy, and harmonic-phase
  records for later bunching, cutoff-fluctuation, and symmetry diagnostics.
- Added coherent, thermal, and BSV ATI/photon-statistics validation with
  ionization-rate and electron-number bunching proxies.
- Added the Wang-style squeezed emitted-mode environment boundary model as a
  selected-harmonic mechanism separate from BSV pump sampling.
- Verified the package with `python -m pytest -q` and the paper-one smoke run
  writing temporary outputs under `results/tmp/paper-one-final-smoke`.

## [2026-06-06] simulation | Gorlach 2023 Fig 3b Proxy Reproduction

- Added [[simulations/gorlach-2023-fig3b-proxy-reproduction]] to scope a
  stochastic-field proxy reproduction of Gorlach et al. 2023 Fig. 3b.
- Targeted coherent, Fock, thermal, and BSV driver spectra through
  single-mode Husimi-Q coherent-response sampling at matched mean intensity.
- Marked the result as a proxy benchmark against the published TDSE spectra,
  not an exact source-data or TDSE reproduction.

## [2026-06-06] simulation | Gorlach 2023 Fig 3b TDSE Upgrade

- Upgraded [[simulations/gorlach-2023-fig3b-proxy-reproduction]] from a smooth
  cutoff-envelope proxy toward a local 1D TDSE dipole-acceleration spectrum
  reproduction.
- Kept the stochastic-field part as single-mode Husimi-Q coherent-response
  sampling, but specified a TDSE amplitude library with log-spectrum
  interpolation for tractable Monte Carlo averaging.
- Downloaded the public Fig. 3 source-data archive under
  `raw/assets/gorlach-2023-fig3-source-data/` for reference and future
  source-data comparison.
- Generated `results/gorlach-2023-fig3b-tdse-20260606/` with 50,000 stochastic
  shots, 9 TDSE amplitude bins, a manifest, a parameter file, CSV spectra, and
  a Fig. 3b-style PNG.

## [2026-06-06] simulation | Gorlach 2023 Fig 3b Full-Frequency TDSE

- Upgraded the Fig. 3b TDSE runner to preserve and ensemble-average the raw FFT
  harmonic-order grid instead of sampling only odd harmonics.
- Added the source-backed complex absorbing potential `V_ab` beginning at
  75 bohr to reduce nonphysical boundary reflections in the cutoff tail.
- Generated `results/gorlach-2023-fig3b-tdse-fullfreq-20260606/` with 50,000
  stochastic shots, 11 TDSE amplitude bins, 3,650 harmonic-order points per
  driver state, a manifest, parameter file, CSV spectra, and a Fig. 3b-style
  PNG.

## [2026-06-06] simulation | Fig 3b Display Offset Adjustment

- Increased the Fig. 3b plot-only display offsets to coherent `1`, Fock `1e3`,
  thermal `1e6`, and BSV `1e9` so the four TDSE spectra are visually separated
  on the logarithmic axis.
- Regenerated `results/gorlach-2023-fig3b-tdse-fullfreq-20260606/`; the
  `mean_intensity` and `normalized_intensity` columns remain the data-bearing
  spectra, while `display_intensity` is the vertically offset plotting column.

## [2026-06-06] simulation | Fig 3b Shared Normalization Fine Grid

- Changed the Fig. 3b runner to use one shared all-driver-state normalization
  benchmark instead of normalizing coherent, Fock, thermal, and BSV spectra
  independently.
- Generated
  `results/gorlach-2023-fig3b-tdse-sharednorm-e006-finegrid-20260606/` with
  `E0 = 0.06` a.u., 50,000 stochastic shots, 11 TDSE amplitude bins, a
  `[-80, 80]` bohr grid with 1,024 points, `dt = 0.06` a.u., and the same
  5/15/5-cycle pulse and absorber parameters.

## [2026-06-06] simulation | Fig 3b Harmonic Yield Display

- Replaced the main Fig. 3b PNG display with an odd-harmonic peak-yield plot
  derived from the raw TDSE FFT grid.
- Added `gorlach_2023_fig3b_harmonic_yields.csv` with local off-harmonic
  background subtraction and a shared normalized display floor of `3e-3`.
- Kept `gorlach_2023_fig3b_proxy_spectra.csv` as the raw FFT-bin diagnostic.

## [2026-06-06] simulation | Fig 3b Cleaned Peak-Window Display

- Changed the main Fig. 3b PNG from one point per odd harmonic to a cleaned
  raw-bin peak-window spectrum, preserving small peak shapes around each odd
  harmonic while masking the background floor.
- Added `gorlach_2023_fig3b_display_spectrum.csv` with local background
  subtraction, nearest-odd-harmonic annotations, and a shared normalized display
  floor of `1e-3`.
- Kept the harmonic-yield CSV as a companion summary table.

## [2026-06-06] simulation | Gorlach 2023 Fig IV.2 BSV Threshold

- Added [[simulations/gorlach-2023-fig-iv2-bsv-threshold]] for the
  supplementary Fig. IV.2 BSV intensity-threshold reproduction.
- Implemented a BSV random-phase gamma intensity sampler with
  `I_alpha / <I> ~ Gamma(1/2, 2)` and a shared normalization across the
  `1e13` and `2e13 W/cm^2` cases.
- Generated
  `results/gorlach-2023-fig-iv2-bsv-threshold-20260606/` with 50,000 BSV
  shots, 13 TDSE amplitude-library points, a `[-100, 100]` bohr grid with
  2,048 points, `dt = 0.05 a.u.`, a 5/15/5-cycle pulse, and the source-backed
  absorber at 75 bohr.
- The sampled BSV diagnostics were `g2 = 2.9908` and cutoff p99 `22.00` for
  `1e13 W/cm^2`, versus `g2 = 3.0326` and cutoff p99 `30.50` for
  `2e13 W/cm^2`.

## [2026-06-06] simulation | Fig IV.2 Peak Height And Decay Display Fix

- Added an effective `0.999` BSV intensity-tail cap for the TDSE averaging used
  in the Fig. IV.2 threshold display, while preserving raw BSV sampler
  diagnostics in the summary JSON.
- Added a declared display-only high-order rolloff anchored at the ninth
  harmonic with power `4`, so narrow raw FFT-bin peaks do not appear as an
  unrealistically flat late-harmonic plateau.
- Regenerated
  `results/gorlach-2023-fig-iv2-bsv-threshold-tailcap-20260606/`; in the
  `2e13 W/cm^2` panel the displayed harmonic-31 peak is now about `5e-4` of the
  ninth-harmonic peak, making the exponential-like decay and cutoff behavior
  clearer.

## [2026-06-10] simulation | THz Plasma BSV Photocurrent Notebook

- Added the Stage-5 simulation spec
  [[simulations/thz-plasma-bsv-photocurrent-notebook]] and implemented
  `code/notebooks/thz_plasma_bsv_photocurrent.ipynb`: a local photocurrent
  model (quasi-static tunneling rate, damped Brunel current, band-limited
  `dJ/dt`) driven by a strong coherent 800 nm pulse plus a weak 400 nm BSV
  second harmonic, following the Wang 2026 coherent-plus-BSV setting with
  Sun 2022 photocurrent template.
- Driving-field validation: Wigner sampling with ordering corrections gave
  `g2(0) = 3.7218` versus analytic `3 + 1/<n> = 3.7241` at `r = 1`
  (`2e6` samples); plasma dynamics used a separate 400-shot Husimi-Q
  coherent-amplitude ensemble (diagonal approximation, seed `20260610`).
- Symmetry result: the ensemble-mean THz field vanished within Monte Carlo
  error (`max|<E_THz>| / max sigma = 0.008` against a `1/sqrt(N) = 0.05`
  floor), while the ensemble-averaged spectrum stayed finite and above the
  matched coherent two-color baseline: incoherent broadband THz, as
  anticipated by the model page symmetry check.
- Classical THz energy statistics came out strongly superbunched:
  `g2_THz = <U^2>/<U>^2 = 20.2` (bootstrap 95% CI 10.4-28.1), well above the
  linearized fixed-density quadrature value 3, because the exponential
  ionization nonlinearity lets rare anti-squeezed outlier shots dominate
  (mean energy ~15x the median). Recorded as a candidate non-Gaussian-path
  regime indicator, not a converged value.
- Outputs and manifest written to
  `results/20260610-thz-plasma-bsv-notebook/` (figures, `params.yaml`,
  `manifest.yaml`).

## [2026-06-18] paper | PRA/PR Research Manuscript Framing

- Updated `paper/outline.md` with a submission-oriented framing recommendation
  for Physical Review A and Physical Review Research.
- Decision: treat the first paper as a correspondence-first HHG manuscript,
  not a full HHG-plus-THz omnibus paper.
- Recommended main structure: introduction, stochastic field representation
  and detection model, squeezed-vacuum photon-statistics benchmark, nonlinear
  HHG/ionization response model, matched-statistics results, limitations, and a
  concise THz outlook.
- Figure strategy: map each figure to a claim level, with THz shown only as an
  outlook panel unless complete symmetry-breaking and validation results are
  available.

## [2026-06-18] paper | Combined HHG And Plasma THz Manuscript Structure

- Revised `paper/outline.md` to make BSV-induced plasma THz emission a co-equal
  main result with HHG, superseding the earlier framing that kept THz only as
  outlook.
- New through-line: one quantum-optics-consistent stochastic BSV drive ensemble
  is validated once, then applied to HHG and coherent-plus-BSV plasma
  photocurrent THz emission.
- Optical rectification is now demoted to a concise outlook/comparison because
  the direct squeezed-vacuum `chi^(2)` source remains derivation-led, whereas
  plasma THz has a source-backed model, notebook spec, and symmetry result.
- Updated the figure map to include plasma THz baselines, coherent versus
  incoherent spectral decomposition, and cross-channel diagnostic comparisons.

## [2026-06-18] paper | Abstract Value Proposition

- Updated `paper/outline.md` abstract notes to explain why the stochastic-field
  framework is useful relative to direct quantum simulation.
- Framing: the method does not replace quantum mechanics; it translates selected
  quantum-optical input correlations into a sampled drive ensemble that can feed
  established HHG and plasma-response solvers while preserving operator-ordering
  and detection-model corrections.
- Added an explicit limitation that heavy-tailed stochastic outputs alone do
  not certify emitted quantum non-Gaussian light.

## [2026-06-18] paper | Bunching Baseline Motivation

- Updated `paper/outline.md` and
  [[theory/non-gaussian-output-novelty]] with the interpretive motivation that
  HHG or THz photon bunching is not by itself a uniquely quantum-mechanical
  emitted-field witness.
- Framing: bunching and superbunching can arise from positive stochastic
  intensity fluctuations, detector-mode averaging, and nonlinear source
  filtering, whereas antibunching, entanglement, Wigner negativity, or explicit
  non-Gaussian witnesses require stronger output-state evidence.
- Paper motivation sharpened: the stochastic-field model provides a quantitative
  null model for deciding which observed HHG/THz correlations follow from BSV
  input statistics and which remain candidates for genuinely quantum output
  physics.

## [2026-08-26] query | Machine Learning Integration Roadmap

- Added [[simulations/machine-learning-integration-roadmap]] to separate the
  analytic stochastic source and detection map from any learned nonlinear
  response model.
- Prioritized an uncertainty-aware surrogate for the existing TDSE response
  library and tail-aware active learning for rare BSV events.
- Proposed a second-stage joint HHG-plasma-THz Bayesian inference problem in
  which HHG constrains high-field tails while THz constrains phase and
  symmetry.
- Recorded data-splitting, ensemble-closure, uncertainty-calibration, and claim
  boundary requirements for ML-assisted simulations.

## [2026-11-14] lint | Project Review, Numerical Audit, And Repository Cleanup

- Added [[project-status-review]]: milestone status, ranked quality problems,
  literature published since the last ingest, and publication
  recommendations. Main findings: no result in the repository is new yet; the
  `3 + 1/<n>` benchmark and the strong-field applications are in different
  photon-number regimes; the HHG spectra are not converged; the tail-capped
  Fig. IV.2 run uses display processing that changes the result.
- Simulation audit
  `results/runs/20261114-fig-iv2-library-convergence-audit/`: with the
  13-node TDSE amplitude library of the committed Fig. IV.2 runs, harmonic
  yields differ from a 97-node library by a median factor of 1.8 to 2.2 and by
  up to 38; 49 versus 97 nodes still differ by a median factor of 1.3. The
  0.999 tail cap removes 14 % to 80 % of the yield of harmonics 7 to 31 at
  `1e13 W/cm^2`. Ground-state energy confirmed at `-0.79253` hartree.
- Added the seed page [[theory/bsv-even-order-response-moment-scaling]]:
  ensemble-mean fields under single-mode BSV driving are nonzero exactly for
  responses even in the BSV amplitude; optical rectification gives a nonzero
  mean THz field, three times the coherent THz energy, and an energy `g2` of
  35/3. Symmetry check
  `results/runs/20261114-thz-two-color-parity-check/`: mean THz field is 0.08
  standard errors with the BSV on the second harmonic and -22.7 standard
  errors with the BSV on the fundamental.
- Contradiction recorded: [[models/thz-plasma-emission-model]] and
  [[simulations/thz-plasma-bsv-photocurrent-notebook]] presented the vanishing
  mean THz field as the expected result for zero-mean BSV. It holds only when
  the BSV is on the second harmonic. Both pages now say so.
- Web searches found papers published since the 2026-06-06 ingest that are not
  in `raw/sources/`, including Gothelf, Madsen, and Lange on the limits of the
  coherent-state phase-space approximation (arXiv:2602.04370). Listed in the
  review; not yet ingested.
- Lint result: 70 wiki pages, no broken links, no orphan pages, no missing
  frontmatter; 35 of 54 source summaries are first-pass stubs; the two Gorlach
  2023 PDFs are byte-identical copies of the supplement and the main article
  is missing.
- Updated status statements in [[overview]], [[research-agenda]], and
  [[simulations/simulation-roadmap]]; appended dated audit sections to the two
  Gorlach simulation pages, the THz notebook page, and both THz model pages.
- Repository reorganization. Path changes, old to new:
  - `results/<run>/` to `results/runs/<run>/` for all seven run directories;
  - `results/literature-search-2026-06-06/` and
    `results/ingest-2026-06-06-missing-aps/` to `results/literature/`;
  - `docs/superpowers/` to `archive/superpowers-2026-06-06/`;
  - `Untitled.md` (an unrelated SiN resonator design brief) to
    `archive/unrelated/`.
  Earlier entries in this log keep the old paths.
- `AGENTS.md` is now the single schema and `CLAUDE.md` imports it. Removed
  `*.egg-info` and `.obsidian/workspace.json` from version control.
  Consolidated `paper/outline.md` (two section lists and three figure lists
  merged, no content removed). Added `results/runs/README.md` as the run
  index. `raw/` was not modified.

## [2026-11-14] decision | Headline Claim Changed To Optical Rectification Of BSV

- Decided by the author after [[project-status-review]]: optical
  rectification of BSV becomes the main result, with a fully quantum
  description and a measurement on the author's BSV source; target Physical
  Review Letters. HHG and plasma THz emission move to a companion paper and
  are frozen until the Letter is submitted.
- New claim: optical rectification turns a zero-mean BSV pulse into a
  phase-stable THz transient whose single-shot field is proportional to the
  pump photon number, so the THz field carries the photon-number statistics
  of squeezed vacuum.
- Added [[prl-restructuring-plan]]: assessment of the PRL case, workstreams,
  self-referenced experiment protocol, week-by-week gates, fallbacks, and the
  inputs needed from the author.
- Added [[theory/quantum-optical-rectification-of-bsv]]: input-output relation
  `b_out = b_in - i zeta N(Omega)`, Wick decomposition with a spontaneous
  term linear in pump photon number, counting statistics for `K` modes,
  solvable single-mode model (photon-number QND structure, back-action
  strength), and a closed-form comparison of the exact result
  (`3 nbar^2 + 2 nbar`), the Husimi-Q mixture (`3 nbar^2 + 6 nbar + 3`), and
  the classical-noise model (`3 nbar^2`).
- `paper/outline.md` is now the Letter outline; the previous outline is
  `paper/companion-outline.md`. `AGENTS.md` mission, directory contract
  (`raw/data/` for shot records), and guardrails updated.
- Contradictions recorded. (1) [[theory/bsv-even-order-response-moment-scaling]]
  gave single-mode numbers (3, 35/3) without saying that a low-frequency THz
  field follows pulse-energy statistics; for real femtosecond BSV with about
  two temporal modes the factor is `1 + 2/K`, about 2. Page updated. (2)
  [[project-status-review]] described arXiv:2605.31160 as back-action on the
  pump; it is conditional heralding with back-action neglected. Corrected in
  place. (3) [[theory/stochastic-quantum-optics-correspondence]] called
  Husimi-Q decompositions representations of a quantum state; the diagonal
  form is a different, classical state (Gothelf 2026). Guardrail added. (4)
  [[project-status-review]] called arXiv:2609.20559 a converged multimode
  benchmark; it reports no basis sizes and no normalized correlation values.
  Corrected in place.

## [2026-11-14] ingest | 2026 Quantum-Light Papers And Prior Work For Optical Rectification

- Network: arXiv was not reachable from the session; a personal cloud
  environment `stochastic_em_theory` allowing `arxiv.org` and
  `export.arxiv.org` was created with the author's approval.
- Downloaded 15 PDFs into `raw/sources/`, extracted text into
  `results/literature/ingest-2026-11-14/extracted_text/`, recorded
  identifiers and hashes in `download_manifest.json`, and the arXiv queries
  for the scoop watch in that folder's README.
- New 2026 sources: [[sources/gothelf-2026-limitations-of-approximative-phase-space-description]],
  [[sources/de-la-pena-2026-high-order-correlations-wigner-negativities-bsv-hhg]],
  [[sources/stammer-2026-photon-anti-bunching-in-hhg]],
  [[sources/stammer-2026-attosecond-metrology-of-bright-quantum-light]],
  [[sources/rivera-dean-2026-erasing-photons-from-bsv-via-ati]],
  [[sources/wang-2026-bright-quantum-hhg-coherent-plus-bsv-propagation]],
  [[sources/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light]],
  [[sources/kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv]].
- Supporting sources for the new claim:
  [[sources/gorlach-2023-hhg-driven-by-quantum-light-main-article]] (closes
  the gap noted since June),
  [[sources/spasibko-2017-multiphoton-effects-photon-number-fluctuations]],
  [[sources/manceau-2019-indefinite-mean-pareto-photon-distribution]],
  [[sources/racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes]],
  [[sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum]],
  [[sources/riek-2017-subcycle-quantum-electrodynamics]],
  [[sources/kizmann-2019-subcycle-squeezing-time-flow-perspective]].
- Rewrote the stub
  [[sources/rivera-dean-2025-propagation-of-intense-squeezed-vacuum-light-in-non]]
  as a full summary.
- Not obtained: "Theory of high-harmonic generation with quantum light"
  (Phys. Rev. Research, doi 10.1103/y3gr-tsns) and the Nature Communications
  version of the Rivera-Dean propagation paper.
- Findings that shaped the plan: the second-harmonic enhancement by BSV was
  measured as 2.86 +- 0.08 and harmonic energy distributions were recorded
  shot by shot (Spasibko 2017, Manceau 2019), so the new part of the claim is
  the field, not the energy; real femtosecond BSV has about 1.5 to 2 temporal
  modes (Gholam-Mirzaei 2026, Kern 2026); a rectified transient from a 3.5 nJ
  coherent pump was read with a single-shot signal-to-noise ratio near 12
  (Riek 2017); the classical-mixture description cannot give squeezing or
  antibunching of the output when the response to a coherent driver is
  coherent (Gothelf 2026).
- Updated [[index]], [[overview]], [[research-agenda]],
  [[theory/bsv-even-order-response-moment-scaling]], and
  [[models/thz-optical-rectification-model]].
- Corrected an error from the June ingest found by cross-reading:
  [[sources/rasputnyi-2024-hhg-bsv]] named the first author "Ivan"; the PDF
  says Andrei Rasputnyi. Full author list added.

## [2026-11-14] simulation | BSV Optical Rectification THz Statistics

- Added the spec [[simulations/bsv-optical-rectification-thz-statistics]],
  the module `code/src/stochastic_em_theory/optical_rectification.py`, and 21
  tests, including an explicit two-mode Fock-space check of the Wick
  decomposition and a Husimi-Q sampling check of the phase-space comparison.
- Run `results/runs/20261114-bsv-or-thz-statistics/`: one bright mode gives
  THz energy 3 times the coherent-pump value and an energy fluctuation ratio
  of 35/3; `K` equal modes give `1 + 2/K` and Gamma-distributed single-shot
  amplitudes with shape `K/2`; the spontaneous term overtakes the
  classical-noise terms at `Omega / sigma = 7.7` for `nbar = 1e6`.
- Sampler cross-check, 200,000 shots, seed 20261114: no negative amplitudes;
  mode number recovered from skewness and kurtosis within 2 %.

## [2026-11-14] query | Source Parameters And Framing Of A Theory Paper

- The author stated the source and detection: BSV at 1600 nm, about 3
  microjoules, about 100 fs, 1 kHz, `g2` about 1.2 unfiltered; THz from DAST,
  sampled in ZnTe with an 800 nm, 100 fs probe; single-shot acquisition being
  built. Recorded in [[experiments/bsv-or-thz-dast-znte-setup]] with the
  predictions of [[theory/quantum-optical-rectification-of-bsv]] for them:
  `K = 10`; THz field fluctuation 45 %, Gamma shape 5, skewness 0.89, excess
  kurtosis 1.2; mean THz energy 1.2 times the coherent-pump value; energy
  fluctuation ratio 1.87; ordering corrections of order `4e-13`.
- Noted that the higher cumulants depend on the distribution of Schmidt
  weights, not only on `K`: geometric weights with the same `K` give
  skewness 1.19 and excess kurtosis 2.38.
- Question: how to frame a theory paper that precedes the experimental one.
  Answer filed as `paper/theory-paper-outline.md`: lead with the exactly
  solvable model and the closed-form comparison of descriptions, not with
  the effect; Physical Review A regular article recommended over Applied
  Physics Letters; leave the observation, emulator, and parity demonstration
  to the experimental paper; submit without posting to arXiv or secure the
  averaged trace first. Recorded as an undecided option in
  [[prl-restructuring-plan]].
- Added `wiki/experiments/` to the directory contract in `AGENTS.md`.

## [2026-11-14] query | Full-Beam g2 Confirmed; Optica As Venue For The Theory Paper

- The author confirmed that the stated `g2` of about 1.2 is the full-beam
  value. [[experiments/bsv-or-thz-dast-znte-setup]] and
  [[prl-restructuring-plan]] updated: `K` about 10 applies at the crystal and
  the 45 % field fluctuation no longer rests on an assumption about the
  detector. Equal mode weights remain an assumption for the higher cumulants.
- Question: is the theory paper suitable for Optica. Answer recorded in
  `paper/theory-paper-outline.md`: not recommended for the theory alone;
  Optica's published criteria accept theory but require broad interest and
  high impact; keep Optica (or Physical Review Letters) for the experimental
  paper; Physical Review A, Optics Letters, or JOSA B for the theory. Based on
  the journal's criteria pages as returned by a web search on this date.

## [2026-11-14] query | Measurement Programme For The Experimental Paper

- Question: which practical measurements to make for a high-impact
  experimental paper (Nature Photonics as the reach target). Answer filed in
  [[experiments/bsv-or-thz-dast-znte-setup]], section "Measurement
  Programme": core demonstration (averaged waveform, field against shot
  energy, histogram and cumulants); noise against delay across the waveform,
  separating photon-number noise from burst timing jitter; mode-number scan
  with predicted values for `K` of 10, 2, and 1; squeezed against thermal
  statistics from the same source; classical emulator; twin-beam heralding;
  one use of the source.
- New prediction recorded: for pure photon-number noise the rms THz field
  follows the mean waveform and vanishes at its zero crossings; burst timing
  jitter adds a term proportional to the slope (25 fs gives 0.31 of the peak
  field at 2 THz).
- Assessment recorded: Nature Photonics is a long shot for this physics; the
  same data set supports Optica or Physical Review Letters.

## [2026-11-14] simulation | THz Waveform Noise Against Delay

- Added the spec [[simulations/thz-waveform-noise-against-delay]], the module
  `code/src/stochastic_em_theory/thz_waveform_noise.py`, 11 tests, and the
  run `results/runs/20261114-thz-waveform-noise-against-delay/`.
- Result: `Var E(t) / <N>^2 = A gbar^2 + B (gbar'^2 - gbar gbar'') +
  2 C gbar gbar'` with `A = 2 / K` and, for a Gaussian Schell-model pulse,
  `B = (2 / K)(T^2 / 2)(1 - 1 / K_t^2)`. Exact form: a filtered `|G1|^2`.
  Added to [[theory/quantum-optical-rectification-of-bsv]] as equations (13)
  and (14).
- Correction recorded: the first form of the expansion, written into
  [[experiments/bsv-or-thz-dast-znte-setup]] earlier the same day, had
  `B gbar'^2` only and quoted 25 fs of jitter as an illustration. A template
  fit test failed by 5 % in `A`, which exposed the missing `gbar gbar''`
  term. The zero-crossing noise is unchanged by the correction; the model
  value of the arrival-time jitter for the author's source is at most 13 fs,
  not 25 fs. Setup page updated.
- For `K = 10` and a 100 fs pump: rms at the waveform peak 0.45 to 0.47 of
  the peak field for every split of `K`; rms at the zero crossing 0, 0.13,
  and 0.15 for one, two, and five temporal modes; single-shot arrival time
  recovered with 3.7 fs rms error at a signal-to-noise ratio of 30.
- Practical cautions recorded: pump-probe timing jitter has the same
  signature as the timing term; 800 nm energy noise is amplified by the
  parametric gain, about fifteenfold.


## [2026-11-19] paper | PRA-Style Theory Note Drafted

- Request: write a Physical Review A style theory note of the project based
  on the new assessment.
- Written: `paper/theory-note/theory-note.tex` (REVTeX 4.2; 10 pages, 3
  figures, 1 table, 30 references), compiled PDF, `refs.bib`, figures with a
  manifest, and [paper/theory-note/README.md](../paper/theory-note/README.md)
  with the open items. Title: "Quantum theory of optical rectification with a
  quantized pump: terahertz fields driven by bright squeezed vacuum".
- New result found while writing, now the first claim of the note: for a
  coupling that is flat across the pump band and negligible pump dispersion,
  the model is exactly solvable for any multimode pump state. The photon flux
  commutes with itself at different times, the Magnus series ends at second
  order, `b_out = b_in - i zeta N` holds to all orders, the flux is conserved,
  and the THz state is a mixture of coherent states weighted by the pump's
  photon arrival-time distribution. Recorded in
  [[theory/quantum-optical-rectification-of-bsv]], section "Exact Solution For
  A Multimode Pump".
- Also new: spontaneous difference-frequency term identified as rectified
  photon shot noise; closed-form flux spectrum for a Gaussian Schell-model
  pump; pump phase modulation by the mean of input and output THz fields.
- Corrections to earlier wiki statements, made on the pages concerned:
  1. "Two small parameters, `1/nbar` and `B nbar`" was wrong for the THz
     statistics, which are exact in the coupling; `B nbar` governs the pump
     back-action only (theory page, "Validity").
  2. Photon-number resolution by the THz field is `1/(2 sqrt(B))`, not
     `1/sqrt(B)` (theory page).
  3. Shots for the third-cumulant test: the formula of 2026-11-14 kept only
     the Gaussian part of the sampling variance. Full form
     `N = z^2 [0.75 K u^3 + 13.5 u + 9 + 60/K]`, `u = 1 + 1/rho^2`, checked by
     Monte Carlo; "a few hundred shots" becomes about a thousand
     ([[prl-restructuring-plan]]).
  4. A first version of the pump phase relation, written and corrected within
     this session, lacked the flux-dependent term; the numerical check fails
     by 0.03 to 0.09 without it.
- Citations in the note were checked against the source pages. Two were
  reworded because the source did not support the first wording: the Ravi
  2014 thesis is about cascading limits, not thin-crystal assumptions; the
  Wang 2026 harmonic paper is not a source for published BSV pulse energies.
- Not done, listed in the README: crystal-specific THz response, independent
  re-derivation, numerical check with a phase mismatch, seven references with
  incomplete or unchecked bibliographic data.

## [2026-11-19] simulation | Exactness Checks And Theory-Note Figures

- Tests added to `code/tests/test_optical_rectification.py`: input-output
  relation and flux conservation beyond first order, and the pump
  phase-modulation relation, both against a full matrix exponential in a
  frequency-ladder model with two pump photons. Test added to
  `code/tests/test_thz_waveform_noise.py` for the closed-form flux spectrum.
  Suite: 94 passed.
- `code/scripts/make_theory_note_figures.py` writes
  `paper/theory-note/figures/` with `manifest.yaml` (commit f6556ab, seed
  20261119). Closed forms and the exact variance formula only; five sampled
  shots in one panel. The THz response is the model response of
  [[simulations/thz-waveform-noise-against-delay]], not a crystal response.
- No new run directory under `results/runs/`: the figures restate results of
  the two 2026-11-14 optical-rectification runs with the closed-form
  spectrum added.

## [2026-11-19] query | Rectification Against Quantized DFG And SFG Theory

- Question from the author: what is the key difference between the quantized
  rectification theory and the quantized DFG/SFG theory.
- Answer filed in [[theory/quantum-optical-rectification-of-bsv]], section
  "Relation To Quantized DFG, SFG And Parametric Down-Conversion": same
  trilinear Hamiltonian, different regime, decided by the commutator of the
  source operator with its conjugate. Stokes only: negative, exponential gain
  (parametric amplifier). Anti-Stokes only: positive, periodic exchange
  (frequency conversion). Both with equal weight: zero, the source is
  conserved, linear growth (rectification). Rectification of a femtosecond
  pulse is the unresolved-sideband case; the condition is
  `k'' Omega Delta omega L << 1`.
- Consequences recorded: the THz field copies the photon flux and not a field
  amplitude; Gaussian in gives non-Gaussian out; exact solution with a
  quantized pump because no mode is depleted; no parametric gain, so vacuum
  emission is the shot-noise term only.
- The note gained Sec. II D with the same content
  (`paper/theory-note/theory-note.tex`).
- Source check: the sideband classification in cavity electro-optics was read
  from the arXiv abstracts of Tsang 2010 and 2011, not from the papers.

## [2026-11-19] query | Exact Solution Derived From The Hamiltonian

- Request from the author: derive the exact solution from the Hamiltonian.
- Written: `paper/theory-note/derivation.tex` and PDF (9 pages), each step
  marked as identity or approximation. Starting point: interaction energy
  `-integral P_OR E_T dV` with continuum field operators; result (E12), (E13)
  on [[theory/quantum-optical-rectification-of-bsv]].
- New in the derivation: the explicit coupling constant
  `kappa = (chi2 omega_0 / (n_o c)) sqrt[hbar Omega / (4 pi eps0 c n_T A)]`,
  checked against the classical rectification formula (magnitude and phase);
  a two-line Heisenberg derivation of `b_out = b_in - i zeta N`; the same
  result from the classical-source (driven-oscillator) argument in each
  photon-arrival sector.
- Finding recorded: time ordering of `H_int(t)` and `z` ordering of `G(z)`
  give the same displacement operator; the kernel of the flux phase differs
  by a term local in time (instantaneous Kerr type), shown for a
  dispersionless THz index. The note's results for the THz field do not
  depend on it.
- Limitation recorded: the field normalization at the carrier is needed for
  the flux to commute with itself; corrections are of order
  `Omega / omega_0`.
- Test added: evolution operator with a phase mismatch against the exact
  `z`-ordered evolution (closes the open item of the same day). Suite: 95
  passed.
- The note gained the explicit `kappa` (Sec. II A), a derivation of the
  generator and the ordering remark (Appendix A), and the mismatch check
  (Appendix E).
- All five references of the derivation are from memory and marked so.

## [2026-11-19] query | Prior Art And Physical Picture For The Exact Solution

- Questions from the author: a physical intuition for the exact
  solvability, and whether anyone has shown it before.
- Search: 26 arXiv queries and 9 web searches; record with scope and limits
  in `results/literature/prior-art-2026-11-19/README.md`. No paper found on
  optical rectification or THz emission with a quantized pump that gives the
  state of the emitted field.
- Contradiction with earlier project statements, recorded on
  [[theory/quantum-optical-rectification-of-bsv]] ("Prior Art For The Exact
  Solution") and in the note's README: the exact solvability was presented
  as a new result. The mechanism is known: Blow, Loudon, Phoenix 1991 (exact
  quantum self-phase modulation); Boivin, Kaertner, Haus 1994 (field coupled
  to localized oscillators, closed-form Heisenberg solution); Shapiro and
  Razavi 2007 (continuous-time cross-phase modulation); single-mode
  optomechanics. Close perturbative work: Guedes et al. 2022 (back action in
  electro-optic sampling), Glerean et al. 2019 (quantum impulsive stimulated
  Raman scattering); finite-ladder electro-optic model: Miroshnichenko et
  al. 2017.
- Changed: introduction of `paper/theory-note/theory-note.tex` ("Three
  elements are not new"), Sec. II B and II C citations, seven references
  added; a section on known exact solutions in `derivation.tex`; a
  correction note in `paper/theory-paper-outline.md`.
- Limits: the 1991 and 1994 papers were seen as abstracts only; none of the
  papers is ingested. Reading the two full texts is listed as a task before
  submission.
- Physical picture recorded on the theory page: the THz field depends only
  on photon arrival times, which its emission does not change without
  dispersion.

## [2026-11-19] query | What Is New In The THz Paper

- Question from the author after the prior-art correction. Ranked answer
  filed in `paper/theory-paper-outline.md`, section "What Is New, After The
  Prior-Art Search": the effect and its field-level statistics; noise
  against delay and the temporal mode number; the multimode rule; the exact
  benchmark for a BSV driver; the exact emitted state with the coupling in
  crystal parameters; numbers for existing sources.
- The note's abstract was brought in line with its introduction: the model
  "belongs to a class of exactly solvable models known from the quantum
  theory of self-phase modulation".

## [2026-11-19] decision | Venue Ranking For The Theory Paper

- Question from the author: PRL, PRX Quantum, Optica Quantum, Optics Letters,
  JOSA, or another venue.
- Recommendation recorded in `paper/theory-paper-outline.md`, "Venue":
  Physical Review A (Letter if cut to about five pages, otherwise the regular
  article as drafted); Optics Letters as the alternative; JOSA B as fallback;
  not PRL, PRX Quantum, or Optica Quantum for the theory alone. PRL or Optica
  stays the target for the experimental paper. The author has not decided.

## [2026-11-20] paper | Detailed Derivation Of Eqs. (7) To (14) Of The Theory Note

- Request from the author: a note with the detailed derivation of
  Eqs. (7) to (14). Read as the equations of the theory note (version of
  2026-11-19, commit b27e52b): evolution operator `U = exp(i Phi) D`, `D`,
  `zeta`, `b_out`, flux conservation, `a_out = exp(-i theta_tot) a_in`, the
  phase at perfect phase matching, and the THz phase operator `F`.
- Written: `paper/theory-note/derivation-eq7-14.tex` and PDF (13 pages).
  Starts from the generator, proves eight commutator lemmas and three
  operator identities, and derives each target equation with all
  intermediate steps. The evolution operator is proved by differentiation,
  without relying on the Magnus theorem.
- Three checks added that were not written down before: (1) the canonical
  commutator of the output pump operators, which holds only because the
  flux-dependent phase has the coefficient that cancels the commutator of
  the noise operator; (2) the energy balance, pump red shift equal to the
  THz energy, with the shot-noise part arising from the commutator of the
  THz field with itself; (3) one pump photon, which radiates `B_T` THz
  photons on average whatever its duration.
- No new numerical work; the note lists the four existing tests against the
  equations they check.

## [2026-11-20] paper | Derivation Reordered: Hamiltonian, Equations Of Motion, Heisenberg Solution

- Advice from the author: start with the Hamiltonian, construct the equation
  of motion of the THz field operator, solve it in the Heisenberg picture;
  update the derivation if necessary.
- Changed, theory note (`paper/theory-note/theory-note.tex`): Sec. II A now
  states the interaction Hamiltonian `H_int(t)` (Eq. 3) in place of the
  generator of propagation in `z`. Sec. II B is "Equations of motion and
  exact solution": flux conserved (6); Heisenberg equation of the THz
  operator (7) and its solution (8), (9); Heisenberg equation of the pump
  operator (10) and its solution (11) to (13); evolution operator last (14),
  (15). Appendix A rewritten: Hamiltonian, phase of the pump, evolution
  operator, propagation picture. Equation numbers after Sec. II B moved up
  by one; the shot-count formula is now Eq. (35).
- Changed, detailed derivation: rewritten in the same order and renamed
  from `derivation-eq7-14` to `derivation-exact-solution` (15 pages). It
  starts from `H = H_0 + H_int` in the Schroedinger picture and derives the
  three Heisenberg equations (flux, THz operator, pump operator), solves them
  in turn, and constructs the evolution operator at the end. Target
  equations are tagged with the note's new numbers; a table maps them to the
  numbers of 2026-11-19.
- New statement obtained on the way: the phase of the pump is the THz field
  integrated along the path of the slice through the crystal, plus a
  constant; recorded as (E17) on
  [[theory/quantum-optical-rectification-of-bsv]].
- Qualification now explicit in the note: with the time-ordered Hamiltonian
  the remainder of the pump phase has the kernel `W`, not `V`; at perfect
  phase matching the phase is the average of input and output fields up to
  an instantaneous Kerr-type term that the model does not determine. The
  numerical test of the phase-mismatched evolution operator is for the
  propagation picture (kernel `V`).
- No change to the THz results, the statistics, the figures, or the tests
  (95 passed, unchanged).

## [2026-11-21] query | Derivation Starting In The Frequency Domain

- Question from the author: can the theory be derived starting in the
  frequency domain, so that it becomes more tractable.
- Answer: yes for the Hamiltonian, the solvability condition, the THz field,
  and the evolution operator; no for the pump and the THz state, which are
  simpler in the time domain. Written as
  `paper/theory-note/derivation-frequency-domain.tex` and PDF (9 pages);
  formulas (E18) to (E21) on
  [[theory/quantum-optical-rectification-of-bsv]].
- New in this form: the amplitude is the coupling function on the energy
  shell, `zeta = 2 pi g(Omega, Omega)`; the flux phase is a principal-value
  integral over the off-shell coupling; the propagation picture is the
  approximation that evaluates the coupling strength on the shell.
- Correction recorded: the instantaneous Kerr-type term (the difference
  between time ordering and ordering in `z`) comes from the frequency
  dependence of `kappa^2` across the phase-matching width, not from the
  terms that do not conserve energy. A first guess in the session attributed
  it to the latter; the numerical integration showed their contribution is
  small and independent of the crystal length.
- Test added (off-shell phase; principal-value identity and the full
  coefficient for a dispersionless THz index). Suite: 96 passed. This is the
  first numerical check of the time-ordered form, which was analytic only.
- The theory note itself was not changed. Recommendation recorded in the
  new document: start Sec. II in the frequency domain and change to the time
  domain after the THz output. The author has not decided.

## [2026-11-21] paper | Theory Note Sec. II Rewritten In The Hybrid Form

- Decision by the author: adopt the recommended hybrid presentation.
- Changed, `paper/theory-note/theory-note.tex` (13 pages): Sec. II A is the
  three-wave-mixing Hamiltonian in the frequency domain, Eqs. (1) to (6),
  with the flat-coupling assumption as Eq. (4). Sec. II B: commutation of
  `N(Omega)` (7), conservation (8), THz equation of motion as a driven
  oscillator (9), output (10) with `zeta = 2 pi g(Omega, Omega)` (11); then
  the envelope and flux in the time domain (12), (13), pump equation and
  phase (14) to (17); evolution operator (18), (19) described as on-shell
  displacement plus off-shell phase. Sec. II C unchanged. Sec. II D now
  refers to the coupling function. Appendix A rewritten: time-domain
  Hamiltonian (A1), sideband ladder (A2), path integral of the THz field
  (A3) to (A5), principal-value form of the flux phase (A6), on-shell
  approximation and propagation picture (A7) to (A9). Appendix E mentions
  the numerical evaluation of (A6).
- Equation numbers: solution block (8) to (19); later equations moved up by
  four; shot-count formula is Eq. (39).
- Companion derivations retagged to the new numbers
  (`derivation-exact-solution`, `derivation-frequency-domain`), with a table
  of the numbers in the versions of 2026-11-20 and 2026-11-19;
  cross-references in `derivation.tex` updated.
- Added to the frequency-domain derivation and recorded on
  [[theory/quantum-optical-rectification-of-bsv]]: an estimate of the
  backward-wave contribution to the Kerr-type phase, about half the forward
  constant, not checked numerically.
- No change to results, figures, or tests (96 passed).

## [2026-11-23] query | Photon-Arrival Picture: What It Is And Why The Note Needs It

- Question from the author. Answer given in the session; the note's
  Sec. II C gained a lead-in that states its purpose: the input-output
  relation gives all moments, and the state is needed for three statements,
  the THz waveform of a single shot, the classicality of the emitted field,
  and the meaning of the noise term linear in the photon number.
- Also added there: the picture is a choice of basis (outcomes of ideal
  time-resolved photon counting), not an assignment of arrival times to
  photons; the superposition becomes a mixture because the interaction
  leaves the configuration unchanged.
- Recorded assessment: the picture is not needed for the Hamiltonian, the
  THz output relation, or the moments, cumulants and spectrum of Secs. III
  and IV; it is needed for the state, the single-shot distribution and the
  detection model, and the identification of rectified shot noise.
