# Correspondence-First HHG Paper Design

Date: 2026-06-06

Updated: 2026-06-06 after the 54-source literature-search and APS ingest.

## Purpose

Design the first paper in this project as a focused, high-impact manuscript on
observable-matched stochastic phase-space field theory for squeezed-vacuum-
driven high harmonic generation (HHG).

The paper should calibrate what stochastic field theory can prove, what it can
compute in high-photon-number nonlinear regimes, and what requires a stronger
quantum-output model.

The expanded source base strengthens HHG as the first nonlinear application.
It adds source-backed targets for BSV source engineering, superbunching,
gain-dependent mode structure, ionization and tunneling under BSV, nonclassical
cutoff fluctuations, photon bunching, symmetry leakage, and displaced or
squeezed harmonic output. The first paper should still avoid certifying
non-Gaussian output states, but its simulation layer should retain enough
per-shot information to support those future diagnostics.

The two later-added APS papers sharpen an important distinction. Lyu et al.
2025 supports a pre-HHG ATI/ionization validation track based on incoherent
coherent-component averaging over photon statistics. Wang et al. 2024 is not a
BSV pump paper; it models squeezed vacuum as the quantum environment of a
selected emitted harmonic mode through a `mu_k(t)` factor. Paper one should
compare these as separate mechanisms rather than merging them into one
"squeezed HHG" bucket.

## Core Thesis

A stochastic phase-space description of squeezed vacuum can exactly reproduce
selected input-field quantum-optics observables when representation, operator
ordering, and detection mode are matched. The same validated ensemble provides
a controlled high-photon-number route to HHG intensity, ionization, and cutoff
observables, while genuine non-Gaussian emitted-state claims require an
additional witness, reconstruction protocol, or quantum-output model.

## New Source-Backed Refinement

The first design treated BSV mainly as single-mode or mode-filtered squeezed
vacuum. The new literature search requires a sharper source-model ladder:

1. ideal single-mode squeezed vacuum for exact analytic validation,
2. equal independent modes for controlled mode-count tests,
3. gain-dependent Schmidt-mode ensembles for realistic BSV,
4. two-color or twin-beam BSV when the experiment requires paired modes,
5. propagated or Kerr-modified BSV as a future non-Gaussian pump-state frontier.

The first implementation should build hooks for this ladder even if it only
quantitatively validates the first two or three levels.

The HHG application should now use a three-path mechanism map:

1. stochastic or BSV pump sampling that changes the drive field realization,
2. ATI/ionization validation that tests photon-statistics effects before
   recombination,
3. squeezed emitted-mode environment modulation for selected harmonic channels.

Only the first two belong in the main simulation pipeline for paper one. The
third is a compact toy or boundary model unless a full quantized emitted-field
calculation is added.

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
   single-mode, mode-filtered, and source-model-tagged cases. The validation
   should show both corrected observables and naive estimators that fail.

3. HHG intensity-level prediction

   The validated ensemble drives a gas HHG response model. Supported observables
   include ensemble-averaged spectra, conditional spectra, ionization or
   tunneling yield distributions, cutoff distributions, shot-to-shot variance,
   ATI/electron-number statistics, rare-event statistics, symmetry-leakage
   channels where the model supports them, and Monte Carlo uncertainty.

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
   compensation where appropriate. Add a source-model table separating ideal
   single-mode, equal-mode, gain-dependent Schmidt-mode, two-color/twin-beam,
   and propagated/non-Gaussian BSV cases.

4. Claim ladder and non-Gaussian boundary

   Use the Yanagimoto/Jankowski non-Gaussian nonlinear optics sources to
   distinguish classical stochastic shot distributions, Gaussian quantum
   observables, and genuine quantum non-Gaussian output states. This section
   protects the paper from overclaiming.

5. HHG gas demonstration

   Use a source-backed, deliberately modest gas HHG model. The preferred first
   target is a single-atom or local gas response before macroscopic propagation,
   with the fast HHG proxy used only as a pipeline smoke test. Report
   intensity-level observables: mean spectra, conditional spectra,
   ionization/tunneling yield distributions, ATI/electron-number statistics,
   cutoff distributions, shot variance, rare-event tails, symmetry-leakage
   proxies when available, and convergence. Add a short boundary subsection on
   squeezed emitted-mode environments using Wang 2024's `mu_k(t)` modulation,
   explicitly separate from BSV pump sampling.

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
  squeezed fields. It records source-model family, mode definitions, squeezing
  parameters, gain or Schmidt weights when used, random seeds, ensemble sizes,
  and uncertainty estimates.

- Source-model component

  Represents the BSV input as an explicit family: single-mode, equal-mode,
  gain-weighted Schmidt modes, two-color/twin-beam, or future propagated/Kerr
  modified BSV. Each result must state which family generated the stochastic
  samples.

- HHG demonstration component

  Uses the validated stochastic ensemble as input to a gas HHG response model.
  It reports only observables compatible with the current model boundary and
  stores per-shot driver quadratures, intensity, phase, ionization proxy,
  cutoff proxy, harmonic amplitudes, and harmonic phases before aggregation.

- ATI validation component

  Tests coherent, thermal, and BSV photon-statistics ensembles before HHG
  recombination. It records ionization yield, electron-number statistics, and
  any momentum or energy distribution proxy needed to check the diagonal
  coherent-component averaging approximation.

- Emission-mode environment component

  Implements a boundary toy model in which a selected harmonic channel is
  multiplied by Wang 2024's squeezed-vacuum factor
  `mu_k(t) = cosh(r_k) + sinh(r_k) exp[-i(2 omega_k t - theta_k)]`. This
  component must be labeled as emitted-mode vacuum modulation, not BSV pump
  sampling.

- Claim-boundary component

  Uses `wiki/theory/non-gaussian-output-novelty.md` to classify each result as
  exact input correspondence, stochastic intensity-level prediction, Gaussian
  output diagnostic, or non-Gaussian quantum-output frontier.

## Data Flow

1. Choose representation, source-model family, mode basis, squeezing
   parameters, gain or mode weights, and detection model.
2. Generate stochastic squeezed-field samples.
3. Validate input diagnostics against analytic targets.
4. Pass validated samples to the HHG response model.
5. Store per-shot records before aggregation.
6. Aggregate mean spectra, conditional spectra, ionization/tunneling yields,
   ATI/electron-number statistics, cutoff distributions, phase/symmetry
   proxies, and uncertainty estimates.
7. For selected harmonic-channel environment tests, apply the `mu_k(t)`
   modulation as a separate branch.
8. Label every result with its mechanism family, source-model family, and
   claim-ladder level before it enters the paper.

## Figure Plan

1. Claim ladder schematic from exact input diagnostics to non-Gaussian frontier.
2. Observable-matching table or diagram.
3. Single-mode `g^(2)(0)` validation, including the failed naive estimator and
   the corrected normally ordered result.
4. Source-model ladder figure: single-mode, equal-mode, Schmidt-mode,
   two-color/twin-beam, and propagated/Kerr-modified BSV.
5. Broadband or mode-filtered `g^(2)` validation showing why detection mode and
   dispersion compensation matter.
6. Squeezed-drive statistics: intensity distribution, rare-event tail,
   superbunching/mode-count dependence, and matched coherent, noisy, and
   squeezed baselines.
7. HHG per-shot observable map: driver quadratures, intensity, phase,
   ionization/tunneling yield, cutoff proxy, harmonic amplitudes, and harmonic
   phases.
8. ATI validation figure: coherent, thermal, and BSV sampled ensembles,
   ionization yield enhancement, electron-number bunching, and diagonal
   averaging caveat.
9. Squeezed emitted-mode environment toy: `mu_k(t)` angle dependence for one
   selected harmonic channel, clearly separated from BSV pump sampling.
10. HHG results: mean spectra plus conditional spectra, cutoff distributions,
   ionization/tunneling yield distributions, or symmetry-leakage proxies.
11. Boundary and outlook map linking HHG to future non-Gaussian witnesses and
   THz/plasma extensions.

## Success Criteria

- The paper proves the stochastic/quantum match for at least one nontrivial
  squeezed-vacuum diagnostic.
- The simulations show that naive stochastic intensity moments give the wrong
  photon-counting answer unless ordering corrections are applied.
- The validation includes a broadband or mode-filtered case, not only a
  single-mode toy example.
- The validation records the BSV source-model family and does not treat one
  single analytic distribution as universal BSV.
- The HHG demonstration uses the validated ensemble, stores per-shot metadata,
  and reports only supported intensity-level, ionization/tunneling, cutoff, or
  symmetry-proxy observables.
- The ATI validation branch compares coherent, thermal, and BSV statistics at
  matched field scale before full HHG claims are made.
- The squeezed emitted-mode environment branch is labeled as a selected
  harmonic-mode effect and is not conflated with stochastic BSV pump sampling.
- The non-Gaussian discussion identifies the next witness or output model
  needed to go beyond positive stochastic sampling.

## Source Grounding

- Raymer/Landes 2022 and 2023 anchor the stochastic/quantum optics
  correspondence, broadband correlations, and vacuum-subtraction caution.
- Sharapova 2015, Agafonov 2009, Iskhakov 2012/2015, Perez 2014, and
  Sharapova 2020 anchor the BSV source-model ladder: two-color BSV,
  superbunching, spatial single-mode engineering, spectral tailoring, and
  gain-dependent Schmidt modes.
- Gorlach 2023, Rasputnyi 2024, Heimerl 2025, Tzur, and Even Tzur 2025 anchor
  phase-space averaging and HHG/strong-field quantum-light boundaries.
- Lemieux 2024, Stammer 2024/2025/2026, Rivera-Dean 2024/2025, Wang 2024/2025,
  Mao 2025, Singh 2026, Khurelbaatar 2026, Jiang 2026, and Liu 2026 expand the
  HHG and strong-field target observables: photon bunching, harmonic squeezing,
  optical coherence, tunneling and ionization, cutoff fluctuations, attosecond
  synthesis, and fluctuation-induced symmetry breaking.
- Wang et al. 2024 anchors a separate squeezed-emitted-mode environment model
  through `mu_k(t)` modulation of a selected harmonic channel.
- Lyu et al. 2025 anchors the ATI/ionization validation branch through qSFA
  coherent-component averaging over coherent, thermal, and BSV photon
  statistics.
- Yanagimoto 2022/2024 and Jankowski 2024 anchor the non-Gaussian claim ladder.
- Florez 2020, Yanagimoto 2021, Kulkarni 2022, Vendromin 2024/2025, and
  Rasputnyi 2025 support the boundary between stochastic Gaussian source
  models and pump-depleted or Kerr-induced non-Gaussian source states.
- Ravi 2014, Schuh 2013, Sun 2022, and Wang 2026 support future THz extensions,
  not the core first-paper demonstration.

## Risks And Controls

- Operator-ordering error: include the failed naive estimator in the validation
  figure and state the corrected estimator next to it.
- Mode ambiguity: require a stated temporal or spectral mode for every
  `g^(2)` or photon-number claim.
- Source-model ambiguity: require a stated BSV source family and mode-weight
  convention for every stochastic ensemble.
- Mechanism ambiguity: require every HHG result to state whether the quantum
  light acts as a pump ensemble, an ATI/ionization photon-statistics ensemble,
  or an emitted-mode squeezed-vacuum environment.
- qSFA diagonal approximation risk: before importing ATI-style averaging into
  HHG, state the diagonal coherent-component approximation and its high-field
  or large-amplitude regime.
- Overclaiming classicality: use the claim ladder for every manuscript result.
- Rare-event numerical instability: report convergence versus ensemble size
  and conditional bins, and store per-shot records so outliers can be audited.
- Draft-source overuse: many 2026 source summaries are first-pass metadata
  ingests. Use them to choose diagnostics now, but extract equations and
  detection assumptions before citing them quantitatively.
- Non-Gaussian overclaiming: do not certify Wigner negativity or genuine
  quantum non-Gaussianity without a witness, reconstruction protocol, or
  quantum-output model.

## Out Of Scope For Paper One

- Full emitted harmonic quantum-state reconstruction.
- Certification of Wigner-negative HHG or THz output states.
- Macroscopic HHG propagation unless the local gas and per-shot metadata model
  are already validated.
- Full squeezed-vacuum optical-rectification theory.
- Plasma THz simulations beyond a concise future-work roadmap.
- Quantitative claims from first-pass 2026 source summaries before
  equation-level follow-up.
- Treating squeezed emitted-mode vacuum modulation as evidence for BSV pump
  sampling without a separate emitted-field model.

## Review Gate

After this design is approved, the next step is an implementation plan for:

1. completing the derivation page,
2. specifying the sampler validation,
3. implementing the BSV source-model ladder and per-shot records,
4. adding ATI/ionization validation and squeezed-emission-mode boundary tasks,
5. choosing the first HHG model fidelity level,
6. defining paper-one figures and result manifests.
