# Correspondence-First HHG Paper Design

Date: 2026-06-06

## Purpose

Design the first paper in this project as a focused, high-impact manuscript on
observable-matched stochastic phase-space field theory for squeezed-vacuum-
driven high harmonic generation (HHG).

The paper should calibrate what stochastic field theory can prove, what it can
compute in high-photon-number nonlinear regimes, and what requires a stronger
quantum-output model.

## Core Thesis

A stochastic phase-space description of squeezed vacuum can exactly reproduce
selected input-field quantum-optics observables when representation, operator
ordering, and detection mode are matched. The same validated ensemble provides
a controlled high-photon-number route to HHG intensity observables, while
genuine non-Gaussian emitted-state claims require an additional witness,
reconstruction protocol, or quantum-output model.

## Claim Ladder

The manuscript should organize all claims by level:

1. Exact input correspondence

   Quadrature moments, mean photon number, and `g^(2)(0)` are reproduced when
   Wigner-to-normal ordering corrections and explicit mode definitions are
   applied. The single-mode proof target is:

   ```text
   g^(2)(0) = 3 + 1/<n>
   ```

2. Validated stochastic simulation

   Monte Carlo squeezed-field ensembles converge to analytic diagnostics for
   single-mode and broadband or mode-filtered cases. The validation should
   show both corrected observables and naive estimators that fail.

3. HHG intensity-level prediction

   The validated ensemble drives a gas HHG response model. Supported observables
   include ensemble-averaged spectra, conditional spectra, cutoff
   distributions, shot-to-shot variance, rare-event statistics, and Monte Carlo
   uncertainty.

4. Gaussian quantum-output diagnostics

   Output covariance, squeezing, purity proxies, and mode selection are allowed
   only if the HHG output model supports them. This level is optional for paper
   one and may be framed as a bridge to future work.

5. Non-Gaussian quantum-output frontier

   Higher cumulants, Wigner negativity, conditional emitted states, and
   pump-output entanglement are not certified by positive stochastic sampling
   alone. Paper one should define these as future targets unless it adds a
   concrete witness or reconstruction model.

## Paper Structure

1. Introduction: the claim problem

   Explain why squeezed vacuum is nonclassical while many HHG and THz
   experiments occur at large photon number. State the central question: which
   quantum-light observables can stochastic field theory legitimately reproduce,
   and which claims require more?

2. Observable-matched correspondence

   Define the field representation, stochastic variables, mode normalization,
   ordering convention, and detection model. Include a table with columns:
   quantum observable, stochastic estimator, required correction, detection-mode
   assumption, and claim status.

3. Squeezed-vacuum validation

   Present the analytic single-mode `g^(2)(0)` derivation and Monte Carlo
   validation. Then extend to a broadband or mode-filtered validation following
   the Raymer/Landes assumptions, including temporal gate and dispersion
   compensation where appropriate.

4. Claim ladder and non-Gaussian boundary

   Use the Yanagimoto/Jankowski non-Gaussian nonlinear optics sources to
   distinguish classical stochastic shot distributions, Gaussian quantum
   observables, and genuine quantum non-Gaussian output states. This section
   protects the paper from overclaiming.

5. HHG gas demonstration

   Use a source-backed, deliberately modest gas HHG model. The preferred first
   target is a single-atom or local gas response before macroscopic propagation.
   Report intensity-level observables: mean spectra, conditional spectra,
   cutoff distributions, shot variance, rare-event tails, and convergence.

6. Discussion and outlook

   State what the framework proves and does not prove. Position plasma THz as
   the bolder sequel. Position optical rectification as a future derivation-led
   branch with Ravi 2014 as the classical propagation baseline.

## Components

- Correspondence theory component

  Reads from `wiki/theory/stochastic-quantum-optics-correspondence.md` and
  `wiki/theory/squeezed-vacuum-g2-proof-plan.md`. It defines the exact input
  observables and the estimator corrections.

- Sampler validation component

  Produces reproducible Monte Carlo validations for single-mode and broadband
  squeezed fields. It records mode definitions, squeezing parameters, random
  seeds, ensemble sizes, and uncertainty estimates.

- HHG demonstration component

  Uses the validated stochastic ensemble as input to a gas HHG response model.
  It reports only observables compatible with the current model boundary.

- Claim-boundary component

  Uses `wiki/theory/non-gaussian-output-novelty.md` to classify each result as
  exact input correspondence, stochastic intensity-level prediction, Gaussian
  output diagnostic, or non-Gaussian quantum-output frontier.

## Data Flow

1. Choose representation, mode basis, squeezing parameters, and detection
   model.
2. Generate stochastic squeezed-field samples.
3. Validate input diagnostics against analytic targets.
4. Pass validated samples to the HHG response model.
5. Aggregate mean spectra, conditional spectra, cutoff distributions, and
   uncertainty estimates.
6. Label every result with its claim-ladder level before it enters the paper.

## Figure Plan

1. Claim ladder schematic from exact input diagnostics to non-Gaussian frontier.
2. Observable-matching table or diagram.
3. Single-mode `g^(2)(0)` validation, including the failed naive estimator and
   the corrected normally ordered result.
4. Broadband or mode-filtered `g^(2)` validation showing why detection mode and
   dispersion compensation matter.
5. Squeezed-drive statistics: intensity distribution, rare-event tail, and
   matched coherent, noisy, and squeezed baselines.
6. HHG results: mean spectra plus conditional spectra or cutoff distributions.
7. Boundary and outlook map linking HHG to future non-Gaussian witnesses and
   THz/plasma extensions.

## Success Criteria

- The paper proves the stochastic/quantum match for at least one nontrivial
  squeezed-vacuum diagnostic.
- The simulations show that naive stochastic intensity moments give the wrong
  photon-counting answer unless ordering corrections are applied.
- The validation includes a broadband or mode-filtered case, not only a
  single-mode toy example.
- The HHG demonstration uses the validated ensemble and reports only supported
  intensity-level observables.
- The non-Gaussian discussion identifies the next witness or output model
  needed to go beyond positive stochastic sampling.

## Source Grounding

- Raymer/Landes 2022 and 2023 anchor the stochastic/quantum optics
  correspondence, broadband correlations, and vacuum-subtraction caution.
- Sharapova 2015 anchors the multimode BSV guardrail.
- Gorlach 2023, Rasputnyi 2024, Heimerl 2025, Tzur, and Even Tzur 2025 anchor
  phase-space averaging and HHG/strong-field quantum-light boundaries.
- Yanagimoto 2022/2024 and Jankowski 2024 anchor the non-Gaussian claim ladder.
- Ravi 2014, Schuh 2013, Sun 2022, and Wang 2026 support future THz extensions,
  not the core first-paper demonstration.

## Risks And Controls

- Operator-ordering error: include the failed naive estimator in the validation
  figure and state the corrected estimator next to it.
- Mode ambiguity: require a stated temporal or spectral mode for every
  `g^(2)` or photon-number claim.
- Overclaiming classicality: use the claim ladder for every manuscript result.
- Rare-event numerical instability: report convergence versus ensemble size
  and conditional bins.
- Non-Gaussian overclaiming: do not certify Wigner negativity or genuine
  quantum non-Gaussianity without a witness, reconstruction protocol, or
  quantum-output model.

## Out Of Scope For Paper One

- Full emitted harmonic quantum-state reconstruction.
- Certification of Wigner-negative HHG or THz output states.
- Macroscopic HHG propagation unless the local gas model is already validated.
- Full squeezed-vacuum optical-rectification theory.
- Plasma THz simulations beyond a concise future-work roadmap.

## Review Gate

After this design is approved, the next step is an implementation plan for:

1. completing the derivation page,
2. specifying the sampler validation,
3. choosing the first HHG model fidelity level,
4. defining paper-one figures and result manifests.
