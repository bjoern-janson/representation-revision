from boolean_world.ast import make
from boolean_world.generators import enumerate_universe
from boolean_world.types import Op, ValueType


def _reference_depths(d: int, max_depth: int):
    """Independent reference enumerator for the small bounded certification case."""
    pools = [{ValueType.BIT: set(), ValueType.BOOL: set()} for _ in range(max_depth + 1)]
    for index in range(d):
        pools[0][ValueType.BIT].add(make(Op.INPUT, index))

    for depth in range(1, max_depth + 1):
        for arg in pools[depth - 1][ValueType.BOOL]:
            pools[depth][ValueType.BOOL].add(make(Op.NOT, arg))

        for op in (Op.AND, Op.OR, Op.XOR):
            for depth_a in range(depth):
                for depth_b in range(depth):
                    if max(depth_a, depth_b) != depth - 1:
                        continue
                    for left in pools[depth_a][ValueType.BOOL]:
                        for right in pools[depth_b][ValueType.BOOL]:
                            if left.canonical_serialize() <= right.canonical_serialize():
                                pools[depth][ValueType.BOOL].add(make(op, left, right))

        if depth == 1:
            bits = sorted(pools[0][ValueType.BIT], key=lambda n: n.canonical_serialize())
            for op in (Op.EQ, Op.NEQ):
                for i, left in enumerate(bits):
                    for right in bits[i:]:
                        pools[depth][ValueType.BOOL].add(make(op, left, right))

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
    assert len(actual) == 77


def test_enumeration_is_deterministic_and_canonical():
    first = enumerate_universe(d=2, max_depth=2)
    second = enumerate_universe(d=2, max_depth=2)

    first_serialized = [node.canonical_serialize() for node in first]
    second_serialized = [node.canonical_serialize() for node in second]

    assert first_serialized == second_serialized
    assert first_serialized == sorted(first_serialized)
    assert len(first_serialized) == len(set(first_serialized))


def test_every_enumerated_node_is_well_typed():
    universe = enumerate_universe(d=3, max_depth=2)

    assert universe
    assert all(node.type in (ValueType.BOOL, ValueType.BIT) for node in universe)
    assert all(node.op in set(Op) for node in universe)
