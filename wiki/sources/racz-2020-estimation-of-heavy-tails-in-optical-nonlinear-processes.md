---
title: Racz Et Al 2020 Estimation Of Heavy Tails In Optical Non-Linear Processes
type: source-summary
status: active
created: 2026-11-14
updated: 2026-11-14
tags: [source, heavy-tails, statistics, estimators, bsv, supercontinuum, methods]
source_count: 1
confidence: high
related:
  - ../project-status-review
  - ../theory/bsv-even-order-response-moment-scaling
  - manceau-2019-indefinite-mean-pareto-photon-distribution
  - spasibko-2017-multiphoton-effects-photon-number-fluctuations
---

# Racz Et Al 2020 Estimation Of Heavy Tails In Optical Non-Linear Processes

## Bibliographic Metadata

- Authors: Eva Racz, Laszlo Ruppert, Radim Filip.
- Year: 2020. Identifier: arXiv:2011.04429v1 [physics.optics], 9 Nov 2020.
  The PDF carries no journal reference or DOI.
- Raw source: [Racz et al. - 2020 - Estimation of heavy tails in optical non-linear processes.pdf](<../../raw/sources/Racz et al. - 2020 - Estimation of heavy tails in optical non-linear processes.pdf>)
- Extracted text:
  [racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes.txt](<../../results/literature/ingest-2026-11-14/extracted_text/racz-2020-estimation-of-heavy-tails-in-optical-nonlinear-processes.txt>)
- Ingest date: 2026-11-14.

## Core Result

Statistics methods paper with simulated data only. It reviews how to estimate
a power-law tail exponent (histogram, empirical tail function, QQ estimator,
Hill estimator) and adapts the Hill estimator to two problems of the
experiment in [[manceau-2019-indefinite-mean-pareto-photon-distribution]]:
detector saturation, Eq. (9), and a bright-squeezed-vacuum (BSV) pump,
Eq. (8). For supercontinuum from a thermal pump the best relative error at
1e4 shots is 3 to 4 %; for a BSV pump it is 10 to 20 % (Figs. 6 and 8).

## Useful Equations Or Model Ingredients

```text
C = lim_{x->inf} -ln Fbar(x) / x = 0          heavy-tailed            (1)
Fbar(x) = x^(-alpha) L(x),  L slowly varying   Pareto-type             (2)
E(X^a) finite for a < alpha, infinite for a > alpha                    (Sec. 2)
Fbar*(x_(k)) = k / N                           empirical tail function (3)
gamma_H(k) = (1/k) sum_{i=1..k} ln x_(i) - ln x_(k+1)        Hill      (4)
RMSE[gamma_H(k)] = gamma / sqrt(k)             pure Pareto data       (Sec. 3.3)
X = D(K sinh^2(I + w1))                        toy supercontinuum      (5)
D(x) = l + w2 (x < l);  x + w2 (l <= x <= L);  L + w2 (x > L)          (6)
ln Lik(a, b) = ((a-1)/k) sum_{i=1..k} ln ln x_(i) - (b/k) sum_{i=1..k} ln x_(i)
               + a ln b - ln Gamma(a, b ln x_(k+1))                    (8)
gamma(k, j) = (j/(k-j)) ln(x_(j+1)/x_(k+1))
              + (1/(k-j)) sum_{i=j+1..k} ln(x_(i)/x_(k+1))             (9)
```

`x` is a positive intensity in arbitrary units, `Fbar(x) = P(X >= x)` the
tail function, `x_(i)` the `i`-th largest of `N` observations, and
`gamma = 1/alpha` the extreme value index. In Eq. (5), `I` is the pump
intensity, exponential with rate `lambda` (thermal) or `GAMMA(1/2, beta)`
(BSV); `w1`, `w2` are Gaussian noises; `l` is the noise floor and `L` the
saturation limit. Eq. (8) treats `ln x` as gamma distributed (the paper
writes `alpha, beta` for `a, b`); it is maximized with `a = 1/2` fixed, and
`1/b` tends to the Hill estimate. Eq. (9) discards the `j` largest
observations. Idealized distributions of the Manceau experiment (Table 2):

| Pump | Process | Output variable | Heavy-tailed | `gamma` |
| --- | --- | --- | --- | --- |
| Thermal | harmonic of order `n` | `[EXP(lambda)]^n` | yes | 0 |
| Thermal | supercontinuum | `sinh^2[EXP(lambda)]` | yes | `2/lambda` |
| BSV | harmonic of order `n` | `[GAMMA(1/2, beta)]^n` | yes | 0 |
| BSV | supercontinuum | `sinh^2[GAMMA(1/2, beta)]` | yes | `2/beta` |

### Estimation Guidance

- If a moment of the distribution is infinite, its sample average does not
  converge as shots are added. Second-order quantities such as correlations
  should not be computed for `alpha < 2` (Sec. 2, citing Spasibko 2017).
- For harmonic generation every moment exists, so there is "no theoretical
  issue" with `g2` (Sec. 4.1). The paper then drops that case and gives no
  convergence analysis for it.
- Naive log-log histogram fits perform worst. If a histogram is used: few
  logarithmic bins (3 for 100 tail points, 5 for 1e4) and a least-squares
  exponential fit to the histogram of `ln X`, weights `1/[p_k (1 - p_k)]`
  (Sec. 3.1, Fig. 2).
- Plot the empirical tail function: a power law is a straight line of slope
  `-alpha` on log-log axes, and detector saturation shows as a sharp cut-off
  that a histogram hides (Sec. 3.2, Fig. 5b).
- Use the Hill estimator, plotted against `ln k`, and read it on a plateau.
  It is biased when `L(x)` is not constant and is positive for any data;
  for an estimate below 0.3, consider other models (Sec. 3.3).
- BSV pump: use Eq. (8). The correction to the power law decays as a power
  of `ln x`, not of `x`, which makes the plain Hill estimator biased (Sec. 4.2).
- Saturation: drop the affected top observations with Eq. (9); the best-case
  error is then proportional to `1 / sqrt(k - j)` (Sec. 4.3, Fig. 9).
- Tail length `k`: of ten automatic procedures tested on 100 samples of 1e4,
  the Guillou and Hall method (ref. 77) was the most reliable and cheapest;
  a path-stability heuristic (Appendix A) also works (Table 3, Sec. 4.4).

## Assumptions

- Independent, identically distributed shots.
- The output is a deterministic function of a single-mode pump intensity,
  with additive Gaussian noise before and after the nonlinearity, Eqs. (5), (6).

## Limitations And Cautions

- No shot-number rule is given. What the paper offers: simulated samples of
  1e4; best-case relative error `1/sqrt(k)` for `k` usable tail points; and,
  for a narrower intensity window, more shots by the ratio of the tail
  probabilities of the old and new windows (Sec. 4.3).
- The usable window lies between noise floor and saturation; if they overlap
  "the experiment cannot be salvaged" (Sec. 1).
- No experimental data are analysed, and Eq. (8) is approximate because the
  true transformation is `sinh^2`, not `exp` (Sec. 4.2).

## Relevance To This Project

- Optical rectification of single-mode BSV gives a THz energy distributed as
  `[GAMMA(1/2, beta)]^2`, the third row of Table 2: heavy-tailed by Eq. (1),
  `gamma = 0`, all moments finite. The energy ratio 35/3 of
  [[../theory/bsv-even-order-response-moment-scaling]] is therefore well
  defined, and tail-exponent estimators are the wrong tool for it.
- The paper does not say how many shots that ratio needs. Project-side
  estimate, not from the paper: the delta method with `<I^k> = (2k-1)!!`
  gives a relative variance `(182.9 + 42.7 - 128.0)/N = 97.5/N` for the
  sample `g2`, so 10 % needs about 1e4 shots and 3 % about 1e5.
- Report the empirical tail function against `Erfc` (Manceau Eq. 10) and the
  usable detector window, not only a moment ratio.
- Consistency check: `gamma = 2/beta` with `beta = 1/(2 kappa <N_B>)` is the
  inverse of the tail exponent in Manceau Eq. (14) for `M = 1`.
