from __future__ import annotations

from .diagnosis import diagnose, target
from .discriminator import find_discriminator
from .revision_universe import candidate_subset
from .types import DiscriminatingEvidence, GeneratorSpec, RRAResult


def rra(
    state: tuple[int, ...],
    evidence: tuple[int, ...],
    current: GeneratorSpec,
    revision_universe: tuple[GeneratorSpec, ...],
    follow_up_probe_pool: tuple[tuple[int, ...], ...],
) -> RRAResult:
    observed_outcome = target(state)
    diagnosis = diagnose(current, state, observed_outcome, evidence)
    if diagnosis.label != "generator-failure":
        return RRAResult(current.generator_id, diagnosis, DiscriminatingEvidence((), (), None))

    # Follow-up probes are only entered after the observed trigger has implicated G.
    candidates = candidate_subset(diagnosis.label, revision_universe)
    disc = find_discriminator(candidates, follow_up_probe_pool)
    if disc.unique_candidate_id is None:
        return RRAResult(None, diagnosis, disc)

    selected = {spec.generator_id: spec for spec in candidates}[disc.unique_candidate_id]
    return RRAResult(selected.generator_id, diagnosis, disc)
