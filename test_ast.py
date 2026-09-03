# test_ast.py
from boolean_world.types import Op
from boolean_world.ast import make

def test_infrastructure():
    # 1. Test Valid Construction
    idx0 = make(Op.INPUT, 0) # Returns BIT
    idx1 = make(Op.INPUT, 1) # Returns BIT
    valid_eq = make(Op.EQ, idx0, idx1) # Expects (BIT, BIT) -> Returns BOOL
    print(f"Valid Construction: {valid_eq.canonical_serialize()}")

    # 2. Test Type Rejection (The Firewall)
    try:
        # BEFORE expects (INDEX, INDEX), but we pass it BITs
        invalid_before = make(Op.BEFORE, idx0, idx1)
        print("FAIL: Type system allowed a semantic breach.")
    except TypeError as e:
        print(f"SUCCESS (Rejected correctly): {e}")

    # 3. Test Commutative Normalization
    eq_a = make(Op.EQ, idx0, idx1)
    eq_b = make(Op.EQ, idx1, idx0) # Flipped arguments
    
    if eq_a.canonical_serialize() == eq_b.canonical_serialize():
        print(f"SUCCESS (Commutative Canonicalization): Both became {eq_a.canonical_serialize()}")
    else:
        print("FAIL: Commutative nodes remained syntactically distinct.")

if __name__ == "__main__":
    test_infrastructure()
