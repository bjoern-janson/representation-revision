from __future__ import annotations

from .types import GeneratorSpec, Representation


def _pair(state: tuple[int, ...]) -> tuple[int, int]:
    if len(state) != 3 or any(bit not in (0, 1) for bit in state):
        raise ValueError("toy assay expects exactly three binary event coordinates")
    return state[0], state[1]


def surface_only(state, evidence=()):
    x0, _ = _pair(state)
    return Representation("g0_surface", (x0,))


def interaction_complete(state, evidence=()):
    x0, x1 = _pair(state)
    return Representation("g1_complete", (x0, x1))


def redundant_surface(state, evidence=()):
    x0, x1 = _pair(state)
    return Representation("g2_redundant", (x0, x0 | x1))


G0 = GeneratorSpec("g0_surface", "Retains only x0; diagnostic/future mode bit is ignored.", surface_only)
G1 = GeneratorSpec("g1_complete", "Retains x0 and x1; diagnostic/future mode bit is ignored.", interaction_complete)
G2 = GeneratorSpec("g2_redundant", "Retains x0 and OR(x0,x1); diagnostic/future mode bit is ignored.", redundant_surface)
