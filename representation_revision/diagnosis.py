from __future__ import annotations

from .types import Diagnosis, GeneratorSpec, Representation


def target(state: tuple[int, ...]) -> int:
    x0, x1 = state[:2]
    return x0 ^ x1


def predicted_target(representation: Representation) -> int:
    if representation.generator_id == "g0_surface":
        (x0,) = representation.features
        return x0
    if representation.generator_id == "g1_complete":
        x0, x1 = representation.features
        return x0 ^ x1
    if representation.generator_id == "g2_redundant":
        x0, combined = representation.features
        x1 = combined & (1 - x0)
        return x0 ^ x1
    raise ValueError("unknown toy generator")


def diagnose(generator: GeneratorSpec, state: tuple[int, ...], observed_outcome: int, evidence=()) -> Diagnosis:
    representation = generator.fn(state, evidence)
    predicted = predicted_target(representation)
    if predicted != observed_outcome:
        return Diagnosis(
            "generator-failure",
            "The observed outcome disagrees with the prediction induced by the current representation.",
        )
    return Diagnosis(
        "not-evaluable",
        "The current generator is not implicated by the observed trigger event.",
    )
