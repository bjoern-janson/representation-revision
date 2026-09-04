from __future__ import annotations

import itertools
import json
import math
import statistics
from pathlib import Path


def q_values_for_leaf_triple(leaves, distance_fn):
    leaves = tuple(leaves)
    if len(leaves) != 3 or len(set(leaves)) != 3:
        raise ValueError("leaves must contain exactly three distinct values")
    return [
        {
            "order": list(order),
            "q": distance_fn(order[0], order[1]) + distance_fn(order[1], order[2]),
        }
        for order in itertools.permutations(leaves)
    ]


def build_profiles(nodes, resistance_fn):
    nodes = tuple(nodes)
    return tuple(
        tuple(int(resistance_fn(source, target)) for target in nodes)
        for source in nodes
    )


def profile_l1_matrix(profiles):
    profiles = tuple(tuple(row) for row in profiles)
    n = len(profiles)
    if any(len(row) != n for row in profiles):
        raise ValueError("profiles must be a square profile table")
    return tuple(
        tuple(sum(abs(a - b) for a, b in zip(profiles[i], profiles[j])) for j in range(n))
        for i in range(n)
    )


def summarize_q_rows(rows):
    values = [int(row["q"]) for row in rows]
    if len(values) != 6:
        raise ValueError("exactly six permutation rows are required")
    return {
        "distinct_q_count": len(set(values)),
        "delta_q": max(values) - min(values),
    }


def _certificate_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "certificate"


def load_fixtures() -> tuple[tuple[str, ...], dict]:
    root = _certificate_dir()
    syntax = tuple(json.loads((root / "U_syntax.json").read_text(encoding="utf-8")))
    semantic = json.loads((root / "U_semantic.json").read_text(encoding="utf-8"))
    return syntax, semantic


def validate_fixtures(syntax: tuple[str, ...], semantic: dict) -> dict[str, int]:
    if len(syntax) != 77 or len(set(syntax)) != 77:
        raise ValueError("certified syntax fixture must contain 77 unique members")
    classes = semantic.get("classes", [])
    if semantic.get("class_count") != 6 or len(classes) != 6:
        raise ValueError("certified semantic fixture must contain 6 classes")
    flattened = [member for record in classes for member in record["members"]]
    if len(flattened) != 77 or set(flattened) != set(syntax) or len(set(flattened)) != 77:
        raise ValueError("semantic classes must partition the certified syntax fixture")
    semantic_pairs = sum(math.comb(len(record["members"]), 2) for record in classes)
    eligible_motifs = sum(
        len(record["members"]) * math.comb(len(record["members"]) - 1, 3)
        for record in classes
        if len(record["members"]) >= 4
    )
    return {
        "syntax_members": len(syntax),
        "semantic_classes": len(classes),
        "semantic_pairs": semantic_pairs,
        "eligible_motifs": eligible_motifs,
    }


def analyze_motifs(syntax, classes, distance_matrices, *, expected_eligible):
    syntax = tuple(syntax)
    index = {name: i for i, name in enumerate(syntax)}
    family_names = tuple(distance_matrices)
    if set(family_names) != {"R_v1", "R_unit", "R_depth"}:
        raise ValueError("exactly the three frozen resistance families are required")

    family_stats = {
        name: {
            "order_sensitive_motifs": 0,
            "distinct_q_counts": {"1": 0, "2": 0, "3": 0},
            "positive_delta_q": [],
        }
        for name in family_names
    }
    eligible = 0
    common_positive = 0
    witness = None
    witness_key = None

    normalized_classes = [tuple(sorted(record["members"])) for record in classes]
    for members in sorted(normalized_classes):
        if len(members) < 4:
            continue
        for center in members:
            leaves_pool = tuple(member for member in members if member != center)
            for leaves in itertools.combinations(leaves_pool, 3):
                eligible += 1
                per_family = {}
                common = True
                for family in family_names:
                    matrix = distance_matrices[family]
                    rows = q_values_for_leaf_triple(
                        leaves,
                        lambda left, right, m=matrix: m[index[left]][index[right]],
                    )
                    summary = summarize_q_rows(rows)
                    d = summary["distinct_q_count"]
                    if d not in (1, 2, 3):
                        raise AssertionError("reversal-invariant S3 statistic must have 1..3 distinct values")
                    family_stats[family]["distinct_q_counts"][str(d)] += 1
                    positive = d > 1
                    if positive:
                        family_stats[family]["order_sensitive_motifs"] += 1
                        family_stats[family]["positive_delta_q"].append(summary["delta_q"])
                    else:
                        common = False
                    per_family[family] = {
                        **summary,
                        "permutations": rows,
                    }
                if common:
                    common_positive += 1
                    candidate_key = (center, *leaves)
                    if witness_key is None or candidate_key < witness_key:
                        witness_key = candidate_key
                        witness = {
                            "center": center,
                            "leaves": list(leaves),
                            "families": per_family,
                        }

    if expected_eligible is not None and eligible != expected_eligible:
        raise AssertionError(f"eligible motif count {eligible} != frozen {expected_eligible}")

    reported_stats = {}
    for family, stats in family_stats.items():
        deltas = stats.pop("positive_delta_q")
        if deltas:
            delta_summary = {
                "min": min(deltas),
                "median": statistics.median(deltas),
                "max": max(deltas),
            }
        else:
            delta_summary = None
        reported_stats[family] = {**stats, "positive_delta_q": delta_summary}

    return {
        "eligible_motifs": eligible,
        "families": reported_stats,
        "common_positive_motifs": common_positive,
        "primary_positive": common_positive > 0,
        "witness": witness,
    }


def run_gamma_ordering_from_components(
    syntax, semantic, nodes, families, *, expected_eligible
):
    profiles = {name: build_profiles(nodes, fn) for name, fn in families.items()}
    distances = {name: profile_l1_matrix(rows) for name, rows in profiles.items()}
    return analyze_motifs(
        tuple(syntax),
        tuple(semantic["classes"]),
        distances,
        expected_eligible=expected_eligible,
    )


def run_gamma_ordering(*, dry_validate_only: bool = False) -> dict[str, object]:
    if dry_validate_only:
        syntax, semantic = load_fixtures()
        return validate_fixtures(syntax, semantic)

    from boolean_world.ast import parse_canonical
    from certificate.verify import load_verified_universe
    from representation_revision.accessibility import resistance
    from representation_revision.resistance_robustness import (
        depth_resistance,
        unit_resistance,
    )

    verified = load_verified_universe(_certificate_dir())
    syntax = tuple(verified.syntax)
    semantic = verified.semantic
    shape = validate_fixtures(syntax, semantic)
    if shape["eligible_motifs"] != 116664 or shape["semantic_pairs"] != 759:
        raise AssertionError("frozen certified-universe counts do not match preregistration")

    nodes = tuple(parse_canonical(text) for text in syntax)
    families = {
        "R_v1": resistance,
        "R_unit": unit_resistance,
        "R_depth": depth_resistance,
    }
    analysis = run_gamma_ordering_from_components(
        syntax,
        semantic,
        nodes,
        families,
        expected_eligible=116664,
    )
    return {
        "artifact": "GAMMA_ORDERING_V1_RESULT",
        "preregistration_commit": "05f718cba12194a42c1578f790081cc9016a151f",
        "preregistration_blob": "16036e8e2576b9fb1b1772870d947b36bdc40742",
        "machine_preregistration_blob": "0d975b002dc4dd55568d981527574cc85f570fe8",
        "universe": {
            **shape,
            "class_sizes": [len(record["members"]) for record in semantic["classes"]],
            "syntax_fixture_blob": "a74165f547390a116caa47f0ea16679e54c025a8",
            "semantic_fixture_blob": "dbeda59e6961eb7cc40672b8f336b1d62e8b793c",
        },
        "resistance_families": ["R_v1", "R_unit", "R_depth"],
        "statistic": "Q_k=sum_{t=0}^4 L_k(G_t,G_{t+2})",
        "reversal_invariant": True,
        "primary_rule": "common_positive_motifs > 0",
        **analysis,
    }
