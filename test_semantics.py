from boolean_world.ast import make
from boolean_world.semantics import semantic_id, semantic_signature
from boolean_world.types import Op


def test_semantic_quotient_distinguishes_syntax_from_meaning():
    in0 = make(Op.INPUT, 0)

    node_a = make(Op.EQ, in0, in0)
    node_b = make(Op.AND, node_a, node_a)

    assert node_a.canonical_serialize() != node_b.canonical_serialize()
    assert semantic_signature(node_a, d=4) == semantic_signature(node_b, d=4)
    assert semantic_id(node_a, d=4) == semantic_id(node_b, d=4)


def test_canonical_identity_implies_same_semantics():
    left = make(Op.EQ, make(Op.INPUT, 0), make(Op.INPUT, 1))
    right = make(Op.EQ, make(Op.INPUT, 1), make(Op.INPUT, 0))

    assert left.canonical_serialize() == right.canonical_serialize()
    assert semantic_signature(left, d=4) == semantic_signature(right, d=4)


def test_semantic_signature_is_exhaustive_and_stable():
    eq = make(Op.EQ, make(Op.INPUT, 0), make(Op.INPUT, 0))
    neq = make(Op.NEQ, make(Op.INPUT, 1), make(Op.INPUT, 1))
    node = make(Op.XOR, eq, neq)

    signature_a = semantic_signature(node, d=2)
    signature_b = semantic_signature(node, d=2)

    assert len(signature_a) == 4
    assert signature_a == signature_b
    assert len(semantic_id(node, d=2)) == 64
