# Code Workspace

Implementation code for stochastic-field samplers, validation tests, HHG
models, and THz emission simulations belongs here.

## Local Setup

```bash
cd code
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
python3 -m pytest
```

Generated run outputs belong under `../results/runs/`. Paper-ready figures
belong under `../results/figures/`.
