from pathlib import Path
import json

from boolean_world.ast import parse_canonical
from certificate.verify import load_verified_universe
from representation_revision.accessibility import accessibility, resistance_profile


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_ROOT = ROOT / "certificate"


def _nodes_and_semantics():
    verified = load_verified_universe(CERTIFICATE_ROOT)
    nodes = tuple(parse_canonical(text) for text in verified.syntax)
    return nodes, verified.semantic


def test_recorded_accessibility_execution_matches_preregistered_result():
    record = json.loads((ROOT / "RECORDED_ACCESSIBILITY_EXECUTION.json").read_text(encoding="utf-8"))
    nodes, semantic = _nodes_and_semantics()
    index = {node.canonical_serialize(): i for i, node in enumerate(nodes)}

    profiles = [resistance_profile(node, nodes) for node in nodes]
    reachable = [accessibility(node, nodes, tau=record["threshold_reachability"]["tau"]) for node in nodes]

    semantic_pairs = []
    for class_record in semantic["classes"]:
        members = [index[text] for text in class_record["members"]]
        for pos, i in enumerate(members):
            for j in members[pos + 1 :]:
                semantic_pairs.append((profiles[i], profiles[j], reachable[i], reachable[j]))

    assert len(nodes) == record["universe"]["syntax_count"] == 77
    assert len(semantic["classes"]) == record["universe"]["semantic_class_count"] == 6
    assert len(semantic_pairs) == record["pair_space"]["semantic_equivalent_pairs"] == 759

    profile_divergence = sum(left != right for left, right, _, _ in semantic_pairs)
    reach_divergence = sum(left != right for _, _, left, right in semantic_pairs)

    assert profile_divergence == record["pair_space"]["within_semantic_profile_divergence_pairs"] == 759
    assert reach_divergence == record["pair_space"]["within_semantic_reachability_divergence_pairs"] == 755


def test_recorded_threshold_reachability_summary_is_reproducible():
    record = json.loads((ROOT / "RECORDED_ACCESSIBILITY_EXECUTION.json").read_text(encoding="utf-8"))
    nodes, _ = _nodes_and_semantics()
    sizes = [len(accessibility(node, nodes, tau=3)) for node in nodes]

    assert min(sizes) == record["threshold_reachability"]["min_size"]
    assert max(sizes) == record["threshold_reachability"]["max_size"]
    assert sum(sizes) / len(sizes) == record["threshold_reachability"]["mean_size"]
