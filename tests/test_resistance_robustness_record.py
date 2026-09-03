from __future__ import annotations

import json
from pathlib import Path

from boolean_world.ast import parse_canonical
from certificate.verify import load_verified_universe
from representation_revision.accessibility import resistance
from representation_revision.resistance_robustness import (
    all_profiles,
    depth_resistance,
    pairwise_jaccard,
    reachable_sets,
    semantic_pairs,
    separating_pairs,
    unit_resistance,
)


ROOT = Path(__file__).resolve().parents[1]


def test_recorded_resistance_robustness_is_reproducible():
    record = json.loads(
        (ROOT / "RECORDED_RESISTANCE_ROBUSTNESS_EXECUTION.json").read_text(encoding="utf-8")
    )
    verified = load_verified_universe(ROOT / "certificate")
    universe = tuple(parse_canonical(text) for text in verified.syntax)
    pairs = semantic_pairs(verified.syntax, verified.semantic)

    families = {
        "R_v1": lambda a, b: resistance(a, b),
        "R_unit": unit_resistance,
        "R_depth": depth_resistance,
    }
    profiles = {name: all_profiles(universe, fn) for name, fn in families.items()}
    reaches = {name: reachable_sets(profile, tau=record["threshold"]) for name, profile in profiles.items()}

    profile_sets = {name: separating_pairs(pairs, profile) for name, profile in profiles.items()}
    reach_sets = {
        name: separating_pairs(pairs, profiles[name], reaches[name])
        for name in families
    }

    assert len(universe) == record["universe"]["syntax_count"] == 77
    assert len(verified.semantic["classes"]) == record["universe"]["semantic_class_count"] == 6
    assert len(pairs) == record["universe"]["semantic_equivalent_pairs"] == 759

    assert {
        name: len(items) for name, items in profile_sets.items()
    } == record["profile"]["separating_pair_counts"]
    assert {
        name: len(items) for name, items in reach_sets.items()
    } == record["reachability"]["separating_pair_counts"]

    assert pairwise_jaccard(profile_sets) == record["profile"]["jaccard"]
    assert pairwise_jaccard(reach_sets) == record["reachability"]["jaccard"]
