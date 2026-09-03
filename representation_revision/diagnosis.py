from __future__ import annotations

from .types import Diagnosis, GeneratorSpec, Representation


def target(state: tuple[int, ...]) -> int:
    x0, x1 = state[:2]
    return x0 ^ x1


def predicted_target(representation: Representation) -> int:
    if len(representation.features) != 1:
        raise ValueError("toy assay decoder expects a one-feature surface representation")
    return representation.features[0]


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
        "The current representation is not implicated by the observed trigger event.",
    )
