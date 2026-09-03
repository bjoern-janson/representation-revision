from __future__ import annotations

import json
from pathlib import Path

from boolean_world.ast import parse_canonical
from certificate.verify import load_verified_universe
from representation_revision.accessibility import (
    DEFAULT_RESISTANCE_SPEC,
    ResistanceSpec,
    accessibility,
    resistance,
    resistance_profile,
)


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_ROOT = ROOT / "certificate"


def _verified_nodes():
    verified = load_verified_universe(CERTIFICATE_ROOT)
    return tuple(parse_canonical(text) for text in verified.syntax), verified.semantic


def test_resistance_is_reflexive_and_directed_by_specification():
    universe, _ = _verified_nodes()
    for node in universe:
        assert resistance(node, node) == 0

    source = parse_canonical("INPUT(0)")
    target = parse_canonical("NOT(NEQ(INPUT(0),INPUT(1)))")
    assert resistance(source, target) != resistance(target, source)


def test_accessibility_is_future_blind_and_universe_bounded():
    universe, _ = _verified_nodes()
    current = parse_canonical("EQ(INPUT(0),INPUT(0))")
    reachable = accessibility(current, universe, tau=3)

    assert set(reachable).issubset(set(universe))
    assert current in reachable


def test_semantic_equivalence_does_not_automatically_imply_geometry_equivalence():
    universe, semantic = _verified_nodes()
    by_semantic_id = {
        record["semantic_id"]: tuple(parse_canonical(text) for text in record["members"])
        for record in semantic["classes"]
        if len(record["members"]) > 1
    }

    comparisons = []
    for members in by_semantic_id.values():
        for i, left in enumerate(members):
            left_profile = resistance_profile(left, universe)
            for right in members[i + 1 :]:
                right_profile = resistance_profile(right, universe)
                comparisons.append((left, right, left_profile != right_profile))

    assert comparisons
    assert any(different for _, _, different in comparisons)


def test_semantic_equivalence_and_thresholded_reachability_are_reported_separately():
    universe, semantic = _verified_nodes()
    tau = 3
    records = []
    for class_record in semantic["classes"]:
        members = tuple(parse_canonical(text) for text in class_record["members"])
        sizes = tuple(len(accessibility(node, universe, tau)) for node in members)
        records.append((class_record["semantic_id"], sizes))

    assert len(records) == 6
    assert all(len(sizes) >= 1 for _, sizes in records)


def test_resistance_spec_is_explicit_and_nonnegative():
    spec = ResistanceSpec(
        operator_substitution_cost=1,
        input_index_substitution_cost=1,
        node_deletion_cost=1,
        node_insertion_cost=2,
    )
    assert spec == DEFAULT_RESISTANCE_SPEC
    assert all(
        value >= 0
        for value in (
            spec.operator_substitution_cost,
            spec.input_index_substitution_cost,
            spec.node_deletion_cost,
            spec.node_insertion_cost,
        )
    )
