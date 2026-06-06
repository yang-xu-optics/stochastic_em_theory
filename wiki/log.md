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
