---
title: THz Plasma Photocurrent Simulation With BSV Second Harmonic
type: simulation
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [thz, plasma, photocurrent, bsv, husimi-q, two-color]
source_count: 3
confidence: medium
related:
  - ../models/thz-plasma-emission-model
  - ../sources/wang-2026-quantum-thz-plasma-bsv
  - ../sources/sun-2022-thz-laser-induced-plasma
  - ../sources/schuh-2013-thz-ionization-gases
---

# THz Plasma Photocurrent Simulation With BSV Second Harmonic

## Target Observables

Following the implementation order in [[../models/thz-plasma-emission-model]]
(coherent-plus-BSV before pure BSV, per Wang 2026):

1. `g^(2)(0)` of the stochastic second-harmonic driving mode, computed from
   the same Husimi-Q samples that drive the plasma, with the
   antinormal-to-normal ordering correction.
2. Ensemble mean and shot-to-shot fluctuation of the generated THz waveform
   `E_THz(t)`: `<E_THz(t)>` with a `+/- 1 sigma(t)` band and example
   single-shot traces.
3. Ensemble mean and fluctuation of the THz intensity spectrum: the total
   (incoherent) spectrum `<|E_THz(nu)|^2>`, the coherent part
   `|<E_THz(nu)>|^2`, and the standard deviation of the per-shot intensity
   spectrum.
4. Shot-to-shot THz pulse-energy distribution and its classical fluctuation
   ratio `<U^2>/<U>^2` (a stochastic-ensemble statistic, *not* a THz photon
   `g^(2)` claim; the emitted-field quantum state is out of scope here).

## Representation And Stochastic Ensemble

The strong 800 nm fundamental is a fixed classical field. The weak 400 nm
second harmonic is one detected mode sampled per shot from the **Husimi-Q**
distribution, following the Wang 2026 phase-space average

```text
S(omega) ∝ integral d^2 beta Q(beta) |j_beta(omega)|^2
```

Driver cases at matched mean photon number `nbar = sinh^2(r)` (vacuum
excepted):

```text
coherent: beta = i sqrt(nbar) + xi,  xi ~ Q vacuum noise  (THz-optimal phase)
bsv_active:   squeezed vacuum, anti-squeezed quadrature along sin(2 w0 t)
bsv_inactive: squeezed vacuum, anti-squeezed quadrature along cos(2 w0 t)
vacuum: beta ~ Q vacuum noise (control / noise floor)
```

`g^(2)(0)` from Q moments uses the antinormal ordering correction

```text
<n> = <|beta|^2>_Q - 1
<a†a†aa> = <|beta|^4>_Q - 4 <|beta|^2>_Q + 2
```

with single-mode squeezed-vacuum target `g^(2)(0) = 3 + 1/<n>` and coherent
target `1`. Both BSV orientations share the same photon statistics; only
their THz response differs, which is the quadrature-sensitivity message.

## Model Equations And Units

Atomic units internally; axes displayed in fs and THz. Local single-point
photocurrent model (Sun 2022 template; no propagation, no depletion of the
THz-active phase by plasma dispersion):

```text
E(t)  = f(t) [ E_w0 cos(w0 t) + s (x_beta cos(2 w0 t) + p_beta sin(2 w0 t)) / sqrt(2) ]
w(t)  = quasistatic tunneling rate (ADK-like, hydrogen-like prefactor):
        w(E) = 4 (2 Ip)^(5/2) / |E| * exp( - 2 (2 Ip)^(3/2) / (3 |E|) )
n_e(t) = 1 - exp( - integral_0^t w dt' )          (no depletion regime)
dJ/dt = E(t) n_e(t)                                (free-electron acceleration)
E_THz(t) ∝ LP[ E(t) n_e(t) ]                       (low-pass below nu_c)
```

The far-field scaling `S(omega) ∝ omega^2 |j(omega)|^2` (Schuh 2013 /
Wang 2026) is omitted in the displayed local-source spectra; THz field is in
arbitrary units throughout.

Default parameters:

```text
lambda0 = 800 nm  (w0 = 0.057 a.u.), second harmonic at 2 w0
E_w0 = 0.05 a.u.  (~8.8e13 W/cm^2)
rms 2w field = 0.15 E_w0  (per-state mean-intensity normalization,
                           as in the Fig. 3b runner)
Ip = 0.579 a.u.   (Ar, 15.76 eV)
Gaussian envelope, field FWHM = 80 fs, window = 65536 * 0.5 a.u. ≈ 792 fs
dt = 0.5 a.u., low-pass cutoff nu_c = 80 THz with smooth rolloff
r = 1.5  (nbar ≈ 4.53, g2 target ≈ 3.221)
```

## Random Seeds And Convergence

Fixed integer seed recorded in the notebook and manifest. Shots per case:
4,000, processed in batches with running mean/variance accumulation.
Convergence checks:

- sampled `g^(2)(0)` of each driver case within Monte Carlo error of its
  analytic target,
- batch standard error of the mean THz pulse energy small compared with the
  between-case differences,
- the vacuum control's THz energy well below the BSV-active case.

## Expected Limiting Cases (Symmetry Check)

- Coherent two-color drive at the optimal relative phase: deterministic THz
  waveform; coherent spectral fraction `|<E(nu)>|^2 / <|E(nu)|^2>` near 1;
  energy fluctuation ratio near 1.
- Zero-mean BSV drive (both orientations): `<E_THz(t)> ≈ 0` because the
  per-shot THz polarity follows the sign of the sampled 2w quadrature, which
  is symmetric. The mean *intensity* spectrum stays large for the THz-active
  orientation. A near-zero mean with large fluctuation is the physically
  meaningful result, per the symmetry guardrail.
- BSV with squeezing rotated by pi (anti-squeezed along the THz-inactive
  cos quadrature): strongly suppressed THz yield at identical `g^(2)(0)`.
- Vacuum 2w control: lowest yield, sets the sampling noise floor.
- Energy fluctuation ratio `<U^2>/<U>^2` near `3` for the THz-active BSV case
  (energy ∝ active-quadrature power, chi-squared-1-like), near 1 for
  coherent.

## Outputs

Notebook: `code/notebooks/thz_plasma_stochastic.ipynb`, generated by
`code/notebooks/build_thz_plasma_stochastic_notebook.py` and executed with
the project venv kernel. The final cell writes a summary JSON and manifest to
a dated directory under `results/` recording seed, shots, parameters, sampled
`g^(2)` values, THz energy statistics, and the implementation caveats above.
