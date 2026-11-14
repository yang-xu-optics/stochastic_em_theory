---
title: Rivera-Dean Et Al 2025 Propagation Of Intense Squeezed Vacuum Light In Non-Linear Media
type: source-summary
status: active
created: 2026-06-06
updated: 2026-11-14
tags: [source, bsv, hhg, propagation, ionization, decoherence, husimi-q, theory]
source_count: 1
confidence: medium
related:
  - ../project-status-review
  - ../models/hhg-gas-model
  - ../theory/squeezed-vacuum-g2-proof-plan
  - ../theory/stochastic-quantum-optics-correspondence
  - ../theory/bsv-even-order-response-moment-scaling
  - spasibko-2017-multiphoton-effects-photon-number-fluctuations
  - wang-2026-bright-quantum-hhg-coherent-plus-bsv-propagation
---

# Rivera-Dean Et Al 2025 Propagation Of Intense Squeezed Vacuum Light In Non-Linear Media

## Bibliographic Metadata

- Authors: J. Rivera-Dean, D. Kanti, P. Stammer, S. Carlstrom,
  N. Tsatrafyllis, M. Yu Ivanov, M. Lewenstein, P. Tzallas.
- Year: 2025. Identifier: arXiv:2509.19608v3 [quant-ph], 4 Nov 2025.
- Publication: none stated in the PDF. Reported by a web search on
  2026-11-14, not verified against the journal: Nature Communications (2026),
  "Propagation effects in high harmonic generation media driven by bright
  squeezed vacuum light", article s41467-026-75173-8.
- Raw source: [Rivera-Dean et al. - 2025 - Propagation of intense squeezed vacuum light in non-linear media.pdf](<../../raw/sources/Rivera-Dean et al. - 2025 - Propagation of intense squeezed vacuum light in non-linear media.pdf>)
- Extracted text:
  [rivera-dean-et-al-2025-propagation-of-intense-squeezed-vacuum-light-in-non-linear-media.txt](<../../results/literature/literature-search-2026-06-06/extracted_text/rivera-dean-et-al-2025-propagation-of-intense-squeezed-vacuum-light-in-non-linear-media.txt>)
- Ingest date: 2026-06-06 (metadata stub); full read 2026-11-14.

## Core Result

Theory. The paper asks how intense 800 nm bright squeezed vacuum (BSV)
survives propagation through argon while driving high harmonic generation
(HHG). BSV ionizes far more than a coherent field of the same mean
intensity. Ionization removes infrared photons; the paper treats this as
linear loss, which turns the pure BSV into a mixed state. It defines
"quantumness" as lost above 12.5 % loss and derives a maximum medium length,
Eq. (3). Within that length, at the saturation intensity `1.3e14 W/cm^2`, a
coherent driver gives at least 50 times more plateau photons, Eq. (6).

## Useful Equations Or Model Ingredients

```text
<Y_i(t)> = 1 - int dE Q(E) exp(-int_{-inf}^{t} Gamma[I(t')] dt')          (1)
A = <N_abs>/<N_IR> = hbar omega <Y_i> n rho_at L_m / (tau <I>),  A <= 1   (2)
L_m <~ tau <I> / (8 hbar omega <Y_i> n rho_at) = L_m^(BSV)                (3)
<N_q> = int dE Q(E) |FT[<psi_E(t)| d |psi_E(t)>]|^2       single atom, p. 4
rho_q = int dE Q(E) |chi_q(E)><chi_q(E)|                  harmonic state, p. 5
<I_q> ~= int dE Q(E) E_q^2(z, t; alpha)                                   (4)
<N_q> ~ < B N_q(I) [1 + e^(-L') - 2 cos(pi L_m/L_c) e^(-L'/2)] >          (5)
B = 4 rho_at^2 L_a / (1 + 4 pi^2 (L_a/L_c)^2),   L' = L_m/L_a
L_a = 1/(sigma1 rho_at),   L_c = pi/|Delta k|
<N_q>^(Coh.) / <N_q>^(BSV) >~ 50                                          (6)
Q(E) = exp[-E_x1^2/(2(1+e^(2r))) - E_x2^2/(2(1+e^(-2r)))] / (pi cosh r)  (B1)
Delta k_el ~= -e^2 omega_q rho_at Y_i(I) / (2 eps0 c m_e omega^2)        (B49)
<a^dag^n a^n>_noisy = t^n <a^dag^n a^n>_0                                (B54)
g2_noisy(0) = g2_0(0)                                                    (B55)
Var(X_i)_noisy = t Var(X_i)_0 + (1 - t);   Var_0 = e^(2r), e^(-2r)       (B58)
```

Units and symbols: `E` in V/cm, `I = c eps0 E^2 / 2` in W/cm^2; `Gamma`
ionization rate (1/s); `Y_i` ionization probability; `n` infrared photons
absorbed per ionized atom; `rho_at` in atoms/cm^3; `tau` pulse duration;
`L_m`, `L_a`, `L_c` medium, absorption, and coherence lengths (cm); `t` loss
transmission; `X_1 = a^dag + a`, `X_2 = -i(a^dag - a)`, vacuum variance 1.
`Q(E)` is a marginal of the Husimi function, obtained as the large-volume
limit `lim P(E, E)` of the generalized positive-P function (App. B 2, B 3).

| Parameter or result | Value | Where |
| --- | --- | --- |
| Target and driver | Ar; 800 nm, linear; `sin^2` envelope, 13 fs; `I_sat` = 1.3e14 W/cm^2 | p. 2, p. 3 |
| Squeezing | `r` about 17 quoted for `I_sat`; volume about 1e-14 cm^3 | p. 2, App. B 1 |
| Ionization probability | coherent 2 % at 1.3e14; BSV 2 % at 9e12 and about 50 % at 1.3e14 W/cm^2 | Fig. 2b, p. 3 |
| Loss threshold | `A = 1/8`, illustrated for `r = 2` | Fig. 3a,b |
| Density and absorption | 1e18 cm^-3, Eq. (6) holds above 2e16 cm^-3; `sigma1` about 1e-17 cm^2 at 20 to 40 eV | Fig. 3, Fig. 4d, App. B 3 |
| Single-atom cutoff at `I_sat` | H29 coherent, H33 BSV; BSV yield over 10 times lower | Fig. 4a,b |
| H15 yield ratio, coherent over BSV | about 30 for `L_m > 2.5 L_a` without loss limit; at least 50 for `L_m` about `2 L_a` | Fig. 4c,d |
| Harmonic photons per pulse | about 5e2 at `I_sat`; about 20 at 1e13 W/cm^2 (1e13-photon BSV) | Discussion, App. B 3 |

- BSV statistics. Under the beam-splitter loss model every normalized
  correlation is unchanged, Eqs. (B54) and (B55), so `g2` keeps its input
  value. The squeezed variance rises toward vacuum, Eq. (B58), and the
  variance product exceeds the minimum-uncertainty value for `0 < A < 1`.
- Harmonic statistics. The state is a mixture of coherent states weighted by
  `Q(E)`. Only mean photon numbers are computed; no harmonic `g2` is given.
  The authors state that none of their results proves a quantum nature of
  the source or of the harmonics (Discussion).

## Assumptions

- Single-mode BSV. Coherence between different coherent-state components is
  neglected, justified by entanglement with the absorbing medium (p. 4).
- Quasistatic ionization rates: TD-CIS above 1e13 W/cm^2, scaled PPT below
  (App. B 2). Dipole: strong-field approximation times a depletion factor
  `exp(-(1/2) int Gamma dt)`, Eq. (B13).
- Harmonic propagation is on-axis and paraxial, Eq. (5), with a
  position-independent atomic response and focusing and dipole phase terms
  dropped. The driver's loss enters only through the number `A`.

## Limitations And Cautions

- Despite the "fully quantized" framing, the computed observables are
  `Q`-weighted averages of semiclassical single-field results, Eqs. (1), (4).
- The loss is linear and intensity independent, but its cause, ionization,
  is strongly nonlinear. A nonlinear absorber lowers `g^(n)` (Methods of
  [[spasibko-2017-multiphoton-effects-photon-number-fluctuations]]), so
  Eq. (B55) does not show that ionization preserves `g2`. Project-side remark.
- `A = 1/8` is a chosen definition, not a derived bound. `r` about 17 and a
  volume of 1e-14 cm^3 disagree under `<I> = c hbar omega sinh^2(r) / V`,
  which gives `r` about 10 (project arithmetic).
- Photon numbers are order-of-magnitude estimates scaled from 60 fs coherent
  experiments (App. B 3). As printed, `B` has `L_a` to the first power and
  `Delta k_med` is 2e-6 rad/cm for H15; neither was checked.

## Relevance To This Project

- Same sampled-field method as [[../models/hhg-gas-model]], plus two things
  the project lacks: ground-state depletion and phase matching, Eq. (5).
- Feasibility: the estimate that 1e13 BSV photons in 60 fs on 2.5e-7 cm^2
  reach about 1e14 W/cm^2 (App. B 3) bears on the intensity question in
  [[../theory/bsv-even-order-response-moment-scaling]]. At that intensity
  about half the atoms ionize, so a BSV fundamental is in the depleted regime.
- Eq. (B54): linear loss leaves all normalized intensity moments, and hence
  the `(2n-1)!!` factors, unchanged. Nonlinear loss is not covered.
