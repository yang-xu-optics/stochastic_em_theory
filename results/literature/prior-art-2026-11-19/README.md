# Prior-Art Search: Exact Solution Of Quantized Optical Rectification

Date: 2026-11-19. Question from the author: has anyone shown before that
optical rectification with a quantized pump is exactly solvable?

## Scope And Limits

- arXiv API (`export.arxiv.org`), title/abstract queries, 26 queries.
- Web search, 9 queries (two in extended mode).
- Full text read for three arXiv papers only by keyword scan
  (2202.03353, 1810.11399, 1605.05770); everything else by abstract.
- Publisher sites are not reachable from this environment. The two key
  papers from 1991 and 1994 predate arXiv; only their abstracts and
  bibliographic records were seen, through third-party indexes.
- Not searched: Web of Science, Scopus, Google Scholar citation trails,
  theses, conference proceedings.
- Nothing was added to `raw/sources/`. The papers below are not ingested.

## Result

No paper was found that treats optical rectification, or THz emission in
general, with a quantized pump and gives the state of the emitted field. The
mechanism that makes the model solvable was found in several earlier works.

| Paper | What it shows | Read | Relation |
| --- | --- | --- | --- |
| Blow, Loudon, Phoenix, J. Opt. Soc. Am. B 8, 1750 (1991), DOI 10.1364/JOSAB.8.001750 | Exact quantum self-phase modulation without linearizing about a classical pump; generalization that removes the singularities of an instantaneous response | abstract | same mechanism: dispersionless field, nonlinearity depends on the flux only |
| Boivin, Kaertner, Haus, Phys. Rev. Lett. 73, 240 (1994), DOI 10.1103/PhysRevLett.73.240 | "Quantum theory of a field in 1+1 dimensions coupled to localized oscillators"; Heisenberg equation solved in closed form (self-phase modulation with a finite response time) | abstract; authors from memory | same model structure: flux coupled linearly to oscillators; oscillators are the medium, not an output |
| Shapiro and Razavi, New J. Phys. 9, 16 (2007), arXiv:quant-ph/0612086 | Continuous-time multimode cross-phase modulation: phase of one beam proportional to the photon flux of the other, plus phase-noise terms | abstract | same form as the pump relation (E7) |
| Shapiro, Phys. Rev. A 73, 062305 (2006) | Single-photon Kerr gates with a non-instantaneous response; causal response injects phase noise | abstract (ADS/OSTI record) | same family |
| Bose, Jacobs, Knight, Phys. Rev. A 56, 4175 (1997); Tsang, Phys. Rev. A 81, 063837 (2010) and 84, 043845 (2011) | Single-mode `g a^dagger a (b + b^dagger)`: exact solution; sideband regimes | arXiv abstracts | single-mode version |
| Miroshnichenko, Kiselev, Trifanov, Gleim, J. Opt. Soc. Am. B 34, 1177 (2017), arXiv:1605.05770 | Electro-optic modulation among a finite number of cavity modes: exactly solvable for a classical microwave field (su(2)); quantized microwave field by polynomially deformed Lie algebras | abstract, keyword scan | finite ladder: the case where the flux operators do not commute |
| Capmany and Fernandez-Pousa, J. Opt. Soc. Am. B 27, A119 (2010), arXiv:0911.0657 | Quantum scattering operator of a phase modulator with a classical drive; the infinite ladder reaches non-positive frequencies and must be modified | abstract | the band-edge caveat |
| Guedes, Vakulchyk, Seletskiy, Leitenstorfer, Moskalenko, Burkard, arXiv:2202.03353 (2022) | Back action in electro-optic sampling of the vacuum: cascaded, perturbative (to fourth order), coherent probe; compares with optomechanics | abstract, keyword scan, introduction | perturbative limit of the pump back action; closest physics |
| Glerean et al., J. Phys. B 52, 145502 (2019), arXiv:1810.11399 | Quantum model of impulsive stimulated Raman scattering; light in coherent states on a frequency ladder; phonon displacement at first order, red shift at second order | abstract, keyword scan | same ladder Hamiltonian with a phonon in place of the THz field; perturbative |
| Virally, Cusson, Seletskiy, Phys. Rev. Lett. 127, 270504 (2021), arXiv:2106.04402 | Electro-optic sampling with nonclassical probes | abstract | quantum light on the probe side of the same interaction |

## Queries

arXiv, first batch (strict): optical rectification with quantized / quantum
theory / photon statistics; electro-optic sampling with back action; THz with
photon number and nondemolition; self-phase modulation exact with response
time; electro-optic phase modulation with quantized microwave; intrapulse
difference frequency quantum; rectification with squeezed light; THz
generation with bright squeezed vacuum or quantum light; impulsive stimulated
Raman with photon number; photon flux constant of motion; electro-optic
sampling with quantum probe.

arXiv, second batch (broad): the same subjects with `all:` fields, plus
electro-optic modulator quantum (titles), frequency-bin electro-optic,
difference-frequency generation with a quantum pump, quantum nondemolition
with electro-optic, THz with quantized pump.

Web: the two 1990s titles; "quantum theory of optical rectification quantized
pump terahertz field exact solution photon flux operator"; optical
rectification with squeezed or quantum light; quantized optical rectification
exactly solvable; Shapiro single-photon Kerr; THz from incoherent light;
quantum light and coherent phonons by impulsive stimulated Raman scattering.

Hits unrelated to the question are not listed. Raw API responses were kept
in the session scratch directory and are not stored in the repository.
