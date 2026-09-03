from __future__ import annotations

import json
from pathlib import Path

from boolean_world.ast import parse_canonical
from certificate.verify import load_verified_universe
from representation_revision.complexity_control import run_complexity_control
from representation_revision.resistance_robustness import semantic_pairs

ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_ROOT = ROOT / "certificate"


def main() -> None:
    verified = load_verified_universe(CERTIFICATE_ROOT)
    universe = tuple(parse_canonical(text) for text in verified.syntax)
    pairs = semantic_pairs(verified.syntax, verified.semantic)

    result = run_complexity_control(universe, pairs)
    result.pop("_profiles")
    result = {
        "protocol_version": 1,
        "preregistration": "ACCESSIBILITY_COMPLEXITY_PREREGISTRATION.json",
        "universe": {
            "syntax_count": len(universe),
            "semantic_class_count": len(verified.semantic["classes"]),
            "semantic_equivalent_pairs": len(pairs),
        },
        "analysis": result,
        "claim_ceiling": "Within the certified finite universe and the preregistered resistance families, the assay can exclude or fail to exclude a declared structural-complexity explanation for the measured magnitude of outgoing-profile divergence. It cannot establish intrinsic representational geometry, semantic causality, future predictive value, behavioral consequences, temporal organization, or representation-space completeness.",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
