from __future__ import annotations

from .types import Diagnosis, GeneratorSpec, Representation


def target(state: tuple[int, ...]) -> int:
    x0, x1 = state[:2]
    return x0 ^ x1


def predicted_target(representation: Representation) -> int:
    if len(representation.features) == 1:
        return representation.features[0]
    if len(representation.features) == 2:
        x0, second = representation.features
        # Supports both g1=(x0,x1) and g2=(x0,x0|x1).
        inferred_x1 = second if second != (x0 | second) else second & (1 - x0)
        return x0 ^ inferred_x1
    raise ValueError("toy assay decoder expects one or two representation features")


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
