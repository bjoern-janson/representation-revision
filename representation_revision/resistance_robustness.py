from __future__ import annotations

from collections import defaultdict
from typing import Callable

from boolean_world.ast import Node

CostFn = Callable[[Node, Node], int]


def node_size(node: Node) -> int:
    total = 1
    for arg in node.args:
        if isinstance(arg, Node):
            total += node_size(arg)
    return total


def _replace_cost(source: Node, target: Node, delete_weight: Callable[[int], int], insert_weight: Callable[[int], int]) -> int:
    def weighted_size(node: Node, depth: int, weight: Callable[[int], int]) -> int:
        total = weight(depth)
        for arg in node.args:
            if isinstance(arg, Node):
                total += weighted_size(arg, depth + 1, weight)
        return total

    return weighted_size(source, 0, delete_weight) + weighted_size(target, 0, insert_weight)


def unit_resistance(source: Node, target: Node) -> int:
    """Unweighted structural edit resistance with unit substitution/insertion/deletion."""
    if source == target:
        return 0
    source_is_input = source.op.name == "INPUT"
    target_is_input = target.op.name == "INPUT"
    if source_is_input and target_is_input:
        return 1
    if source_is_input or target_is_input:
        return node_size(source) + node_size(target)
    if len(source.args) != len(target.args):
        return node_size(source) + node_size(target)
    cost = 1 if source.op != target.op else 0
    for a, b in zip(source.args, target.args):
        if not isinstance(a, Node) or not isinstance(b, Node):
            return node_size(source) + node_size(target)
        cost += unit_resistance(a, b)
    return cost


def depth_resistance(source: Node, target: Node) -> int:
    """Hierarchy-weighted structural resistance; local operation cost is depth+1."""
    def rec(a: Node, b: Node, depth: int) -> int:
        weight = depth + 1
        if a == b:
            return 0
        a_input = a.op.name == "INPUT"
        b_input = b.op.name == "INPUT"
        if a_input and b_input:
            return weight
        if a_input or b_input or len(a.args) != len(b.args):
            return _replace_cost(
                a,
                b,
                lambda d: depth + d + 1,
                lambda d: depth + d + 1,
            )
        cost = weight if a.op != b.op else 0
        for aa, bb in zip(a.args, b.args):
            if not isinstance(aa, Node) or not isinstance(bb, Node):
                return _replace_cost(
                    a,
                    b,
                    lambda d: depth + d + 1,
                    lambda d: depth + d + 1,
                )
            cost += rec(aa, bb, depth + 1)
        return cost

    return rec(source, target, 0)


def all_profiles(universe: tuple[Node, ...], resistance_fn: CostFn) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(resistance_fn(source, target) for target in universe) for source in universe)


def reachable_sets(
    profiles: tuple[tuple[int, ...], ...], tau: int
) -> tuple[frozenset[int], ...]:
    if tau < 0:
        raise ValueError("tau must be non-negative")
    return tuple(frozenset(j for j, cost in enumerate(row) if cost <= tau) for row in profiles)


def semantic_pairs(syntax: tuple[str, ...], semantic_fixture: dict) -> tuple[tuple[int, int], ...]:
    index = {text: i for i, text in enumerate(syntax)}
    pairs: list[tuple[int, int]] = []
    for record in semantic_fixture["classes"]:
        members = [index[text] for text in record["members"]]
        for pos, i in enumerate(members):
            for j in members[pos + 1 :]:
                pairs.append((i, j))
    return tuple(pairs)


def separating_pairs(
    pairs: tuple[tuple[int, int], ...],
    profiles: tuple[tuple[int, ...], ...],
    reachable: tuple[frozenset[int], ...] | None = None,
) -> frozenset[tuple[int, int]]:
    if reachable is None:
        return frozenset((i, j) for i, j in pairs if profiles[i] != profiles[j])
    return frozenset((i, j) for i, j in pairs if reachable[i] != reachable[j])


def jaccard(left: frozenset[tuple[int, int]], right: frozenset[tuple[int, int]]) -> float:
    union = left | right
    if not union:
        return 1.0
    return len(left & right) / len(union)


def pairwise_jaccard(sets: dict[str, frozenset[tuple[int, int]]]) -> dict[str, dict[str, float]]:
    names = tuple(sets)
    return {
        a: {b: jaccard(sets[a], sets[b]) for b in names}
        for a in names
    }


def intersection_sizes(sets: dict[str, frozenset[tuple[int, int]]]) -> dict[str, dict[str, int]]:
    names = tuple(sets)
    return {
        a: {b: len(sets[a] & sets[b]) for b in names}
        for a in names
    }
