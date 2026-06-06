---
title: THz Plasma Emission Model
type: model
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [thz, plasma, photocurrent, ionization, squeezed-vacuum]
source_count: 6
confidence: high
related:
  - ../overview
  - ../theory/non-gaussian-output-novelty
  - ../simulations/simulation-roadmap
  - ../sources/schuh-2013-thz-ionization-gases
  - ../sources/sun-2022-thz-laser-induced-plasma
  - ../sources/wang-2026-quantum-thz-plasma-bsv
---

# THz Plasma Emission Model

This page defines the plasma-emission path for THz generation driven by
stochastic squeezed optical fields.

## Minimal Photocurrent Picture

A common time-domain model evolves a free-electron current `J(t)` driven by the
optical field and ionization-generated electron density:

```text
dJ/dt + nu J = (q^2/m) n_e(t) E(t) + source_terms
dn_e/dt = W[E(t)] (n_gas - n_e)
E_THz proportional to dJ/dt
```

The exact source terms, ionization rate, and propagation model must be chosen
from sources before implementation.

## Source-Backed Current Form

Schuh 2013 gives a microscopic gas model in which the emitted THz source is the
current change:

```text
j(t) = (1/V) sum_k f_k(t) e hbar k / m
c(nu) = integral dt exp(2 pi i nu t) d j_z(t) / dt
```

Sun 2022 gives a practical photocurrent template:

```text
dn_e/dt = w(t) [N_0 - n_e(t)]
J(t) = - integral e v(t, t') dn_e(t')
E_THz proportional to dJ/dt
```

Wang 2026 gives the BSV-specific plasma THz phase-space average:

```text
S(omega) =
  omega^2 / (6 pi^2 c^3 epsilon_0)
  integral d^2 E_alpha Q(E_alpha) |j_alpha(omega)|^2
```

## Symmetry Check

For a zero-mean stochastic drive, the ensemble-averaged plasma current may
vanish unless a physical asymmetry is present. Candidate asymmetry mechanisms:

- two-color mixing or carrier-envelope asymmetry,
- biased or oriented medium,
- conditioning on high-field events,
- propagation or ionization gating that breaks time-reversal symmetry,
- nonzero coherent displacement of the squeezed field.

The paper should treat a zero-result as scientifically meaningful if symmetry
requires it.

The direct BSV plasma source currently ingested, Wang 2026, uses a strong
coherent 800 nm field plus a weak 400 nm BSV field. That coherent field should
be treated as the first reproducible setting before testing pure BSV plasma
emission.

## Non-Gaussian Novelty Path

Wang 2026 predicts bunched, thermal-like THz output in a coherent-plus-BSV
plasma setting. The new mesoscopic non-Gaussian sources suggest a sharper
follow-up question: when does plasma THz emission move beyond thermal-like
Gaussian or Bose-Einstein statistics?

Candidate mechanisms:

- ionization gating acts as a nonlinear measurement of the squeezed pump,
- conditioning on ionization bursts or THz energy prepares non-Gaussian output
  ensembles,
- pump-output or electron-field entanglement creates higher cumulants not
  reducible to covariance,
- strong BSV-induced current bursts produce mode-selective non-Gaussian THz
  quadrature statistics.

For now, treat these as hypotheses. A stochastic current model can identify
candidate regimes, but a quantum emitted-field model or witness is needed to
claim genuine non-Gaussian THz light.

## Proposed Observables

- Ensemble-averaged THz field.
- Ensemble-averaged THz intensity.
- Shot-to-shot THz waveform distribution.
- Correlation of ionization bursts with field quadrature statistics.
- Dependence on squeezing phase and displacement.
- Two-color phase and squeezing-angle scans.
- Conditional spectra binned by sampled BSV amplitude.
- Higher-order cumulants of THz energy and selected THz mode quadratures.
- Non-Gaussianity witnesses if an emitted-field measurement model is added.

## First Simulation Target

Start with a local-current model before macroscopic propagation:

1. sample `E_j(t)`,
2. compute ionization rate `W[E_j(t)]`,
3. evolve `n_e,j(t)` and `J_j(t)`,
4. band-limit `dJ_j/dt` to THz frequencies,
5. compare ensemble mean, variance, and conditional statistics.

## Implementation Order

1. Reproduce a classical one-color and two-color photocurrent baseline.
2. Add BSV as a weak second harmonic sampled from a Husimi Q distribution,
   following the coherent-plus-BSV Wang 2026 setup.
3. Scan the BSV squeezing angle and mean intensity.
4. Only after that, test pure zero-mean BSV and document whether symmetry
   forces `<E_THz(t)>` to vanish.
