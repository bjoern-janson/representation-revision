from __future__ import annotations

from .types import GeneratorSpec, Representation


def _pair(state: tuple[int, ...]) -> tuple[int, int]:
    if len(state) != 2 or any(bit not in (0, 1) for bit in state):
        raise ValueError("toy assay expects exactly two binary input features")
    return state


def surface_only(state, evidence=()):
    x0, _ = _pair(state)
    return Representation("g0_surface", (x0,))


def interaction_complete(state, evidence=()):
    x0, x1 = _pair(state)
    return Representation("g1_complete", (x0, x1))


def redundant_surface(state, evidence=()):
    x0, x1 = _pair(state)
    return Representation("g2_redundant", (x0, x0 | x1))


G0 = GeneratorSpec("g0_surface", "Retains only the first binary feature.", surface_only)
G1 = GeneratorSpec("g1_complete", "Retains both binary features.", interaction_complete)
G2 = GeneratorSpec("g2_redundant", "Retains the first feature and its OR with the second.", redundant_surface)
