---
title: Squeezed Vacuum g2 Proof Plan
type: concept
status: seed
created: 2026-06-06
updated: 2026-06-06
tags: [squeezed-vacuum, g2, proof, quantum-optics]
source_count: 0
confidence: low
related:
  - stochastic-quantum-optics-correspondence
  - ../simulations/simulation-roadmap
---

# Squeezed Vacuum g2 Proof Plan

Goal: prove that the stochastic field description reproduces the standard
single-mode squeezed-vacuum result

```text
g^{(2)}(0) = <a^\dagger a^\dagger a a> / <a^\dagger a>^2
           = 3 + 1/<n>
```

where `<n> = sinh^2(r)` for a pure squeezed vacuum with squeezing parameter
`r`.

## Quantum Optics Route

1. Define the squeezed vacuum state:

```text
|0, zeta> = S(zeta)|0>
zeta = r exp(i phi)
```

2. Compute second moments:

```text
<a^\dagger a> = n = sinh^2(r)
<a a> = m = -exp(i phi) sinh(r) cosh(r)
|m|^2 = n(n + 1)
```

3. Use Gaussian moment factoring for the zero-mean state:

```text
<a^\dagger a^\dagger a a> = 2 n^2 + |m|^2 = 3 n^2 + n
```

4. Divide by `n^2`:

```text
g^{(2)}(0) = 3 + 1/n
```

## Stochastic Wigner Route

1. Sample `alpha` from a zero-mean complex Gaussian with:

```text
<|alpha|^2>_W = n + 1/2
<alpha^2>_W = m
```

2. Use Gaussian moment factoring:

```text
<|alpha|^4>_W = 2 (n + 1/2)^2 + |m|^2
```

3. Convert Wigner moments to normally ordered moments:

```text
<a^\dagger a> = <|alpha|^2>_W - 1/2
<a^\dagger a^\dagger a a> =
  <|alpha|^4>_W - 2 <|alpha|^2>_W + 1/2
```

4. Substitute the moments:

```text
<a^\dagger a^\dagger a a> = 3 n^2 + n
```

5. Therefore:

```text
g^{(2)}(0) = 3 + 1/n
```

## Numerical Validation Target

Implement Monte Carlo sampling for several `r` values. For each value:

- estimate `<|alpha|^2>_W`,
- estimate `<|alpha|^4>_W`,
- convert to `<n>` and `<a^\dagger a^\dagger a a>`,
- compare `g^{(2)}(0)` against `3 + 1/<n>`,
- report uncertainty versus ensemble size.

## Extension Questions

- How does loss change `g^{(2)}(0)` for squeezed vacuum?
- How does finite detection bandwidth define the effective temporal mode?
- What is the multimode bright squeezed vacuum formula under the chosen
  detection model?
- Which stochastic representation is most stable for high-intensity nonlinear
  propagation simulations?

