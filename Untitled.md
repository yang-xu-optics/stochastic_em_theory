# Goal: design SiN racetrack resonators for type-0 EFISH SHG TM00(1560) →

TM00(780) — double resonance preferred, single resonance acceptable — and gauge SPDC 780 → 1560 and design new coupler for SPDC if necessary.

  

# Device material stack (from bottom up): doped silicon substrate, 1-micron thermal silicon oxide, 2-micron SiN core, 1-micron top PECVD silicon oxide, 6-micron of top silicon rich nitride as photoconductive layer, 30 nm of ITO as the top electrode

  

# Computation tools: tidy3d for FDTD and mode solving

  

# Deliverables: GDS file for fabrication, html report, list of design specs of devices, anticipated performance report

  

# Design Steps:

## Step 1 — Layer stack + mode model

- Use the layer stack information mentioned above.

- Mode solves: solve for the mode dispersion of TM00 @ ~1560 and TM00 @ ~780 at a proper width where the phase mismatch is minimized;

- The best guess of the width of the straight waveguide section is ~3 microns, but it can change based on the simulation of the mode dispersion. 

- The cross section of the waveguide is rectangular.

  

## Step 2 — EFISH QPM

- Δn(λ) = n_TM00(λ/2) − n_TM00(λ) over 1540–1600 nm; poling period Λ = λ/(2Δn) and

  sign map. CHECK against the 10-µm printing floor (this is the smallest poling period we can print on the chip using the current setup).

- Electrode phase bookkeeping over the bends (if electrodes cover straights only).

  

## Step 3 — Euler bend design

- Constant waveguide width through the bends (no width tapering; PM inside the bends is irrelevant because the unpoled, field-free bends generate no SH). 

- Maximize the transmission of both FH and SH, and make sure the mode conversion is small across the bending sections

  

## Step 4 — Coupler design

- The resonator should couple to the bus waveguide through a single directional coupler. Design the coupling length, gap width, and tapering (if necessary) so that the resonator can have (or at least sitting close to) a double resonance. 

  

## Step 5 — Resonator performance and Q factor

- Based on the previous simulation results and design, put every piece together and gauge the performance of resonators designed for SHG. Use FDTD to compute the Q-factor of each design. 

- The final GDS should cover a range of reasonable design specs including coupler gap, coupling length, bending geometries, straight waveguide length.

- Use RIT_Doc_Brown_Tapeout_12_14_2025_Final.gds as a gds template. 

  

## Step 6 — Efficiency + SPDC gauge

- SPDC: same phase matching reversed; pair rate ∝ same |χ⁽²⁾_eff|²·Q-product scaling;

  gauge pairs/s/mW against typical χ⁽²⁾ microring SPDC literature; flag that EFISH

  χ⁽²⁾ is field-programmable (E_DC on) — a switchable SPDC source.

- The device is now pumped with 780 nm sources. Determine if the coupler needs redesign for optimal pair production rate at the output.