---
title: Rivera-Dean Et Al 2026 Erasing Photons From BSV Via ATI
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, bsv, theory, ati, heralding, non-gaussian, wigner-negativity]
source_count: 1
confidence: medium
related:
  - ../project-status-review
  - ../theory/non-gaussian-output-novelty
  - ../theory/stochastic-quantum-optics-correspondence
  - lyu-2025-photon-statistics-ati
  - mao-2025-benchmarking-atomic-ionization-driven-by-strong-quantum-light
  - imai-2026-heralded-ultrafast-generation-of-macroscopic-quantum-states-in
---

# Rivera-Dean Et Al 2026 Erasing Photons From BSV Via ATI

## Bibliographic Metadata

- Authors: J. Rivera-Dean, T. Rook, G. Singh, P. Stammer, M. Khokhlova,
  E. Pisanty, C. Figueira de Morisson Faria.
- Year: 2026.
- Identifier: arXiv:2605.31160v1 [quant-ph], 29 May 2026. Preprint, 31 pages
  including Supplementary Material (SM, Secs. A to C). No DOI.
- Raw source: [Rivera-Dean et al. - 2026 - Erasing photons from bright squeezed vacuum light via above-threshold ionization.pdf](<../../raw/sources/Rivera-Dean et al. - 2026 - Erasing photons from bright squeezed vacuum light via above-threshold ionization.pdf>)
- Extracted text:
  [rivera-dean-2026-erasing-photons-from-bsv-via-ati.txt](<../../results/literature/ingest-2026-11-14/extracted_text/rivera-dean-2026-erasing-photons-from-bsv-via-ati.txt>)
- Ingest date: 2026-11-14.

## Core Result

Theory, no experiment. One atom is ionized by single-mode BSV
(above-threshold ionization, ATI) and the light is conditioned on a
photoelectron detected with momentum `p_f`. The heralded light state is the
BSV coherent-state superposition with every component reweighted by the
semiclassical direct-ATI amplitude for the classical field of that component
(Eq. 17). The amplitudes are negligible below about 0.01 a.u. field strength,
so conditioning removes the centre of phase space and leaves two lobes of
opposite field sign: a large, cat-like, non-Gaussian state.

## Useful Equations Or Model Ingredients

Representation: coherent-state expansion with amplitude `c(a)`; the Husimi
function is `Q(a) = pi |c(a)|^2`. Atomic units unless marked SI.

```text
(10)  |Psi(t0)> = |g> x S_L(r)|0>
(A6)  c(a) = exp{-[|a|^2 + a*^2 tanh(r)] / 2} / [pi sqrt(cosh r)]
(14)  |Phi(p_f,t)> = <p_f|Psi(t)>                       (heralded light state)
(17)  |Phi(p_f,t)> = int d2a c~(a) |a>,   c~(a) = int dt' c(a) b(p_f,t';a)
(18)  b(p_f,t';a) = i exp[i S(p_f,t,t';a)]
                    * <p~_f(a) + A_cl(t';a)| r |g> . E_cl(t';a)
(19)  p~_f^2 / 2 = n omega_L - I_p - eps^2 / (4 omega_L^2),   n integer
      eps(a) = 2 g(omega_L) a,   g(omega) = sqrt(hbar omega / (2 eps_0 V))  (SI)
(29)  N = -1 + int dX1 dX2 |W(X1,X2)|            (Wigner negativity; W: Eq. 24)
(32)  rho(p) = int dp' w(p|p') |Phi(p',t)><Phi(p',t)|,   w Gaussian, width sigma
(34)  <B> = sum_ij (-1)^(ij) <Pi(beta_A^i) x Pi(beta_B^j)>,   local: |<B>| <= 2
(A44) P(p_f) = int d2a Q_0(a) | int dt' b(p~_f,t';a) |^2
```

`|g>` is the atomic ground state; `b` the semiclassical direct-ATI amplitude
for the classical field `E_cl(t;a) = <a|E_L(t)|a>`, with vector potential
`A_cl`, action `S` (Eqs. 16, A45) and canonical momentum `p~_f`; `eps` is the
field strength; Eq. (19) gives the ATI rings on which `c~` peaks; `Pi(beta)`
is the displaced parity operator; `w` is the momentum-detector response.

| Quantity | Value | Where |
| --- | --- | --- |
| System | hydrogen, `I_p = 0.5 a.u.`; `omega_L = 0.057 a.u.` (800 nm); four optical cycles | Figs. 3-7 |
| Field strength that contributes | `abs(eps)` about 1e-2 a.u.; `abs(a)` about 1e6 for `g = 1e-8 a.u.`, `r` about 10 | Sec. II B, SM C 2 |
| Rescaled runs | `g = 5e-3 a.u.`, `abs(a)` about 10, lobes at `X1 = +-10`, Fock cutoff 200 | Fig. 5, SM C 2 |
| Non-Gaussianity | `N` about 0.7 at `p_par = 0`, 0.47 at 0.1 a.u., about 0.1 for 0.2-0.6 a.u.; only even photon numbers at `p_f = 0`, `P_even` tends to 0.5 at large `p_par` | Eq. 28, Figs. 5d-g, 6e (read off) |
| Finite resolution, `p_f = (0.1, 0)` a.u. | `N` falls from 0.47 to about 0.22 at `sigma_par = 0.01 a.u.` and about 0.1 at 0.1 a.u.; nearly unchanged for `sigma_perp` up to 0.1 a.u. | Fig. 6e (read off) |
| CHSH value | about 2.7 at `p_par = 0.01 a.u.` (Tsirelson 2.83); below 2 above about 0.09 a.u.; about 2.07 at `p_par = 0` for `sigma_par = 2e-3 a.u.` | Fig. 7c (read off) |

Stated experimental requirements (Sec. IV B, with Secs. III C-D):

- A BSV source that is effectively single-mode and strong enough for ATI.
  Current sources are down-conversion based and multimode; the authors point
  to spatial and spectral filtering that approaches one mode (their ref. 55).
- Heralding on the photoelectron momentum, with fine resolution along the
  polarization direction. Resolution across it matters little.
- A way to characterize the state: standard tomography is impractical at
  these photon numbers, and the suggested alternatives are not yet complete.

## Assumptions

- Driving field: one monochromatic, linearly polarized mode with real `r`,
  other modes in vacuum, no pulse envelope (four optical cycles). Single
  active electron, dipole approximation; direct ionization only (Eq. A17).
- No dynamical back-action of the electron on the field: the displacement it
  causes (about 1e-4) is set to identity and the quadratic field term is
  dropped (Eqs. A30, A37).
- Strong-field approximation: in each component the classical field replaces
  the field operator, valid in the tails of `c(a)` (Eq. A38). Saddle-point
  evaluation of the ionization-time integral (Eq. A46).
- Numerics: discrete coherent-state lattice, and a coupling `g` raised from
  1e-8 to 5e-3 a.u. so that `eps` stays near 1e-2 a.u. with `abs(a)` about 10.

## Limitations And Cautions

- All quantitative non-Gaussianity values come from the rescaled runs
  (`abs(a)` about 10, up to hundreds of photons), not from the realistic
  regime (`abs(a)` about 1e6). The authors state that rescaling keeps only
  qualitative features. The `r` used for Figs. 5-7 is not stated.
- CHSH values are local optima of a restricted search, given as lower bounds.
- One atom and no absolute heralding probability (curves are normalized to
  their maximum). A gas target with many ionization events per shot, optical
  loss, and pulsed multimode light are not treated.
- Conventions: Eq. (10) defines `S_L(r) = exp[r (a_L^2 - h.c.)]`, while
  Eq. (A6) has the Fock coefficients of the usual `exp[(r/2)(...)]` operator;
  Eqs. (16) and (A45) give the action with different prefactors and signs.
- Table values marked "read off" come from figure axes and are approximate.

## Relevance To This Project

- Correction to [[../project-status-review]], which lists this paper under
  "back-action on the pump". Dynamical back-action is explicitly neglected
  here. The effect is conditional: detecting the electron filters the pump
  state.
- Marks the boundary of the classical-noise model. Unconditional
  photoelectron spectra equal the Husimi-weighted average of semiclassical
  responses (Eq. A44), which an incoherent mixture also reproduces. Only
  conditioning plus a coherence-sensitive measurement separates the two
  (SM A 4). See [[../theory/non-gaussian-output-novelty]] and
  [[lyu-2025-photon-statistics-ati]].
- No bearing on BSV source parameters or on optical rectification.
