from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class HHGShotRecord:
    shot_index: int
    source_model_kind: str
    source_model_label: str
    mechanism: str
    driver_x: float
    driver_p: float
    driver_intensity: float
    driver_phase: float
    field_amplitude_au: float
    ionization_rate_proxy: float
    cutoff_order: float
    harmonic_phase_proxy: float


def shot_records_to_rows(records: list[HHGShotRecord]) -> list[dict[str, int | float | str]]:
    return [asdict(record) for record in records]
