---
title: Kizmann Et Al 2019 Subcycle Squeezing From A Time Flow Perspective
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, theory, chi2, squeezed-vacuum, time-domain, electro-optic-sampling, mid-infrared, bogoliubov]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../models/thz-optical-rectification-model
  - ../theory/stochastic-quantum-optics-correspondence
  - ../sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum
  - ../sources/riek-2017-subcycle-quantum-electrodynamics
---

# Kizmann Et Al 2019 Subcycle Squeezing From A Time Flow Perspective

## Bibliographic Metadata

- Authors: Matthias Kizmann, Thiago Lucena de M. Guedes, Denis V. Seletskiy,
  Andrey S. Moskalenko, Alfred Leitenstorfer, Guido Burkard.
- Year: 2018 for this preprint; filed under 2019 after the raw filename.
- Identifier: arXiv:1807.10519v1 [quant-ph], 27 Jul 2018. The ingest request
  gives Nature Physics 15, 960 (2019) as the journal version; the PDF states
  no journal reference, so this is not verified from the source.
- DOI: not printed in the PDF.
- Raw source:
  [Kizmann et al. - 2019 - Subcycle squeezing of light from a time flow perspective.pdf](<../../raw/sources/Kizmann et al. - 2019 - Subcycle squeezing of light from a time flow perspective.pdf>)
- Extracted text (equations below were transcribed from rendered PDF pages):
  [kizmann-2019-subcycle-squeezing-time-flow-perspective.txt](<../../results/literature/ingest-2026-11-14/extracted_text/kizmann-2019-subcycle-squeezing-time-flow-perspective.txt>)
- Ingest date: 2026-11-14.

## Core Result

Theory. A classical coherent mid-infrared driving field `E(z,t)` co-propagates
in a thin `chi^(2)` crystal with an orthogonally polarized quantum field
`eps(z,t)` of the same frequency range, which enters as vacuum. The operator
obeys a first-order linear equation (Eq. 1), solved exactly by the method of
characteristics: the output is the input field evaluated at a drive-dependent
"conformal time" `tau`, multiplied by `d tau/dt` (Eq. 2). Electro-optic
sampling (EOS) is a convolution with the normalized probe intensity envelope
(Eq. 8). The model contains no near-infrared pump and no optical-
rectification (OR) source term.

## Useful Equations Or Model Ingredients

Field representation: Heisenberg-picture operator `eps` on a one-dimensional
plane-wave continuum; the drive is a c-number. `W` angular frequency (rad/s);
fields in V/m; `d` in m/V; `r` dimensionless; `(M)` unnumbered Methods line.

```text
(M)  P^(2)(z,t) = -eps0 d E(z,t) eps(z,t)       [y component only; C/m^2]
(5)  d eps(z;W)/dz = -(i d W / (n c0)) int dW1 E^*(z; W1 - W) eps(z; W1)
(1)  d eps/dz = (d / (n c0)) [(dE/dt) eps + (E - n^2/d) d eps/dt]
(2)  eps(z,t) = [d tau(z,t)/dt] eps_in(tau(z,t)),   tau(-l/2, t) = t
(M)  tau(z,t) = f^-1[f(t - n z/c0) + (z + l/2)/(n c0)] - n l/(2 c0)
     df/dt' = 1 / (d E'(t')),   E(z,t) = E'(t'),   t' = t - n z/c0
(3)  E'(t') = E0 sech(G0 t'),   r = |E0 d| G0 l / (n c0)
(8)  eps_d(t_d) = int dt' R(t_d - t') eps'_out(t')
     R(t) = |E_p'(t)|^2 / int dt' |E_p'(t')|^2 ~ I_p'(t) / int dt' I_p'(t')
(9)  eps_d(t_d) = int dt R(t_d - tau_out^-1(t)) eps_in(t)
(4)  RDV(t_d) = [V(t_d) - Dvac^2] / Dvac^2,   V(t_d) = <eps_d(t_d)^2>
(M)  RDN(t_d) = [sqrt(V(t_d)) - Dvac] Dvac / (DE_p,SN)^2
(S5) a(z;W) = a(W) + (z/l + 1/2) sign(W) int dW1 Xi(W, W1) a^dag(W1) [all W1]
     Xi(W, W1) = -(i d l / (n c0)) sign(W W1) sqrt(|W W1|) E_{W1 + W}
(S8) <0| :eps_out(t_d)^2: |0> = [hbar G0^2 / (4 pi n eps0 c0 A)] (r / 6)
       [tanh^3(x) sech(x) - 5 tanh(x) sech^3(x)],   x = G0 t_d,   r << 1
```

- Role of the classical drive in Eq. (1): `dE/dt` multiplies `eps` (local
  gain or loss, the `exp f(t)` factor of Riek 2017) and `E - n^2/d`
  multiplies `d eps/dt` (a drive-dependent propagation speed, which defines
  `tau`). At a fixed time the field variance changes by `(d tau_out/dt)^2`.
- No carrier or envelope is introduced for the drive. The only envelope in
  the model is the probe intensity envelope, the detector function `R(t)`.
- Eq. (1) is linear and homogeneous in `eps`: no classical source term. The
  Methods state that the drive "can be external but the situation is similar
  if this field is generated in the same crystal" (Riek 2017).
- Eq. (S5) is a first-order Bogoliubov transformation with the drive spectrum
  as kernel. Eq. (S6), not transcribed, gives the unitary `S` with pair and
  frequency-conversion terms. `A` in Eq. (S8) is the normalization area.

| Quantity | Value | Status |
| --- | --- | --- |
| Drive rate `G0/(2 pi)`; crystal for estimates | 26 THz; ZnTe, `l` = 15 um, `n` = 2.57 | assumed |
| Validity bounds | `r << n G0 l/c0`, about 20 (Eq. S1); causality `g(r) <= 13` (Eq. S2) | calculated |
| Squeezing strengths `r`; probe FWHM `t_p` | 0.1, 0.5, 2, 5; 0.49, 5.9, 14.7 fs (Gaussian intensity) | assumed |
| Single-cycle drive, `r` = 0.5, `t_p` = 5.9 fs | squeezing 49.6 %, anti-squeezing -35 % (Fig. 4b) | calculated |

## Assumptions

- Plane waves, thin crystal, perfect phase matching, linear dispersion
  `k_W = n W / c0`; dispersionless `chi^(2)` (ZnTe phonon near 5 THz ignored).
- Broadband slowly-varying-amplitude approximation (SVAA): `d^2 eps/dz^2`
  neglected against `k_W d eps/dz`, requiring `E0 d << n^2`; no `chi^(3)`.
- The drive is a prescribed classical waveform that propagates undistorted,
  polarized along `x`; the quantum field is along `y`, with vacuum input.
- Detection: Gaussian probe intensity envelope; theory from Moskalenko 2015.

## Limitations And Cautions

- OR is outside the model: there is no near-infrared pump, and the classical
  mid-infrared field is an input, not an output.
- One-dimensional: transverse modes are replaced by the area `A`. The
  half-cycle `sech` drive has a nonzero time integral (see Eq. S3).
- A probe short enough for time resolution also samples unaffected
  high-frequency vacuum modes, so the RDV is far smaller than the degree of
  squeezing; the authors call this a loss inherent to the measurement.
- Probe shot noise enters only the RDN expression. Only variances are
  computed. Eqs. (S5)-(S6) rely on ref. 28, listed as in preparation.

## Relevance To This Project

- Covers the generation side only in part: a time-domain operator equation
  for a `chi^(2)` crystal with a classical drive. The OR source term needed
  by the claim in [[../project-status-review]] (THz polarization from the
  pump intensity) must be added; see
  [[../models/thz-optical-rectification-model]].
- Sets the size of a correction to that claim: an OR field of peak `E0`
  squeezes the THz vacuum with strength `r = |E0 d| G0 l/(n c0)`. The noise
  around the OR transient is bare vacuum only for `r << 1`.
- Eq. (8) is the time-domain EOS gate: the sampled field is the field
  convolved with the normalized probe intensity envelope, the plane-wave,
  phase-matched counterpart of `R(W)` in
  [[../sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum]].
- Project inference: Eq. (2) is a linear map of the input field, so
  Wigner-sampled vacuum realizations can be pushed through it directly; see
  [[../theory/stochastic-quantum-optics-correspondence]].
