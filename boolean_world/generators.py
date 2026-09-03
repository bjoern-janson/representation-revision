from __future__ import annotations

from typing import Dict, List, Set

from .ast import COMMUTATIVE_OPS, SIGNATURES, Node, make
from .types import Op, ValueType


def enumerate_universe(d: int = 4, max_depth: int = 2) -> List[Node]:
    """
    Exhaustively enumerate canonical, well-typed ASTs of depth <= max_depth.

    Completeness is with respect to the declared SIGNATURES, input indices
    0..d-1, and the specified depth bound. Nodes at each exact depth are
    generated bottom-up, and every valid binary child-depth pair satisfying
    max(child_depths) == depth - 1 is considered.
    """
    if d < 0:
        raise ValueError("d must be non-negative")
    if max_depth < 0:
        raise ValueError("max_depth must be non-negative")

    pools: List[Dict[ValueType, Set[Node]]] = [
        {value_type: set() for value_type in ValueType}
        for _ in range(max_depth + 1)
    ]

    for index in range(d):
        leaf = make(Op.INPUT, index)
        pools[0][leaf.type].add(leaf)

    for depth in range(1, max_depth + 1):
        for op, (arg_types, return_type) in SIGNATURES.items():
            if op == Op.INPUT:
                continue

            if len(arg_types) == 1:
                child_depth = depth - 1
                for arg in pools[child_depth][arg_types[0]]:
                    pools[depth][return_type].add(make(op, arg))
                continue

            if len(arg_types) != 2:
                raise AssertionError(f"unsupported arity for {op.name}")

            type_a, type_b = arg_types
            for depth_a in range(depth):
                for depth_b in range(depth):
                    if max(depth_a, depth_b) != depth - 1:
                        continue

                    for a in pools[depth_a][type_a]:
                        for b in pools[depth_b][type_b]:
                            if op in COMMUTATIVE_OPS:
                                if a.canonical_serialize() > b.canonical_serialize():
                                    continue
                            pools[depth][return_type].add(make(op, a, b))

    nodes: List[Node] = []
    for depth in range(max_depth + 1):
        for value_type in ValueType:
            nodes.extend(pools[depth][value_type])

    # Sets make construction order arbitrary; the returned universe is a
    # deterministic canonical sequence for reproducible assays and fixtures.
    return sorted(nodes, key=lambda node: node.canonical_serialize())
