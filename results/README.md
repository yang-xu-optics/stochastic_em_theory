# Results Workspace

Generated outputs only. Nothing here is edited by hand except the README
files.

- `runs/`: one directory per simulation run, each with a `manifest.yaml`
  (commit hash, seed, parameters, entry point). [runs/README.md](runs/README.md)
  is the run index and says which runs are current, superseded, or not usable
  for the paper.
- `figures/`: paper-ready figures only. Empty until a run passes the
  convergence and comparison checks listed in the run index.
- `literature/`: literature-search API responses, download manifests, and
  text extracted from the PDFs in `../raw/sources/`.
- `tmp/`: scratch outputs such as smoke runs. Ignored by git.

Name new run directories `YYYYMMDD-short-name`.
