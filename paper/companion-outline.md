# Manuscript Outline

Working title: Classical stochastic electrodynamics theory of high harmonic
generation and THz emission driven by squeezed vacuum.

> **Status (2026-11-14).** Outline only: no draft text and no paper-ready
> figures yet. This file was consolidated on 2026-11-14 from two overlapping
> section lists and three figure lists; no planned content was removed. The
> framing below is the one decided on 2026-06-18. An evaluation of that
> framing against work published since, and a recommended change of headline
> claim, are in [[wiki/project-status-review]]. Decide that before drafting.

## Framing

The first submission should be a two-result stochastic-field paper: validate the
bright-squeezed-vacuum (BSV) field representation against quantum-optics
diagnostics, then use the same representation to drive two nonlinear gas/plasma
emission channels: high-harmonic generation (HHG) and BSV-induced plasma THz
emission. The through-line is not "many applications"; it is one reusable
quantum-optics-consistent stochastic drive ensemble tested on two nonlinear
source mechanisms with different symmetry and detection behavior.

For Physical Review A, frame the manuscript as AMO and quantum optics: BSV
statistics are mapped into strong-field ionization, HHG spectra, cutoff
fluctuations, and plasma photocurrent THz emission. For Physical Review
Research, frame it more broadly as a reproducible phase-space simulation
framework connecting quantum-light statistics to nonlinear radiation sources.

Candidate titles:

```text
Stochastic-field theory of bright-squeezed-vacuum-driven high-harmonic and plasma THz emission
```

or:

```text
Bright squeezed vacuum as a stochastic drive for high-harmonic generation and plasma THz emission
```

Optical rectification should not be a main result in this version. It can appear
as a short outlook or comparison point because the direct squeezed-vacuum
`chi^(2)` source remains derivation-led, whereas plasma THz has a concrete
coherent-plus-BSV photocurrent model, validation observable, and symmetry
prediction. (A first derivation now exists as a seed page:
[[wiki/theory/bsv-even-order-response-moment-scaling]].)

## Abstract Notes

- State the motivation: squeezed vacuum as a nonclassical drive for nonlinear
  emission.
- State the interpretive problem: photon bunching in HHG or THz emission is
  often discussed as a quantum-light signature, but bunching by itself is not
  equivalent to entanglement, antibunching, Wigner negativity, or any other
  strictly nonclassical output witness. A stochastic theory gives the necessary
  baseline for deciding which observed correlations follow from input-field
  intensity fluctuations and which require genuinely quantum output physics.
- Explain why the stochastic-field route is useful: a full quantum treatment of
  multimode squeezed light coupled to ionization, HHG, plasma currents, and
  propagation is generally too large for direct Hilbert-space simulation,
  whereas a validated phase-space ensemble lets standard classical or
  semiclassical strong-field solvers be driven shot by shot by quantum-light
  statistics.
- Emphasize that the advantage is not replacing quantum mechanics, but
  translating selected quantum-optical input correlations into calculable
  nonlinear source terms while keeping the representation, operator ordering,
  and detection model explicit.
- State the method: stochastic electromagnetic field ensemble with explicit
  quantum-optics correspondence.
- State the validation: squeezed-vacuum `g^{(2)}(0)` and related diagnostics.
- State applications: HHG in gas and BSV-induced plasma THz emission.
- State the limitation: emitted-field nonclassicality requires additional
  measurement or phase-space witnesses; heavy-tailed stochastic outputs alone
  are not claimed to certify quantum non-Gaussian light.

Draft abstract value-proposition sentence:

```text
The stochastic-field formulation is useful because it converts the quantum
statistics of bright squeezed vacuum into a sampled drive ensemble that can be
passed through established strong-field and plasma-response models, avoiding
the exponential cost of a full multimode quantum treatment while preserving the
operator-ordering corrections needed to compare with photon-counting
observables.
```

Draft abstract misconception-clarifying sentence:

```text
This distinction is important because bunching and superbunching can arise from
positive stochastic intensity fluctuations, whereas antibunching, entanglement,
or Wigner negativity require stronger witnesses; the stochastic calculation
therefore provides a null model against which genuinely quantum output claims
can be tested.
```

## Section Plan

### 1. Introduction

Use a funnel structure: quantum light is becoming a strong-field control knob;
bright squeezed vacuum has large fluctuations and nontrivial photon statistics;
HHG, ionization, and plasma photocurrent observables are nonlinear filters of
those statistics; a classical or semiclassical stochastic simulation is useful
only if the field representation, ordering, and detection model are explicit.

Points to cover:

- Squeezed vacuum and bright squeezed vacuum as structured quantum light.
- Why nonlinear strong-field HHG and plasma THz emission are complementary
  testbeds.
- Need for a practical stochastic-field simulation framework.
- Summary of contributions and limits.

End the introduction with four precise contributions:

1. A stochastic representation and detection prescription that reproduces
   squeezed-vacuum photon-counting diagnostics.
2. A reproducible ensemble pipeline for squeezed, thermal, and coherent drive
   statistics.
3. HHG/ionization observables showing which signatures are input-statistics
   effects and which would require a stronger quantum-output claim.
4. A coherent-plus-BSV plasma photocurrent THz model showing the distinction
   between ensemble-mean THz fields, incoherent spectra, and classical THz
   energy statistics.

### 2. Stochastic Field Representation And Detection Model

Define the field modes, phase-space representation, quadratures, squeezing
parameter, squeezing phase, loss or mode filtering, and units before discussing
any nonlinear physics. This section should contain the operator-ordering bridge
that keeps raw stochastic intensity moments separate from normally ordered
photon-counting correlations.

- Define field modes and stochastic amplitudes.
- Specify Wigner or other chosen representation.
- State operator-ordering rules.
- Wiki: [[wiki/theory/stochastic-quantum-optics-correspondence]].
- Anchor sources: Raymer/Landes 2023 for stochastic vacuum subtraction;
  Sharapova 2015 for multimode BSV cautions.

### 3. Benchmark: Squeezed-Vacuum Photon Statistics

Make the benchmark the first result, not a preliminary appendix. Show the
single-mode result `g^{(2)}(0)=3+1/<n>` with `<n>=sinh^2(r)`, then show the
multimode or mode-filtered generalization used in the simulations. Include a
figure comparing analytic, corrected stochastic, and naive stochastic
estimators so the reader sees exactly why the ordering correction matters.

- Quantum derivation of quadrature moments and photon statistics.
- Stochastic derivation of the same observables.
- Numerical Monte Carlo validation.
- Wiki: [[wiki/theory/squeezed-vacuum-g2-proof-plan]].
- Anchor source: Raymer/Landes 2022 for broadband `g^(2)(0)` and dispersion
  compensation.

### 4. Shared Nonlinear Response Framework

Introduce a common stochastic-response average before splitting into HHG and
THz:

```text
observable = integral d lambda P(lambda) observable_coh(lambda)
```

where `lambda` denotes the stochastic field variables or coherent-response
labels. State which representation feeds each observable: Wigner samples for
input photon-counting diagnostics; Husimi-Q or coherent-component samples where
the nonlinear response is built as a diagonal coherent-state average. Then
define the two response families:

1. HHG/ionization response: proxy, Lewenstein/SFA, TDSE library, or propagation
   model, depending on the result included.
2. Plasma THz response: coherent 800 nm fundamental plus weak 400 nm BSV
   component, ionization-generated density, damped photocurrent, and
   band-limited `dJ/dt` as the THz source.

### 5. Results: HHG And Ionization Under Matched Drive Statistics

Organize results by claim strength:

1. Input-field validation and convergence.
2. Coherent, thermal, and BSV/ squeezed-drive comparisons at matched mean
   intensity.
3. Conditional spectra or high-intensity-tail bins.
4. Ionization/cutoff/variance diagnostics.
5. Optional selected-emission-mode squeezed-vacuum boundary model, clearly
   marked as a distinct mechanism from BSV pump sampling.

Content:

- Define gas and drive model.
- Present stochastic ensemble HHG source calculation.
- Compare coherent, noisy, and squeezed drives.
- Analyze spectra, cutoff statistics, and shot-to-shot variance.
- Wiki: [[wiki/models/hhg-gas-model]],
  [[wiki/simulations/gorlach-2023-fig3b-proxy-reproduction]],
  [[wiki/simulations/gorlach-2023-fig-iv2-bsv-threshold]].
- Anchor sources: Gorlach 2023 supplement for 1D gas baseline; Rasputnyi 2024
  and Heimerl 2025 for coherent-response averaging and conditional spectra;
  Tzur et al. and Even Tzur 2025 for output-state extensions.
- Literature-search additions: Lemieux 2024 for photon bunching, Stammer 2024
  and Rivera-Dean 2024 for squeezed/entangled HHG output, Wang 2024 for
  attosecond synthesis in intense squeezed light, Stammer 2025 for optical
  coherence, and the 2025-2026 BSV/quantum-light papers for symmetry leakage,
  cutoff fluctuations, tunneling, and ionization validation targets.
- Newly added APS papers: Wang et al. 2024 for squeezed-vacuum control of a
  selected harmonic emission mode, and Lyu et al. 2025 for ATI ionization
  benchmarks under coherent, thermal, and BSV photon statistics.
- Novelty branch: identify whether selected harmonic channels can develop
  higher cumulants, conditional non-Gaussian states, or Wigner-negativity
  witnesses.

### 6. Results: BSV-Induced Plasma THz Emission

Make plasma THz a second main result, not an outlook. The section should begin
with the physical setting: a strong coherent 800 nm fundamental plus a weak
400 nm BSV second harmonic, following the coherent-plus-BSV plasma THz
configuration. Then present:

1. Driving-field validation: BSV `g^{(2)}(0)` from ordering-corrected Wigner
   sampling, kept separate from the Husimi-Q coherent-component ensemble used
   for plasma dynamics.
2. Classical baselines: one-color coherent field as a symmetry-null case and
   coherent two-color mixing as a deterministic photocurrent reference.
3. Coherent-plus-BSV ensemble: mean THz waveform, shot-to-shot fluctuations,
   total ensemble-averaged spectrum, coherent spectrum, and incoherent
   component.
4. Symmetry result: a zero-mean BSV component can yield vanishing
   ensemble-mean THz field while retaining finite ensemble-averaged THz
   intensity.
5. Classical THz energy statistics, explicitly labeled as stochastic
   shot-distribution statistics rather than normally ordered photon
   correlations.

Content:

- Define the ionization-current model and THz source proportional to
  band-limited `dJ/dt`.
- Analyze symmetry requirements for nonzero ensemble-mean THz emission.
- Wiki: [[wiki/models/thz-plasma-emission-model]],
  [[wiki/simulations/thz-plasma-bsv-photocurrent-notebook]].
- Anchor sources: Schuh 2013 for microscopic gas current, Sun 2022 for plasma
  THz mechanism taxonomy, Wang 2026 for coherent-plus-BSV plasma THz sampling.

### 7. Cross-Channel Comparison And Claim Ladder

Compare what HHG and plasma THz are doing to the same BSV input statistics.
HHG emphasizes nonlinear spectral/cutoff response and high-field-tail
conditioning (spectra, cutoff distributions, ionization/tunneling validation);
plasma THz emphasizes symmetry, coherent versus incoherent emission, and
current-burst/energy statistics. Use this section to separate:

- input-field nonclassical statistics,
- nonlinear classical ensemble effects,
- emitted-field squeezing or bunching claims,
- candidate non-Gaussian quantum-output witnesses that require a stronger
  emitted-mode measurement model.

Novelty branch: identify whether either channel supports higher cumulants,
conditional non-Gaussian states, or Wigner-negativity witnesses, while keeping
classical shot distributions separate from quantum non-Gaussian output.
Wiki: [[wiki/theory/non-gaussian-output-novelty]].

### 8. Discussion: What The Stochastic Theory Does And Does Not Prove

This section should be unusually explicit. State that reproducing
photon-counting diagnostics by a matched phase-space stochastic ensemble does
not by itself prove full quantum equivalence of the nonlinear emitted field.
Distinguish input nonclassical statistics, classical shot-distribution
heavy tails, emitted-mode squeezing, conditional spectra, and genuine
non-Gaussian quantum-output witnesses.

- Relation to quantum optics, semiclassical nonlinear optics, and strong-field
  physics.
- Clarify the common misconception: photon bunching is not automatically a
  uniquely quantum-mechanical emitted-field signature. Classical thermal light,
  positive phase-space BSV ensembles, and nonlinear shot-to-shot intensity
  filtering can all produce bunched statistics. Antibunching, entanglement, and
  Wigner negativity require stronger measurements or state witnesses.
- Explain why this distinction matters experimentally: the stochastic model is
  a quantitative baseline for deciding whether HHG or THz bunching reflects
  input BSV statistics, nonlinear source filtering, detector-mode averaging, or
  genuinely nonclassical emitted radiation.
- Distinguish non-Gaussian classical shot distributions from non-Gaussian
  quantum states.
- Experimental observables and possible tests.

### 9. Outlook: Optical Rectification And Propagation Extensions

Keep optical rectification concise. The `chi^(2)` source term requires a
derivation of which ensemble-averaged low-frequency observable survives and how
vacuum subtraction enters. Future extensions should also include macroscopic
HHG propagation, plasma propagation, phase matching, and detector-mode
selection.

- Define nonlinear polarization model.
- Study ensemble-averaged THz field and intensity.
- Identify role of squeezing phase, bandwidth, and medium symmetry.
- Wiki: [[wiki/models/thz-optical-rectification-model]],
  [[wiki/theory/bsv-even-order-response-moment-scaling]].
- Anchor source: Ravi 2014 for classical tilted-pulse-front OR propagation,
  cascading, and 2D depletion limits.
- Anchor source: Jankowski 2024 for the bridge from classical `chi^(2)`
  nonlinear optics to non-Gaussian quantum dynamics.
- Status: no source for direct squeezed-vacuum `chi^(2)` OR was found in the
  2026-06-06 search or in two web searches on 2026-11-14. Treat the stochastic
  extension as derivation-led.

### 10. Conclusion

- Summarize correspondence proof.
- Summarize HHG and plasma THz simulation findings.
- State open problems.

### Appendices / Supplemental Material

Use appendices for the algebra that would slow the main line:

- Wigner-to-normal ordering derivation.
- Multimode `g^{(2)}` derivation and mode-count conventions.
- Sampling algorithms, random seeds, and convergence diagnostics.
- HHG/TDSE/proxy model details and units.
- Plasma photocurrent equations, baselines, filters, and unit conversions.
- Additional optical-rectification derivation notes if included only as
  outlook.

## Figure Plan

Main figures, each tied to one claim. "Evidence today" says what exists in
`results/runs/` as of 2026-11-14; see `results/runs/README.md` for why none of
it is paper-ready yet.

| # | Figure | Claim it supports | Evidence today |
| --- | --- | --- | --- |
| 1 | Concept schematic: sampled squeezed field, ordering-corrected detection, nonlinear response averaging | framing | not started |
| 2 | Squeezed-vacuum benchmark: analytic, corrected stochastic, and naive `g^{(2)}(0)` versus squeezing parameter | exact input correspondence | code and tests exist; only uncommitted smoke runs |
| 3 | Mode-filtered or multimode validation: `g^{(2)}` versus effective mode number | exact input correspondence | code and tests exist; only uncommitted smoke runs |
| 4 | Matched drive ensembles: coherent, thermal, and BSV intensity distributions at equal mean intensity | ensemble definition | not started |
| 5 | HHG spectra or ionization proxy under matched statistics, with uncertainty | HHG intensity prediction | four Fig. 3b reproduction runs; not converged, no uncertainty bands, not compared with the published source data |
| 6 | Conditional HHG spectra, cutoff, and yield fluctuations binned by sampled intensity | HHG intensity prediction | proxy model only |
| 7 | Plasma THz baselines: one-color symmetry-null case and coherent two-color photocurrent reference | plasma THz model check | in the notebook spectrum figure |
| 8 | Coherent-plus-BSV plasma THz: mean waveform with fluctuation band, total versus coherent/incoherent spectra, squeezing-angle dependence | plasma THz symmetry result | notebook figures at 400 shots; angle scan not done |
| 9 | Cross-channel diagnostic ladder: HHG high-field tails versus plasma THz coherent/incoherent emission and candidate non-Gaussian witnesses | claim ladder | not started |

Backlog figures (earlier plans, kept for reference):

- Example stochastic bright squeezed-vacuum waveforms and spectra.
- Broadband `g^(2)(0)` validation with and without dispersion compensation.
- HHG conditional versus unconditional spectra under BSV sampling.
- Plasma THz coherent-plus-BSV squeezing-angle scan.
- Plasma THz coherent, incoherent, and total spectral decomposition.
- Classical OR benchmark showing undepleted prediction versus depleted
  cascading-limited propagation.
- Non-Gaussian diagnostic ladder: higher cumulants, conditional output
  states, and candidate witness for one HHG or THz channel.
- HHG quantum-light observable map: photon bunching, harmonic squeezing,
  phase locking, symmetry leakage, cutoff fluctuations, and ionization
  conditioning.
