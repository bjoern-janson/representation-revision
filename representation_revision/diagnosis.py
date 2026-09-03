from __future__ import annotations

from collections import defaultdict

from .types import Diagnosis, GeneratorSpec, Representation


def target(state: tuple[int, ...]) -> int:
    x0, x1 = state[:2]
    return x0 ^ x1


def diagnose(generator: GeneratorSpec, states: list[tuple[int, ...]], evidence: tuple[int, ...] = ()) -> Diagnosis:
    buckets: dict[tuple[int, ...], set[int]] = defaultdict(set)
    for state in states:
        rep: Representation = generator.fn(state, evidence)
        buckets[rep.features].add(target(state))
    ambiguous = sum(1 for labels in buckets.values() if len(labels) > 1)
    if ambiguous:
        return Diagnosis("generator-failure", "The current representation aliases diagnostic states with different target outcomes.")
    return Diagnosis("not-evaluable", "The current generator is sufficient on the declared diagnostic domain.")
