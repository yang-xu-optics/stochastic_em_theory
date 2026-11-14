# stochastic_em_theory

Research wiki, manuscript workspace, and simulation code for work on emission
driven by bright squeezed vacuum (BSV) light. The current target is a Letter
on THz generation by optical rectification of BSV: a phase-stable THz field
whose single-shot amplitude follows the pump photon number. A companion paper
on stochastic-field descriptions of high-harmonic generation (HHG) and plasma
THz emission comes after.

The repository follows the LLM Wiki pattern: immutable sources in `raw/`, an
agent-maintained synthesis in `wiki/`, and code, results, and manuscript kept
in their own folders. It is also an Obsidian vault.

## Where to start

| If you want to... | Read |
| --- | --- |
| See the plan to submission | [wiki/prl-restructuring-plan.md](wiki/prl-restructuring-plan.md) |
| Read the 2026-11-14 evaluation that led to it | [wiki/project-status-review.md](wiki/project-status-review.md) |
| Browse the research synthesis | [wiki/index.md](wiki/index.md) |
| See what was done and when | [wiki/log.md](wiki/log.md) |
| Read the Letter outline | [paper/outline.md](paper/outline.md) |
| Read the companion-paper outline | [paper/companion-outline.md](paper/companion-outline.md) |
| Run the code | [code/README.md](code/README.md) |
| Find a simulation output | [results/runs/README.md](results/runs/README.md) |

## Layout

```text
AGENTS.md    operating schema for coding agents (CLAUDE.md imports it)
raw/         immutable sources: 70 PDFs in sources/, published source data in assets/
wiki/        synthesis: theory/, models/, simulations/, sources/, index, log
code/        Python package, scripts, notebook, tests
results/     runs/ (simulation outputs with manifests), figures/, literature/
paper/       Letter outline and companion-paper outline; drafts and figures go here
archive/     historical planning documents and unrelated notes; not maintained
```

`AGENTS.md` defines the directory contract, page format, and the physics
guardrails that every wiki page and simulation must follow.
