---
title: THz Waveform Noise Against Delay
type: simulation
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [simulation, thz, optical-rectification, bsv, noise, timing-jitter, temporal-modes]
source_count: 2
confidence: medium
related:
  - ../theory/quantum-optical-rectification-of-bsv
  - ../experiments/bsv-or-thz-dast-znte-setup
  - bsv-optical-rectification-thz-statistics
  - ../sources/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light
  - ../sources/kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv
---

# THz Waveform Noise Against Delay

Specification for `code/src/stochastic_em_theory/thz_waveform_noise.py`,
`code/scripts/run_thz_waveform_noise.py`, and
`code/tests/test_thz_waveform_noise.py`. It covers measurement 4 of the
programme in [[../experiments/bsv-or-thz-dast-znte-setup]]: the shot-to-shot
rms of the THz field as a function of electro-optic-sampling delay.

## Observable

For each delay `t`: the ensemble mean `<E(t)>` and the variance `Var E(t)` of
the single-shot THz field; the decomposition of the variance into a
photon-number part and an arrival-time part; the single-shot estimate of the
arrival time of the pump photon flux from the field at a zero crossing.

## Field Representation

Bright (classical-noise) limit of the quantum model in
[[../theory/quantum-optical-rectification-of-bsv]]. Each spatial mode of the
pump is a real Gaussian random field `X(t')` on the anti-squeezed quadrature
with covariance `G1(t1, t2) / M_s`; the photon flux is `I(t') = sum X^2`.
Ordering corrections of order `1/nbar` and the spontaneous term are dropped.
For comparison, thermal light uses a circular complex Gaussian field with
the same `G1`.

## Model Equations And Units

Times in fs, frequencies in THz, field and flux in arbitrary units.

```text
E_j(t) = integral dt' g(t - t') I_j(t')                              (1)

Gaussian Schell model of the pump:
  G1(t1, t2) = sqrt(Ibar(t1) Ibar(t2)) gamma(t1 - t2)
  Ibar(t) = exp[-t^2 / (2 T^2)],  gamma(tau) = exp[-tau^2 / (2 tau_c^2)]
  K_t = sqrt(1 + 4 T^2 / tau_c^2)        temporal mode number
  K = M_s K_t                            total mode number

exact variance (BSV; thermal has 1 in place of 2):
  Var E(t) = (2 / M_s) double-integral g(t - t1) g(t - t2) G1(t1, t2)^2   (2)

moment expansion to second order in T / (THz period), with
N = integral I, M1 = integral t' I, M2 = integral t'^2 I:
  dE_j(t) ~ g(t) dN_j - g'(t) dM1_j + (1/2) g''(t) dM2_j
  Var E(t) / <N>^2 ~ A gbar^2 + B (gbar'^2 - gbar gbar'') + 2 C gbar gbar'  (3)
  A = Var N / <N>^2 = 2 / K
  B = Var(M1) / <N>^2 = (2 / K) (T^2 / 2) (1 - 1 / K_t^2)
  C = -Cov(N, M1) / <N>^2 = 0 for a symmetric pulse
  gbar(t) = <E(t)> / <N> = g + (T^2 / 2) g'' + ...
```

The `gbar gbar''` part of (3) comes from `Cov(N, M2) / <N>^2 =
(2 / K)(T^2 / 2)(1 + 1 / K_t^2)` combined with the difference between `g` and
`gbar`; the two together give exactly `-B`. Consequences: at a zero crossing
the noise is `sqrt(B) |gbar'|`; at a peak it is
`sqrt(A + B |gbar'' / gbar|) |gbar|`; for a nearly monochromatic waveform of
angular frequency `w` the timing term is the constant floor `B w^2`.

`T` is the rms duration of the mean intensity envelope (FWHM divided by
2.355). `g` is a model response, the first derivative of a Gaussian of rms
width 150 fs: single cycle, spectrum peaked near 1.1 THz with content to
about 3 THz. It stands in for the DAST and ZnTe response, which is not yet
modelled.

## Stochastic Ensemble And Seeds

20,000 shots per case, seed 20261114. Cases share `K = 10` and
`T = 42.5 fs` (100 fs FWHM) and differ in how `K` splits:
`(M_s, K_t) = (10, 1), (5, 2), (2, 5)`. Pump grid 4 fs, THz grid 10 fs.

## Convergence And Validation

- `K_t` from the eigenvalues of the discretized `G1` against the closed form.
- Sampled `Var N` and `Var(N t_c)` against `A` and `B`.
- Sampled variance against the exact double integral (2).
- Template fit of (3) to the exact variance against `A` and `B`. A first
  version of (3) without the `gbar gbar''` term failed this check by 5 % in
  `A`, which is how the term was found.
- Thermal statistics give half the variance at every delay.

## Expected Limiting Cases

```text
K_t = 1:        Var E(t) = (2/K) <E(t)>^2 exactly; no noise at zero crossings
K_t -> inf:     B / A -> T^2 / 2
same K, any split: identical noise at the waveform peaks
```

## Outputs

`results/runs/20261114-thz-waveform-noise-against-delay/`: CSV of mean, rms,
and components against delay for each case; summary JSON; parameters;
manifest; four-panel PNG.

## First Run

`results/runs/20261114-thz-waveform-noise-against-delay/`, 20,000 shots per
case, `K = 10`, 100 fs pump, model response. Fields in units of the peak of
the mean waveform.

| Pump (temporal x spatial) | rms at peak | rms at zero crossing | Arrival-time jitter | `K_t` from exact-model fit |
| --- | --- | --- | --- | --- |
| 1 x 10 | 0.448 | 0.000 | 0 fs | 1.00 |
| 2 x 5 | 0.464 | 0.128 | 11.6 fs | 1.95 |
| 5 x 2 | 0.467 | 0.148 | 13.2 fs | 4.05 |

- Sampled `A` and `B` agree with the closed forms within 2 %; the sampled
  variance agrees with the exact double integral within 3 %.
- The second-order template fit returns `A` within 2 % and `B` about 10 %
  high; the excess is fourth order in pulse duration over THz period.
- The zero-crossing noise saturates with `K_t`: it separates one temporal
  mode from two clearly and two from five poorly.
- Single-shot arrival time from the field at the zero crossing, with
  detection noise of one thirtieth of the mean peak field: rms error 3.7 fs
  against a true spread of 11 fs, for shots above half the mean energy.

## Out Of Scope

The real crystal and sampling response; instrument timing jitter between
pump and probe; technical energy noise of the pump laser; second-order
moments of the photon flux (duration fluctuations), which the exact formula
(2) contains but the expansion (3) does not.
