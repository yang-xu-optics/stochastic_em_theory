from __future__ import annotations

from enum import Enum


class ClaimLevel(str, Enum):
    EXACT_INPUT_CORRESPONDENCE = "exact_input_correspondence"
    VALIDATED_STOCHASTIC_SIMULATION = "validated_stochastic_simulation"
    HHG_INTENSITY_PREDICTION = "hhg_intensity_prediction"
    GAUSSIAN_OUTPUT_DIAGNOSTIC = "gaussian_output_diagnostic"
    NON_GAUSSIAN_FRONTIER = "non_gaussian_frontier"
