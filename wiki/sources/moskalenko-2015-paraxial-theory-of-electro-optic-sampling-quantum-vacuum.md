---
title: Moskalenko Et Al 2015 Paraxial Theory Of Electro-Optic Sampling
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, theory, electro-optic-sampling, detection-model, quantum-vacuum, chi2, thz, shot-noise]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../models/thz-optical-rectification-model
  - ../theory/stochastic-quantum-optics-correspondence
  - ../sources/riek-2017-subcycle-quantum-electrodynamics
  - ../sources/kizmann-2019-subcycle-squeezing-time-flow-perspective
---

# Moskalenko Et Al 2015 Paraxial Theory Of Electro-Optic Sampling

## Bibliographic Metadata

- Authors: A. S. Moskalenko, C. Riek, D. V. Seletskiy, G. Burkard,
  A. Leitenstorfer (University of Konstanz).
- Year: 2015.
- Identifier: arXiv:1508.06953v1 [quant-ph], 27 Aug 2015, with Supplemental
  Material. Journal version: Phys. Rev. Lett. 115, 263601 (2015), taken from
  the reference lists of Riek 2017 and Kizmann 2019; not printed in the PDF.
- DOI: not printed in the PDF.
- Raw source:
  [Moskalenko et al. - 2015 - Paraxial theory of direct electro-optic sampling of the quantum vacuum.pdf](<../../raw/sources/Moskalenko et al. - 2015 - Paraxial theory of direct electro-optic sampling of the quantum vacuum.pdf>)
- Extracted text:
  [moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum.txt](<../../results/literature/ingest-2026-11-14/extracted_text/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum.txt>)
- Ingest date: 2026-11-14.

## Core Result

Theory only. The paper derives the operator measured by electro-optic sampling
(EOS) with balanced ellipsometric detection. The photon-number difference per
probe pulse is `S = S_eo + S_sn` (Eq. 8). `S_eo` is linear in the THz field
operator, filtered by a response function `R(W)` and weighted by the probe
intensity profile (Eq. 10). `S_sn` is probe shot noise with variance `N`, the
detected photons per pulse. For THz vacuum input `<S> = 0` and the variance is
`N + <S_eo^2>` with `<S_eo^2>` proportional to `N^2` (Eq. 13).

## Useful Equations Or Model Ingredients

Field representation: Heisenberg-picture operators in paraxial Laguerre-
Gaussian modes; classical probe `E_p` plus vacuum fluctuation `dE`. `W`, `w`,
`w_p`: THz, probe and mean detected probe angular frequency; fields in V/m;
`d`, `r41` in m/V.

```text
(1)  P_s^(2)(t) = -eps0 d E_THz,s(t) E_p(t),  P_z^(2) = 0,  d = -n^4 r41
(5)  E^(2)(r; w) = int_{-inf}^{inf} dW E_THz(r; W) E_p(r; w - W) zeta(w, W)
     zeta(w, W) = -i d (l w / (2 c0 n)) sinc[(l W / (2 c0)) (n_W - n_g)]
(8)  S = N_s - N_z = S_eo + S_sn                 [photons per probe pulse]
(10) S_eo = (d l N w_p / (c0 n)) int d^2r g00(r)^2
            int_{-inf}^{inf} dW E_THz(r; W) R(W)
     g00(r)  = sqrt(2/pi) (1/w0) exp(-r^2 / w0^2)                   [1/m]
     R(W)    = sinc[(l W / (2 c0)) (n_W - n_g)] f(W)        [dimensionless]
     f(W)    = [f_+^*(W) + f_-(W)] / 2
     f_+-(W) = int dw eta(w) a_p^*(w) a_p(w +- W) / int dw eta(w) |a_p(w)|^2
(12) S_eo = -i sqrt(B) int_0^inf dW sqrt(W / n_W) [a_s00(W) R(W) - H.c.]
     B = d^2 l^2 N^2 w_p^2 hbar / (4 pi^2 eps0 c0^3 n^2 w0^2)
(13) <S_eo^2> = N^2 [n^3 (l w_p / c0) r41]^2
                * hbar int_0^inf dW W (n / n_W) |R(W)|^2
                  / (4 pi^2 eps0 c0 n w0^2)
     <S_sn^2> = N,   <S^2> = <S_eo^2> + <S_sn^2>,   <S> = 0
(S11) <S_eo^2>_sv(tau) / <S_eo^2>
        = 1 + 2 a M + 2 b sqrt(M (M + 1)) cos(theta - 2 W_c tau)
```

- Kept: classical probe times quantized THz field, for `W` of both signs
  (`E_THz(-W) = E_THz^dag(W)`), hence `f_+` and `f_-`. Dropped: probe
  fluctuations inside `P^(2)` and second-order terms in `dE` (note 35). In
  this orientation the probe generates no THz field by optical rectification
  (Supplement Sec. 1).
- In Eq. (13) the second factor has units (m/V)^2 and the third (V/m)^2: the
  squared effective rms vacuum field filtered by `R(W)`.
- Sampled mode: LG00 THz mode of waist `w0/sqrt(2)`, polarized perpendicular
  to the probe (Eqs. 11-12). A probe delay enters as `R0(W) exp(-i W tau)`,
  so a squeezed THz vacuum gives a delay-dependent variance (Eq. S11) with
  overlap coefficients `b <= a <= 1` (Eqs. S12-S14).

| Quantity | Value | Status |
| --- | --- | --- |
| Probe | centre 255 THz, 150 THz rectangular band, flat phase; 5.9 fs intensity FWHM; `w_p/(2 pi)` = 247 THz; waist `w0` = 3 um | assumed |
| Crystal | ZnTe, `l` = 7 um, probe along [110]; `r41` = 4 pm/V; `n` = 2.76; `n_g` = 2.9; `n_W` = 2.55 to 2.59 | assumed |
| Diffraction cutoff | modes with `lambda/(2 n_W) > w0` excluded (below about 20 THz) | assumed |
| Vacuum plateau `Delta S_eo/N` | about 3.7e-6 (read from Fig. 2b) | calculated |
| rms increase over shot noise | about 6.7 % at `N` = 1e10, linear in `N` (read from Fig. 2c) | calculated |
| Squeezed example | constant squeezing over 20 to 60 THz, all modes alike; minimum 36 % of the vacuum EOS variance (Fig. 3c) | calculated |

## Assumptions

- Paraxial fields; crystal at the beam waist, anti-reflection coated, thin
  against the THz Rayleigh range (`l << k_W w0^2/2`).
- Strong classical probe in the fundamental Gaussian mode; all probe photons
  detected with `eta(w) ~ 1`; small rotation `phi = i E^(2)/E_p`.
- Instantaneous `chi^(2)` and constant `n`, `n_g` over the probe band; phase
  matching only through the `sinc` factor.
- `R(W)` does not overlap the probe spectrum, so the variance terms add.

## Limitations And Cautions

- Only the mean and variance of `S` are evaluated; the single-shot
  distribution is not derived.
- This version quotes neither the vacuum amplitude in V/cm nor a design `N`;
  the Fig. 2 values in the table are read from the plots.
- The text prints `sinh r = 2` and `M = sinh r`; Fig. 3(a) (`r` near 1.15)
  and the factor `sqrt(M(M+1))` fit `M = sinh^2 r = 2` (ingest reading).
- Diffraction is a hard cutoff; without it the vacuum EOS variance is about
  21 % larger (Supplement Sec. 3). Since `b < a < 1`, the variance cannot be
  fully suppressed at any delay (Supplement Sec. 4).

## Relevance To This Project

- Detection model for the claim in [[../project-status-review]]: one EOS shot
  returns `S = S_eo + S_sn`, with `S_eo/N = -n^3 r41 (l w_p/c0) E_bar(tau)`
  from Eq. (10). `E_bar` is the THz field at the probe delay, filtered by
  `R(W)` and averaged over `g00^2`: a Hermitian field amplitude.
- Ingest evaluation, not quoted by the paper: Eq. (13) with the table values
  gives an rms vacuum field near 12 V/cm and a shot-noise-equivalent field
  `c0/(sqrt(N) n^3 l w_p r41)` near 33 V/cm at `N` = 1e10 (104 V/cm at 1e9).
- Project inference: `S_eo` is linear in the field, so the histogram of `S` is
  the distribution of `E_bar` convolved with shot and vacuum noise. Eq. (13)
  is a vacuum-inclusive variance, which a Wigner-type stochastic field samples
  directly; see [[../theory/stochastic-quantum-optics-correspondence]].
- No generation model here; see
  [[../sources/riek-2017-subcycle-quantum-electrodynamics]].
