---
title: Stammer Et Al 2026 Photon Anti-Bunching In High Harmonic Generation
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, hhg, photon-statistics, anti-bunching, heisenberg-picture]
source_count: 1
confidence: medium
related:
  - ../project-status-review
  - ../theory/non-gaussian-output-novelty
  - ../models/hhg-gas-model
  - stammer-2025-theory-of-quantum-optics-and-optical-coherence-in
  - gorlach-2020-quantum-optical-nature-hhg
  - gothelf-2026-limitations-of-approximative-phase-space-description
---

# Stammer Et Al 2026 Photon Anti-Bunching In High Harmonic Generation

## Bibliographic Metadata

- Authors: Philipp Stammer, Javier Rivera-Dean, Maciej Lewenstein.
- Year: 2026. Identifier: arXiv:2606.17620v1 [quant-ph], 16 Jun 2026.
  Preprint; no journal reference or DOI in the PDF.
- Raw source: [Stammer et al. - 2026 - Photon anti-bunching in high harmonic generation.pdf](<../../raw/sources/Stammer et al. - 2026 - Photon anti-bunching in high harmonic generation.pdf>)
- Extracted text: [stammer-2026-photon-anti-bunching-in-hhg.txt](<../../results/literature/ingest-2026-11-14/extracted_text/stammer-2026-photon-anti-bunching-in-hhg.txt>)
- Ingest date: 2026-11-14.

## Core Result

The paper predicts photon anti-bunching in the two-time intensity correlation
of single harmonics, for HHG driven by a coherent state. The driver is not
squeezed: it is `|alpha>` with `|alpha| ~ 1e6`, and the dipole is propagated
with the classical mean field.

- Single atom: `g2(0) < 1` and `g2(0) < g2(tau)` for all odd harmonics 11 to
  23 (Fig. 2) and for 7 and 9 (Fig. 5). Quoted values: `g2(0) ~ 5e-3` for
  harmonic 11 and `~ 3e-3` for harmonic 13.
- `N` uncorrelated atoms: `g2(tau)` rises with `N` and reaches 1 for large
  `N` (Fig. 3, `N` from `1e2` to `1e7`). The Mandel parameter `Q/<n>` goes
  from about -1 to 0 over the same range (Fig. 4).
- The three-step-model explanation (one electron cannot recombine twice at
  once) is offered as intuition, not derived.

## Useful Equations Or Model Ingredients

Field representation: Heisenberg-picture field operators; normally ordered
correlation functions; emitted modes start in vacuum. Units: `hbar` kept,
coupling constant `g`, harmonic index `q`; numerical values in atomic units.

```text
H = H_F + H_S + H_I,  H_F = sum_q hbar w_q a_q^dag a_q,
H_I = - sum_{i=1..N} d_i . E_Q                                              (1)
E_Q = -i g hbar sum_q sqrt(q) eps_q (a_q^dag - a_q)                         (2)
a_q(t) = a_q e^{-i w_q t}
       + g sqrt(q) int_{t0}^{t} dt' e^{-i w_q (t-t')} sum_i eps_q . d_i(t')  (3)
```

The dipole is taken to zeroth order in the quantized field:
`d(t) = U_sc^dag(t) d(0) U_sc(t)` with `H_sc = H_S - sum_i d_i . E_cl(t)`,
`E_cl = Tr[E_Q |alpha><alpha|]`. Intensity correlation of harmonic `q`:

```text
G2(t1,t2) = <E-(t1) E-(t2) E+(t2) E+(t1)> = <: I(t1) I(t2) :>               (4)
g2(tau) = <: I_q(t) I_q(t+tau) :> / (<I_q(t)> <I_q(t+tau)>)             (5, 12)
        = G2(t, t+tau) / (G1(t+tau) G1(t)),  G1 = G1_coh + G1_inc      (13, 14)
G2(t, t+tau) = hbar^4 g^4 q^2 <N(t,tau)>                                    (6)
<N(t,tau)> = g^4 q^2 int_{t0}^{t} dt1 int_{t0}^{t+tau} dt2 int_{t0}^{t+tau} dt3
             int_{t0}^{t} dt4 e^{-i w_q (t1+t2-t3-t4)} D(t1,t2,t3,t4)       (7)
one atom: D = <g| d(t1) d(t2) d(t3) d(t4) |g>                               (9)
            = <d(t1)d(t2)><d(t3)d(t4)> + <D[d(t1)d(t2)] D[d(t3)d(t4)]>     (10)
D[d(t1)d(t2)] = d(t1)d(t2) - <d(t1)d(t2)>                                  (11)
N atoms: sum_{ijkl} <d_i(t1) d_j(t2) d_k(t3) d_l(t4)>
         = N!/(N-4)! <d(t1)><d(t2)><d(t3)><d(t4)> + O(N^3)                 (15)
Q = <n> (g2(0) - 1)
```

Conditions used: a classical field obeys `g2(0) >= g2(tau)` and
`g2(0) >= 1`. Anti-bunching is `g2(0) < g2(tau)`; `g2(tau) < 1` is
non-classical. Parameters of Fig. 2: `E0 = 0.053`, `w_L = 0.057`, `I_p = 0.5`
atomic units (hydrogen), `t = T = 2 pi/w`, 50 delay values, `|tau|` up to
about 27 atomic units.

## Assumptions

- Coherent-state driver; emitter back-action on the driver and quantum
  corrections to the dipole are neglected (zeroth order in the quantum field).
- Emitters are uncorrelated, identical, and see the same field (App. C).
- Only the dipole component along the laser polarization; one harmonic mode
  per correlation function; no propagation or phase matching.

## Limitations And Cautions

- The evaluation of the four-time dipole correlation is in a Supplementary
  Material that is not part of the PDF. The atomic model behind Fig. 2 could
  not be verified.
- The delays shown cover about a quarter of an optical cycle (`T` is about
  110 atomic units at `w_L = 0.057`). The paper notes that current detectors
  do not resolve this.
- Eq. (7) repeats the prefactor `g^4 q^2` already present in Eq. (6);
  transcribed as printed.
- Preprint. The claim to be the first prediction of this kind is the
  authors'.

## Relevance To This Project

- Not a squeezed-light paper. It concerns emitter-induced non-classicality,
  which a classical pump model with a deterministic response cannot give; see
  Eq. (24) of
  [[gothelf-2026-limitations-of-approximative-phase-space-description]].
- It bounds where that matters. The coherent term of Eq. (15) scales as
  `N^4` and the rest at most as `N^3`, so `g2 -> 1` for many emitters. For a
  macroscopic optical-rectification crystal this supports treating the
  response to each pump amplitude as a coherent classical field, with
  emitter-noise corrections falling at least as `1/N` (our inference from
  Eq. 15; the paper treats HHG in atoms only).
- The Heisenberg-picture source-field solution, Eq. (3), is the natural
  starting point for the "full quantum treatment" of the THz mode in the
  headline claim: replace the coherent-state average by a squeezed-vacuum
  average and keep the operator ordering. The paper does not do this.
- Companion theory paper:
  [[stammer-2025-theory-of-quantum-optics-and-optical-coherence-in]].
