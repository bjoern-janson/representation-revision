from __future__ import annotations

from .assay import FOLLOW_UP_PROBE_POOL, FUTURE_INPUTS, TRIGGER
from .diagnosis import target
from .discriminator import find_discriminator
from .generator import G0, G1, G2
from .revision_universe import coverage_report, enumerate_universe
from .rra import rra
from .shadow import paired_future_evaluation

POOL = FOLLOW_UP_PROBE_POOL


def certify_finiteness_and_determinism():
    a = enumerate_universe()
    b = enumerate_universe()
    assert len(a) == 3 and len(a) < float("inf")
    assert tuple(s.generator_id for s in a) == tuple(s.generator_id for s in b)
    report = coverage_report()
    assert report.status == "certified-complete"
    assert report.deterministic and report.independent_of_current_generator
    assert report.omitted_ids == ()
    return report


def certify_coverage_independence():
    ids = tuple(s.generator_id for s in enumerate_universe())
    assert ids == (G0.generator_id, G1.generator_id, G2.generator_id)
    return ids


def certify_discrimination():
    disc = find_discriminator((G1, G2), POOL)
    assert disc.unique_candidate_id == G1.generator_id
    assert disc.probes
    assert len(disc.candidate_signatures) == 2
    return disc


def certify_adoption():
    result = rra(TRIGGER, (), G0, enumerate_universe(), POOL)
    assert result.diagnosis.label == "generator-failure"
    assert result.generator_id == G1.generator_id
    assert target(TRIGGER) == 0
    return result


def certify_persistence_and_future_divergence():
    result = rra(TRIGGER, (), G0, enumerate_universe(), POOL)
    selected = {spec.generator_id: spec for spec in enumerate_universe()}[result.generator_id]
    pairs = paired_future_evaluation(selected, G0, FUTURE_INPUTS)
    assert result.generator_id != G0.generator_id
    assert any(p.adaptive_representation.features != p.shadow_representation.features for p in pairs)
    return pairs


def run_all_certifications():
    return {
        "coverage": certify_finiteness_and_determinism(),
        "coverage_ids": certify_coverage_independence(),
        "discrimination": certify_discrimination(),
        "adoption": certify_adoption(),
        "persistence": certify_persistence_and_future_divergence(),
    }
