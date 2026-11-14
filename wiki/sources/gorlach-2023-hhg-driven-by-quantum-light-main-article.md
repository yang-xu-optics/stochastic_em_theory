---
title: Gorlach Et Al 2023 HHG Driven By Quantum Light Main Article
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, hhg, bsv, husimi-q, generalized-p, coherent-state-sampling]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../models/hhg-gas-model
  - ../theory/stochastic-quantum-optics-correspondence
  - ../simulations/gorlach-2023-fig3b-proxy-reproduction
  - ../simulations/gorlach-2023-fig-iv2-bsv-threshold
  - gorlach-2023-hhg-driven-quantum-light-supplement
  - gothelf-2026-limitations-of-approximative-phase-space-description
---

# Gorlach Et Al 2023 HHG Driven By Quantum Light Main Article

## Bibliographic Metadata

- Authors: Alexey Gorlach, Matan Even Tzur, Michael Birk, Michael Kruger,
  Nicholas Rivera, Oren Cohen, Ido Kaminer.
- Year: 2023 (preprint November 2022). Identifier: arXiv:2211.03188v1;
  equation numbers below are from this version. Published as Nature Physics
  19, 1689 (2023), DOI 10.1038/s41567-023-02127-y (not printed in the arXiv
  PDF; the journal version was not compared).
- Raw source: [Gorlach et al. - 2023 - High harmonic generation driven by quantum light - main article arXiv 2211.03188v1.pdf](<../../raw/sources/Gorlach et al. - 2023 - High harmonic generation driven by quantum light - main article arXiv 2211.03188v1.pdf>)
- Extracted text: [gorlach-2023-hhg-driven-by-quantum-light-main-article.txt](<../../results/literature/ingest-2026-11-14/extracted_text/gorlach-2023-hhg-driven-by-quantum-light-main-article.txt>)
- Ingest date: 2026-11-14.

## Core Result

The driver state is expanded in coherent states with the generalized
(positive) P distribution. In the limit of vanishing single-photon field
amplitude at fixed total field, the expansion becomes diagonal with the
Husimi Q function as weight: the electron state and the emitted spectrum are
averages of semiclassical results over `Q` of the complex field amplitude
(Eqs. 4-5). Coherent and Fock drivers keep the usual cutoff; thermal and BSV
drivers give a cutoff proportional to `I_p (U_p/(hbar w0))^(2/3)` (Eqs. 6-8),
from the maximum of the ADK ionization probability times `Q`. The main
article prints no explicit `Q`; the forms below are quoted from the
supplement ([[gorlach-2023-hhg-driven-quantum-light-supplement]]).

## Useful Equations Or Model Ingredients

Representation: generalized P (Eq. 2), reduced to Husimi Q in the limit. SI
units; `alpha` dimensionless; `E_a` and `eps1` are field amplitudes.

```text
E_alpha(t) = (i/2) e_ks f(t) (E_a e^{-i w0 t} - E_a* e^{i w0 t})
i hbar d|phi_a>/dt = (H_0 + d . E_alpha(t)) |phi_a>                         (1)
rho_drive = int P(alpha, beta*) |alpha><beta|/<beta|alpha> d^2alpha d^2beta (2)
P(alpha, alpha*) = Q(alpha)/(4 pi)
i hbar d rho/dt = [H_0 + d . E_hat(t), rho]                                 (3)
E_hat(t) = i sum_{k,s} eps1 e_ks (a_ks e^{-i w t} - a_ks^dag e^{i w t})
E_a = 2 eps1 alpha;  limit V -> inf (eps1 -> 0), <n> -> inf, E_a fixed
rho_electron = int d^2 E_a Q(E_a) |phi_a(t)><phi_a(t)|                      (4)
d eps/d w = w^4/(6 pi^2 c^3 eps0) int d^2 E_a Q(E_a) |d_a(w)|^2             (5)
cutoff(coherent, Fock) = 3.17 U_p + I_p                                     (6)
cutoff(thermal) = 1.92 I_p (U_p/(hbar w0))^(2/3) + I_p                      (7)
cutoff(BSV)     = 3.05 I_p (U_p/(hbar w0))^(2/3) + I_p                      (8)
U_p = e^2 E_classical^2/(4 m w0^2), same mean intensity for all states
rho_HHG = int d^2alpha d^2beta P(alpha, beta*) rho_ab(t),
i hbar d rho_ab/dt = (d_a(t) . E_hat) rho_ab - d_b(t) . (rho_ab E_hat)      (9)
```

From the supplement (Secs. I-II), the limit and the distributions in terms
of `E_a`; `Ebar` is the amplitude of a coherent state of the same intensity:

```text
P(alpha, beta*) = (1/4pi) exp(-|alpha - beta*|^2/4) Q((alpha + beta*)/2)
lim_{eps1 -> 0} (1/4pi) (1/(4 eps1^2)) exp(-|E_a - E_b|^2/(16 eps1^2))
    = delta2(E_a - E_b)                                   (before I.17)
breaks down when |E_a|^2/(16 eps1^2) = V I/(8 c hbar w) ~ 1           (I.25)
coherent: Q(E_a) = exp(-|E_a - Ebar|^2/(4 eps1^2))/(4 pi eps1^2)       (I.26)
Fock: Q = (1/pi) exp(-|E_a|^2/(4 eps1^2)) |E_a|^(2n)/((4 eps1^2)^n n!) (I.27)
  both tend to a delta function as eps1 -> 0
thermal: Q(E_a) = exp(-|E_a|^2/|Ebar|^2)/(pi |Ebar|^2)                (I.29)
BSV: Q = exp(-2 a_y^2/(1+e^{2r}) - 2 a_x^2/(1+e^{-2r}))/(pi cosh r)    (I.30)
  nbar = sinh^2 r >> 1:  Q ~ exp(-a_y^2/(2 nbar)) exp(-a_x^2)         (I.31)
  Q_BSV(E_a) = (1/(2|Ebar|^2)) exp(-Im[E_a]^2/(2|Ebar|^2)) delta(Re[E_a])
  random phase: Q_BSV(E_a) ~ exp(-|E_a|^2/(2|Ebar|^2))/(2 pi |Ebar|^2) (I.32)
Q_th(U) = exp(-U/Ubar)/Ubar (II.6);  Q_BSV(U) = exp(-U/(2Ubar))/(2Ubar) (II.7)
P(U) ~ exp(-a U^(-1/2) - U/(b Ubar)), b = 2 (BSV), 1 (thermal)       (II.13)
a = 2 sqrt(2) I_p^(3/2)/(3 w0) (II.3, atomic units)
U_max = (a b Ubar/2)^(2/3),  cutoff = I_p + 3.17 U_max          (II.15, II.8)
```

## Assumptions

- One driver mode; dipole approximation; single atom, said to carry over to
  many equivalent atoms.
- Perturbation theory in `eps1` for the emitted light: first order for the
  separable light-matter state, second order for the emitted energy.
- Cutoff estimate: ADK rate times `Q`; the most probable ionizing amplitude
  sets `U_max`. Spectra come from TDSE dipoles (details in the supplement).

## Limitations And Cautions

- The main text prints `eps1 = sqrt(hbar/(2 w V eps0))`; SI Eq. (I.25)
  corresponds to `eps1^2 = hbar w/(2 V eps0)`.
- The text calls Eq. (5) a "coherent sum"; the formula is an incoherent
  average of `|d_a(w)|^2`. Fig. 3 calls `Q` "approximately sufficient".
- Non-classical properties of the harmonics are expected from Eq. (9), not
  computed. Agreement of Eqs. (6)-(8) with simulations is called "relatively
  good" (Fig. 5, intensities up to about `1.4e14 W/cm^2`).
- Our checks, not statements of the paper: the fixed-phase BSV line is not
  unit-normalized as printed (a 1D Gaussian of variance `|Ebar|^2` has
  prefactor `(2 pi |Ebar|^2)^(-1/2)`), and Eq. (I.32) has
  `<|E_a|^2> = 2 |Ebar|^2`, twice the fixed-phase value, so it serves the
  tail argument but is not a consistent sampling distribution.

## Relevance To This Project

- Origin of the Husimi-Q coherent-state averaging the project used, and of
  the scaling limit that [[../project-status-review]] calls the macroscopic
  limit. In it, coherent and Fock drivers reduce to one amplitude and BSV to
  a real Gaussian amplitude of variance `|Ebar|^2` on the anti-squeezed
  quadrature. That is the classical Gaussian amplitude-noise model of the new
  headline claim: the model is here; an error bound and the quantum
  corrections are not.
- With `E_a = 2 eps1 alpha`, Eq. (I.25) reads `|alpha|^2/4 ~ 1` (our
  rewriting): the stated validity condition is large photon number. It does
  not cover the fluctuation errors of the emitted field found in
  [[gothelf-2026-limitations-of-approximative-phase-space-description]].
- Used by [[../simulations/gorlach-2023-fig3b-proxy-reproduction]] and
  [[../simulations/gorlach-2023-fig-iv2-bsv-threshold]].
