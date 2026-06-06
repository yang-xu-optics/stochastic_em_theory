---
title: Paper One Correspondence HHG Simulation Spec
type: simulation
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [paper-one, squeezed-vacuum, validation, hhg]
source_count: 54
confidence: high
related:
  - ../theory/stochastic-quantum-optics-correspondence
  - ../theory/squeezed-vacuum-g2-proof-plan
  - ../theory/non-gaussian-output-novelty
  - ../models/hhg-gas-model
  - simulation-roadmap
---

# Paper One Correspondence HHG Simulation Spec

## Goal

Produce reproducible simulations for the correspondence-first HHG paper:

1. validate squeezed-vacuum stochastic sampling against exact input-field quantum optics diagnostics,
2. show why Wigner-to-normal ordering corrections are required for photon-counting `g^(2)(0)`,
3. add a mode-filtered validation that makes mode definition explicit,
4. record the BSV source-model family used to generate each ensemble,
5. drive HHG intensity-level observables with the validated stochastic ensemble,
6. retain per-shot HHG metadata for ionization, cutoff, bunching, and symmetry diagnostics,
7. add a pre-HHG ATI/photon-statistics validation branch for coherent, thermal, and BSV ensembles,
8. add a separate squeezed-emission-mode boundary model for selected harmonic channels,
9. label every output with the mechanism family and claim-ladder level it supports.

## Units

- Single-mode and mode-filtered validation use dimensionless oscillator units.
- HHG proxy outputs use atomic units for field amplitude, angular frequency, ionization potential, and cutoff energy.
- Result manifests must state the units used by each run.

## Random Seed Strategy

- Every validation or ensemble run accepts an integer seed.
- Every result directory stores the seed in `manifest.yaml`.
- Tests use fixed seeds and broad statistical tolerances; paper runs use larger sample counts and record Monte Carlo uncertainty.

## Stage A: Single-Mode Validation

Observable targets:

```text
<n> = sinh^2(r)
g^(2)(0) = 3 + 1/<n>
```

Wigner estimators:

```text
<a^dagger a> = <|alpha|^2>_W - 1/2
<a^dagger a^dagger a a> =
  <|alpha|^4>_W - 2 <|alpha|^2>_W + 1/2
```

Outputs:

- CSV with `r`, analytic `<n>`, estimated `<n>`, corrected `g2`, naive `g2`, standard errors.
- Figure showing corrected and naive `g2` against analytic target.
- Manifest with claim level `exact_input_correspondence`.

## Stage B: Mode-Filtered Validation

Use independent equal squeezed modes as a controlled mode-filtered validation. For `M` equal modes with per-mode mean photon number `n`, the total photon-counting target is:

```text
g_total^(2)(0) = 1 + 2/M + 1/(M n)
```

Record the source-model family for each run:

```text
single_mode
equal_mode
schmidt_mode
two_color_twin_beam
propagated_nongaussian_frontier
```

Outputs:

- CSV with `M`, per-mode `r`, analytic total `g2`, estimated total `g2`, and standard error.
- Figure showing the transition from single-mode superbunching toward the multimode limit.
- Manifest with claim level `exact_input_correspondence`.
- Source-model summary with effective mode count and source references.

## Stage C: HHG Intensity Pipeline

Use the validated ensemble to drive intensity-level HHG observables. The first implementation uses a fast cutoff-weighted HHG proxy to test ensemble averaging, conditional spectra, per-shot records, result manifests, and figure generation. The 1D soft-core split-operator utilities are implemented and tested as the first physics-fidelity upgrade.

Supported paper-one observables:

- ensemble mean HHG spectrum,
- conditional spectra binned by sampled drive intensity,
- ionization/tunneling proxy distributions,
- cutoff distribution,
- shot-to-shot variance,
- per-shot driver quadratures, intensity, phase, ionization proxy, cutoff proxy,
  harmonic amplitudes, and harmonic phases,
- convergence versus ensemble size.

## Stage D: ATI/Photon-Statistics Validation

Before full HHG recombination modeling, validate the upstream ionization step
using coherent, thermal, and BSV photon-statistics ensembles. This branch is
inspired by Lyu 2025 and uses diagonal coherent-component averaging:

```text
W(p) = integral dE_alpha P(E_alpha) |M_alpha(p)|^2
```

The first implementation uses ionization-rate and electron-number proxies, not
a quantitative qSFA momentum solver.

Outputs:

- CSV comparing coherent, thermal, and BSV sampled ensembles at matched mean
  intensity.
- Estimated `g2` hierarchy:

```text
g2_coherent = 1
g2_thermal = 2
g2_BSV = 3
```

- Ionization-yield enhancement and electron-number bunching proxies.
- Manifest with mechanism family `ati_photon_statistics`.

## Stage E: Squeezed Emission-Mode Environment Boundary Model

Model Wang 2024 as a separate mechanism from BSV pump sampling. For a selected
harmonic mode, use:

```text
mu_k(t) = cosh(r_k) + sinh(r_k) exp[-i(2 omega_k t - theta_k)]
```

and compare the targeted-channel amplitude with and without `mu_k(t)`.

Outputs:

- CSV over squeezing angle for one selected harmonic order.
- Figure or summary showing modulation of the targeted harmonic amplitude.
- Manifest with mechanism family `squeezed_emission_mode_environment`.

## Unsupported paper-one claims

- emitted harmonic Wigner negativity,
- full harmonic quantum-state reconstruction,
- macroscopic propagation,
- non-Gaussian quantum-output certification.

## Result Manifest Fields

Each run writes:

```yaml
run_id: YYYYMMDD-short-name
created: YYYY-MM-DD
claim_level: exact_input_correspondence | hhg_intensity_prediction
mechanism:
source_model:
code_entrypoint:
git_commit:
parameter_file:
random_seeds:
observable:
units:
notes:
```
