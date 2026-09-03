from __future__ import annotations

from .types import FuturePair, GeneratorSpec


def paired_future_evaluation(adaptive: GeneratorSpec, shadow: GeneratorSpec, future_inputs: tuple[tuple[int, ...], ...]) -> tuple[FuturePair, ...]:
    pairs = []
    for state in future_inputs:
        evidence: tuple[int, ...] = ()
        pairs.append(FuturePair(state, evidence, adaptive.fn(state, evidence), shadow.fn(state, evidence)))
    return tuple(pairs)
