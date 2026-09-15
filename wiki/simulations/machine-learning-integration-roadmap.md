---
title: Machine Learning Integration Roadmap
type: synthesis
status: seed
created: 2026-08-26
updated: 2026-08-26
tags: [machine-learning, surrogate-model, active-learning, inverse-design, hhg, thz]
source_count: 0
confidence: low
related:
  - simulation-roadmap
  - paper-one-correspondence-hhg-simulation-spec
  - ../theory/stochastic-quantum-optics-correspondence
  - ../models/hhg-gas-model
  - ../models/thz-plasma-emission-model
  - thz-plasma-bsv-photocurrent-notebook
---

# Machine Learning Integration Roadmap

This page is a project proposal, not yet a source-backed result. It identifies
where machine learning can accelerate or invert the stochastic strong-field
framework without hiding the field representation, operator ordering, or
detection model inside a black box.

## Architectural Principle

Keep the stochastic source, physical response, and detection map separate:

```text
lambda_j ~ P_R(lambda | theta_q)
E_j(t) = E(t; lambda_j)
y_j = F_phys[E_j(t); theta_m]
O = ensemble_average_j D_R[y_j]
```

Here `R` is the Wigner, Husimi-Q, Positive-P, or other explicitly named
representation; `theta_q` contains squeezing, displacement, loss, bandwidth,
and mode parameters; `theta_m` contains material and pulse parameters; and
`D_R` contains the observable and any ordering or vacuum correction.

The safest first ML insertion is

```text
y_j approximately F_ML[E_j(t); theta_m],
```

with `P_R` and `D_R` remaining analytic and auditable. Training an end-to-end
map from squeezing parameter directly to a final spectrum would entangle
source statistics, material response, and detection assumptions and make
representation errors difficult to diagnose.

## Ranked Opportunities

| Direction | Learned object | Scientific value | Priority |
| --- | --- | --- | --- |
| Coherent-response surrogate | TDSE/SFA/photocurrent response for one field realization | Makes large stochastic ensembles and parameter scans feasible | First |
| Tail-aware active learning | Which new expensive solver points to evaluate | Resolves rare BSV events that dominate nonlinear yields | First |
| Bayesian inverse model | Posterior over squeezing and material parameters given observables | Turns HHG and THz into stochastic-field diagnostics | Second |
| Waveform/operator surrogate | Map an input waveform to dipole/current waveform | Supports multimode and shaped stochastic fields | Later |
| Closed-loop optimization | Pulse, squeezing, and post-selection settings | Optimizes a chosen emitted spectrum or witness | Later |

## Pilot: Uncertainty-Aware HHG Response Surrogate

The current Fig. 3b implementation already builds a TDSE response library and
interpolates log spectra across field amplitude. This is the natural pilot
interface.

### Scope

For the present one-dimensional input, first benchmark monotone interpolation
and a Gaussian-process surrogate; a deep network is not justified merely to
replace a one-dimensional lookup table. Expand the input only after this
baseline closes:

```text
x = (E0, carrier-envelope phase, omega, pulse duration,
     ionization potential, soft-core parameter)
```

Candidate targets are:

```text
y = (log harmonic yields, cutoff order, ionization yield,
     selected harmonic complex amplitudes)
```

If harmonic phase and attosecond synthesis matter, learn the dipole-acceleration
trace or a compressed complex spectrum rather than power alone.

### Model Ladder

1. Piecewise or shape-preserving interpolation as the reference baseline.
2. PCA or another fixed spectral basis followed by one Gaussian process per
   retained coefficient. This is appropriate for tens to hundreds of TDSE
   runs and supplies epistemic uncertainty.
3. A small neural ensemble after the parameter space and training set become
   genuinely multidimensional.
4. A convolutional model or neural operator only when the input is a full
   multimode waveform rather than a short parameter vector.

The model must never silently extrapolate. A prediction outside the training
domain should be rejected or routed to the physical solver.

## Tail-Aware Active Learning

Uniform accuracy is not the right objective for BSV-driven HHG. A rare field
amplitude can have small probability and still dominate the mean because the
response is extremely nonlinear. Select new solver points using both surrogate
uncertainty and their contribution to the target ensemble:

```text
A(lambda) = p_target(lambda) sigma_ML(lambda) w_O(lambda),
```

where `p_target` is a mixture covering all coherent, thermal, and BSV source
models to be compared, `sigma_ML` is predictive uncertainty, and `w_O`
weights sensitivity of the desired observable. Retain an explicit exploration
term so the algorithm cannot ignore poorly sampled tails.

Convergence should be judged on final ensemble quantities, not only pointwise
prediction error. For each target source distribution compare ML-assisted and
direct-solver estimates of:

```text
mean spectrum
spectrum variance
high-intensity conditional spectrum
cutoff distribution and upper quantiles
ionization-yield distribution
```

Importance sampling or stratified quantile sampling can then be combined with
the surrogate. Any clipping of BSV tails must remain a named model parameter,
not an ML preprocessing step.

## Joint HHG-THz Inference

A more original second-stage project is stochastic strong-field tomography.
Infer a posterior rather than a point estimate:

```text
p(theta_q, theta_m | z_HHG, z_THz, z_input),
```

with candidate quantum-light parameters

```text
theta_q = (r, squeezing angle, displacement, loss,
           effective Schmidt-mode number, bandwidth).
```

The channels are complementary. HHG is strongly sensitive to the rare
high-field tail through ionization and cutoff statistics. Coherent-plus-BSV
plasma THz is sensitive to relative phase, symmetry, and the division between
coherent and incoherent emission. Joint inference may therefore break
degeneracies that remain when either spectrum is analyzed alone.

Begin with synthetic likelihood-free inference or Bayesian calibration using
summary statistics:

```text
z_input = ordering-corrected input g^(2) and quadrature variances
z_HHG = selected yields, cutoff quantiles, conditional spectra
z_THz = mean-field norm, total/coherent spectral ratio, energy quantiles
```

An identifiability study must precede experimental claims: simulate distinct
parameter settings, test whether their observable distributions overlap, and
report posterior coverage on held-out synthetic data.

## Physics Constraints And Features

Use constraints that follow from the physical model rather than expecting the
training data to teach them inefficiently:

- encode phase variables as sine and cosine;
- enforce nonnegative intensity outputs or learn their logarithms;
- preserve phase periodicity and known inversion or temporal symmetries;
- retain complex harmonic amplitudes if phase locking is an observable;
- keep units in the dataset and model manifest;
- include representation, mode basis, and detection bandwidth as metadata;
- apply Wigner-to-normal ordering corrections outside the model;
- distinguish classical THz energy statistics from normally ordered photon
  correlations.

Symmetry-forbidden channels are useful diagnostics. A surrogate that predicts a
spurious nonzero ensemble-mean THz field for a symmetric zero-mean drive has
failed a physics test even if its average numerical loss is small.

## Data Splitting And Validation

Do not randomly split per-shot rows when many shots reuse the same underlying
TDSE response library. Split by unique physical-solver inputs and reserve
entire parameter regions for interpolation and extrapolation tests.

Required validation layers are:

1. Response fidelity: log-spectrum error, cutoff error, integrated yield error,
   and phase error where applicable.
2. Ensemble closure: direct versus ML-assisted Monte Carlo for means,
   variances, upper quantiles, and conditional bins.
3. Tail stress test: source distributions brighter or more strongly squeezed
   than the training mixture, without presenting extrapolation as a prediction.
4. Symmetry and limiting cases: coherent limit, one-color THz null, matched
   mean-energy baselines, and known harmonic selection rules.
5. Uncertainty calibration: nominal predictive or posterior intervals must
   attain their stated coverage on held-out physical-solver cases.

Neural agreement with a stochastic simulation does not upgrade the claim
ladder. It accelerates the same model and inherits its quantum-output boundary.

## Reproducible Dataset Contract

Each expensive solver row should store:

```text
solver_input_id
field representation and coherent-component labels
E0, phase, omega, pulse and material parameters with units
random seed if the solver itself is stochastic
time-domain dipole/current trace or its stable artifact path
complex spectrum and intensity spectrum
ionization yield, cutoff, and selected summary observables
solver discretization and convergence metadata
git commit and code entry point
```

Each ML run should additionally record the exact train/validation/test solver
IDs, preprocessing transforms, model version, random seeds, training-domain
bounds, and ensemble distributions used for validation.

## Minimal Implementation Sequence

1. Write a dedicated surrogate simulation spec with observables, units,
   solver grid, seeds, convergence tests, and limiting cases.
2. Export the existing TDSE amplitude library through a stable dataset schema.
3. Establish interpolation and PCA-plus-Gaussian-process baselines.
4. Add tail-aware active learning and request new TDSE points until ensemble
   observables close to a predetermined tolerance.
5. Replace the internal interpolation behind a common response-model interface;
   leave field sampling and detection unchanged.
6. Extend inputs to carrier phase and pulse duration, then test whether a
   neural model provides a real advantage.
7. Couple the validated HHG surrogate to the existing plasma-THz notebook for a
   synthetic joint-inference study.

## First Falsifiable Milestone

At matched mean energy, use the surrogate to reproduce direct-TDSE coherent,
thermal, and BSV ensemble spectra and the top-intensity conditional spectrum.
The milestone succeeds only if the surrogate's uncertainty interval covers the
direct Monte Carlo result, including the BSV high-field tail, while using
substantially fewer TDSE evaluations than a fixed dense response grid.

