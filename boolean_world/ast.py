# boolean_world/ast.py
from dataclasses import dataclass
from typing import Tuple, Any
from .types import Op, ValueType

# The authoritative signature table
SIGNATURES = {
    Op.INPUT: (ValueType.INDEX, ValueType.BIT),
    Op.CTX: (ValueType.INDEX, ValueType.CONTEXT),
    Op.NOT: ((ValueType.BOOL,), ValueType.BOOL),
    Op.AND: ((ValueType.BOOL, ValueType.BOOL), ValueType.BOOL),
    Op.OR:  ((ValueType.BOOL, ValueType.BOOL), ValueType.BOOL),
    Op.XOR: ((ValueType.BOOL, ValueType.BOOL), ValueType.BOOL),
    Op.EQ:  ((ValueType.BIT, ValueType.BIT), ValueType.BOOL),
    Op.NEQ: ((ValueType.BIT, ValueType.BIT), ValueType.BOOL),
    Op.BEFORE: ((ValueType.INDEX, ValueType.INDEX), ValueType.BOOL),
    Op.ADJACENT: ((ValueType.INDEX, ValueType.INDEX), ValueType.BOOL),
}

COMMUTATIVE_OPS = {Op.AND, Op.OR, Op.XOR, Op.EQ, Op.NEQ}

@dataclass(frozen=True)
class Node:
    op: Op
    args: Tuple[Any, ...]
    type: ValueType

    def canonical_serialize(self) -> str:
        if not self.args:
            return self.op.name
        arg_strs = [a.canonical_serialize() if isinstance(a, Node) else str(a) for a in self.args]
        return f"{self.op.name}({','.join(arg_strs)})"

def make_leaf(value: int, target_type: ValueType) -> Any:
    # A tiny wrapper for raw integers (indices)
    return value

def make(op: Op, *args) -> Node:
    if op not in SIGNATURES:
        raise ValueError(f"Unknown operator: {op}")
    
    sig = SIGNATURES[op]
    
    # Handle accessors (INPUT, CTX) which take raw integers as arguments
    if op in (Op.INPUT, Op.CTX):
        expected_arg_type, return_type = sig
        if not isinstance(args[0], int):
            raise TypeError(f"{op.name} requires an integer index.")
        return Node(op=op, args=(args[0],), type=return_type)

    # Handle combinatorial operators
    expected_arg_types, return_type = sig
    if len(args) != len(expected_arg_types):
        raise TypeError(f"{op.name} expects {len(expected_arg_types)} arguments, got {len(args)}")
    
    for i, (arg, expected_type) in enumerate(zip(args, expected_arg_types)):
        if not isinstance(arg, Node) or arg.type != expected_type:
            actual_type = arg.type.name if isinstance(arg, Node) else type(arg).__name__
            raise TypeError(f"Argument {i} for {op.name} must be {expected_type.name}, got {actual_type}")

    # Commutative normalization
    normalized_args = list(args)
    if op in COMMUTATIVE_OPS and len(args) == 2:
        if args[0].canonical_serialize() > args[1].canonical_serialize():
            normalized_args = [args[1], args[0]]

    return Node(op=op, args=tuple(normalized_args), type=return_type)
