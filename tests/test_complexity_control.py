from __future__ import annotations

from boolean_world.ast import make
from boolean_world.types import Op, ValueType
from representation_revision.complexity_control import (
    ast_depth,
    ast_size,
    complexity_vector,
    pairwise_complexity_delta,
    profile_hamming,
    profile_l1,
)


def test_leaf_size_and_depth() -> None:
    x0 = make(Op.INPUT, 0)
    assert ast_size(x0) == 1
    assert ast_depth(x0) == 0
    assert complexity_vector(x0) == (1, 0, 1, 0, 0, 0, 0, 0, 0)


def test_recursive_size_and_depth() -> None:
    x0 = make(Op.INPUT, 0)
    x1 = make(Op.INPUT, 1)
    node = make(Op.AND, x0, make(Op.NOT, make(Op.NOT, x1)))
    assert node.type == ValueType.BOOL
    assert ast_size(node) == 5
    assert ast_depth(node) == 3
    assert complexity_vector(node) == (5, 3, 2, 2, 1, 0, 0, 0, 0)


def test_pairwise_delta_is_orientation_invariant() -> None:
    x0 = make(Op.INPUT, 0)
    x1 = make(Op.INPUT, 1)
    assert pairwise_complexity_delta(x0, x1) == pairwise_complexity_delta(x1, x0)


def test_profile_distances() -> None:
    left = (0, 1, 2, 2)
    right = (0, 3, 2, 5)
    assert profile_hamming(left, right) == 2
    assert profile_l1(left, right) == 5
