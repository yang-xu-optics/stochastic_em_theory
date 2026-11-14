---
title: BSV Even-Order Response And Moment Scaling
type: concept
status: seed
created: 2026-11-14
updated: 2026-11-14
tags: [theory, bsv, symmetry, optical-rectification, thz, moments]
source_count: 0
confidence: low
related:
  - stochastic-quantum-optics-correspondence
  - ../models/thz-optical-rectification-model
  - ../models/thz-plasma-emission-model
  - ../project-status-review
---

# BSV Even-Order Response And Moment Scaling

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
intensity, which is probably above what current BSV sources deliver (to be
checked against Rasputnyi 2024 and later source papers).

## Open Points

- Multimode BSV. With `M` comparable temporal modes inside the pulse the
  intensity statistics move toward `g2 = 1 + 2/M` and the factors above shrink.
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
- Prior art. Two web searches on 2026-11-14 found no paper on OR or THz
  generation with a BSV pump. The enhancement factor `(2n - 1)!!` for
  `n`-photon processes driven by BSV is known from the multiphoton literature
  and should be cited; find and ingest the source.
