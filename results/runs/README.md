# Run Index

One row per directory. Every directory has a `manifest.yaml` with the commit
hash, seed, parameters, and entry point. "Paper" says whether the run may be
used as evidence in the manuscript as it stands. Reasons are given in
`../../wiki/project-status-review.md`.

| Run | What it is | Status | Paper |
| --- | --- | --- | --- |
| `gorlach-2023-fig3b-proxy-20260606` | Gorlach 2023 Fig. 3b with the smooth cutoff-law proxy response | superseded | no: not a physics model |
| `gorlach-2023-fig3b-tdse-20260606` | Fig. 3b with a 9-node TDSE library, short 1.5/3/1.5-cycle pulse, odd orders only | superseded | no |
| `gorlach-2023-fig3b-tdse-fullfreq-20260606` | Fig. 3b, 11-node library, 5/15/5-cycle pulse, `E0 = 0.08` a.u., full FFT grid | superseded | no: top library node (0.341 a.u.) has a quiver radius larger than the grid |
| `gorlach-2023-fig3b-tdse-sharednorm-e006-finegrid-20260606` | Fig. 3b, 11-node library, `E0 = 0.06` a.u., 1,024-point grid, shared normalization | latest Fig. 3b run | no: library not converged; coherent and Fock drivers carry 14 % and 10 % artificial intensity noise from `nbar = 100`; figure is background-subtracted and floored |
| `gorlach-2023-fig-iv2-bsv-threshold-20260606` | Supplementary Fig. IV.2, BSV at `1e13` and `2e13 W/cm^2`, 13-node library, raw spectrum | latest unprocessed Fig. IV.2 run | no: harmonic yields differ from a 97-node library by a typical factor of 2 and up to 38 |
| `gorlach-2023-fig-iv2-bsv-threshold-tailcap-20260606` | Same, with a 0.999 intensity-tail cap and a `(9/q)^4` display rolloff | do not use | no: both steps were added to make the plot resemble the published one and change the result |
| `20260610-thz-plasma-bsv-notebook` | Plasma photocurrent THz, coherent 800 nm plus BSV 400 nm, 400 shots, `r = 1` | latest THz run | no: 400 shots, energy `g2` interval 10 to 28, finite-`n` Husimi-Q ensemble |
| `20261114-fig-iv2-library-convergence-audit` | Fig. IV.2 peak yields for 13, 25, 49, 97 library nodes, with and without the tail cap; ground-state energy check | review evidence | supporting only |
| `20261114-thz-two-color-parity-check` | Mean THz field with the BSV on the second harmonic versus on the fundamental, 4,000 shots each | review evidence | supporting only: symmetry check, not a quantitative prediction |

## Before a run may be copied to `../figures/`

1. Converged in the number of amplitude nodes (or shots), grid spacing, and
   time step, with the convergence shown in the run directory.
2. Every amplitude used lies inside what the grid can represent: quiver radius
   `E / omega^2` well below the absorber start.
3. Drive ensemble taken in the macroscopic limit, or the photon number
   justified.
4. Uncertainty band on every curve.
5. No display transform beyond one stated normalization.
6. Compared quantitatively with reference data where it exists
   (`../../raw/assets/gorlach-2023-fig3-source-data/`).

## Conventions

- New runs: `YYYYMMDD-short-name`. The six Gorlach runs predate this and keep
  their original names because their manifests record those names as `run_id`.
- The Fig. 3b output files are named `..._proxy_...` even for TDSE runs. The
  `spectrum_model` field in each manifest says which model was used.
- Directories were moved here from `results/` on 2026-11-14. Log entries
  before that date in `../../wiki/log.md` use the old paths.
