# stochastic_em_theory

Research wiki, manuscript workspace, and simulation code for a paper on
classical stochastic-field descriptions of high-harmonic generation (HHG) and
THz emission driven by squeezed vacuum light.

The repository follows the LLM Wiki pattern: immutable sources in `raw/`, an
agent-maintained synthesis in `wiki/`, and code, results, and manuscript kept
in their own folders. It is also an Obsidian vault.

## Where to start

| If you want to... | Read |
| --- | --- |
| See where the project stands and what to do next | [wiki/project-status-review.md](wiki/project-status-review.md) |
| Browse the research synthesis | [wiki/index.md](wiki/index.md) |
| See what was done and when | [wiki/log.md](wiki/log.md) |
| Read the manuscript plan | [paper/outline.md](paper/outline.md) |
| Run the code | [code/README.md](code/README.md) |
| Find a simulation output | [results/runs/README.md](results/runs/README.md) |

## Layout

```text
AGENTS.md    operating schema for coding agents (CLAUDE.md imports it)
raw/         immutable sources: 55 PDFs in sources/, published source data in assets/
wiki/        synthesis: theory/, models/, simulations/, sources/, index, log
code/        Python package, scripts, notebook, tests
results/     runs/ (simulation outputs with manifests), figures/, literature/
paper/       manuscript outline; drafts and figures go here
archive/     historical planning documents and unrelated notes; not maintained
```

`AGENTS.md` defines the directory contract, page format, and the physics
guardrails that every wiki page and simulation must follow.
