---
title: Gorlach 2023 Fig 3b Proxy Reproduction
type: simulation
status: active
created: 2026-06-06
updated: 2026-06-06
tags: [hhg, quantum-light, husimi-q, fig3b, proxy]
source_count: 2
confidence: medium
related:
  - ../sources/gorlach-2023-hhg-driven-quantum-light-supplement
  - paper-one-correspondence-hhg-simulation-spec
---

# Gorlach 2023 Fig 3b Proxy Reproduction

## Target

Reproduce the qualitative content of Fig. 3b in Gorlach et al. 2023:
high-harmonic emission spectra for coherent, Fock, thermal, and bright
squeezed-vacuum driving light at matched mean driving intensity. The Nature
page identifies Fig. 3 as the spectra comparison, and the public source-data
archive includes `SourceData_3b.mat` for this panel. The local supplementary
PDF provides the coherent-state phase-space sampling formulation and the
1D soft-core TDSE baseline.

This page specifies a local stochastic-field proxy reproduction, not an exact
TDSE reproduction of the published panel.

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

The primary observable is the ensemble-mean proxy HHG energy spectrum versus
harmonic order:

```text
S_state(q) = mean_shots[S_proxy(q; E_shot)]
```

The output CSV should include raw matched-intensity spectra and a display
column with vertical offsets for a Fig. 3b-like plot. The display offsets are
only for visual comparison and must not be interpreted as absolute emitted
energy differences.

## Model Equations And Units

Use the existing fast HHG proxy:

```text
U_p = E_shot^2 / (4 omega0^2)
E_cutoff = I_p + 3.17 U_p
q_cutoff = E_cutoff / omega0
```

The proxy spectrum uses odd harmonic orders, a smooth low-order turn-on, and
an exponential rolloff beyond `q_cutoff`.

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

## Expected Outputs

Under a dated result directory:

```text
gorlach_2023_fig3b_proxy_spectra.csv
gorlach_2023_fig3b_proxy_summary.json
gorlach_2023_fig3b_proxy.png
manifest.yaml
```

The manifest must record the source URLs, raw local source path, random seed,
shots, driver-state parameters, field normalization, code entry point, commit
hash if available, and the approximation caveat.
