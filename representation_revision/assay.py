from __future__ import annotations

from .diagnosis import target
from .generator import G0
from .revision_universe import enumerate_universe
from .rra import rra
from .shadow import paired_future_evaluation

# Trigger is deliberately a state where G0's one-feature decoder predicts x0=1,
# while the observed target is x0 XOR x1 = 0. This is the corrective discrepancy.
TRIGGER = (1, 1, 0)
FOLLOW_UP_PROBE_POOL = ((1, 0, 0), (1, 1, 0))
FUTURE_INPUTS = ((0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1))


def run_scientific_assay():
    universe = enumerate_universe()
    result = rra(TRIGGER, (), G0, universe, FOLLOW_UP_PROBE_POOL)
    by_id = {spec.generator_id: spec for spec in universe}
    adaptive = by_id[result.generator_id] if result.generator_id else G0
    # Persistent state is the selected GeneratorSpec carried unchanged into the
    # held-out future evaluation. The shadow never updates and remains G0.
    pairs = paired_future_evaluation(adaptive, G0, FUTURE_INPUTS)
    return {
        "trigger_state": TRIGGER,
        "trigger_outcome": target(TRIGGER),
        "g0_id": G0.generator_id,
        "selected_generator_id": result.generator_id,
        "result": result,
        "future_pairs": pairs,
    }
