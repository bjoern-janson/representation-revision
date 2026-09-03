from __future__ import annotations

import hashlib
import itertools

from .ast import Node
from .types import Op


def evaluate(node: Node, x: tuple[int, ...]) -> bool:
    """Pure deterministic Boolean evaluation of a well-typed AST."""
    if node.op == Op.INPUT:
        index = node.args[0]
        return bool(x[index])

    args = [evaluate(arg, x) for arg in node.args]

    if node.op == Op.NOT:
        return not args[0]
    if node.op == Op.AND:
        return args[0] and args[1]
    if node.op == Op.OR:
        return args[0] or args[1]
    if node.op == Op.XOR:
        return bool(args[0]) != bool(args[1])
    if node.op == Op.EQ:
        return args[0] == args[1]
    if node.op == Op.NEQ:
        return args[0] != args[1]

    raise ValueError(f"Unknown operator in evaluation: {node.op}")


def semantic_signature(node: Node, d: int = 4) -> str:
    """Return the exhaustive truth-table signature over d Boolean inputs."""
    if d < 0:
        raise ValueError("d must be non-negative")
    results = []
    for x in itertools.product((0, 1), repeat=d):
        results.append("1" if evaluate(node, x) else "0")
    return "".join(results)


def semantic_id(node: Node, d: int = 4) -> str:
    """Return a stable content-derived identifier for the semantic signature."""
    signature = semantic_signature(node, d=d).encode("ascii")
    return hashlib.sha256(signature).hexdigest()
