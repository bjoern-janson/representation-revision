# test_generators.py
from boolean_world.generators import enumerate_universe

def test_enumeration():
    universe = enumerate_universe(d=4, max_depth=1)
    print(f"Total enumerated canonical generators (depth <= 1): {len(universe)}")

    # Print a small sample
    for i, g in enumerate(universe[:10]):
        print(f"[{i}] Type: {g.type.name} | AST: {g.canonical_serialize()}")

if __name__ == "__main__":
    test_enumeration()
