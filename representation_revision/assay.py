from __future__ import annotations

from .diagnosis import target
from .generator import G0
from .revision_universe import enumerate_universe
from .rra import rra
from .shadow import paired_future_evaluation

DIAGNOSTIC_POOL = ((0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0))
FUTURE_INPUTS = ((0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1))


def run_scientific_assay():
    universe = enumerate_universe()
    result = rra((1, 0, 0), (), G0, universe, DIAGNOSTIC_POOL)
    by_id = {s.generator_id: s for s in universe}
    adaptive = by_id[result.generator_id] if result.generator_id else G0
    pairs = paired_future_evaluation(adaptive, G0, FUTURE_INPUTS)
    return {
        "trigger_state": (1, 0, 0),
        "trigger_outcome": target((1, 0, 0)),
        "g0_id": G0.generator_id,
        "result": result,
        "future_pairs": pairs,
    }
