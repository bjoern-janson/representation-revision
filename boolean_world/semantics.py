# boolean_world/semantics.py
import itertools
from .types import Op
from .ast import Node

def evaluate(node: Node, x: tuple, ctx: int = 0) -> bool:
    """
    Pure deterministic evaluation of a canonical AST against an input vector.
    """
    if node.op == Op.INPUT:
        return bool(x[node.args[0]])
    if node.op == Op.CTX:
        return ctx

    # Evaluate children recursively
    args = [evaluate(arg, x, ctx) for arg in node.args]

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

    # For index-based relations (if implemented in the factory later)
    if node.op == Op.BEFORE:
        return args[0] < args[1]
    if node.op == Op.ADJACENT:
        return abs(args[0] - args[1]) == 1

    raise ValueError(f"Unknown operator in evaluation: {node.op}")

def get_semantic_id(node: Node, d: int = 4, ctx_domain: tuple = (0,)) -> str:
    """
    Calculates the exhaustive truth table for d bits.
    Returns a string of '0's and '1's representing the exact semantic signature.
    """
    results = []
    # Iterate over all possible contexts, then all possible bit vectors
    for c in ctx_domain:
        for x in itertools.product([0, 1], repeat=d):
            res = evaluate(node, x, ctx=c)
            results.append('1' if res else '0')

    return "".join(results)
