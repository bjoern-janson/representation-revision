from __future__ import annotations

from itertools import combinations

from .diagnosis import target
from .types import DiscriminatingEvidence, GeneratorSpec


def _can_decode_target(spec: GeneratorSpec, probes: tuple[tuple[int, ...], ...]) -> bool:
    buckets: dict[tuple[int, ...], set[int]] = {}
    for probe in probes:
        rep = spec.fn(probe, ())
        buckets.setdefault(rep.features, set()).add(target(probe))
    return all(len(labels) == 1 for labels in buckets.values())


def _signature(spec: GeneratorSpec, probes: tuple[tuple[int, ...], ...]) -> str:
    return ";".join(f"{spec.fn(p, ()).features}->{target(p)}" for p in probes)


def find_discriminator(candidates: tuple[GeneratorSpec, ...], probe_pool: tuple[tuple[int, ...], ...]) -> DiscriminatingEvidence:
    if not candidates:
        return DiscriminatingEvidence((), (), None)
    for size in range(1, len(probe_pool) + 1):
        for probes in combinations(probe_pool, size):
            viable = tuple(spec for spec in candidates if _can_decode_target(spec, probes))
            if len(viable) == 1:
                return DiscriminatingEvidence(
                    probes=probes,
                    candidate_signatures=tuple((s.generator_id, _signature(s, probes)) for s in candidates),
                    unique_candidate_id=viable[0].generator_id,
                )
    return DiscriminatingEvidence(
        probes=probe_pool,
        candidate_signatures=tuple((s.generator_id, _signature(s, probe_pool)) for s in candidates),
        unique_candidate_id=None,
    )
