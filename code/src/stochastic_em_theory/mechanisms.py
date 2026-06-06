from __future__ import annotations

from enum import Enum


class MechanismFamily(str, Enum):
    BSV_PUMP_ENSEMBLE = "bsv_pump_ensemble"
    ATI_PHOTON_STATISTICS = "ati_photon_statistics"
    SQUEEZED_EMISSION_MODE_ENVIRONMENT = "squeezed_emission_mode_environment"


def mechanism_manifest_value(mechanism: MechanismFamily | str) -> str:
    if isinstance(mechanism, MechanismFamily):
        return mechanism.value
    if not mechanism:
        raise ValueError("mechanism must be a non-empty string")
    return mechanism
