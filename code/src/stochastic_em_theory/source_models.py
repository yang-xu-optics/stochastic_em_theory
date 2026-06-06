from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np


class SourceModelKind(str, Enum):
    SINGLE_MODE = "single_mode"
    EQUAL_MODE = "equal_mode"
    SCHMIDT_MODE = "schmidt_mode"
    TWO_COLOR_TWIN_BEAM = "two_color_twin_beam"
    PROPAGATED_NONGAUSSIAN_FRONTIER = "propagated_nongaussian_frontier"


@dataclass(frozen=True)
class SourceModeWeight:
    label: str
    nbar: float
    weight: float


@dataclass(frozen=True)
class SourceModelSpec:
    kind: SourceModelKind
    label: str
    mode_weights: tuple[SourceModeWeight, ...]
    source_refs: tuple[str, ...]
    notes: str


def _nbar_from_r(r: float) -> float:
    if r < 0:
        raise ValueError("r must be non-negative")
    return float(np.sinh(r) ** 2)


def _normalize_brightness(labels: list[str], nbars: list[float]) -> tuple[SourceModeWeight, ...]:
    if not labels:
        raise ValueError("at least one mode is required")
    if len(labels) != len(nbars):
        raise ValueError("labels and nbars must have the same length")
    if any(nbar < 0 for nbar in nbars):
        raise ValueError("mode brightness values must be non-negative")
    total = float(sum(nbars))
    if total <= 0:
        weights = [1.0 / len(nbars)] * len(nbars)
    else:
        weights = [nbar / total for nbar in nbars]
    return tuple(
        SourceModeWeight(label=label, nbar=float(nbar), weight=float(weight))
        for label, nbar, weight in zip(labels, nbars, weights, strict=True)
    )


def single_mode_source(*, r: float, label: str = "single_mode") -> SourceModelSpec:
    nbar = _nbar_from_r(r)
    return SourceModelSpec(
        kind=SourceModelKind.SINGLE_MODE,
        label=label,
        mode_weights=_normalize_brightness(["mode_0"], [nbar]),
        source_refs=("Raymer/Landes 2022", "Perez 2014"),
        notes="Ideal single detected mode used for exact input-correspondence validation.",
    )


def equal_mode_source(*, r: float, modes: int, label: str = "equal_mode") -> SourceModelSpec:
    if modes <= 0:
        raise ValueError("modes must be positive")
    nbar = _nbar_from_r(r)
    labels = [f"mode_{index}" for index in range(modes)]
    return SourceModelSpec(
        kind=SourceModelKind.EQUAL_MODE,
        label=label,
        mode_weights=_normalize_brightness(labels, [nbar] * modes),
        source_refs=("Sharapova 2015", "Sharapova 2020"),
        notes="Controlled equal-mode model used to test detection-mode dependence.",
    )


def schmidt_mode_source(*, gain: float, eigenvalues: list[float], label: str = "schmidt_mode") -> SourceModelSpec:
    if gain < 0:
        raise ValueError("gain must be non-negative")
    eigenvalue_array = np.asarray(eigenvalues, dtype=np.float64)
    if eigenvalue_array.ndim != 1 or eigenvalue_array.size == 0:
        raise ValueError("eigenvalues must be a non-empty one-dimensional list")
    if np.any(eigenvalue_array < 0):
        raise ValueError("eigenvalues must be non-negative")
    if float(np.sum(eigenvalue_array)) <= 0:
        raise ValueError("at least one eigenvalue must be positive")

    normalized = eigenvalue_array / np.sum(eigenvalue_array)
    nbars = [float(np.sinh(gain * np.sqrt(value)) ** 2) for value in normalized]
    labels = [f"schmidt_{index}" for index in range(len(nbars))]
    return SourceModelSpec(
        kind=SourceModelKind.SCHMIDT_MODE,
        label=label,
        mode_weights=_normalize_brightness(labels, nbars),
        source_refs=("Sharapova 2015", "Sharapova 2020"),
        notes="Gain-dependent Schmidt-mode brightness model for realistic BSV source studies.",
    )


def two_color_twin_beam_source(
    *,
    r: float,
    signal_label: str = "signal",
    idler_label: str = "idler",
    label: str = "two_color_twin_beam",
) -> SourceModelSpec:
    nbar = _nbar_from_r(r)
    return SourceModelSpec(
        kind=SourceModelKind.TWO_COLOR_TWIN_BEAM,
        label=label,
        mode_weights=_normalize_brightness([signal_label, idler_label], [nbar, nbar]),
        source_refs=("Agafonov 2009", "Iskhakov 2012"),
        notes="Two-color or twin-beam BSV model for paired-mode source bookkeeping.",
    )


def effective_mode_count(source: SourceModelSpec) -> float:
    weights = np.asarray([mode.weight for mode in source.mode_weights], dtype=np.float64)
    return float(1.0 / np.sum(weights**2))
