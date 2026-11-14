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

