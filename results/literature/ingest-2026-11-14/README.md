# Ingest 2026-11-14

Sources added for the change of headline claim to optical rectification of
bright squeezed vacuum (BSV). PDFs are in `../../../raw/sources/`; extracted
text (`pdftotext -layout`) is in `extracted_text/`; `download_manifest.json`
lists arXiv identifiers, page counts, and SHA-256 hashes.

## Downloaded (15, all from arxiv.org)

New 2026 work on quantum-light-driven strong-field physics:

| arXiv | First author | Title | Published |
| --- | --- | --- | --- |
| 2602.04370 | Gothelf | Limitations of an approximative phase-space description in strong-field quantum optics | Phys. Rev. A 113, 063107 (2026) |
| 2605.31160 | Rivera-Dean | Erasing photons from bright squeezed vacuum light via above-threshold ionization | preprint |
| 2606.17620 | Stammer | Photon anti-bunching in high harmonic generation | preprint |
| 2607.06395 | Stammer | Attosecond metrology of bright quantum light | preprint |
| 2607.20941 | Wang (Wentao) | Generation of bright quantum high-order harmonic driven by combined coherent and bright squeezed vacuum light | preprint |
| 2608.16027 | Gholam-Mirzaei | Sub-cycle metrology of bright quantum light | preprint |
| 2609.20559 | de-la-Pena | High-order correlations and ultrafast Wigner negativities in bright-squeezed-vacuum-driven high-harmonic generation | preprint |
| 2509.17746 | Kern | Single-shot pulse retrieval of femtosecond bright squeezed vacuum | Optica 13, 395 (2026) |

Supporting sources for the new claim:

| arXiv | First author | Title | Published |
| --- | --- | --- | --- |
| 2211.03188 | Gorlach | High harmonic generation driven by quantum light (main article; only the supplement was in `raw/` before) | Nature Physics 19, 1689 (2023) |
| 1705.07159 | Spasibko | Multiphoton effects enhanced due to ultrafast photon-number fluctuations | Phys. Rev. Lett. 119, 223603 (2017) |
| 1807.11784 | Manceau | Indefinite-mean Pareto photon distribution from amplified quantum noise | Phys. Rev. Lett. 123, 123606 (2019) |
| 2011.04429 | Racz | Estimation of heavy tails in optical non-linear processes | preprint as downloaded |
| 1508.06953 | Moskalenko | Paraxial theory of direct electro-optic sampling of the quantum vacuum | Phys. Rev. Lett. 115, 263601 (2015) |
| 1611.06773 | Riek | Subcycle quantum electrodynamics | Nature 541, 376 (2017) |
| 1807.10519 | Kizmann | Subcycle squeezing of light from a time flow perspective | see source page |

Journal references are those returned by the arXiv API on 2026-11-14.

## Not Obtained

- "Theory of high-harmonic generation with quantum light", Phys. Rev.
  Research, doi 10.1103/y3gr-tsns. Not found on arXiv under that title.
- "Propagation effects in high harmonic generation media driven by bright
  squeezed vacuum light", Nature Communications 2026, article
  s41467-026-75173-8. Probably the published version of arXiv:2509.19608,
  which is already in `raw/sources/`; not verified.
- Publisher sites are not on the session's network allowlist. Add these PDFs
  to `raw/sources/` by hand.

## arXiv Queries For The Scoop Watch

Run through `https://export.arxiv.org/api/query?search_query=...`, sorted by
submission date. Result counts are from 2026-11-14.

| Query | Hits | Relevant hits |
| --- | --- | --- |
| `all:terahertz AND all:"bright squeezed vacuum"` | 0 | none |
| `all:"optical rectification" AND (all:"squeezed vacuum" OR all:"squeezed light" OR all:"quantum light")` | 0 | none |
| `all:"bright squeezed vacuum" AND all:"difference frequency"` | 0 | none |
| `all:"optical rectification" AND all:"photon statistics"` | 0 | none |
| `all:"electro-optic sampling" AND (all:"bright squeezed" OR all:"squeezed vacuum")` | 2 | 1611.06773 (Riek 2017); 2208.02103 (electro-optic sampling with single-photon detectors, not ingested) |
| `all:"squeezed" AND all:terahertz AND all:"electro-optic sampling" AND all:"quantum"` | 2 | 1508.06953 (Moskalenko 2015); 2208.02103 |
| `all:"bright squeezed vacuum" AND all:"optical harmonics"` | 2 | 1705.07159, 1807.11784 |
| `all:"bright squeezed vacuum" AND (all:"supercontinuum" OR all:"Kerr") AND all:"statistics"` | 2 | 2512.17797 (already in `raw/`), 2011.04429 |
| `all:"anti-bunching" AND all:"high harmonic generation" AND all:"squeezed"` | 2 | 2606.17620; 2604.20388 (Ilin et al.; possibly a later version of the Ilin 2026 paper already in `raw/`, not checked) |

The arXiv API matches exact phrases in titles and abstracts only. A paper
that describes the same physics in other words would not be found by these
queries; widen them before relying on a negative result.
