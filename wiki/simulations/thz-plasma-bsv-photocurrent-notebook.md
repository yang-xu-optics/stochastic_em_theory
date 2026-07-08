---
title: THz Plasma Photocurrent Notebook With BSV Driving
type: simulation
status: draft
created: 2026-06-10
updated: 2026-06-10
tags: [simulation, thz, plasma, photocurrent, bsv, husimi-q, notebook]
source_count: 4
confidence: medium
related:
  - ../models/thz-plasma-emission-model
  - ../theory/stochastic-quantum-optics-correspondence
  - simulation-roadmap
  - ../sources/wang-2026-quantum-thz-plasma-bsv
  - ../sources/sun-2022-thz-laser-induced-plasma
  - ../sources/schuh-2013-thz-ionization-gases
---

# THz Plasma Photocurrent Notebook With BSV Driving

Specification for the notebook
`code/notebooks/thz_plasma_bsv_photocurrent.ipynb`, implementing Stage 5 of
[[simulation-roadmap]] at the local-current level (no macroscopic propagation).

## Goal

Model plasma-photocurrent THz emission driven by a strong coherent 800 nm
fundamental plus a weak 400 nm BSV second harmonic, following the
coherent-plus-BSV setting of
[[../sources/wang-2026-quantum-thz-plasma-bsv]], with the photocurrent template
of [[../sources/sun-2022-thz-laser-induced-plasma]].

## Field Representation

- Driving-field statistics for photon-counting diagnostics: single-mode
  squeezed-vacuum **Wigner** samples with explicit symmetric-to-normal
  ordering corrections (library functions `fields.sample_single_mode_wigner`
  and `observables.estimate_single_mode_moments`).
- Driving-field ensemble for plasma dynamics: single-mode squeezed-vacuum
  **Husimi-Q** coherent amplitudes (`fields.sample_single_mode_husimi_q`),
  matching the Wang 2026 coherent-state decomposition. Each Q sample defines a
  classical waveform; observables built from `|j_alpha(omega)|^2` are
  Q-weighted coherent-component averages (diagonal approximation, as in Wang
  2026 / Lyu 2025).
- These two ensembles are not interchangeable; the notebook states which one
  feeds which observable.

## Model Equations (atomic units unless noted)

Per shot `j`, with Gaussian envelope `f(t)`:

```text
E_j(t) = f(t) [ E_w cos(w t) + eps Re(alpha_j e^{i (2 w t + theta)}) ]
dn_e/dt = w_ADK(|E_j(t)|) (N0 - n_e),  n_e analytic: N0 (1 - exp(-int w dt))
dJ/dt + nu J = n_e(t) E_j(t)            (Brunel/photocurrent, e = m = 1)
E_THz,j(t) propto [dJ/dt](t) band-limited to nu < nu_max
```

- `w_ADK`: quasi-static tunneling rate
  `w = 4 (2 Ip)^{5/2} / |E| * exp(-2 (2 Ip)^{3/2} / (3 |E|))` (hydrogen-like
  ADK form; quantitative ionization modeling is out of scope and flagged).
- `eps` converts the dimensionless mode quadrature to field amplitude; it is
  fixed by the target mean BSV intensity ratio
  `<I_2w>/I_w = eps^2 (<n>+1/2-ish ordering choice stated in-notebook) ...`
  the notebook states the exact convention it uses.
- Units: microscopic dynamics in atomic units; time axes also shown in fs and
  spectra in THz (1 a.u. time = 24.18884 as).

## Stochastic Ensemble And Seeds

- `N_shots = 400` Husimi-Q samples for dynamics; `2e6` Wigner samples for the
  `g^(2)(0)` validation (cheap, fast convergence).
- Single fixed seed via `numpy.random.default_rng(seed)`; seed recorded in the
  notebook and in the result manifest.
- Convergence check: ensemble-averaged THz spectrum computed from half versus
  full ensemble.

## Baselines

1. One-color coherent fundamental only (symmetry baseline; THz should be
   negligible).
2. Two-color coherent baseline: deterministic `E_2w` with the same mean
   intensity as the BSV component and relative phase `theta = pi/2`
   (classical photocurrent reference, nonzero mean THz field).
3. Coherent-plus-BSV ensemble (main case).

## Observables And Validation

- `g^(2)(0)` of the BSV driving mode from Wigner samples with ordering
  correction, validated against `3 + 1/<n>` with `<n> = sinh^2(r)`.
- Classical energy-fluctuation ratio of the emitted THz,
  `g2_THz = <U^2>/<U>^2` with `U = int |E_THz|^2 dt`, explicitly labeled a
  classical stochastic statistic, not a normally ordered photon correlation.
- Ensemble mean THz waveform `<E_THz(t)>` and shot-to-shot standard deviation
  band (mean field and fluctuation on one plot).
- Ensemble-averaged THz spectrum `<|E_THz(nu)|^2>` (total) and coherent part
  `|<E_THz(nu)>|^2`; incoherent part is their difference.

## Expected Limiting Cases

- One-color coherent drive: ensemble mean and per-shot THz both ~ 0.
- Two-color coherent baseline: deterministic nonzero THz waveform; coherent
  spectrum equals total spectrum.
- Zero-mean BSV second harmonic: `alpha -> -alpha` symmetry of the Q
  distribution flips the current asymmetry, so `<E_THz(t)>` should vanish
  within Monte Carlo error while `<|E_THz(nu)|^2>` stays finite: incoherent,
  thermal-like broadband THz, consistent with the bunched prediction of Wang
  2026. A near-zero mean field is a meaningful symmetry result, not a bug
  ([[../models/thz-plasma-emission-model]] symmetry check).

## Outputs

Figures and a manifest are written to
`results/<YYYYMMDD>-thz-plasma-bsv-notebook/` (manifest with seed, parameters,
entry point, commit hash if available).

## Out Of Scope

- Macroscopic propagation, phase matching, plasma shielding.
- Quantitative ADK/PPT ionization rates.
- Quantum state claims for the emitted THz mode (a positive stochastic
  ensemble cannot certify nonclassicality; see
  [[../theory/stochastic-quantum-optics-correspondence]]).
