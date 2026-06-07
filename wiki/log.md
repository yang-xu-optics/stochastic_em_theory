---
title: Wiki Log
type: synthesis
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [log]
source_count: 54
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
