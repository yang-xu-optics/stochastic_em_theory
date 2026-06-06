---
title: Sun Et Al 2022 THz Generation From Laser-Induced Plasma
type: source-summary
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [source, thz, plasma, review, photocurrent, four-wave-mixing]
source_count: 1
confidence: high
related:
  - ../models/thz-plasma-emission-model
  - ../models/thz-optical-rectification-model
---

# Sun Et Al 2022 THz Generation From Laser-Induced Plasma

## Bibliographic Metadata

- Authors: Wenfei Sun et al.
- Year: 2022.
- Venue: Opto-Electronic Science 1, 220003.
- Raw source: [Sun et al. - 2022 - Terahertz generation from laser-induced plasma.pdf](<../../raw/sources/Sun et al. - 2022 - Terahertz generation from laser-induced plasma.pdf>)
- Ingest date: 2026-06-06.

## Core Result

This review summarizes THz generation mechanisms in laser-induced plasmas,
including ponderomotive forces, dipole/current radiation, transition-Cherenkov
emission, four-wave rectification/mixing, and photocurrent mechanisms.

## Useful Equations Or Model Ingredients

- Ponderomotive force model for one-color plasma THz:

```text
F_pm = -grad(e^2 I_opt / (2 epsilon_0 c m_e omega_opt^2))
```

- Two-color four-wave rectification/mixing scaling:

```text
E_THz(t) proportional to chi^(3) E_2omega(t) E_omega^*(t) E_omega^*(t) cos(phi)
```

- Photocurrent template:

```text
E_L(t) = [E_omega cos(omega t)
        + E_2omega cos(2 omega t + phi)] exp(-t^2 / (2 T_0^2))
dn_e/dt = w(t) [N_0 - n_e(t)]
J(t) = - integral e v(t, t') dn_e(t')
E_THz proportional to dJ/dt
```

## Assumptions

- Multiple plasma THz mechanisms can coexist; dominance depends on gas,
  intensity, pulse duration, plasma length, wavelength, and harmonic content.
- In two-color gases, photocurrent and four-wave-mixing pictures can both be
  useful, but plasma current often dominates once ionization is appreciable.

## Limitations And Cautions

- This is a broad review, not a BSV-specific theory.
- For the optical rectification chapter, distinguish true `chi^(2)` OR in
  noncentrosymmetric media from effective `chi^(3)` rectification/mixing in
  plasma.

## Relevance To This Project

This source anchors the THz mechanism taxonomy and helps avoid mixing optical
rectification, four-wave rectification, and plasma photocurrent language.

