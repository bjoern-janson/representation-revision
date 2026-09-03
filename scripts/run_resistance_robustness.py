from __future__ import annotations

import json
from pathlib import Path

from boolean_world.ast import parse_canonical
from certificate.verify import load_verified_universe
from representation_revision.accessibility import resistance
from representation_revision.resistance_robustness import (
    all_profiles,
    depth_resistance,
    intersection_sizes,
    jaccard,
    pairwise_jaccard,
    reachable_sets,
    semantic_pairs,
    separating_pairs,
    unit_resistance,
)

ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_ROOT = ROOT / "certificate"
TAU = 3


def main() -> None:
    verified = load_verified_universe(CERTIFICATE_ROOT)
    universe = tuple(parse_canonical(text) for text in verified.syntax)
    pairs = semantic_pairs(verified.syntax, verified.semantic)

    families = {
        "R_v1": lambda a, b: resistance(a, b),
        "R_unit": unit_resistance,
        "R_depth": depth_resistance,
    }

    profiles = {name: all_profiles(universe, fn) for name, fn in families.items()}
    reaches = {name: reachable_sets(profile, TAU) for name, profile in profiles.items()}
    profile_sets = {
        name: separating_pairs(pairs, profile)
        for name, profile in profiles.items()
    }
    reach_sets = {
        name: separating_pairs(pairs, profiles[name], reaches[name])
        for name in families
    }

    result = {
        "protocol_version": 1,
        "preregistration": "ACCESSIBILITY_ROBUSTNESS_PREREGISTRATION.json",
        "universe": {
            "syntax_count": len(universe),
            "semantic_class_count": len(verified.semantic["classes"]),
            "semantic_equivalent_pairs": len(pairs),
        },
        "threshold": TAU,
        "families": {
            "R_v1": {
                "rationale_id": "frozen-v1",
                "implementation": "representation_revision.accessibility.resistance",
            },
            "R_unit": {
                "rationale_id": "unit-edit",
                "implementation": "representation_revision.resistance_robustness.unit_resistance",
            },
            "R_depth": {
                "rationale_id": "hierarchy-weighted",
                "implementation": "representation_revision.resistance_robustness.depth_resistance",
            },
        },
        "profile": {
            "separating_pair_counts": {name: len(items) for name, items in profile_sets.items()},
            "intersection_sizes": intersection_sizes(profile_sets),
            "jaccard": pairwise_jaccard(profile_sets),
        },
        "reachability": {
            "separating_pair_counts": {name: len(items) for name, items in reach_sets.items()},
            "intersection_sizes": intersection_sizes(reach_sets),
            "jaccard": pairwise_jaccard(reach_sets),
        },
        "cross_checks": {
            "ordered_nonidentical_pairs": len(universe) * (len(universe) - 1),
            "v1_profile_separating_pairs": len(profile_sets["R_v1"]),
            "v1_reach_separating_pairs": len(reach_sets["R_v1"]),
        },
    }

    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
