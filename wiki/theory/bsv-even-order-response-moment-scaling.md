---
title: BSV Even-Order Response And Moment Scaling
type: concept
status: draft
created: 2026-11-14
updated: 2026-11-14
tags: [theory, bsv, symmetry, optical-rectification, thz, moments]
source_count: 3
confidence: low
related:
  - quantum-optical-rectification-of-bsv
  - stochastic-quantum-optics-correspondence
  - ../models/thz-optical-rectification-model
  - ../models/thz-plasma-emission-model
  - ../project-status-review
---

# BSV Even-Order Response And Moment Scaling

> Update 2026-11-14 (later the same day). The optical-rectification part of
> this page now has a fully quantum derivation with multimode formulas and
> exact finite-photon-number corrections:
> [[quantum-optical-rectification-of-bsv]]. The `(2n - 1)!!` rule is sourced:
> [[../sources/spasibko-2017-multiphoton-effects-photon-number-fluctuations]]
> measured 2.86 +- 0.08 for second-harmonic generation against the ideal 3.
> The shot-to-shot sign flip is measured directly in
> [[../sources/kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv]].
> Real femtosecond BSV has about 1.5 to 2 temporal modes
> ([[../sources/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light]]),
> so use the `K`-mode formulas of the quantum page, not the single-mode
> numbers below, when comparing with a source. This page remains the
> statement of the parity rule and of the plasma two-colour check.

Seed derivation written during the 2026-11-14 project review. It is not backed
by an ingested source. It answers two questions that the model pages leave
open: whether optical rectification (OR) of squeezed vacuum survives ensemble
averaging, and which plasma two-colour configurations give a nonzero mean THz
field. Check every statement here against the literature before it goes into
the manuscript.

## Representation And Assumptions

- Representation: macroscopic limit of single-mode bright squeezed vacuum
  (BSV), in which the Wigner, Husimi-Q, and P distributions of the scaled
  field amplitude coincide. Ordering corrections are of relative order
  `1/<n>` and are dropped.
- One spatiotemporal mode with a fixed complex envelope `A(t)`.
- The squeezed quadrature is neglected (variance ratio `exp(-4r)`), so each
  shot is

```text
E_j(t) = X_j Re[A(t) exp(-i omega_0 t)],   X_j real,  X_j ~ N(0, sigma^2)
I_j = X_j^2 / sigma^2 ~ chi-squared with 1 degree of freedom,  <I> = 1
<I^k> = (2k - 1)!!        (k = 1, 2, 3, 4:  1, 3, 15, 105)
```

  `X` and `E` in field units; `I` dimensionless (shot intensity over mean
  intensity).
- Undepleted pump, no propagation, response computed independently per shot
  (diagonal approximation).

## Parity Rule

The only randomness is the real amplitude `X`, and its distribution is
symmetric under `X -> -X`. Split any response into parts even and odd in `X`:

```text
R(X) = R_even(X) + R_odd(X)
<R> = <R_even>,     <R_odd> = 0
```

So the ensemble-mean emitted field is nonzero exactly for the part of the
response that is even in the BSV amplitude:

| Process | Dependence on `X` | Ensemble-mean field |
| --- | --- | --- |
| Odd harmonics in an inversion-symmetric medium | odd | zero; sign flips shot to shot |
| Optical rectification, `P ~ chi^(2) E E*` | even (`X^2`) | nonzero |
| Second harmonic, `P ~ chi^(2) E E` | even (`X^2`) | nonzero |
| Two-colour plasma THz, coherent `omega` + BSV `2 omega` | odd (linear in `X_2w`) | zero |
| Two-colour plasma THz, BSV `omega` + coherent `2 omega` | even | nonzero |
| Two-colour plasma THz, BSV `omega` + its own second harmonic | even | nonzero |

For the two-colour rows: replacing `X` by `-X` on the fundamental equals a
time shift of the whole waveform by half a fundamental period, because
`cos(omega (t + T/2)) = -cos(omega t)` while `cos(2 omega (t + T/2) + theta) =
cos(2 omega t + theta)`. The THz transient is unchanged apart from a 1.3 fs
envelope shift at 800 nm.

Consequence for [[../models/thz-plasma-emission-model]]: the vanishing mean
THz field found in [[../simulations/thz-plasma-bsv-photocurrent-notebook]] is
specific to putting the BSV on the second harmonic. It is not a general
property of BSV-driven plasma THz emission.

## Optical Rectification Of Single-Mode BSV

With `P_THz(t) = (epsilon_0 chi_eff^(2) / 2) |X A(t)|^2` and a linear,
deterministic THz response `g(t)` to the intensity envelope (SI units for
`P`; `g` carries the field units):

```text
E_THz,j(t) = I_j g(t)
```

Every shot emits the same waveform shape with the same sign, scaled by the
shot intensity. Then:

| Quantity | BSV pump | Thermal pump | Coherent pump |
| --- | --- | --- | --- |
| Mean THz field `<E_THz>` / `g(t)` | 1 | 1 | 1 |
| Relative field fluctuation, `std / mean` | `sqrt(2)` | 1 | 0 |
| Single-shot field distribution | one-sided, chi-squared (1 d.o.f.) | one-sided, exponential | fixed |
| Mean THz energy / coherent value, `<I^2>` | 3 | 2 | 1 |
| THz energy `g2`, `<I^4> / <I^2>^2` | 35/3 = 11.67 | 6 | 1 |

Reading: the THz field inherits the intensity statistics of the pump. The
mean waveform equals that of a coherent pump with the same mean energy, so it
can be averaged in electro-optic sampling. The single-shot amplitude histogram
is one-sided with its mode at zero, which is a strongly non-Gaussian field
distribution. The THz state is a classical mixture of coherent states; none of
this certifies a nonclassical THz field.

For a general process whose emitted field scales as `I^k`:

```text
mean field enhancement over coherent  = <I^k>      = (2k - 1)!!
mean energy enhancement over coherent = <I^(2k)>   = (4k - 1)!!
energy g2 = <I^(4k)> / <I^(2k)>^2 = (8k - 1)!! / [(4k - 1)!!]^2
```

For `k = 1` this gives 3 and 35/3 as above. For `k = 2` (perturbative
two-colour mixing with a self-generated second harmonic) the mean energy
enhancement is 105 and the mean field enhancement is `<I^2> = 3`. These
perturbative numbers do not apply to tunnel-ionization photocurrents, which
are far more nonlinear and saturate.

## Numerical Check Of The Parity Rule

Run: `results/runs/20261114-thz-two-color-parity-check/`
(`code/scripts/check_thz_two_color_parity.py`, seed 20261114, 4,000 shots per
case, same local photocurrent model as the notebook, mean fundamental
intensity `1e14 W/cm^2`, second harmonic at 2 %).

| Case | Mean field / standard error | Shots with positive / negative field | Coherent share of THz energy |
| --- | --- | --- | --- |
| A: coherent 800 nm + BSV 400 nm | 0.08 | 50.0 % / 50.0 % | 2e-6 |
| B: BSV 800 nm + coherent 400 nm | -22.7 | 1.1 % / 79.3 % | 0.10 |

The remaining 20 % of case-B shots have negligible ionization and emit
nothing. This confirms the symmetry statement. It is not a quantitative
prediction: the model has an ADK-form rate without saturation physics, no
propagation, and case B asks for a BSV fundamental at `1e14 W/cm^2` mean
intensity. Rivera-Dean 2025 estimate that `1e13` BSV photons in 60 fs on
`2.5e-7 cm^2` reach about that value, where roughly half the atoms ionize,
so case B would sit in the depleted regime
([[../sources/rivera-dean-2025-propagation-of-intense-squeezed-vacuum-light-in-non]]).

## Open Points

- Multimode BSV. With `M` comparable temporal modes inside the pulse the
  pulse-energy statistics move toward `g2 = 1 + 2/M`, and the factors above
  shrink for any response that integrates over the pulse, such as a
  low-frequency THz field. They do not shrink for the mean yield of a fast
  process such as harmonic generation, which follows the instantaneous
  intensity (Spasibko 2017, Fig. 3).
  The mean OR field should still follow the mean intensity envelope. Needs
  the Schmidt-mode sampler that `source_models.py` only describes.
- Vacuum terms. In Wigner sampling the mean OR polarization contains
  `(1/2) sum_k psi_k*(omega) psi_k(omega + Omega)`, which by completeness
  contributes only at `Omega = 0`. The THz intensity (second moment) does
  contain vacuum-signal cross terms that need the Raymer and Landes 2023
  subtraction. Not derived here.
- Stationary limit. For continuous-wave-pumped BSV the mean intensity has no
  envelope, so the mean OR field vanishes at `Omega != 0` and only the
  fluctuation spectrum remains.
- Pump depletion and cascading (Ravi 2014) are ignored.
- Prior art. Web and arXiv searches on 2026-11-14 found no paper on OR or THz
  generation with a BSV pump. The enhancement factor `(2n - 1)!!` for
  `n`-photon processes driven by BSV is Spasibko 2017 (now ingested). One
  difference from harmonic generation matters: a harmonic responds to the
  instantaneous intensity, so its mean yield follows the single-mode
  `g^(n)` even for broadband BSV, whereas a low-frequency THz field
  integrates the intensity over the pulse and follows the pulse-energy
  statistics, `1 + 2/K`.
