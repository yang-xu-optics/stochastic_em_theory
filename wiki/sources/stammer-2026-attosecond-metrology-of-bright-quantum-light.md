---
title: Stammer Et Al 2026 Attosecond Metrology Of Bright Quantum Light
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, bsv, theory, attosecond-streaking, husimi-q, squeezing]
source_count: 1
confidence: medium
related:
  - ../project-status-review
  - ../theory/stochastic-quantum-optics-correspondence
  - ../theory/squeezed-vacuum-g2-proof-plan
  - kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv
  - gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light
---

# Stammer Et Al 2026 Attosecond Metrology Of Bright Quantum Light

## Bibliographic Metadata

- Authors: P. Stammer, J. Rivera-Dean, E. Pisanty, M. Lewenstein.
- Year: 2026.
- Identifier: arXiv:2607.06395v1 [quant-ph], 7 July 2026. Preprint, 7 pages,
  no supplement. No DOI.
- Raw source: [Stammer et al. - 2026 - Attosecond metrology of bright quantum light.pdf](<../../raw/sources/Stammer et al. - 2026 - Attosecond metrology of bright quantum light.pdf>)
- Extracted text:
  [stammer-2026-attosecond-metrology-of-bright-quantum-light.txt](<../../results/literature/ingest-2026-11-14/extracted_text/stammer-2026-attosecond-metrology-of-bright-quantum-light.txt>)
- Ingest date: 2026-11-14.

## Core Result

Theory proposal, no experiment. Attosecond streaking is modelled with a
quantized infrared (IR) streaking field in an arbitrary state and a coherent
XUV ionizing pulse. The exact photoelectron spectrogram is a generalized-P
average over products of semiclassical streaking amplitudes (Eq. 9); for
large photon numbers it reduces to a Husimi-Q-weighted sum of semiclassical
spectrograms (Eq. 10). For BSV the trace has no mean oscillation and its
energy width is modulated at twice the IR frequency (Fig. 2). The authors
propose to read quadrature squeezing from this delay-dependent width.

## Useful Equations Or Model Ingredients

Representation: generalized P, then Husimi Q. Atomic units throughout.

```text
(1)  M_a(p,tau) = int dt E_X(t + tau) G_a(p,t) exp(i Delta_p t)
     G_a(p,t)   = D(p + A_a(t)) exp[i Phi_a(p,t)]
(2)  Phi_a(p,t) = - int_t^inf dt' [ p.A_a(t') + A_a(t')^2 / 2 ]
     Delta_p = (|p|^2 - |p_0|^2) / 2,   |p_0| = sqrt(2 (Omega + E_0)),  E_0 < 0
(3)  E_Q(t) = -i [g_0 a_IR^dag exp(i omega t) + g b_X^dag exp(i Omega t)] + h.c.
(9)  S_Q(p,tau) = int d2a int d2b P(a,b*) M_a(p,tau) M*_{b*}(p,tau)
(10) S_Q(p,tau) = int d2a Q(a) |M_a(p,tau)|^2,    Q(a) = <a|rho_IR|a> / pi
(11) A_am(t) = f(t) [ A_0 cos(omega t) + A_IR cos(omega t) ]     (as printed)
(12) A_ph(t) = f(t) (A_0 + A_IR) cos(omega t)
```

`S_Q` is the photoelectron spectrum at momentum `p` and XUV-IR delay `tau`.
`a`, `b` under the integrals are coherent amplitudes of the IR mode (the
paper's alpha, beta); `a_IR`, `b_X` are the mode operators; `E_X` is the XUV
envelope; `A_a` the classical vector potential of component `a`; `D` the
transition dipole. In (11)-(12) `f(t)` is the envelope and `A_IR` a classical
random amplitude that stands for the anti-squeezed noise.

Parameters of the figures: `omega = 0.057 a.u.`, squeezing intensity
`I_squ = 5e-5 a.u.`, IR duration 5 fs FWHM, helium (`I_p = 0.904 a.u.`),
`Omega = 3.3 a.u.`; displaced states with `I_coh / I_sq` about 6 (Figs. 2, 3).

Which field moments the spectrogram carries:

- First moment: the centre of the trace follows the Q-ensemble mean of the
  field. It vanishes for BSV and oscillates at `omega` for displaced squeezed
  states (Figs. 2, 3).
- Second moment: the energy variance at delay `tau` follows the variance of
  the field quadrature selected by `tau`, broad on the anti-squeezed and
  narrow on the squeezed quadrature. The delay acts like the local-oscillator
  phase in homodyne detection (Conclusion).

The squeezing claim, item by item:

- Measured quantity: photoelectron kinetic-energy distribution versus delay.
  Proposed signature: its variance compared with that for a coherent field.
- Shown: traces for BSV and for amplitude- and phase-squeezed displaced states
  (Figs. 2, 3); and that classical fields carrying only the anti-squeezed
  noise, Eqs. (11)-(12), give a larger variance than a coherent field,
  `Delta Var = Var_am/ph - Var_cl >= 0` for delays of -5 to 5 fs (Fig. 4b, d).
- Not shown: a variance below the coherent-state value for a squeezed state,
  an extracted squeezing parameter, or any treatment of loss, XUV bandwidth,
  spectrometer resolution, shot number, or multimode fields.

## Assumptions

- One IR mode and one XUV mode, dipole coupling, one active electron, coherent
  XUV; a 5 fs envelope is imposed on the single-mode IR field.
- Volkov-phase streaking amplitude: no Coulomb interaction in the continuum.
- Eq. (10) takes the quasi-classical limit of the positive-P function, which
  removes interference between different coherent components. It is justified
  by citing the decay of coherent-state overlaps (ref. 57).

## Limitations And Cautions

- The abstract says the scheme "can measure quantum squeezing below the shot
  noise limit". The body supports sensitivity of the trace width to quadrature
  noise, but has no sub-shot-noise demonstration and no noise budget.
- Eqs. (11) and (12) as printed are the same function of `A_IR`, while the
  text describes (11) as a change of carrier-envelope phase. Probably a
  misprint; it cannot be resolved from the PDF.
- In Eq. (10) the IR state enters only through the positive function `Q`, so
  the predicted trace equals that of a classical random field with density
  `Q`. Project note, not in the paper: `Q` adds one unit of vacuum noise to
  each quadrature, so squeezing can lower the `Q` variance of a quadrature by
  at most a factor 2 relative to a coherent state.
- The 5 fs single-mode BSV assumed here is shorter and purer than measured
  pulses ([[kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv]],
  [[gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light]]).
- The pi phase ambiguity of BSV is not discussed, only the vanishing mean.

## Relevance To This Project

- Eq. (10) has the structure of the project's ensemble: a phase-space-weighted
  average of semiclassical responses. See
  [[../theory/stochastic-quantum-optics-correspondence]].
- Citable support for the null-model caution (p. 4): `g2(0) = 3` and a
  long-tailed photon-number distribution have classical counterparts, and
  multimode squeezed light can look thermal. A THz histogram that reproduces
  the pump photon statistics does not certify squeezing.
- Analogy for the planned experiment: the electro-optic probe delay plays the
  role of `tau`. For optical rectification the first moment (mean THz field)
  is nonzero, unlike the BSV streaking trace.
- No source parameters and nothing on optical rectification or THz.
