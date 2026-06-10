# CLAUDE.md

Codex operating schema for this research workspace.

This project follows the LLM Wiki pattern described by Andrej Karpathy:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

The aim is to maintain a persistent, compounding research wiki for a paper on
classical stochastic electrodynamics descriptions of high harmonic generation
and THz emission driven by squeezed vacuum fields.

## Mission

Develop a paper and reproducible numerical simulations around three linked
claims:

1. Stochastic electromagnetic field theory can reproduce standard quantum
   optics diagnostics of squeezed vacuum when the stochastic variables,
   operator ordering, and detection model are matched correctly.
2. The same stochastic-field description can drive classical or semiclassical
   simulations of high harmonic generation in gas.
3. The framework can be extended to THz emission through optical rectification
   and plasma photocurrent mechanisms.

## Directory Contract

- `raw/`: immutable source layer. Put papers, articles, notes, downloaded
  figures, and datasets here. Codex may read this folder but must not alter
  source files once added.
- `raw/sources/`: source documents, preferably with stable filenames.
- `raw/assets/`: figures and other downloaded media referenced by sources.
- `wiki/`: Codex-maintained knowledge layer. This is the working synthesis.
- `wiki/index.md`: content index. Read this first for research queries.
- `wiki/log.md`: append-only chronological work log.
- `wiki/theory/`: mathematical correspondence, proofs, definitions,
  conventions, and open theoretical issues.
- `wiki/models/`: physical models for HHG and THz mechanisms.
- `wiki/simulations/`: numerical roadmaps, experiment specifications, and
  validation criteria.
- `code/`: implementation workspace for samplers, simulations, notebooks, and
  tests.
- `results/`: generated outputs, figures, run manifests, and processed data.
- `paper/`: manuscript outline, drafts, figure plans, and submission notes.

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

