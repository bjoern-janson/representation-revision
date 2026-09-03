from representation_revision.assay import DIAGNOSTIC_POOL, FUTURE_INPUTS
from representation_revision.certification import run_all_certifications
from representation_revision.generator import G0, G1
from representation_revision.rra import rra
from representation_revision.shadow import paired_future_evaluation


def test_frozen_contracts():
    out = run_all_certifications()
    assert out["coverage"].status == "certified-complete"
    assert out["coverage"].omitted_ids == ()
    assert out["discrimination"].unique_candidate_id == G1.generator_id
    assert out["adoption"].generator_id == G1.generator_id


def test_non_failure_retains_current_generator():
    result = rra((0, 0, 0), (), G1, (G0, G1), DIAGNOSTIC_POOL)
    assert result.generator_id == G1.generator_id
    assert result.diagnosis.label == "not-evaluable"


def test_paired_shadow_is_genuinely_held_out_and_identical():
    result = rra((1, 0, 0), (), G0, (G0, G1), DIAGNOSTIC_POOL)
    assert result.generator_id == G1.generator_id
    pairs = paired_future_evaluation(G1, G0, FUTURE_INPUTS)
    assert set(FUTURE_INPUTS).isdisjoint(set(DIAGNOSTIC_POOL))
    assert tuple((p.input_state, p.evidence) for p in pairs) == tuple((s, ()) for s in FUTURE_INPUTS)
    assert any(p.adaptive_representation.features != p.shadow_representation.features for p in pairs)
