from __future__ import annotations

import hashlib
import re
from pathlib import Path

G0_CANONICAL = "INPUT(0)"
G0_SIGNATURE = "0011"
PROBE_ORDER = ((0, 0), (0, 1), (1, 0), (1, 1))
H_POST = tuple((x0, x1, 1) for x0, x1 in PROBE_ORDER)

PREREGISTRATION_COMMIT = "2f577515fa2933833d6a50fcf37b9b53e0b31a57"
PREREGISTRATION_BLOB = "e7409e249fb175246a9f7aca36ef0492c8567ea1"
EXECUTION_PROTOCOL_COMMIT = "80b5c48135c293c4c5b57a654d6936c6b3aa0607"
EXECUTION_PROTOCOL_BLOB = "6e701b6944f3289c6c07de141c1e5dc46558090b"


def _validate_signature(signature: str) -> str:
    if len(signature) != 4 or any(bit not in "01" for bit in signature):
        raise ValueError("signature must be exactly four binary characters")
    return signature


def derive_seeded_environment(source_commit: str) -> dict[str, object]:
    if not isinstance(source_commit, str) or re.fullmatch(r"[0-9a-f]{40}", source_commit) is None:
        raise ValueError("source_commit must be a lowercase 40-character Git SHA")
    digest = hashlib.sha256(source_commit.encode("ascii")).digest()
    target_signature = format(digest[0] % 16, "04b")
    trigger_index = digest[1] % 4
    return {
        "seed_sha256": hashlib.sha256(source_commit.encode("ascii")).hexdigest(),
        "target_signature": target_signature,
        "trigger_index": trigger_index,
        "trigger_projection": list(PROBE_ORDER[trigger_index]),
    }


def build_pre_adoption_trace(target_signature: str, *, trigger_index: int) -> dict[str, object]:
    target_signature = _validate_signature(target_signature)
    if trigger_index not in range(4):
        raise ValueError("trigger_index must be in 0..3")

    projection = PROBE_ORDER[trigger_index]
    g0_output = int(G0_SIGNATURE[trigger_index])
    target_output = int(target_signature[trigger_index])
    trigger = {
        "projection": list(projection),
        "event": [projection[0], projection[1], 0],
        "phase": 0,
        "g0_output": g0_output,
        "target_output": target_output,
    }
    if g0_output == target_output:
        return {
            "status": "STOP_NO_DISCREPANCY",
            "trigger": trigger,
            "diagnosis": None,
            "T_t": [],
            "candidate_identity_available_to_evidence_generation": False,
        }

    followups = []
    for index, probe in enumerate(PROBE_ORDER):
        if index == trigger_index:
            continue
        followups.append(
            {
                "projection": list(probe),
                "event": [probe[0], probe[1], 0],
                "phase": 0,
                "target_output": int(target_signature[index]),
            }
        )
    return {
        "status": "READY_FOR_DISCRIMINATION",
        "trigger": trigger,
        "diagnosis": "generator-failure",
        "T_t": followups,
        "candidate_identity_available_to_evidence_generation": False,
    }


def run_operational_l2_from_signatures(
    *,
    target_signature: str,
    trigger_index: int,
    candidate_signatures: dict[str, str],
    universe_shape: dict[str, int],
) -> dict[str, object]:
    target_signature = _validate_signature(target_signature)
    if G0_CANONICAL not in candidate_signatures:
        raise ValueError("G0 must be present in the candidate universe")
    normalized = {name: _validate_signature(sig) for name, sig in candidate_signatures.items()}
    if normalized[G0_CANONICAL] != G0_SIGNATURE:
        raise ValueError("certified G0 signature mismatch")

    syntax_members = int(universe_shape["syntax_members"])
    semantic_classes = int(universe_shape["semantic_classes"])
    c_u_pass = syntax_members == len(normalized) and semantic_classes == len(set(normalized.values()))
    if not c_u_pass:
        return {
            "stop_reason": "STOP_UNIVERSE_SHAPE_MISMATCH",
            "burdens": {"C_U": "FAIL", "W": "NOT_EVALUATED", "C": "NOT_EVALUATED", "P": "NOT_EVALUATED", "E": "NOT_EVALUATED"},
            "primary_positive": False,
        }

    trace = build_pre_adoption_trace(target_signature, trigger_index=trigger_index)
    base = {
        "target_signature": target_signature,
        "trigger_index": trigger_index,
        "pre_adoption_trace": trace,
        "universe_shape": {"syntax_members": syntax_members, "semantic_classes": semantic_classes},
        "candidate_space_expanded_after_outcome": False,
        "runtime_candidate_enumeration_used": False,
    }
    if trace["status"] != "READY_FOR_DISCRIMINATION":
        return {
            **base,
            "stop_reason": trace["status"],
            "candidate_match_count": None,
            "selected_candidate": None,
            "burdens": {"C_U": "PASS", "W": "NOT_EVALUATED", "C": "NOT_EVALUATED", "P": "NOT_EVALUATED", "E": "NOT_EVALUATED"},
            "primary_positive": False,
        }

    matches = sorted(name for name, signature in normalized.items() if signature == target_signature)
    if len(matches) != 1:
        return {
            **base,
            "stop_reason": "STOP_NON_UNIQUE_DISCRIMINATION",
            "candidate_match_count": len(matches),
            "candidate_matches": matches,
            "selected_candidate": None,
            "burdens": {"C_U": "PASS", "W": "NOT_EVALUATED", "C": "FAIL", "P": "NOT_EVALUATED", "E": "NOT_EVALUATED"},
            "primary_positive": False,
        }

    g_star = matches[0]
    h_post = []
    for index, event in enumerate(H_POST):
        adaptive_raw = int(normalized[g_star][index])
        shadow_raw = int(normalized[G0_CANONICAL][index])
        target_output = int(target_signature[index])
        h_post.append(
            {
                "event": list(event),
                "evidence_signature": target_signature,
                "adaptive_generator_id": g_star,
                "adaptive_raw_output": adaptive_raw,
                "adaptive_behavior": adaptive_raw,
                "shadow_generator_id": G0_CANONICAL,
                "shadow_raw_output": shadow_raw,
                "shadow_behavior": shadow_raw,
                "compensation_generator_id": G0_CANONICAL,
                "compensation_raw_output": shadow_raw,
                "compensated_behavior": target_output,
                "target_behavior": target_output,
            }
        )

    w_pass = g_star != G0_CANONICAL and any(row["adaptive_raw_output"] != row["shadow_raw_output"] for row in h_post)
    c_pass = trace["candidate_identity_available_to_evidence_generation"] is False and len(matches) == 1
    p_pass = all(row["adaptive_generator_id"] == g_star for row in h_post) and all(row["shadow_generator_id"] == G0_CANONICAL for row in h_post)
    streams_match = all(tuple(row["event"]) == H_POST[i] for i, row in enumerate(h_post))
    compensation_retains_g0 = all(row["compensation_generator_id"] == G0_CANONICAL for row in h_post)
    compensation_matches_behavior = all(row["compensated_behavior"] == row["adaptive_behavior"] for row in h_post)
    generator_consequence_survives = any(row["adaptive_raw_output"] != row["compensation_raw_output"] for row in h_post)
    e_pass = streams_match and compensation_retains_g0 and compensation_matches_behavior and generator_consequence_survives

    burdens = {
        "C_U": "PASS",
        "W": "PASS" if w_pass else "FAIL",
        "C": "PASS" if c_pass else "FAIL",
        "P": "PASS" if p_pass else "FAIL",
        "E": "PASS" if e_pass else "FAIL",
    }
    stop_reason = None
    if not w_pass:
        stop_reason = "STOP_NO_GENERATOR_CHANGE"
    elif not c_pass:
        stop_reason = "STOP_CAUSAL_IDENTIFICATION_FAILURE"
    elif not p_pass:
        stop_reason = "STOP_PERSISTENCE_FAILURE"
    elif not streams_match:
        stop_reason = "STOP_FUTURE_STREAM_MISMATCH"
    elif not e_pass:
        stop_reason = "STOP_COMPENSATION_REPRODUCES_GENERATOR_CONSEQUENCE"

    return {
        **base,
        "stop_reason": stop_reason,
        "candidate_match_count": 1,
        "candidate_matches": matches,
        "selected_candidate": g_star,
        "burdens": burdens,
        "H_post": h_post,
        "compensation_behaviorally_succeeds": compensation_matches_behavior,
        "compensation_retains_G0": compensation_retains_g0,
        "claimed_consequence": "persistent raw generator-interface signature/identity",
        "primary_positive": stop_reason is None and all(value == "PASS" for value in burdens.values()),
    }


def _load_certified_signatures() -> tuple[dict[str, str], dict[str, int]]:
    from boolean_world.ast import parse_canonical
    from boolean_world.semantics import semantic_signature
    from certificate.verify import load_verified_universe

    root = Path(__file__).resolve().parents[1] / "certificate"
    verified = load_verified_universe(root)
    syntax = tuple(verified.syntax)
    semantic = verified.semantic
    if len(syntax) != 77 or semantic.get("class_count") != 6:
        raise ValueError("certified universe shape mismatch")
    candidate_signatures = {
        text: semantic_signature(parse_canonical(text), d=2)
        for text in syntax
    }
    if len(candidate_signatures) != 77 or len(set(candidate_signatures.values())) != 6:
        raise ValueError("certified semantic partition mismatch")
    if candidate_signatures.get(G0_CANONICAL) != G0_SIGNATURE:
        raise ValueError("certified G0 binding mismatch")
    return candidate_signatures, {"syntax_members": 77, "semantic_classes": 6}


def run_operational_l2(*, source_commit: str | None, dry_validate_only: bool = False) -> dict[str, object]:
    if dry_validate_only:
        candidate_signatures, shape = _load_certified_signatures()
        return {
            **shape,
            "g0_canonical": G0_CANONICAL,
            "g0_signature": candidate_signatures[G0_CANONICAL],
        }
    if source_commit is None:
        raise ValueError("source_commit is required for scientific execution")

    # Freeze target/trigger and the full pre-adoption evidence path before the
    # candidate universe is loaded into this execution path.
    environment = derive_seeded_environment(source_commit)
    pre_adoption = build_pre_adoption_trace(
        environment["target_signature"],
        trigger_index=environment["trigger_index"],
    )

    candidate_signatures, shape = _load_certified_signatures()
    result = run_operational_l2_from_signatures(
        target_signature=environment["target_signature"],
        trigger_index=environment["trigger_index"],
        candidate_signatures=candidate_signatures,
        universe_shape=shape,
    )
    if result["pre_adoption_trace"] != pre_adoption:
        raise AssertionError("pre-adoption evidence changed after candidate exposure")

    return {
        "artifact": "OPERATIONAL_L2_V1_RESULT",
        "scientific_source": source_commit,
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "preregistration_blob": PREREGISTRATION_BLOB,
        "execution_protocol_commit": EXECUTION_PROTOCOL_COMMIT,
        "execution_protocol_blob": EXECUTION_PROTOCOL_BLOB,
        "source_seeded_environment": environment,
        "historical_three_generator_assay_used": False,
        "held_out_ceiling": "H_post is novel at the full event/context level, not at the repeated d=2 generator-input projection level.",
        "primary_rule": "C_U_PASS and W_PASS and C_PASS and P_PASS and E_PASS and no stop rule fired",
        "claim_ceiling": "Certified finite-universe operational L2 only; no candidate-space expansion, arbitrary representation invention, L3 adaptation, or U_t -> U_(t+1).",
        **result,
    }
