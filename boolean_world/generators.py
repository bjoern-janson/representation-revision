# boolean_world/generators.py
from typing import Dict, List, Set, Tuple
from .types import Op, ValueType
from .ast import make, Node, SIGNATURES, COMMUTATIVE_OPS

def enumerate_universe(d: int = 4, max_depth: int = 2) -> List[Node]:
    """
    Exhaustively enumerates canonical, well-typed ASTs up to max_depth
    using a type-indexed, bottom-up dynamic programming approach.
    """
    # Structure: pools[depth][value_type] = set of canonical Nodes
    pools: List[Dict[ValueType, Set[Node]]] = [
        {vt: set() for vt in ValueType} for _ in range(max_depth + 1)
    ]

    # Depth 0: Base Leaves
    # 1. INPUT indices (0 to d-1) -> BIT
    for i in range(d):
        leaf = make(Op.INPUT, i)
        pools[0][leaf.type].add(leaf)

    # 2. CTX indices (e.g., context 0) -> CONTEXT
    ctx_leaf = make(Op.CTX, 0)
    pools[0][ctx_leaf.type].add(ctx_leaf)

    # Helper to fetch all available nodes up to a certain depth for a given type
    def get_nodes_up_to(d_max: int, v_type: ValueType) -> List[Node]:
        collected = set()
        for curr_d in range(d_max + 1):
            collected.update(pools[curr_d][v_type])
        return list(collected)

    # Bottom-up DP from depth 1 to max_depth
    for depth in range(1, max_depth + 1):
        for op, (arg_types, return_type) in SIGNATURES.items():

            # Case A: Unary Operators (e.g., NOT)
            if isinstance(arg_types, tuple) and len(arg_types) == 1:
                req_type = arg_types[0]
                # Sub-expression must have max depth such that 1 + sub_depth == depth
                sub_depth = depth - 1
                for arg in pools[sub_depth][req_type]:
                    try:
                        node = make(op, arg)
                        pools[depth][return_type].add(node)
                    except (TypeError, ValueError):
                        continue

            # Case B: Binary Operators (e.g., AND, EQ, BEFORE)
            elif isinstance(arg_types, tuple) and len(arg_types) == 2:
                type_a, type_b = arg_types

                # Iterate over possible depth combinations for left and right children
                for d_a in range(depth):
                    d_b = depth - 1  # Ensure exact target depth is hit by at least one branch
                    if max(d_a, d_b) != depth - 1:
                        continue

                    left_candidates = get_nodes_up_to(d_a, type_a)
                    right_candidates = get_nodes_up_to(d_b, type_b)

                    for a in left_candidates:
                        for b in right_candidates:
                            # Enforce commutative ordering key during generation to avoid duplicate permutations
                            if op in COMMUTATIVE_OPS:
                                if a.canonical_serialize() > b.canonical_serialize():
                                    continue
                            try:
                                node = make(op, a, b)
                                pools[depth][return_type].add(node)
                            except (TypeError, ValueError):
                                continue

    # Flatten the pools into a single unique list of canonical representation generators
    universe = []
    seen_serializers = set()
    for d in range(max_depth + 1):
        for vt in ValueType:
            for node in pools[d][vt]:
                ser = node.canonical_serialize()
                if ser not in seen_serializers:
                    seen_serializers.add(ser)
                    universe.append(node)

    return universe
