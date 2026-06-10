---
title: Gorlach 2023 Fig 3b TDSE Reproduction
type: simulation
status: active
created: 2026-06-06
updated: 2026-06-09
tags: [hhg, quantum-light, husimi-q, fig3b, tdse]
source_count: 2
confidence: medium
related:
  - ../sources/gorlach-2023-hhg-driven-quantum-light-supplement
  - paper-one-correspondence-hhg-simulation-spec
---

# Gorlach 2023 Fig 3b TDSE Reproduction

## Target

Reproduce the qualitative content of Fig. 3b in Gorlach et al. 2023:
high-harmonic emission spectra for coherent, Fock, thermal, and bright
squeezed-vacuum driving light at matched mean driving intensity. The Nature
page identifies Fig. 3 as the spectra comparison, and the public source-data
archive includes `SourceData_3b.mat` for this panel. The local supplementary
PDF provides the coherent-state phase-space sampling formulation and the
1D soft-core TDSE baseline.

The current upgrade replaces the previous smooth cutoff envelope with a local
1D TDSE dipole-acceleration coherent-response library. The next fidelity fix is
to preserve the full frequency-resolved TDSE acceleration spectrum instead of
sampling only odd harmonic orders. It remains an approximate local
reproduction, not the authors' exact grid, code, or source-data reconstruction.
The public source-data archive is stored locally at
`raw/assets/gorlach-2023-fig3-source-data/`.

## Representation And Driver Ensemble

Use Husimi-Q coherent-state sampling for the incident single optical mode.
Each sampled coherent amplitude `alpha` drives one classical HHG proxy response.
The spectra are averaged incoherently over the ensemble.

For all source states, normalize the per-shot field by the sampled ensemble mean:

```text
E_shot = E0 sqrt(|alpha|^2 / mean(|alpha|^2))
```

This matches the mean driving intensity across source states while preserving
photon-statistics-driven intensity fluctuations.

Driver states:

```text
coherent: alpha = sqrt(nbar) + xi,        xi ~ complex normal Q vacuum noise
Fock:     |alpha|^2 ~ Gamma(n + 1, 1),    arg(alpha) uniform
thermal:  alpha ~ circular complex normal with mean |alpha|^2 = nbar + 1
BSV:      single-mode squeezed-vacuum Husimi-Q sample with r and phase
```

The Fock and coherent curves should remain narrow compared with thermal and
BSV. Thermal light has an exponential intensity distribution. Single-mode BSV
has a broader squeezed-Q intensity tail, which should extend the proxy cutoff
relative to the matched coherent driver.

## Observable

The primary observable is the ensemble-mean HHG energy spectrum versus
harmonic order:

```text
S_state(q) = mean_shots[S_TDSE(q; E_shot)]
```

The TDSE output CSV should include frequency-resolved rows on the FFT harmonic
order grid, not only odd harmonic samples. The CSV should include raw
matched-intensity spectra and a display column with vertical offsets for a
Fig. 3b-like plot. The display offsets are only for visual comparison and must
not be interpreted as absolute emitted energy differences. The current plot
uses decade-scale offsets for readability: coherent `1`, Fock `1e3`, thermal
`1e6`, and BSV `1e9`.

All four driver-state curves must share a single normalization benchmark. The
benchmark is the maximum ensemble-mean spectrum across all driver states over
the configured normalization harmonic-order range. This avoids hiding absolute
yield differences by renormalizing each source state independently.

The main PNG plots the raw FFT-bin ensemble-mean spectra as continuous curves
with per-state decade display offsets, matching the visual form of the
published figure. The earlier masked peak-window display produced unreadable
striped plots and hid the artifact described below; it is retained only as the
secondary CSV products. The raw FFT-bin spectrum is kept in
`gorlach_2023_fig3b_proxy_spectra.csv`; a one-row-per-harmonic companion table
is stored in `gorlach_2023_fig3b_harmonic_yields.csv`; the cleaned
peak-window table is stored in `gorlach_2023_fig3b_display_spectrum.csv`.

When the extracted published reference CSV is available, the runner also
writes `gorlach_2023_fig3b_published_overlay.png` with per-state panels
overlaying the local ensemble-mean spectrum on the published source-data
curve, both normalized at the 9th-harmonic peak.

## Model Equations And Units

For each coherent component, solve the 1D soft-core TDSE in atomic units:

```text
i d_t psi(x,t) = [-1/2 d_x^2 + V(x) + V_ab(x) + x E(t)] psi(x,t)
V(x) = -(x^2 + a^2)^(-1/2)
V_ab(x) = -i 5e-4 (|x| - x0)^3 for |x| >= x0, else 0
E(t) = E_shot f(t) sin(omega0 t + phi)
a(t) = -<psi(t) | d_x V(x) + E(t) | psi(t)>
S_TDSE(omega) = |FFT[a(t) w(t)]|^2
q = omega / omega0
```

The Gorlach supplement used a trapezoid temporal envelope with 5-cycle ramp-up,
15-cycle flat top, and 5-cycle ramp-down, a 1D grid from `-100` to `100` bohr,
`dx = 0.06` bohr, `dt = 0.02` atomic units, `a = 0.8160` bohr, and
`I_p = 0.7924` hartree. It also used a complex absorbing potential beginning at
`x0 = 75` bohr to avoid nonphysical boundary reflections. The local
implementation exposes these as parameters. Test and smoke runs may use a
smaller grid and shorter pulse; such outputs must record the reduced fidelity
in the manifest.

To keep stochastic averaging tractable, the runner evaluates TDSE spectra on a
field-amplitude library and interpolates `log(S + floor)` at the sampled
shot amplitudes. This keeps the stochastic-field ensemble intact while avoiding
one TDSE solve per Monte Carlo shot.

For the TDSE model, the interpolation target should be the raw FFT harmonic
order grid:

```text
q_i = omega_i / omega0
S_state(q_i) = mean_shots[S_TDSE(q_i; E_shot)]
```

Odd harmonic peak heights may be retained only as a legacy proxy output. They
must not be the primary TDSE Fig. 3b reproduction because they erase the
between-peak valleys and make the plot look like a smooth envelope.

Default physical scales:

```text
lambda0 = 800 nm
omega0 = 0.057 atomic units
I_p = 0.7924 hartree
E0 in atomic units
harmonic order dimensionless
```

## Random Seeds And Convergence

Use a fixed integer seed in manifests. The default production run should use at
least `50_000` shots; tests may use smaller ensembles. Convergence checks:

- coherent and Fock spectra remain close through the coherent cutoff region,
- thermal extends beyond coherent/Fock,
- BSV extends beyond thermal for the same `E0`,
- increasing shot count changes the normalized display curves only mildly.
- increasing the number of TDSE amplitude bins changes log-normalized spectra
  less than the stochastic Monte Carlo uncertainty over the plotted harmonic
  range.

## Expected Outputs

Under a dated result directory:

```text
gorlach_2023_fig3b_proxy_spectra.csv
gorlach_2023_fig3b_harmonic_yields.csv
gorlach_2023_fig3b_display_spectrum.csv
gorlach_2023_fig3b_proxy_summary.json
gorlach_2023_fig3b_proxy.png
parameters.yaml
manifest.yaml
```

The manifest must record the source URLs, raw local source path, random seed,
shots, driver-state parameters, field normalization, code entry point, commit
hash if available, TDSE grid and pulse parameters, amplitude-library metadata,
and the approximation caveat.

The first full-frequency upgraded local run is stored at
`results/gorlach-2023-fig3b-tdse-fullfreq-20260606/`. It uses 50,000
stochastic shots, 11 TDSE amplitude bins, a `[-80, 80]` bohr grid with 768
points, `dt = 0.08` a.u., a 5-cycle ramp / 15-cycle flat-top / 5-cycle ramp
pulse, a complex absorber starting at 75 bohr, 3,650 harmonic-order FFT
points per driver state, and decade-separated display offsets.

The lower-field finer-grid rerun is stored at
`results/gorlach-2023-fig3b-tdse-sharednorm-e006-finegrid-20260606/`. It uses
the shared all-driver-state normalization benchmark, `E0 = 0.06` a.u.,
50,000 stochastic shots, 11 TDSE amplitude bins, a `[-80, 80]` bohr grid with
1,024 points, `dt = 0.06` a.u., the same 5-cycle ramp / 15-cycle flat-top /
5-cycle ramp pulse, the same complex absorber parameters, and the harmonic-yield
display processing described above.

## Published Source-Data Reference

The published Fig. 3b curves are recoverable exactly: the source-data archive's
`Dot fig files/Figure 3b/Spectra.fig` is a MATLAB v7 figure whose four
`graph2d.lineseries` objects (Coherent state, Number state, Thermal light,
Squeezed Vacuum; 1,510 points each on a 0.1-order grid up to order 151) load
with `scipy.io.loadmat`. The extraction entry point is
`code/scripts/extract_gorlach_2023_fig3b_reference.py`, writing
`results/gorlach-2023-fig3b-published-reference/fig3b_published_curves.csv`.
The published intensities include per-state display offsets of roughly three
decades, so only curve shapes, comb structure, and cutoffs are comparable.

Key published features that any local reproduction must match:

- a strong below-threshold resonance peak near harmonic 9 in every state
  (consistent with a bound-bound transition of the 1D soft-core model atom),
- coherent and Fock combs ending near order 20-27 followed by a smooth
  numerical floor,
- thermal and BSV combs persisting far beyond the coherent cutoff with
  visible odd-harmonic contrast.

## Grid-Artifact Diagnosis (2026-06-09)

Overlaying the `e006-finegrid` run on the published curves showed the local
coherent and Fock spectra carrying a fake harmonic comb to order 80+ with no
cutoff. Controlled single-TDSE comparisons at `E0 = 0.06` isolated the cause:
the `[-80, 80]` bohr grid leaves only 5 bohr of complex absorber beyond the
75-bohr onset, so ionized wavepackets reflect or wrap around the periodic
split-operator boundary and rescatter. Beyond harmonic order 50 the old grid
leaves a spurious plateau at `~1e-2` of the 9th-harmonic reference level; a
`[-100, 100]` bohr grid with 2,048 points, `dt = 0.03` a.u., and a converged
imaginary-time ground state (2,000 iterations at `dt = 0.05`) drops that band
to `~1e-8`. The dipole-acceleration expectation now also uses the analytic
soft-core gradient instead of a finite-difference `np.gradient`.

Field calibration against the published coherent curve: `E0 = 0.038` a.u.
(about `5.1e13 W/cm^2`) reproduces the published 9th-harmonic resonance
prominence, plateau, and cutoff near order 25, while `E0 = 0.06` overshoots
the cutoff (order ~29 by the semiclassical formula). The production defaults
are now `E0 = 0.038`, `bsv_r = 3.0` (so `sinh^2(r) ~ 100` matches the
coherent/Fock mean photon number), 17 TDSE amplitude bins, and a `0.999`
amplitude-quantile tail cap on the TDSE library so rare extreme BSV samples
do not stretch the interpolation range; clipped fractions are recorded per
state.

## Calibrated Production Run (2026-06-09)

Result directory:

```text
results/gorlach-2023-fig3b-tdse-calibrated-20260609/
```

50,000 shots, seed 20230603, `E0 = 0.038` a.u., `bsv_r = 3.0`, 17 TDSE
amplitude bins on the `[-100, 100]` bohr 2,048-point grid, `dt = 0.03` a.u.,
5/15/5-cycle pulse, absorber from 75 bohr. Key diagnostics:

```text
coherent: cutoff p99 = 22.2, intensity CV = 0.14, clipped fraction = 0
fock:     cutoff p99 = 21.6, intensity CV = 0.10, clipped fraction = 0
thermal:  cutoff p99 = 42.5, intensity CV = 1.00, clipped fraction = 2e-4
bsv:      cutoff p99 = 55.0, intensity CV = 1.41, clipped fraction = 3.8e-3
```

The published-overlay panels (`gorlach_2023_fig3b_published_overlay.png`)
now match the source-data curves through the plotted range: coherent and
Fock track the published plateau and cutoff near order 25 (the published
smooth tail beyond ~27 is the authors' numerical floor, which sits above the
local floor), and thermal/BSV reproduce the persistent odd-harmonic comb to
order 60 with slight overshoot at high orders. The main raw-grid PNG shows
the Fig. 3b ordering directly: coherent and Fock combs collapse near order
25-30, thermal persists to roughly order 60, and BSV continues beyond order
100.
