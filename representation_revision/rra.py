from __future__ import annotations

from .diagnosis import diagnose, target
from .discriminator import find_discriminator
from .revision_universe import candidate_subset
from .types import DiscriminatingEvidence, GeneratorSpec, RRAResult


def rra(state: tuple[int, ...], evidence: tuple[int, ...], current: GeneratorSpec, revision_universe: tuple[GeneratorSpec, ...], probe_pool: tuple[tuple[int, ...], ...]) -> RRAResult:
    representation = current.fn(state, evidence)
    outcome = target(state)
    del representation, outcome
    diagnosis = diagnose(current, list(probe_pool), evidence)
    if diagnosis.label != "generator-failure":
        return RRAResult(current.generator_id, diagnosis, DiscriminatingEvidence((), (), None))
    candidates = candidate_subset(diagnosis.label, revision_universe)
    disc = find_discriminator(candidates, probe_pool)
    if disc.unique_candidate_id is None:
        return RRAResult(None, diagnosis, disc)
    selected = {s.generator_id: s for s in candidates}[disc.unique_candidate_id]
    return RRAResult(selected.generator_id, diagnosis, disc)
