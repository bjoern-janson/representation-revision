from itertools import combinations_with_replacement, product

from boolean_world.ast import make
from boolean_world.generators import enumerate_universe
from boolean_world.types import Op, ValueType


def _reference_depths(d: int, max_depth: int):
    """Small independent reference enumerator used only for bounded certification."""
    pools = [{ValueType.BIT: set(), ValueType.BOOL: set()} for _ in range(max_depth + 1)]
    for index in range(d):
        pools[0][ValueType.BIT].add(make(Op.INPUT, index))

    bool_unary = (Op.NOT,)
    bool_binary = (Op.AND, Op.OR, Op.XOR)
    bit_binary = (Op.EQ, Op.NEQ)

    def add_commutative(pool, op, lefts, rights):
        for a in lefts:
            for b in rights:
                pool.add(make(op, a, b))

    for depth in range(1, max_depth + 1):
        for op in bool_unary:
            for arg in pools[depth - 1][ValueType.BOOL]:
                pools[depth][ValueType.BOOL].add(make(op, arg))

        for op in bool_binary:
            children = []
            for da in range(depth):
                for db in range(depth):
                    if max(da, db) == depth - 1:
                        children.append((pools[da][ValueType.BOOL], pools[db][ValueType.BOOL]))
            for lefts, rights in children:
                add_commutative(pools[depth][ValueType.BOOL], op, lefts, rights)

        # EQ/NEQ have BIT children, so they only occur when the maximum child
        # depth is depth-1. BIT leaves exist only at depth 0 in this DSL.
        if depth == 1:
            for op in bit_binary:
                add_commutative(
                    pools[depth][ValueType.BOOL],
                    op,
                    pools[0][ValueType.BIT],
                    pools[0][ValueType.BIT],
                )

    return {
        node.canonical_serialize()
        for depth_pool in pools
        for typed_pool in depth_pool.values()
        for node in typed_pool
    }


def test_bounded_enumeration_matches_independent_reference():
    actual = {node.canonical_serialize() for node in enumerate_universe(d=2, max_depth=2)}
    expected = _reference_depths(d=2, max_depth=2)

    assert actual == expected
    assert len(actual) == 79


def test_enumeration_is_deterministic_and_canonical():
    first = enumerate_universe(d=2, max_depth=2)
    second = enumerate_universe(d=2, max_depth=2)

    assert [node.canonical_serialize() for node in first] == [
        node.canonical_serialize() for node in second
    ]
    assert [node.canonical_serialize() for node in first] == sorted(
        node.canonical_serialize() for node in first
    )

    serializations = [node.canonical_serialize() for node in first]
    assert len(serializations) == len(set(serializations))


def test_every_enumerated_node_is_well_typed():
    universe = enumerate_universe(d=3, max_depth=2)

    assert universe
    assert all(node.type in (ValueType.BOOL, ValueType.BIT) for node in universe)
    assert all(node.op in set(Op) for node in universe)
