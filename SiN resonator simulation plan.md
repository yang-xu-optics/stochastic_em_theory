## Aim of the project
We would like to extend our current work on programmable electric field induced second harmonic generation in silicon nitride waveguide(published in https://www.nature.com/articles/s41586-025-09620-9) to resonator structures. The hope is to use the resonant enhancement of racetrack resonator structures to achieve greater conversion efficiencies than channel waveguides. We want to achieve a broadband second harmonic with fundamental harmonic ranging from 1520 nm to 1600 nm through modal phase matching (TM00 FH to TM20 SH) since the minimum poling period we can print on the device is around 10 microns. We should only use our poling programmability to adjust for minor phase mismatch between FH and SH. We should use Tidy3D for the entire simulation. 

## Relevant ideas
**Dispersion:**  simulate the dispersion of straight waveguides for varying widths and different FH wavelengths from 1520 nm to 1600 nm (the range of our Santec tunable laser).  Use the dispersion model found here ([https://refractiveindex.info/?shelf=main&book=Si3N4&page=Luke](https://refractiveindex.info/?shelf=main&book=Si3N4&page=Luke)).  The thickness of our nitrides was initially set to 800 nm and the claddings were SiO2.  

## Step 1: Design the waveguide and determine mode overlap
We expect a Si substrate, 2um of bottom silicon oxide, 800 nm of LPCVD SiN, and 1 um of top silicon oxide cladding.  Start the width of the waveguide from 1 um. Run the mode solver simulation and check if the modal overlap between the FH (TM00 from 1520 nm to 1600 nm) and the SH (TM20 from 760 nm to 800 nm) is good for second harmonic generation. 

Then scan the width of the waveguide such that the waveguide geometry can match the propagation constant of the FH wave (TM00) at 1560 nm and the SH (TM20) at 780 nm. Perform the same scan for a 700 nm-thick SiN too. 
## Step 2: Determining the poling period on a straight waveguide
Now use the material dispersion of SiN and compute the modal dispersion of the FH and SH wave respectively. Then for the FH from 1520 nm to 1600 nm, compute and the corresponding periodic poling period we need to impose onto the device to compensate for the phase mismatch.  
## Step 3: Mode and loss at bending

## Step 4: Work on the input and output coupling section
**Bus/Resonator Coupling**:  A challenge of achieving double resonance (among other things) is aligning the resonance frequencies of the FH and SH modes.  By over-coupling the FH, we will have an extremely wide FH resonance, meaning it is very likely that we will be able to get some overlap between the FH and SH modes.  So the main advantage of our resonant enhancement is high SH power confinement.  

For now, we scan the coupling gaps between from 300 um to 450 um.  