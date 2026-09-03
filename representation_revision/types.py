from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal

CoverageStatus = Literal["certified-complete", "bounded-partial", "unknown"]
DiagnosisLabel = Literal["not-evaluable", "state-error", "representation-failure", "generator-failure"]
GeneratorFn = Callable[[tuple[int, ...], tuple[int, ...]], "Representation"]

@dataclass(frozen=True)
class Representation:
    generator_id: str
    features: tuple[int, ...]

@dataclass(frozen=True)
class Diagnosis:
    label: DiagnosisLabel
    rationale: str

@dataclass(frozen=True)
class DiscriminatingEvidence:
    probes: tuple[tuple[int, ...], ...]
    candidate_signatures: tuple[tuple[str, str], ...]
    unique_candidate_id: str | None

@dataclass(frozen=True)
class GeneratorSpec:
    generator_id: str
    description: str
    fn: GeneratorFn

@dataclass(frozen=True)
class RRAResult:
    generator_id: str | None
    diagnosis: Diagnosis
    discriminating_evidence: DiscriminatingEvidence

@dataclass(frozen=True)
class CoverageReport:
    status: CoverageStatus
    universe_ids: tuple[str, ...]
    enumerated_ids: tuple[str, ...]
    omitted_ids: tuple[str, ...]
    deterministic: bool
    independent_of_current_generator: bool

@dataclass(frozen=True)
class FuturePair:
    input_state: tuple[int, ...]
    evidence: tuple[int, ...]
    adaptive_representation: Representation
    shadow_representation: Representation
