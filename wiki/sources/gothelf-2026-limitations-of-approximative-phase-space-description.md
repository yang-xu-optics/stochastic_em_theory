---
title: Gothelf Et Al 2026 Limitations Of An Approximative Phase-Space Description
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, hhg, quantum-light, phase-space, husimi-q, positive-p]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../theory/stochastic-quantum-optics-correspondence
  - ../theory/non-gaussian-output-novelty
  - gothelf-2025-hhg-in-a-crystal-driven-by-quantum-light
  - gorlach-2023-hhg-driven-by-quantum-light-main-article
  - de-la-pena-2026-high-order-correlations-wigner-negativities-bsv-hhg
---

# Gothelf Et Al 2026 Limitations Of An Approximative Phase-Space Description

## Bibliographic Metadata

- Authors: R. V. Gothelf, L. B. Madsen, C. S. Lange (Aarhus). Year: 2026.
- Identifier: arXiv:2602.04370v1 [quant-ph], 4 Feb 2026 (equation numbers
  below). Journal reference as supplied with the ingest request, not printed
  in the arXiv PDF, not checked: Phys. Rev. A 113, 063107 (2026),
  DOI 10.1103/cxff-kky6.
- Raw source: [Gothelf et al. - 2026 - Limitations of an approximative phase-space description in strong-field quantum optics.pdf](<../../raw/sources/Gothelf et al. - 2026 - Limitations of an approximative phase-space description in strong-field quantum optics.pdf>)
- Extracted text: [gothelf-2026-limitations-of-an-approximative-phase-space-description.txt](<../../results/literature/ingest-2026-11-14/extracted_text/gothelf-2026-limitations-of-an-approximative-phase-space-description.txt>)
- Ingest date: 2026-11-14.

## Core Result

The paper names and tests the "approximative positive P (APP) representation":
the diagonal coherent-state expansion with the Husimi Q function as weight,
used by most quantum-light strong-field papers.

- APP replaces the driver by the classical mixture
  `int d^2 alpha Q(alpha) |alpha><alpha|` (Eqs. 12, 25), equivalent to a
  coherent laser with amplitude and phase drawn per shot from `Q` (Eq. 14).
- Proven (Sec. III A, App. A): if a coherent driver yields coherent harmonic
  light (no dipole correlations), APP cannot give squeezing below vacuum
  (Eqs. 21-23), `g2(0) < 1` (Eq. 24), or Wigner negativity (Eq. A5) in an
  emitted mode, for any driver state.
- Right in the bright limit: driver photon number (off by exactly 1), driver
  `<a>` and `<a^2>`, harmonic spectrum (relative error `O(1/|alpha|^2)`).
- Wrong: driver quadrature variance, Fock-driver statistics, and the harmonic
  quadrature variance in an exactly solvable one-band model (Fig. 2).

## Useful Equations Or Model Ingredients

Representation: generalized P, specialised to Glauber-Sudarshan P (Eq. 6),
positive P (Eq. 7), APP (Eq. 11). One driver mode, others in vacuum. Atomic
units; amplitudes dimensionless; vacuum variance 1/4 for
`X(theta) = (a e^{-i theta} + a^dag e^{i theta})/2`. APP makes Eq. (8) diagonal:

```text
P_PP(alpha, beta) = (1/4pi) exp(-|alpha - beta*|^2/4) Q((alpha + beta*)/2)  (8)
Q(alpha) = (1/pi) <alpha| rho_L |alpha>                                     (9)
P_PP ~ P_APP(alpha, beta) = delta2(alpha - beta*) Q((alpha + beta*)/2)     (10)
rho_APP(t) = int d^2 alpha Q(alpha) |psi^alpha(t)><psi^alpha(t)|           (11)
```

The limit is not re-derived. Sec. II B lists the published arguments: field
amplitude `2 g0 alpha` fixed while `g0 = sqrt(2 pi/V) -> 0` (Gorlach 2023);
the same with `g0 N` fixed for `N` emitters; lowest order in
`(alpha - beta)/(alpha + beta)`. Driver moments, APP left, exact right:

```text
<a^dag a>_APP = <a a^dag> = <a^dag a> + 1;  <a>, <a^2> unchanged       (28a-c)
<DX^2(theta)>_APP = <DX^2(theta)> + 1/2                                    (29)
g2_APP(0) = g2(0) n^2/(n+1)^2 + (4n + 2)/(n+1)^2,  n = <a^dag a>           (30)
Fock state: g2_APP(0) = 1 + 1/(n+1);  exact g2(0) = 1 - 1/n
```

One-band benchmark (Sec. III C): 1D chain, `L` sites, half filling,
`E(q) = sum_l b_l cos(a l q)`, coherent driver. The current commutes with
the Hamiltonian, so the emitted state is exactly a multimode coherent state:

```text
gamma_n = G_n sum_l C_l J_n(l gt0 |alpha|) e^{i n phi_alpha},  n odd       (36)
G_n = 4 pi a g0 delta(w_n - n w_L)/sqrt(w_n),  gt0 = 2 a g0/sqrt(w_L),
C_l = l b_l sum_q cos(a l q);  exact <DX_n^2(theta)> = 1/4                 (38)
```

Spectrum: APP differs from exact by a relative `O(1/|alpha|^2)`, term by
term (Eqs. 40, 42, 43). Variance of harmonic `n`, leading order in `|alpha|`:

```text
<DX_n^2>_APP - 1/4 = (1/4) { 2 K1 + [ e^{-2 i theta} K2 + c.c. ] }         (48)
K1 = <a_n^dag a_n>_APP - |<a_n>_APP|^2 ~ (G_n^2/|alpha|^2) sum_{l1,l2}
     C_l1 C_l2 [ n^2 A0 A0' + 2 A1 A1' + n A1 A0' + n A0 A1' ]       (46, B21)
K2 = <a_n^2>_APP - (<a_n>_APP)^2 ~ (G_n^2/|alpha|^2) e^{2 i n phi_alpha}
     sum_{l1,l2} C_l1 C_l2 [ 2 A1 A1' + n A1 A0' + n A0 A1' ]        (47, B22)
A0 = J_n(x), A1 = -(x/2) J_{n+1}(x), x = gt0 l1 |alpha|; primes: l2  (B14, B17)
```

Scaling stated by the paper: `gamma -> K gamma` multiplies the error by `K^2`;
`gamma` grows with emitter number and, as harmonic peaks sharpen, with pulse
duration. Fig. 2 (`n = 3`, ZnO band, `g0 = 4e-8`, `w_L = 0.005`,
`<n_L> = 7.35e11`): the error is positive at all angles and rises as `L^2`,
from a few `1e-14` of 1/4 at `L = 1e3` to a few `1e-2` at `L = 1e9` (log plot).

## Assumptions

- Single driver mode; dipole approximation; `A^2` neglected; one output mode.
- The no-go statements need coherent-in, coherent-out (Eqs. 15-16): exact for
  the one-band model, not for atoms, multiband or correlated solids.
- Benchmark: time-periodic pulse, normalised to a 20-cycle sin^2 simulation.

## Limitations And Cautions

- No error is computed for a BSV driver: the driver examples are general
  moments and Fock states, and the HHG benchmark uses a coherent driver.
- The emitted-mode `g2` error is not computed (expected small and positive, no
  `L^2` growth). With dipole correlations the error is "not controlled".

## Relevance To This Project

- The project's Husimi-Q coherent-state sampler is the APP; this paper states
  its limits. See [[../theory/stochastic-quantum-optics-correspondence]].
- Supports the new headline for intensity-type observables: driver and
  spectrum errors are `O(1/<n>)`. Squeezed vacuum in Eq. (30) gives
  `g2_APP = 3 - 1/(<n>+1)` against the exact `3 + 1/<n>` (our evaluation).
- `1/<n>` is not the only small parameter: the `n^2` term of Eq. (B21) is
  `n^2 |gamma_n|^2/|alpha|^2`, harmonic over pump photon number times order
  squared (our reading). A THz error bound needs the analogous ratio.
- With coherent-in, coherent-out, a classical-mixture pump never gives output
  squeezing below vacuum, `g2 < 1`, or Wigner negativity; see
  [[../theory/non-gaussian-output-novelty]]. Q-sampled variances carry +1/2.
