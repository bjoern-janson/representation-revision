import hashlib

import pytest

from representation_revision.operational_l2 import (
    G0_CANONICAL,
    G0_SIGNATURE,
    PROBE_ORDER,
    build_pre_adoption_trace,
    derive_seeded_environment,
    run_operational_l2,
    run_operational_l2_from_signatures,
)


def test_seeded_environment_is_deterministic_and_frozen_shape():
    source = "0" * 40
    digest = hashlib.sha256(source.encode("ascii")).digest()
    env = derive_seeded_environment(source)
    assert env["target_signature"] == format(digest[0] % 16, "04b")
    assert env["trigger_index"] == digest[1] % 4
    assert tuple(env["trigger_projection"]) == PROBE_ORDER[env["trigger_index"]]


def test_seeded_environment_rejects_non_commit_input():
    with pytest.raises(ValueError):
        derive_seeded_environment("not-a-commit")


def test_pre_adoption_trace_stops_if_fixed_trigger_has_no_discrepancy():
    # target == G0 everywhere, so any source-seeded trigger must fail to wound G0.
    trace = build_pre_adoption_trace(G0_SIGNATURE, trigger_index=2)
    assert trace["status"] == "STOP_NO_DISCREPANCY"
    assert trace["diagnosis"] is None
    assert trace["T_t"] == []


def test_pre_adoption_trace_fixes_diagnosis_before_three_followups():
    # 0101 differs from G0=0011 at indices 1 and 2; choose index 1 as the fixed trigger.
    trace = build_pre_adoption_trace("0101", trigger_index=1)
    assert trace["status"] == "READY_FOR_DISCRIMINATION"
    assert trace["trigger"]["projection"] == [0, 1]
    assert trace["trigger"]["g0_output"] == 0
    assert trace["trigger"]["target_output"] == 1
    assert trace["diagnosis"] == "generator-failure"
    assert [row["projection"] for row in trace["T_t"]] == [[0, 0], [1, 0], [1, 1]]
    assert all(row["phase"] == 0 for row in trace["T_t"])


def test_non_unique_behavioral_evidence_is_a_scientific_stop():
    candidates = {
        G0_CANONICAL: "0011",
        "xor-a": "0110",
        "xor-b": "0110",
    }
    result = run_operational_l2_from_signatures(
        target_signature="0110",
        trigger_index=1,
        candidate_signatures=candidates,
        universe_shape={"syntax_members": 3, "semantic_classes": 2},
    )
    assert result["stop_reason"] == "STOP_NON_UNIQUE_DISCRIMINATION"
    assert result["candidate_match_count"] == 2
    assert result["burdens"]["C"] == "FAIL"
    assert result["primary_positive"] is False


def test_unique_candidate_can_persist_while_compensation_matches_behavior_only():
    candidates = {
        G0_CANONICAL: "0011",
        "INPUT(1)": "0101",
    }
    result = run_operational_l2_from_signatures(
        target_signature="0101",
        trigger_index=1,
        candidate_signatures=candidates,
        universe_shape={"syntax_members": 2, "semantic_classes": 2},
    )
    assert result["selected_candidate"] == "INPUT(1)"
    assert result["burdens"] == {"C_U": "PASS", "W": "PASS", "C": "PASS", "P": "PASS", "E": "PASS"}
    assert result["primary_positive"] is True
    assert all(row["adaptive_behavior"] == row["compensated_behavior"] for row in result["H_post"])
    assert all(row["compensation_generator_id"] == G0_CANONICAL for row in result["H_post"])
    assert any(row["adaptive_raw_output"] != row["compensation_raw_output"] for row in result["H_post"])


def test_certified_dry_validation_consumes_literal_certificate_only():
    out = run_operational_l2(source_commit=None, dry_validate_only=True)
    assert out["syntax_members"] == 77
    assert out["semantic_classes"] == 6
    assert out["g0_canonical"] == G0_CANONICAL
    assert out["g0_signature"] == G0_SIGNATURE
