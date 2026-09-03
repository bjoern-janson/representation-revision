from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, Union

from .types import Op, ValueType


# Authoritative constructor signatures.
# INPUT is the only accessor: its raw integer argument is an input index,
# while the resulting AST node has value type BIT.
SIGNATURES = {
    Op.INPUT: ("INDEX_LITERAL", ValueType.BIT),
    Op.NOT: ((ValueType.BOOL,), ValueType.BOOL),
    Op.AND: ((ValueType.BOOL, ValueType.BOOL), ValueType.BOOL),
    Op.OR: ((ValueType.BOOL, ValueType.BOOL), ValueType.BOOL),
    Op.XOR: ((ValueType.BOOL, ValueType.BOOL), ValueType.BOOL),
    Op.EQ: ((ValueType.BIT, ValueType.BIT), ValueType.BOOL),
    Op.NEQ: ((ValueType.BIT, ValueType.BIT), ValueType.BOOL),
}

COMMUTATIVE_OPS = {Op.AND, Op.OR, Op.XOR, Op.EQ, Op.NEQ}


@dataclass(frozen=True)
class Node:
    op: Op
    args: Tuple[Union["Node", int], ...]
    type: ValueType

    def canonical_serialize(self) -> str:
        arg_strs = [
            arg.canonical_serialize() if isinstance(arg, Node) else str(arg)
            for arg in self.args
        ]
        return f"{self.op.name}({','.join(arg_strs)})"


def make(op: Op, *args: Union["Node", int]) -> Node:
    if op not in SIGNATURES:
        raise ValueError(f"Unknown operator: {op}")

    expected_arg_types, return_type = SIGNATURES[op]

    if op == Op.INPUT:
        if len(args) != 1 or not isinstance(args[0], int) or args[0] < 0:
            raise TypeError("INPUT requires one non-negative integer index")
        return Node(op=op, args=(args[0],), type=return_type)

    if len(args) != len(expected_arg_types):
        raise TypeError(
            f"{op.name} expects {len(expected_arg_types)} arguments, got {len(args)}"
        )

    for i, (arg, expected_type) in enumerate(zip(args, expected_arg_types)):
        if not isinstance(arg, Node) or arg.type != expected_type:
            actual_type = arg.type.name if isinstance(arg, Node) else type(arg).__name__
            raise TypeError(
                f"Argument {i} for {op.name} must be {expected_type.name}, got {actual_type}"
            )

    normalized_args = tuple(args)
    if op in COMMUTATIVE_OPS and len(args) == 2:
        a, b = args
        if a.canonical_serialize() > b.canonical_serialize():
            normalized_args = (b, a)

    return Node(op=op, args=normalized_args, type=return_type)


def parse_canonical(serialized: str) -> Node:
    """Parse the canonical serialization emitted by Node.canonical_serialize()."""

    text = serialized.strip()
    if not text:
        raise ValueError("empty canonical serialization")

    pos = 0

    def parse_node() -> Node:
        nonlocal pos
        start = pos
        while pos < len(text) and (text[pos].isalpha() or text[pos] == "_"):
            pos += 1
        if start == pos:
            raise ValueError(f"expected operator at offset {pos}")

        name = text[start:pos]
        try:
            op = Op[name]
        except KeyError as exc:
            raise ValueError(f"unknown operator {name!r}") from exc

        if pos >= len(text) or text[pos] != "(":
            raise ValueError(f"expected '(' after {name}")
        pos += 1

        args = []
        if pos < len(text) and text[pos] != ")":
            while True:
                if op == Op.INPUT:
                    start_num = pos
                    while pos < len(text) and text[pos].isdigit():
                        pos += 1
                    if start_num == pos:
                        raise ValueError("INPUT requires an integer index")
                    args.append(int(text[start_num:pos]))
                else:
                    args.append(parse_node())

                if pos < len(text) and text[pos] == ",":
                    pos += 1
                    continue
                break

        if pos >= len(text) or text[pos] != ")":
            raise ValueError(f"expected ')' for {name}")
        pos += 1
        return make(op, *args)

    node = parse_node()
    if pos != len(text):
        raise ValueError(f"unexpected trailing text at offset {pos}")
    return node
