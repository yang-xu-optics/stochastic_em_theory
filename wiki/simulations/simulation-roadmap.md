---
title: Simulation Roadmap
type: simulation
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [simulation, roadmap, validation]
source_count: 17
confidence: high
related:
  - ../theory/squeezed-vacuum-g2-proof-plan
  - ../theory/non-gaussian-output-novelty
  - ../models/hhg-gas-model
  - ../models/thz-optical-rectification-model
  - ../models/thz-plasma-emission-model
---

# Simulation Roadmap

## Stage 0: Project Conventions

- Choose units: SI for propagation and material response, with explicit
  conversion if atomic units are used for strong-field electron dynamics.
- Define optical field normalization and mode functions.
- Define random seed handling and reproducibility policy.
- Decide where notebooks end and reusable library code begins.

## Stage 1: Squeezed-Field Sampler

Validation observables:

- quadrature variances,
- `<n>`,
- `g^{(2)}(0)` with Wigner-to-normal ordering corrections,
- convergence versus ensemble size,
- loss and finite mode-filter tests.

Expected result for single-mode pure squeezed vacuum:

```text
g^{(2)}(0) = 3 + 1/<n>
```

### Stage 1A: Single-Mode Wigner Validation

- Sample `alpha` from the squeezed-vacuum Wigner Gaussian.
- Estimate symmetric moments.
- Convert to normal ordering:

```text
<a^\dagger a> = <|alpha|^2>_W - 1/2
<a^\dagger a^\dagger a a> =
  <|alpha|^4>_W - 2 <|alpha|^2>_W + 1/2
```

- Validate `g^(2)(0)` versus `3 + 1/<n>`.

### Stage 1B: Broadband Raymer/Landes Validation

- Implement the broadband Bogoliubov transform:

```text
b(omega) = f(omega) a(omega) + g(omega) a^\dagger(2 omega_0 - omega)
```

- Add temporal gating and optional dispersion compensation.
- Validate the compensated formula:

```text
g^(2)(0) = (2 + xi) + 1/nbar
```

- Use `xi = 1` only for the indistinguishable collinear case.

## Stage 2: Time-Domain Bright Squeezed Vacuum

Construct stochastic waveforms with spectral and temporal mode structure.

Validation observables:

- optical spectrum,
- temporal correlation function,
- intensity distribution,
- mode-resolved photon-number statistics,
- dependence on squeezing phase and bandwidth.
- effective Schmidt-mode count if multimode BSV is modeled.

## Stage 3: HHG in Gas

Start with a single-atom or local response model. Add propagation only after
basic ensemble behavior is understood.

Outputs:

- harmonic spectra,
- cutoff distributions,
- shot-to-shot variance,
- comparison against coherent and thermal baselines.

Implementation targets:

1. Reproduce the 1D soft-core gas baseline from the Gorlach 2023 supplement.
2. Generate coherent-response spectra over a grid of amplitudes and phases.
3. Integrate over BSV Husimi samples.
4. Report mean spectra, conditional spectra, cutoff distributions, and Monte
   Carlo uncertainty.
5. Keep generated harmonic quantum-state claims out of this stage unless a
   Positive P/Husimi output-state reconstruction is added.

## Stage 4: THz Optical Rectification

Start with a local `chi^(2)` polarization model and THz filtering. Add
dispersion and phase matching after validating the source term.

Outputs:

- ensemble mean THz field,
- ensemble mean THz intensity,
- shot-to-shot waveform distribution,
- dependence on squeezing phase and detection bandwidth.

Current status: classical OR propagation is now sourced by Ravi 2014, but
squeezed-vacuum OR remains derivation-led.

Implementation targets:

1. Reproduce an undepleted deterministic OR calculation:

```text
P_THz(Omega) =
  epsilon_0 chi_eff^(2)
  integral d omega A_op(omega + Omega) A_op^*(omega)
```

2. Add tilted-pulse-front phase matching:

```text
n_THz(Omega) cos(gamma) = n_g,opt(omega_0)
```

3. Replace the deterministic optical pump with sampled stochastic waveforms and
   compare:

```text
<P_THz(t)>_ensemble
<|P_THz(omega)|^2>_ensemble
```

4. After the stochastic source term is validated, add Ravi-style pump depletion,
   cascading, angular-dispersion GVD, absorption, SPM/SRS, and eventually 2D
   transverse Fourier propagation.
5. Report THz beam quality and spatial chirp if using the 2D model, not only
   conversion efficiency.

## Stage 5: THz Plasma Emission

Start with a local photocurrent model. Treat symmetry as a first-class test.

Outputs:

- current and density traces,
- THz spectra,
- ensemble mean and variance,
- conditional statistics for high-field events,
- symmetry-breaking parameter scans.

Implementation targets:

1. Reproduce a classical one-color/two-color photocurrent baseline.
2. Add coherent-plus-BSV sampling following Wang 2026.
3. Compute:

```text
<E_THz(t)>_ensemble
<|E_THz(omega)|^2>_ensemble
```

4. Scan two-color phase, BSV squeezing angle, BSV mean intensity, and
   post-selection bins.
5. Test pure zero-mean BSV as a symmetry experiment and record whether the
   ensemble-averaged field vanishes.

## Stage 6: Non-Gaussian Output Diagnostics

This stage is claim-gating for the high-impact novelty direction. It should be
started after the HHG or THz source model identifies promising modes or
conditional bins.

Diagnostic ladder:

1. Classical stochastic diagnostics:

```text
skewness, kurtosis, higher energy cumulants, conditional histograms
```

2. Gaussian quantum diagnostics:

```text
mode covariance matrix, squeezing, purity proxy, Gaussian entanglement
```

3. Non-Gaussian quantum diagnostics:

```text
higher-order cumulants beyond covariance
non-Gaussian witnesses
mode-selective Husimi or Wigner reconstruction
Wigner negativity if the model supports it
```

Implementation rules:

- Define the mode before computing any cumulant or witness.
- Label whether the non-Gaussian object is the pump, emitted HHG/THz mode,
  joint pump-output state, or a conditional postselected state.
- Track pump depletion/backaction when possible; frozen-pump models can erase
  the mechanism that creates non-Gaussianity.
- Do not certify quantum non-Gaussianity from a positive stochastic ensemble
  alone.

## Cross-Cutting Numerical Rules

- Store every random seed used for source-term ensembles.
- Report convergence versus sample count because rare BSV outliers can dominate
  nonlinear observables.
- For every plotted quantity, label whether the average is over field
  amplitudes before or after spectral magnitude is taken.
- Keep coherent, thermal, and BSV baselines matched by mean energy and stated
  mode definition.

## Suggested Code Layout

```text
code/
  src/
    stochastic_em_theory/
      fields.py
      observables.py
      hhg.py
      thz_or.py
      thz_plasma.py
  notebooks/
  tests/
```

This layout is a target, not yet implemented.

## Result Manifest Template

Each completed run should include a small manifest:

```yaml
run_id: YYYYMMDD-short-name
created: YYYY-MM-DD
code_entrypoint:
git_commit:
parameter_file:
random_seeds:
observable:
notes:
```
