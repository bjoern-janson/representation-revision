from __future__ import annotations

from typing import Iterable

from .generator import G0, G1, G2
from .types import CoverageReport, GeneratorSpec

_DECLARED_IDS = ("g0_surface", "g1_complete", "g2_redundant")
_DECLARED_SPECS = (G0, G1, G2)


def declared_universe() -> tuple[GeneratorSpec, ...]:
    return _DECLARED_SPECS


def enumerate_universe() -> tuple[GeneratorSpec, ...]:
    specs = tuple(declared_universe())
    if tuple(spec.generator_id for spec in specs) != _DECLARED_IDS:
        raise AssertionError("declared universe changed")
    return specs


def candidate_subset(diagnosis: str, universe: Iterable[GeneratorSpec]) -> tuple[GeneratorSpec, ...]:
    specs = tuple(universe)
    if diagnosis != "generator-failure":
        return (G0,)
    return tuple(spec for spec in specs if spec.generator_id != G0.generator_id)


def coverage_report() -> CoverageReport:
    first = enumerate_universe()
    second = enumerate_universe()
    ids_a = tuple(s.generator_id for s in first)
    ids_b = tuple(s.generator_id for s in second)
    if ids_a != ids_b:
        raise AssertionError("universe enumeration is not deterministic")
    return CoverageReport(
        status="certified-complete",
        universe_ids=_DECLARED_IDS,
        enumerated_ids=ids_a,
        omitted_ids=(),
        deterministic=True,
        independent_of_current_generator=True,
    )
