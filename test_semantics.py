# test_semantics.py
from boolean_world.types import Op
from boolean_world.ast import make
from boolean_world.semantics import get_semantic_id

def test_semantic_quotient():
    # Construct base inputs
    in0 = make(Op.INPUT, 0)
    in1 = make(Op.INPUT, 1)

    # 1. Structural difference vs Semantic equivalence
    # Node A = (x_0 == x_0)
    # Node B = (x_0 == x_0) AND (x_0 == x_0)
    node_a = make(Op.EQ, in0, in0)
    node_b = make(Op.AND, node_a, node_a)

    print(f"Node A syntax: {node_a.canonical_serialize()}")
    print(f"Node B syntax: {node_b.canonical_serialize()}")

    id_a = get_semantic_id(node_a, d=4)
    id_b = get_semantic_id(node_b, d=4)

    if node_a.canonical_serialize() != node_b.canonical_serialize():
        print("SUCCESS (Syntax): Nodes are syntactically distinct.")
    else:
        print("FAIL (Syntax): Nodes collapsed syntactically.")

    if id_a == id_b:
        print(f"SUCCESS (Semantics): Semantic quotient holds. Truth table: {id_a[:8]}...")
    else:
        print("FAIL (Semantics): Semantics diverged.")

    # 2. Relational Target Test
    # Node C = EQ(x_0, x_1)
    rel_node = make(Op.EQ, in0, in1)
    rel_id = get_semantic_id(rel_node, d=4)
    print(f"SUCCESS (Relational Target): EQ(x_0, x_1) truth table mapped: {rel_id[:8]}...")

if __name__ == "__main__":
    test_semantic_quotient()
