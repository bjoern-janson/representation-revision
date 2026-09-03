from __future__ import annotations

from collections import defaultdict
from typing import Callable, Hashable

from boolean_world.ast import Node
from boolean_world.types import Op

from representation_revision.accessibility import resistance
from representation_revision.resistance_robustness import depth_resistance, unit_resistance

ResistanceFn = Callable[[Node, Node], int]

COMPLEXITY_OPS = (
    Op.INPUT,
    Op.NOT,
    Op.AND,
    Op.OR,
    Op.XOR,
    Op.EQ,
    Op.NEQ,
)


def ast_size(node: Node) -> int:
    total = 1
    for arg in node.args:
        if isinstance(arg, Node):
            total += ast_size(arg)
    return total


def ast_depth(node: Node) -> int:
    child_depths = [ast_depth(arg) for arg in node.args if isinstance(arg, Node)]
    return 0 if not child_depths else 1 + max(child_depths)


def operator_counts(node: Node) -> tuple[int, ...]:
    counts = {op: 0 for op in COMPLEXITY_OPS}

    def visit(current: Node) -> None:
        counts[current.op] += 1
        for arg in current.args:
            if isinstance(arg, Node):
                visit(arg)

    visit(node)
    return tuple(counts[op] for op in COMPLEXITY_OPS)


def complexity_vector(node: Node) -> tuple[int, ...]:
    """z(G): size, depth, then fixed operator counts."""
    return (ast_size(node), ast_depth(node), *operator_counts(node))


def pairwise_complexity_delta(source: Node, target: Node) -> tuple[int, ...]:
    left = complexity_vector(source)
    right = complexity_vector(target)
    return tuple(abs(a - b) for a, b in zip(left, right))


def profile_hamming(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if len(left) != len(right):
        raise ValueError("profiles must have equal length")
    return sum(a != b for a, b in zip(left, right))


def profile_l1(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if len(left) != len(right):
        raise ValueError("profiles must have equal length")
    return sum(abs(a - b) for a, b in zip(left, right))


def pair_indices(count: int) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(count) for j in range(i + 1, count))


def profile_distance_matrices(
    universe: tuple[Node, ...],
    families: dict[str, ResistanceFn],
) -> tuple[dict[str, tuple[tuple[int, ...], ...]], dict[str, dict[tuple[int, int], int]], dict[str, dict[tuple[int, int], int]]]:
    profiles = {
        name: tuple(tuple(fn(source, target) for target in universe) for source in universe)
        for name, fn in families.items()
    }
    hamming = {
        name: {
            (i, j): profile_hamming(matrix[i], matrix[j])
            for i, j in pair_indices(len(universe))
        }
        for name, matrix in profiles.items()
    }
    l1 = {
        name: {
            (i, j): profile_l1(matrix[i], matrix[j])
            for i, j in pair_indices(len(universe))
        }
        for name, matrix in profiles.items()
    }
    return profiles, hamming, l1


def exact_semantic_complexity_strata(
    semantic_pairs: tuple[tuple[int, int], ...],
    universe: tuple[Node, ...],
) -> dict[tuple[int, ...], tuple[tuple[int, int], ...]]:
    strata: dict[tuple[int, ...], list[tuple[int, int]]] = defaultdict(list)
    for i, j in semantic_pairs:
        strata[pairwise_complexity_delta(universe[i], universe[j])].append((i, j))
    return {key: tuple(value) for key, value in strata.items()}


def matched_strata(
    strata: dict[tuple[int, ...], tuple[tuple[int, int], ...]]
) -> dict[tuple[int, ...], tuple[tuple[int, int], ...]]:
    return {key: pairs for key, pairs in strata.items() if len(pairs) >= 2}


def safe_mean(values: list[int]) -> float:
    return 0.0 if not values else sum(values) / len(values)


def summarize_family(
    semantic_pairs: tuple[tuple[int, int], ...],
    strata: dict[tuple[int, ...], tuple[tuple[int, int], ...]],
    hamming: dict[tuple[int, int], int],
    l1: dict[tuple[int, int], int],
) -> dict[str, object]:
    matched = matched_strata(strata)
    matched_pairs = tuple(pair for pairs in matched.values() for pair in pairs)
    nonconstant = {
        key: pairs
        for key, pairs in matched.items()
        if len({hamming[pair] for pair in pairs}) > 1
    }
    nonconstant_pairs = tuple(pair for pairs in nonconstant.values() for pair in pairs)
    matched_hamming = [hamming[pair] for pair in matched_pairs]
    matched_l1 = [l1[pair] for pair in matched_pairs]

    return {
        "N_eligible": len(semantic_pairs),
        "N_matched": len(matched_pairs),
        "N_separated": sum(hamming[pair] > 0 for pair in matched_pairs),
        "exact_semantic_strata": len(strata),
        "matched_semantic_strata": len(matched),
        "nonconstant_matched_semantic_strata": len(nonconstant),
        "pairs_in_nonconstant_matched_strata": len(nonconstant_pairs),
        "D_hamming": {
            "min": min(matched_hamming) if matched_hamming else None,
            "max": max(matched_hamming) if matched_hamming else None,
            "mean": safe_mean(matched_hamming),
        },
        "profile_L1": {
            "min": min(matched_l1) if matched_l1 else None,
            "max": max(matched_l1) if matched_l1 else None,
            "mean": safe_mean(matched_l1),
        },
        "nonconstant_examples": [
            {
                "complexity_delta": list(key),
                "pair_count": len(pairs),
                "D_hamming_values": sorted({hamming[pair] for pair in pairs}),
                "pair_indices": [list(pair) for pair in pairs],
            }
            for key, pairs in sorted(nonconstant.items())
        ],
    }


def run_complexity_control(
    universe: tuple[Node, ...],
    semantic_pairs: tuple[tuple[int, int], ...],
) -> dict[str, object]:
    families: dict[str, ResistanceFn] = {
        "R_v1": resistance,
        "R_unit": unit_resistance,
        "R_depth": depth_resistance,
    }
    profiles, hamming, l1 = profile_distance_matrices(universe, families)
    strata = exact_semantic_complexity_strata(semantic_pairs, universe)
    summary = {
        name: summarize_family(semantic_pairs, strata, hamming[name], l1[name])
        for name in families
    }
    return {
        "families": summary,
        "meta": {
            "syntax_count": len(universe),
            "semantic_equivalent_pairs": len(semantic_pairs),
            "unordered_nonidentical_pairs": len(pair_indices(len(universe))),
            "profile_width": len(universe),
            "complexity_vector_width": len(complexity_vector(universe[0])),
            "semantic_complexity_strata": len(strata),
        },
        "_profiles": profiles,
    }
