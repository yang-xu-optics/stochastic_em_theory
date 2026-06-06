---
title: Wiki Log
type: synthesis
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [log]
source_count: 14
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
