---
title: Gorlach 2023 Fig IV.2 BSV Threshold TDSE Reproduction
type: simulation
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [hhg, bsv, tdse, neon, threshold]
source_count: 1
confidence: medium
related:
  - ../sources/gorlach-2023-hhg-driven-quantum-light-supplement
  - ../models/hhg-gas-model
  - gorlach-2023-fig3b-proxy-reproduction
---

# Gorlach 2023 Fig IV.2 BSV Threshold TDSE Reproduction

## Target Observable

Reproduce the qualitative threshold comparison in supplementary Fig. IV.2 of
Gorlach et al. 2023: ensemble-averaged HHG spectra for a model Ne atom driven
by bright squeezed vacuum (BSV) pulses with mean peak intensities
`1e13 W/cm^2` and `2e13 W/cm^2` at `lambda0 = 800 nm`.

The observable is the incoherent ensemble mean of TDSE dipole-acceleration
spectra,

```text
S_BSV(q; <I>) = integral dI_alpha Q_BSV(I_alpha; <I>) S_TDSE(q; I_alpha)
```

where `q = omega / omega0` is harmonic order. The plotted diagnostic should use
a common y-axis and common normalization for both intensities, because the
threshold claim is the emergence of pronounced harmonic peaks above the
background at the higher BSV mean intensity.

## Atom And Initial State

Use the one-dimensional soft-core Ne-like atom from the supplement:

```text
V(x) = -1 / sqrt(x^2 + a^2)
a = 0.8160 bohr
Ip = 0.7924 hartree
```

The initial electronic state is the field-free ground state. The supplement
obtains it by diagonalizing the field-free Hamiltonian on a Cartesian grid. The
local implementation currently obtains the same model's ground state by
imaginary-time split-operator propagation; result manifests must record this
implementation caveat.

## Units And Field Conversion

The TDSE uses atomic units. Convert mean peak intensity to electric-field
amplitude through

```text
I [W/cm^2] = 3.50944506e16 * E0^2 [a.u.]
E0 [a.u.] = sqrt(I / 3.50944506e16)
```

The driving angular frequency is `omega0 = 0.057 a.u.`, corresponding to
approximately `800 nm`.

## Stochastic Ensemble

For Fig. IV.2, model the BSV driver as a single detected spatiotemporal mode
with random phase and BSV intensity distribution:

```text
Q_BSV(I_alpha; <I>) =
  1 / sqrt(2 pi <I> I_alpha) * exp[-I_alpha / (2 <I>)]
```

Equivalently, sample

```text
I_alpha / <I> ~ Gamma(shape = 1/2, scale = 2)
```

so that `<I_alpha> = <I>` and
`<I_alpha^2> / <I_alpha>^2 = 3`. Each TDSE coherent response is driven by
field amplitude `E_alpha = sqrt(I_alpha)` in atomic units with carrier phase
fixed to zero. The ensemble seed and sample count must be recorded.

## Numerical Plan

The source-grid target is:

```text
x_min = -100 bohr
x_max = 100 bohr
dx = 0.06 bohr
dt = 0.02 a.u.
absorber: V_ab = -i 5e-4 (|x| - 75)^3 for |x| >= 75 bohr
pulse: 5-cycle rise, 15-cycle plateau, 5-cycle fall
```

That exact grid is expensive for iterative local development. The local
reproduction should record the grid actually used and prioritize:

- a 5/15/5-cycle pulse shape,
- absorber onset at `75 bohr`,
- a fine enough grid to preserve peak structure,
- an amplitude library over BSV intensity quantiles,
- log-spectrum interpolation between library amplitudes,
- shared normalization for the `1e13` and `2e13 W/cm^2` spectra.

## Expected Limiting Cases

- The BSV intensity sampler should reproduce `g^(2) = 3` in the sampled
  intensity distribution.
- The `1e13 W/cm^2` curve should show mainly low-order structure and a decaying
  high-order tail.
- The `2e13 W/cm^2` curve should show more pronounced high-harmonic peaks above
  the background near and beyond harmonic order 25.
- Increasing the TDSE amplitude-library resolution should not change the
  qualitative threshold ordering.

## Outputs

Each result directory must contain:

- raw ensemble-mean FFT-grid spectrum CSV,
- cleaned display-spectrum CSV,
- summary JSON with sampler and cutoff statistics,
- parameter YAML,
- manifest YAML with source references, commit hash, seed, and caveats,
- Fig. IV.2-style PNG with two log-scale panels.

## First Local TDSE Run

Result directory:

```text
results/gorlach-2023-fig-iv2-bsv-threshold-20260606/
```

Run parameters:

```text
shots = 50000
seed = 20230604
intensities = [1e13, 2e13] W/cm^2
TDSE library amplitudes = 13
x_min = -100 bohr
x_max = 100 bohr
grid_points = 2048
dx = 0.09765625 bohr
dt = 0.05 a.u.
pulse = 5-cycle rise, 15-cycle plateau, 5-cycle fall
absorber_start = 75 bohr
absorber_strength = 5e-4
```

Key diagnostics:

```text
BSV 1e13 W/cm^2: sampled g2 = 2.9908, cutoff p99 = 22.00
BSV 2e13 W/cm^2: sampled g2 = 3.0326, cutoff p99 = 30.50
```

The local run reproduces the qualitative threshold effect: at `2e13 W/cm^2`
the high-order spectrum retains a pronounced plateau and visible peaks through
the 30th harmonic region, while at `1e13 W/cm^2` the high-order yield collapses
toward the display floor. The result is still not an exact source-grid
reproduction because `dx = 0.09765625 bohr` and the ground state is obtained by
imaginary-time propagation rather than Hamiltonian diagonalization.
