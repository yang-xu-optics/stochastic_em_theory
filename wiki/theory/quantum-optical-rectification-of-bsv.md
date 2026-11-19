---
title: Quantum Optical Rectification Of BSV
type: concept
status: draft
created: 2026-11-14
updated: 2026-11-19
tags: [theory, quantum, optical-rectification, thz, bsv, photon-number, qnd, exact-solution]
source_count: 8
confidence: medium
related:
  - bsv-even-order-response-moment-scaling
  - stochastic-quantum-optics-correspondence
  - ../models/thz-optical-rectification-model
  - ../simulations/bsv-optical-rectification-thz-statistics
  - ../simulations/thz-waveform-noise-against-delay
  - ../prl-restructuring-plan
  - ../../paper/theory-note/README
  - ../sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum
  - ../sources/kizmann-2019-subcycle-squeezing-time-flow-perspective
  - ../sources/spasibko-2017-multiphoton-effects-photon-number-fluctuations
  - ../sources/gothelf-2026-limitations-of-approximative-phase-space-description
  - ../sources/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light
  - ../sources/kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv
  - ../sources/riek-2017-subcycle-quantum-electrodynamics
---

# Quantum Optical Rectification Of BSV

A fully quantum description of THz generation by optical rectification (OR)
of bright squeezed vacuum (BSV), written during the 2026-11-14 restructuring.
Both the pump and the THz field are quantized. No phase-space sampling and no
coherent-state expansion of the pump is used. The derivation is this
project's own; the algebra is checked numerically (see "Checks"), but the
page is not yet backed by a published derivation of the same result.

Update 2026-11-19: the model is exactly solvable for an arbitrary multimode
pump, not only to first order in the coupling (section "Exact Solution For A
Multimode Pump"). The statements below that say "first order" or "undepleted
pump" are kept as written on 2026-11-14 and are superseded where that section
says so. The linear argument is the manuscript draft in
`paper/theory-note/theory-note.tex`.

## Representation

- Heisenberg picture, continuous-frequency operators.
- Pump: `a(omega)`, `[a(omega), a^dagger(omega')] = delta(omega - omega')`,
  units `s^(1/2)`.
- THz: `b(Omega)`, same commutator, `Omega > 0`, units `s^(1/2)`.
- Photon numbers are dimensionless. Ordering is stated for every moment.

## Hamiltonian And Assumptions

Difference-frequency part of the `chi^(2)` interaction, one spatial mode,
collinear:

```text
H_I = hbar integral dOmega integral domega  kappa(Omega)
        [ b^dagger(Omega) a^dagger(omega) a(omega + Omega) + h.c. ]
```

`kappa(Omega)` (units `s^(1/2)` after integrating over the crystal) contains
`chi_eff^(2)`, the field normalizations, and the phase-matching function. It
is taken independent of `omega` across the pump bandwidth, which is the usual
OR approximation: the mismatch depends on the optical group index and the THz
phase index, `Delta k = Omega (n_g - n_THz) / c`.

Assumptions: undepleted pump and first order in `kappa`; no absorption; no
competing `chi^(2)` or `chi^(3)` processes; sum-frequency terms dropped
(they radiate near `2 omega_0`).

## Input-Output Relation

```text
b_out(Omega) = b_in(Omega) - i zeta(Omega) N(Omega)                 (1)
N(Omega) = integral domega  a^dagger(omega) a(omega + Omega)        (2)
```

`N(Omega)` is the Fourier component of the photon-flux operator
`I(t) = a^dagger(t) a(t)`, and `N(0)` is the total photon-number operator.
In words: the THz field operator is its vacuum input plus a linear filter of
the pump photon-flux operator.

Two consequences follow before any state is chosen.

(For the exact status of (1), see the next section.)

1. `N` is normally ordered. Pump vacuum fluctuations do not rectify. A Wigner
   sampling of the pump would need the `1/2` per mode subtracted; here it
   never appears.
2. The mean THz field depends only on the mean photon flux,
   `<b_out(Omega)> = -i zeta(Omega) <N(Omega)>`. A pump with zero mean
   electric field but a pulsed mean intensity radiates a THz field with a
   definite phase. This is the operator form of the parity rule in
   [[bsv-even-order-response-moment-scaling]], and it holds for any number of
   modes.

## Exact Solution For A Multimode Pump

Added 2026-11-19. Representation: operators, Heisenberg and Schroedinger
pictures; no phase-space sampling. Pump envelope operator `a(tau)` in the
frame moving with the pump group velocity, `tau = t - z/v_g`,
`[a(tau), a^dagger(tau')] = delta(tau - tau')`. Photon flux
`I(tau) = a^dagger(tau) a(tau)` (photons per second),
`N(Omega) = integral dtau e^{i Omega tau} I(tau)` (dimensionless).

Generator of propagation along `z` (interaction picture), with `kappa(Omega)`
real, units `s^(1/2) m^-1`, and `Delta k = k_T(Omega) - Omega / v_g`:

```text
G(z) = hbar integral dOmega kappa [ e^{-i Delta k z} b^dagger(Omega) N(Omega) + h.c. ]   (E1)
```

Assumptions: (a) `kappa` and `Delta k` independent of pump frequency across
the pump band, i.e. no pump group-velocity dispersion in the crystal; (b) one
transverse mode; (c) no pump absorption; (d) no sum-frequency generation and
no coupling among THz modes.

The key fact is that the flux commutes with itself at different times:

```text
[I(tau), I(tau')] = 0,   so  [N(Omega), N(Omega')] = [N(Omega), N^dagger(Omega')] = 0     (E2)
[G(z), G(z')] = 2 i hbar^2 integral dOmega kappa^2 sin[Delta k (z - z')] N^dagger N       (E3)
```

(E3) commutes with `G`, so the Magnus series ends at its second term:

```text
U     = exp(i Phi) D                                                                      (E4)
D     = exp{ -i integral dOmega [ zeta b^dagger N + h.c. ] }
zeta  = kappa L exp(-i Delta k L / 2) sinc(Delta k L / 2)          units s^(1/2)
Phi   = - integral dOmega phi(Omega) N^dagger N
phi   = kappa^2 [Delta k L - sin(Delta k L)] / Delta k^2            -> 0 at Delta k = 0
```

No expansion in the coupling. Consequences, for any pump state:

```text
b_out(Omega) = b_in(Omega) - i zeta(Omega) N(Omega)          exact, not first order       (E5)
I_out(tau)   = I_in(tau)                                     flux conserved at each instant (E6)
a_out(tau)   = exp[-i theta_tot(tau)] a_in(tau)              pump is only phase modulated (E7)
theta_tot    = [F_in(tau) + F_out(tau)] / 2 + theta(tau)
F(tau)       = integral dOmega [ zeta b^dagger e^{i Omega tau} + h.c. ]
F_out - F_in = 2 integral dtau' S(tau' - tau) I(tau'),   S(x) = integral dOmega |zeta|^2 sin(Omega x)
theta(tau)   = 2 integral dtau' V(tau - tau') I(tau') + V(0),   V(x) = integral dOmega phi cos(Omega x)
```

(E7) is the electro-optic effect: the pump is phase modulated by the THz
field it travels with, the average of input (vacuum) and output (generated)
fields for perfect phase matching, plus the cascaded Kerr phase `theta` for a
mismatch. The pump energy drops by `hbar integral Omega |zeta|^2 <N^dagger N>`
through a red shift; photon number and arrival times do not change.

Correction 2026-11-19: a first version of (E7) had only `F_in + theta`. The
flux-dependent part `integral S I` comes from `[F(tau'), F(tau)] = -2 i
S(tau' - tau)` and is required by energy conservation. The numerical check
below fails by 0.03 to 0.09 without it.

THz state. The joint eigenstates of the flux are photon-arrival
configurations `|tau_1 .. tau_n>` with `I(tau) = sum_i delta(tau - tau_i)`.
On each, `D` displaces the THz vacuum to a coherent state, so for vacuum THz
input

```text
rho_THz = sum_n integral d^n tau  p_n(tau_1..tau_n) |beta><beta|,
beta(Omega) = -i zeta(Omega) sum_i e^{i Omega tau_i}                                      (E8)
E_THz(t) = E_vac(t) + sum_i g(t - tau_i)                                                  (E9)
```

`p_n` is the outcome distribution of ideal time-resolved photon counting on
the pump, and `g(t)` the THz transient per pump photon. This generalizes
(10) below from the photon-number distribution of one mode to the
arrival-time distribution of any pump. The THz Glauber-Sudarshan P function
is non-negative for every pump state. (E9) is a filtered point process (Rice
shot noise; from memory: S. O. Rice, Bell Syst. Tech. J. 23, 282 (1944), not
ingested).

Shot-noise identity. From the commutator,

```text
<I(tau) I(tau')> = <: I(tau) I(tau') :> + delta(tau - tau') <I(tau)>                      (E10)
```

The last term, filtered by `g`, is Campbell's theorem for (E9) and equals the
"spontaneous" term (6d): spontaneous difference-frequency generation and
rectified photon shot noise are the same thing.

Closed-form spectrum for a Gaussian Schell-model pump (rms duration `T` of
the mean intensity, `K_t` temporal modes, `K = K_s K_t` modes in total,
bright limit, common squeezing phase):

```text
<N^dagger N> / Nbar^2 = exp(-Omega^2 T^2) + (2/K) exp(-Omega^2 T^2 / K_t^2) + 1/Nbar      (E11)
mean/fluctuation crossover  Omega_x = (1/T) sqrt[ ln(K/2) / (1 - 1/K_t^2) ]   (K > 2)
```

Mean field, fluctuation (wider by `K_t`), shot noise. For 100 fs FWHM,
`K = 10`, `K_t = 2`, `Nbar = 2.4e13`: crossover 5.5 THz; shot noise exceeds
the fluctuation above about 40 THz. Implemented as
`gaussian_schell_flux_spectrum` in `code/src/stochastic_em_theory/thz_waveform_noise.py`.

What changes relative to the 2026-11-14 text:

- (1) is exact in the coupling under assumptions (a) to (d). The THz
  statistics do not need `N_THz << N_pump` or `B nbar << 1`.
- The conversion strength enters only through the pump phase (E7). The
  model fails when that phase modulation broadens the pump spectrum until
  pump dispersion matters (the cascading limit analysed classically in
  [[../sources/ravi-2014-thz-generation-optical-rectification]]).
- The single-mode model below is the special case with one occupied mode and
  scattering into empty modes dropped.

## Schmidt-Mode Form

Expand the pump in an orthonormal mode basis, `a(omega) = sum_k psi_k(omega)
A_k`, with BSV in independent squeezed modes: `<A_k^dagger A_l> = delta_kl
nbar_k`, `<A_k A_l> = delta_kl m_k`, `|m_k|^2 = nbar_k (nbar_k + 1)`.

```text
N(Omega) = sum_kl c_kl(Omega) A_k^dagger A_l                        (3)
c_kl(Omega) = integral domega  psi_k^*(omega) psi_l(omega + Omega)  (4)
c_kl(0) = delta_kl
```

Mean field:

```text
<N(Omega)> = sum_k c_kk(Omega) nbar_k                               (5)
```

which is the Fourier transform of the mean intensity envelope
`sum_k nbar_k |psi_k(t)|^2`.

Second moment (Wick's theorem for the Gaussian pump):

```text
<N^dagger(Omega) N(Omega)> =
    |sum_k c_kk nbar_k|^2                       coherent             (6a)
  + sum_kl conj(c_kl) c_lk conj(m_l) m_k        phase-sensitive      (6b)
  + sum_kl |c_kl|^2 nbar_l nbar_k               bunching             (6c)
  + sum_kl |c_kl|^2 nbar_l                      spontaneous          (6d)
```

The THz photon number per unit angular frequency is
`|zeta(Omega)|^2` times (6).

- (6a) is the square of the mean field.
- (6b) exists only for phase-sensitive (squeezed) light. For thermal light it
  is absent; that is the whole difference between factor 3 and factor 2 below.
- (6c) is ordinary intensity bunching.
- (6d) is linear in the pump photon number. It is spontaneous
  difference-frequency generation: one pump photon splits into a THz photon
  and a red-shifted photon in a mode that was empty. The sum over `k` runs
  over all modes, occupied or not, and `sum_k |c_kl|^2 = 1`.

## Relation To The Classical-Noise Model

Replace each `A_k` by a real Gaussian amplitude `X_k` with `<X_k^2> =
nbar_k`. Wick's theorem then gives (6a), (6b), and (6c) with
`nbar_k (nbar_k + 1)` replaced by `nbar_k^2`, and no (6d). So:

```text
classical-noise model = quantum result
                        - spontaneous term (6d)
                        - corrections of relative order 1 / nbar_k
```

For one occupied Gaussian mode, `|c(Omega)|^2 = exp[-Omega^2 / (4 sigma^2)]`
with `sigma` the rms width of the intensity spectrum, and

```text
<N^dagger N> = |c(Omega)|^2 (3 nbar^2 + nbar) + nbar               (7)
relative error of the classical model = 1 / (3 nbar |c(Omega)|^2)
crossover to the spontaneous term at Omega / sigma = 2 sqrt(ln(3 nbar))
```

The crossover is at 7.7 for `nbar = 1e6` and 10.7 for `nbar = 1e12`. Inside
the pump-envelope bandwidth the classical-noise model is exact for all
practical purposes; far outside it, the emission is purely quantum but very
weak. This is the error bound the review asked for, obtained for this process
without approximation in the pump state.

## Three Descriptions Compared On One Exactly Solvable Case

One squeezed mode, low-frequency limit, THz energy in units of the per-photon
value. "APP" is the approximative phase-space description analysed in
[[../sources/gothelf-2026-limitations-of-approximative-phase-space-description]]:
a Husimi-Q weighted mixture of coherent drivers, each evolved exactly. For a
coherent driver `|alpha>` this model gives `<n^2> = |alpha|^4 + |alpha|^2`.

```text
exact quantum            <n^2>                    = 3 nbar^2 + 2 nbar
APP (Q-weighted)         <|alpha|^4 + |alpha|^2>_Q = 3 nbar^2 + 6 nbar + 3
classical Gaussian noise <X^4>, <X^2> = nbar       = 3 nbar^2

mean field:  exact nbar;  APP nbar + 1;  classical nbar
relative error of the THz energy:  APP +4/(3 nbar);  classical -2/(3 nbar)
```

That paper computes no error for a BSV driver; this is one, in closed form.
All three agree at leading order, and the classical-noise model is the
closer of the two approximations. Note also that in this model a coherent
driver does not give a coherent THz state: the pump shot noise is copied
onto the THz amplitude (`<n^2> - <n>^2 = nbar`), which a semiclassical pump
omits.

## Low-Frequency Limit: Full Counting Statistics

For `Omega` well below the bandwidth of every occupied mode, `c_kl ->
delta_kl` and `N(Omega) -> N_tot`. In an electro-optic-sampling window that
selects such frequencies the THz field is

```text
E_THz(t) = E_vac(t) + g(t) N_tot                                    (8)
```

with `g(t)` the deterministic THz waveform per pump photon (field units).
Normally ordered THz moments are therefore ordinary moments of the pump
photon number, to all orders. For one squeezed mode, from the generating
function `<z^n> = [1 + nbar (1 - z^2)]^(-1/2)`:

```text
k1 = nbar
k2 = 2 nbar (1 + nbar)
k3 = 4 nbar (1 + nbar)(1 + 2 nbar)
k4 = 8 nbar (1 + nbar)(1 + 6 nbar + 6 nbar^2)
<n^2> = 3 nbar^2 + 2 nbar
<n^4> = 105 nbar^4 + 180 nbar^3 + 84 nbar^2 + 8 nbar
```

Cumulants of independent modes add.

| Quantity | One squeezed mode, exact | Bright limit | `K` equal bright modes |
| --- | --- | --- | --- |
| Mean THz energy / coherent pump | `(3 nbar + 2) / (nbar + 1)` | 3 | `1 + 2/K` |
| Energy ratio `<U^2> / <U>^2` | `<n^4> / <n^2>^2` | `35/3 + 40/(9 nbar)` | `(K+4)(K+6) / [K (K+2)]` |
| Relative field fluctuation | `sqrt(2 (1 + 1/nbar))` | `sqrt(2)` | `sqrt(2/K)` |
| Field skewness | `k3 / k2^(3/2)` | `2 sqrt(2)` | `2 sqrt(2/K)` |
| Field excess kurtosis | `k4 / k2^2` | 12 | `12/K` |
| Single-shot field distribution | photon-number distribution, even `n` only | chi-squared, 1 d.o.f. | Gamma, shape `K/2` |

For unequal modes replace `K` in the second-moment entries by the Schmidt
number `K = (sum nbar_k)^2 / sum nbar_k^2`, which is also `2 / (g2 - 1)` of
the pump. Weak-squeezing limit of one mode: energy ratio to coherent tends to
2 and `<U^2> / <U>^2` to `2 / nbar` (photon pairs).

The factor 3 and the general `(2n - 1)!!` enhancement of `n`-photon processes
by BSV are known from optical-harmonic experiments
([[../sources/spasibko-2017-multiphoton-effects-photon-number-fluctuations]]).
What (8) adds is that for OR the emitted *field*, not only its energy, is a
linear copy of the photon number with a fixed sign. There is also a
difference in which statistics enter. A harmonic follows the instantaneous
intensity, so its mean yield scales with the single-mode `g^(n)` even for
broadband BSV (Fig. 3 of that paper). A low-frequency THz field integrates
the intensity over the pulse, so it follows the pulse-energy statistics and
the factor is `1 + 2/K`, not 3, unless the pump is single-mode.

## Exactly Solvable Single-Mode Model

If the pump occupies one mode and scattering into empty modes is dropped,
`N(Omega) = c(Omega) n` with `n = A^dagger A`, and

```text
H_I = hbar n integral dOmega [ kappa(Omega) c(Omega) b^dagger(Omega) + h.c. ]
[H_I, n] = 0
```

This is solvable to all orders. It is the pulsed, free-space form of the
radiation-pressure-type Hamiltonian `hbar g a^dagger a (b + b^dagger)` used
in cavity optomechanics and cavity electro-optics (from memory: Tsang, Phys.
Rev. A 81, 063837 (2010); not ingested).

```text
U = exp[i theta n^2] exp[ n integral dOmega (beta(Omega) b^dagger - h.c.) ]
beta(Omega) = -i zeta(Omega) c(Omega)

|psi_out> = sum_n c_n exp(i theta n^2) |n>_pump |n beta>_THz         (9)
rho_THz   = sum_n P(n) |n beta><n beta|                              (10)
rho_pump,nm -> rho_pump,nm exp[-B (n - m)^2 / 2] exp[i theta (n^2 - m^2)]
B = integral dOmega |beta(Omega)|^2
```

Reading:

- (10): the THz state is a mixture of coherent states weighted by the pump
  photon-number distribution. Its Glauber P function is positive, so the THz
  field is classical in the quantum-optics sense, and strongly non-Gaussian.
  For this observable the "incoherent mixture of classical states" criticized
  in [[../sources/gothelf-2026-limitations-of-approximative-phase-space-description]]
  is not an approximation; it is the exact reduced state.
- (9): pump and THz are entangled in the photon-number basis. OR is a
  quantum non-demolition measurement of the pump photon number with the THz
  field as the meter. `n` is conserved to all orders, which is the
  Manley-Rowe statement that rectification red-shifts pump photons without
  destroying them.
- Back-action is dephasing in the number basis with strength `B`, plus a
  Kerr-like phase `theta n^2` (cascaded rectification and electro-optic
  effect). `B` is the number of THz photons emitted per unit `<n^2>`:
  `N_THz = B <n^2>`.

Illustrative size (assumed numbers, not a source value): a 1 microjoule pump
at 1.03 micrometres has `nbar = 5e12`; a THz energy of 10 pJ at 1 THz is
`1.5e10` photons; then `B = N_THz / (3 nbar^2) = 2e-16`. Back-action is
negligible, the THz field resolves the pump photon number to
`1 / sqrt(B) = 7e7` photons (relative `1.4e-5`, against a shot-noise scale of
`4e-7`), and the classical-noise description is exact to that level. A
quantum-limited photon-number readout would need `B nbar` of order one, that
is, more THz photons than pump photons, which is the cascading regime.

Correction 2026-11-19: with the matched THz mode `b_m = integral zeta^* b /
sqrt(B)`, the displacement is `sqrt(B) n` and the vacuum variance of the
measured quadrature is 1/2, so homodyne detection resolves `n` to
`1 / (2 sqrt(B))`, half the value above. Shot-noise resolution needs
`B nbar = 1/4`. For the user's source (`Nbar = 2.4e13`, `K = 10`) and an
assumed 1 nJ at 2 THz: THz/pump photon ratio 3 %, `B Nbar = 0.026`,
resolution about 3 times the pump shot noise.

## What Electro-Optic Sampling Returns

Single-shot electro-optic sampling at delay `t_d` returns, per shot `j`,

```text
s_j = eta g(t_d) n_j + xi_j                                         (11)
```

with `eta` the detection gain and `xi_j` Gaussian noise: probe shot noise with
variance equal to the detected probe photon number, electronics, and the
sampled THz vacuum. In the operator theory of electro-optic sampling the
signal is linear in the THz field filtered by a response function, and the
vacuum adds a few percent to the shot noise even in a configuration designed
to see it
([[../sources/moskalenko-2015-paraxial-theory-of-electro-optic-sampling-quantum-vacuum]]).
The histogram of `s` is the pump photon-number distribution convolved with a
Gaussian. Additive Gaussian noise changes only the second cumulant, so the
third and fourth cumulants of `s` are direct, noise-immune measures of the
photon-number statistics. For `K` equal bright modes:

```text
k3 = 8 k1^3 / K^2,      k4 = 48 k1^4 / K^3
K = sqrt(8 k1^3 / k3) = cbrt(48 k1^4 / k4)                          (12)
```

Two independent estimates of `K` from the THz field that must agree with each
other and with `K = 2 / (g2 - 1)` measured on the pump.

## Waveform Noise And Temporal Moments Of The Photon Flux

Away from the low-frequency limit the single-shot field is the filtered flux,
`E_j(t) = integral g(t - t') I_j(t') dt'`, and its shot-to-shot variance is a
filtered intensity covariance. For Gaussian pump statistics in the bright
limit `Cov(I(t1), I(t2)) = |G1(t1, t2)|^2 + |M(t1, t2)|^2`, with `G1` the
normal and `M` the anomalous field correlation; for BSV with a common phase
the two are equal, for thermal light `M = 0`:

```text
Var E(t) = (2 / M_s) double-integral g(t - t1) g(t - t2) |G1(t1, t2)|^2   (13)
```

`M_s` spatial modes, units of `g` squared times flux squared. Expanding in
the temporal moments of the flux, `N`, `M1 = integral t' I`, `M2 = integral
t'^2 I`, to second order in pulse duration over THz period:

```text
Var E(t) / <N>^2 = A gbar^2 + B (gbar'^2 - gbar gbar'') + 2 C gbar gbar'   (14)
A = Var N / <N>^2,  B = Var M1 / <N>^2,  C = -Cov(N, M1) / <N>^2
Gaussian Schell-model pulse, rms duration T, K_t temporal modes:
A = 2 / K,   B = (2 / K)(T^2 / 2)(1 - 1 / K_t^2),   C = 0
```

`gbar = <E> / <N>` is the measured mean waveform per photon. The single-shot
THz waveform therefore carries the photon number of each pump pulse in its
amplitude and the arrival time of its photon flux in its zero crossings. One
temporal mode gives `B = 0` and noise that vanishes at the zero crossings;
the noise there measures `K_t`. Derivation of the `gbar gbar''` term,
numerical checks, and numbers:
[[../simulations/thz-waveform-noise-against-delay]].

## What Is Genuinely Quantum Here

- The spontaneous term (6d): THz-optical photon pairs with the BSV as pump.
  Linear in pump energy, present where the stimulated terms vanish.
- Pump-THz entanglement in (9). Observable only if `B nbar` approaches one.
- With twin-beam BSV: the THz amplitude generated by the signal beam tracks
  the idler photon number. A classical-noise model reproduces the correlation
  down to shot noise but not below it; resolving that needs a photon-number
  readout at relative precision `1 / sqrt(nbar)`.
- None of these is within reach of a first experiment. The honest statement
  for the Letter is that the measured statistics are quantum in origin (they
  are the photon statistics of squeezed vacuum) and classical in description.

## Validity

Statement of 2026-11-14, superseded: "Two small parameters control the
classical description, not one: `1/nbar` and `B nbar`."

Corrected 2026-11-19: the classical description of the THz statistics is
controlled by `1/nbar` alone. `B nbar` (about the ratio of emitted THz photons
to pump photons, divided by `1 + 2/K`) controls the pump back-action (E7) and
with it the validity of the flat-coupling assumption, not the THz statistics.
The comparison with the scaling of the phase-space error with emitted photon
number in
[[../sources/gothelf-2026-limitations-of-approximative-phase-space-description]]
therefore does not carry over.

```text
pump spectrum stays inside the band where kappa is flat   (replaces "N_THz << N_pump")
B nbar << 1                        negligible pump back-action only
Omega << mode bandwidth            for the counting statistics (8)
one spatial mode                   otherwise K counts spatial modes too
no absorption or two-photon loss   otherwise n is not conserved
```

Real femtosecond BSV pulses consist of one to a few time-localized bursts,
each with single-mode statistics and a random sign: 1.5 bursts per shot on
average and a shot-energy `g2` of 2.08 in
[[../sources/gholam-mirzaei-2026-sub-cycle-metrology-of-bright-quantum-light]],
1.62 spectral modes in
[[../sources/kern-2026-single-shot-pulse-retrieval-of-femtosecond-bsv]]. So
`K` is about 2 unless the source is filtered, and the multimode results above
are the ones to compare with experiment. In the burst picture the THz field
is a sum of time-shifted copies, `E_THz(t) = sum_k n_k g(t - t_k)`, all with
the same sign.

One further effect is outside this model: the generated THz transient itself
squeezes the co-propagating THz vacuum through the electro-optic effect, a
second pass of `chi^(2)`
([[../sources/riek-2017-subcycle-quantum-electrodynamics]],
[[../sources/kizmann-2019-subcycle-squeezing-time-flow-perspective]]). The
noise around the transient is bare vacuum only while that squeezing strength
is small; with a fluctuating pump it would also vary from shot to shot.

## Checks

- Photon-number cumulants against the explicit distribution, `nbar` from
  0.05 to 12.
- Equation (6) against an explicit two-mode Fock-space calculation with a
  random complex overlap matrix.
- Bright-limit values and leading corrections.
- All in `code/tests/test_optical_rectification.py`; run in
  `results/runs/20261114-bsv-or-thz-statistics/`. Spec:
  [[../simulations/bsv-optical-rectification-thz-statistics]].
- Added 2026-11-19, same test file. Frequency-ladder model
  `H = g (b^dagger N + b N^dagger)`, `N = sum_j a_j^dagger a_{j+1}`, one THz
  mode, two pump photons in a three-bin wave packet, full matrix exponential:
  - (E5), (E6): `<b>`, `<b^dagger b>` and `<N>` agree with the exact relations
    at `g t = 0.3` and `0.6` to better than 1e-6. In a finite ladder
    `[N, N^dagger] = n_first - n_last`; residuals 3e-4, 1e-6, 3e-9 for 9, 13,
    17 bins track the edge-bin population. A first-order relation would be
    off by order `(g t)^2`.
  - (E7): the output pump coherence `<a_j^dagger a_k>` from the closed-form
    kernel agrees with the matrix exponential to 7e-10 (`g t = 0.3`) and 2e-7
    (`g t = 0.6`); without the flux-dependent phase the difference is 0.03
    and 0.09. The mean pump frequency drops by one bin per THz photon.
  - (E11) against the discretized covariance:
    `code/tests/test_thz_waveform_noise.py`.
- Not checked numerically: (E4) with a phase mismatch (`Phi`, `theta`), which
  needs a `z`-dependent generator; analytic only.

## Open Points

- Derive `zeta(Omega)` and `g(t)` for a specific crystal with phase matching
  and absorption, and `c_kl(Omega)` for the measured Schmidt modes.
- Done 2026-11-19 for flat coupling: all orders in `kappa` (section "Exact
  Solution For A Multimode Pump"). Still open: pump group-velocity dispersion
  and absorption, which break (E2) to (E6); an independent re-derivation of
  (E3) to (E8); a numerical check with `Delta k != 0`.
- Spatial modes and focusing.
- Find and ingest the cavity electro-optics papers for the Hamiltonian, the
  THz parametric down-conversion literature for the spontaneous term, and
  the incoherent-light THz spectroscopy literature for classical precedents
  of THz fields that follow optical intensity noise.
