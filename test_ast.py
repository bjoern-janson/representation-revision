import pytest

from boolean_world.ast import make, parse_canonical
from boolean_world.types import Op


def test_valid_construction_and_immutable_nodes():
    in0 = make(Op.INPUT, 0)
    in1 = make(Op.INPUT, 1)
    node = make(Op.EQ, in0, in1)

    assert node.type.name == "BOOL"
    assert node.canonical_serialize() == "EQ(INPUT(0),INPUT(1))"

    with pytest.raises((AttributeError, TypeError)):
        node.type = node.type


def test_type_firewall_rejects_illegal_operator_arguments():
    in0 = make(Op.INPUT, 0)
    in1 = make(Op.INPUT, 1)

    with pytest.raises(TypeError):
        make(Op.AND, in0, in1)


def test_commutative_normalization_is_canonical():
    in0 = make(Op.INPUT, 0)
    in1 = make(Op.INPUT, 1)

    eq_a = make(Op.EQ, in0, in1)
    eq_b = make(Op.EQ, in1, in0)

    assert eq_a == eq_b
    assert eq_a.canonical_serialize() == eq_b.canonical_serialize()


def test_canonical_serialization_round_trip():
    in0 = make(Op.INPUT, 0)
    in1 = make(Op.INPUT, 1)
    node = make(Op.XOR, make(Op.EQ, in0, in1), make(Op.NEQ, in0, in1))

    serialized = node.canonical_serialize()
    reparsed = parse_canonical(serialized)

    assert reparsed == node
    assert reparsed.canonical_serialize() == serialized


def test_parser_rejects_noncanonical_or_malformed_input():
    with pytest.raises(ValueError):
        parse_canonical("")
    with pytest.raises(ValueError):
        parse_canonical("UNKNOWN(INPUT(0))")
    with pytest.raises(ValueError):
        parse_canonical("INPUT(-1)")
