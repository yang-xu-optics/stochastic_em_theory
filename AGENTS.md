# AGENTS.md

Operating schema for coding agents (Codex, Claude Code) in this research
workspace. This file is the single canonical copy; `CLAUDE.md` only imports it.

This project follows the LLM Wiki pattern described by Andrej Karpathy:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

The aim is to maintain a persistent, compounding research wiki for papers on
emission driven by bright squeezed vacuum (BSV): first a Letter on THz
generation by optical rectification of BSV, then a companion paper on
stochastic-field descriptions of high harmonic generation and plasma THz
emission.

## Mission

Headline claim since 2026-11-14 (Letter, target Physical Review Letters):

> Optical rectification turns a zero-mean bright squeezed vacuum pulse into a
> phase-stable THz transient whose single-shot field is proportional to the
> pump photon number. The THz field therefore carries the photon-number
> statistics of squeezed vacuum. A fully quantum model gives this exactly; a
> classical Gaussian amplitude-noise model reproduces it up to corrections of
> order `1/<n>`; a single-shot electro-optic-sampling experiment tests it.

The Letter has three parts: the quantum description, its classical-noise limit
with an error bound, and the measurement on the author's BSV source. The plan
is `wiki/prl-restructuring-plan.md`; the linear argument is `paper/outline.md`.

Companion paper (after the Letter; plan in `paper/companion-outline.md`),
built on the original three claims:

1. Stochastic electromagnetic field theory can reproduce standard quantum
   optics diagnostics of squeezed vacuum when the stochastic variables,
   operator ordering, and detection model are matched correctly.
2. The same stochastic-field description can drive classical or semiclassical
   simulations of high harmonic generation in gas.
3. The framework can be extended to THz emission through optical rectification
   and plasma photocurrent mechanisms.

## Directory Contract

- `raw/`: immutable source layer. Put papers, articles, notes, downloaded
  figures, and datasets here. Agents may read this folder but must not alter,
  rename, or delete source files once added.
- `raw/sources/`: source documents, preferably with stable filenames.
- `raw/assets/`: figures and other downloaded media referenced by sources.
- `raw/data/`: experimental shot records from the BSV source, one dated
  folder per acquisition with a README of the acquisition settings. Immutable
  once added, like every other file under `raw/`.
- `wiki/`: agent-maintained knowledge layer. This is the working synthesis.
- `wiki/index.md`: content index. Read this first for research queries.
- `wiki/log.md`: append-only chronological work log.
- `wiki/project-status-review.md`: latest evaluation of progress, result
  quality, and publication strategy. Read it before planning new work.
- `wiki/theory/`: mathematical correspondence, proofs, definitions,
  conventions, and open theoretical issues.
- `wiki/models/`: physical models for HHG and THz mechanisms.
- `wiki/simulations/`: numerical roadmaps, experiment specifications, and
  validation criteria.
- `wiki/sources/`: one source-summary page per unique document in
  `raw/sources/`.
- `code/`: implementation workspace for samplers, simulations, notebooks, and
  tests.
- `results/`: generated outputs.
- `results/runs/`: one directory per simulation run, each with a manifest.
  `results/runs/README.md` is the run index and records which runs are
  current, superseded, or not usable for the paper.
- `results/figures/`: paper-ready figures only.
- `results/literature/`: literature-search API dumps, download manifests, and
  text extracted from source PDFs.
- `results/tmp/`: scratch outputs; ignored by git.
- `paper/`: manuscript outline, drafts, figure plans, and submission notes.
  `paper/outline.md` is the Letter; `paper/companion-outline.md` is the
  companion paper.
- `archive/`: historical planning documents and notes that do not belong to
  this project. Nothing here is maintained; do not treat it as current.

Do not create a duplicate folder if an equivalent one exists. Prefer updating
the closest existing page over adding a near-duplicate page.

## Wiki Page Format

Use kebab-case filenames. New wiki pages should start with YAML frontmatter:

```yaml
---
title: Page Title
type: concept | model | source-summary | simulation | synthesis | question
status: seed | draft | active | stale | contradicted | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
source_count: 0
confidence: low | medium | high
related: []
---
```

Use Obsidian-style links for internal references, for example
`[[theory/squeezed-vacuum-g2-proof-plan]]`.

## Source and Claim Discipline

- Treat `raw/` as the source of truth.
- When ingesting a source, create or update a source-summary page under
  `wiki/sources/` only if that folder is needed. Until sources exist, keep
  source-backed claims out of source-summary pages.
- Every nontrivial physics claim in the wiki should eventually be traceable to
  a source, a derivation page, or a simulation result.
- Mark unsourced initial ideas as "seed" and keep confidence low.
- If a new source contradicts an existing page, update both pages and record the
  contradiction in `wiki/log.md`.
- Prefer equations and assumptions over prose-only summaries.

## Operations

### Ingest

When the user adds a source to `raw/sources/` and asks for ingest:

1. Read `wiki/index.md` and `wiki/log.md`.
2. Read the new source from `raw/sources/`.
3. Create a source-summary page with bibliographic metadata, core results,
   equations, assumptions, limitations, and relevance to this project.
4. Update all relevant concept/model/simulation pages.
5. Update `wiki/index.md`.
6. Append one `## [YYYY-MM-DD] ingest | Source Title` entry to `wiki/log.md`.

### Query

For research questions:

1. Read `wiki/index.md`.
2. Read the most relevant wiki pages before answering.
3. If the answer creates durable synthesis, file it as a new wiki page or update
   an existing page.
4. Append a concise query entry to `wiki/log.md` when durable wiki changes are
   made.

### Lint

When asked to lint or health-check the wiki, inspect for:

- contradictions between pages,
- stale or unsourced claims,
- missing cross-references,
- orphan pages,
- concepts mentioned repeatedly without their own page,
- simulation plans that lack validation observables,
- results that lack run manifests or parameter files.

### Simulation Work

Before implementing a numerical simulation:

1. Write or update a simulation spec under `wiki/simulations/`.
2. State the observable, model equations, units, stochastic ensemble, random
   seed strategy, convergence tests, and expected limiting cases.
3. Keep code in `code/`; keep generated outputs in `results/`.
4. Every result directory should contain a manifest with commit hash if
   available, parameter file, random seeds, code entry point, and brief notes.
5. Add or update tests when implementing reusable code.

### Paper Work

The manuscript lives in `paper/`. The wiki should hold evolving synthesis; the
paper folder should hold the linear argument, figure plan, and drafts. When a
wiki page becomes part of the manuscript, link it from `paper/outline.md`.

## Physics Guardrails

- Always specify the field representation: Wigner, positive-P, Glauber-Sudarshan
  P, semiclassical random process, or another representation.
- Do not equate stochastic intensity moments with normally ordered photon
  correlations unless the ordering correction has been derived.
- For squeezed vacuum, track the mode count, squeezing parameter `r`, squeezing
  phase, displacement, loss, detection bandwidth, and temporal mode definition.
- For a single-mode pure squeezed vacuum seed target, the quantum optics result
  is `g^{(2)}(0) = 3 + 1/<n>` with `<n> = sinh^2(r)`. Treat this as a proof
  target, not as a replacement for the derivation.
- For multimode bright squeezed vacuum, define the measured mode basis and
  detection model before quoting any `g^{(2)}` value.
- For HHG, distinguish single-atom response, macroscopic propagation, phase
  matching, ionization depletion, and detector averaging.
- For optical rectification, track whether the low-frequency polarization comes
  from `chi^(2)`, cascaded effects, or effective symmetry breaking.
- For optical rectification of BSV, state the Schmidt number `K` of the pump
  with every statistic, say whether a moment is of the THz field or of the THz
  energy, and say whether a photon-number moment is ordinary or normally
  ordered. Bright-limit values (`1 + 2/K`, `35/3`) are limits, not identities.
- Do not call the generated THz field nonclassical because it is bunched or
  non-Gaussian. In the first-order model its P function is positive.
- For experimental statistics with heavy tails, report the estimator and its
  uncertainty; do not quote a bare sample `g2`.
- For plasma THz emission, check symmetry carefully. A zero-mean stochastic
  optical field may produce zero ensemble-averaged current unless a mechanism
  breaks temporal or inversion symmetry.
- Record units on every equation and simulation parameter file.

## Naming and Logging

Use append-only log headings in this exact style:

```markdown
## [YYYY-MM-DD] action | Short Title
```

Valid actions include `setup`, `ingest`, `query`, `lint`, `simulation`,
`paper`, and `decision`.

