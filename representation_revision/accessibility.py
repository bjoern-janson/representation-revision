from __future__ import annotations

from dataclasses import dataclass

from boolean_world.ast import Node


@dataclass(frozen=True)
class ResistanceSpec:
    """Frozen structural resistance parameters.

    The relation is deliberately a primitive measurement convention for the
    finite assay. It is not claimed to be an intrinsic metric of representation.
    Costs are future-blind and depend only on the source/target AST structure.
    """

    operator_substitution_cost: int = 1
    input_index_substitution_cost: int = 1
    node_deletion_cost: int = 1
    node_insertion_cost: int = 2

    def __post_init__(self) -> None:
        if any(
            value < 0
            for value in (
                self.operator_substitution_cost,
                self.input_index_substitution_cost,
                self.node_deletion_cost,
                self.node_insertion_cost,
            )
        ):
            raise ValueError("resistance costs must be non-negative")


DEFAULT_RESISTANCE_SPEC = ResistanceSpec()


def node_size(node: Node) -> int:
    """Return the number of AST nodes in ``node``."""

    total = 1
    for arg in node.args:
        if isinstance(arg, Node):
            total += node_size(arg)
    return total


def _replace_subtree_cost(source: Node, target: Node, spec: ResistanceSpec) -> int:
    return (
        node_size(source) * spec.node_deletion_cost
        + node_size(target) * spec.node_insertion_cost
    )


def resistance(
    source: Node,
    target: Node,
    spec: ResistanceSpec = DEFAULT_RESISTANCE_SPEC,
) -> int:
    """Return deterministic directed structural resistance ``source -> target``.

    Same-root operators are aligned recursively. If root arity/kind changes,
    the source subtree is deleted and the target subtree is inserted. Input
    indices have their own substitution cost. Canonical AST ordering is already
    enforced by ``boolean_world.ast.make``.

    This is intentionally a *proxy relation*, not a claim of natural geometry.
    """

    if source == target:
        return 0

    source_is_input = source.op.name == "INPUT"
    target_is_input = target.op.name == "INPUT"

    if source_is_input and target_is_input:
        source_index = source.args[0]
        target_index = target.args[0]
        if source_index == target_index:
            return 0
        return spec.input_index_substitution_cost

    if source_is_input or target_is_input:
        return _replace_subtree_cost(source, target, spec)

    if len(source.args) != len(target.args):
        return _replace_subtree_cost(source, target, spec)

    cost = 0
    if source.op != target.op:
        cost += spec.operator_substitution_cost

    for source_arg, target_arg in zip(source.args, target.args):
        if not isinstance(source_arg, Node) or not isinstance(target_arg, Node):
            return _replace_subtree_cost(source, target, spec)
        cost += resistance(source_arg, target_arg, spec)

    return cost


def accessibility(
    current: Node,
    universe: tuple[Node, ...],
    tau: int,
    spec: ResistanceSpec = DEFAULT_RESISTANCE_SPEC,
) -> tuple[Node, ...]:
    """Return the thresholded reachable set from ``current``.

    The current representation itself is included because its resistance is 0.
    Results are returned in the universe's supplied deterministic order.
    """

    if tau < 0:
        raise ValueError("tau must be non-negative")

    return tuple(
        candidate
        for candidate in universe
        if resistance(current, candidate, spec) <= tau
    )


def resistance_profile(
    current: Node,
    universe: tuple[Node, ...],
    spec: ResistanceSpec = DEFAULT_RESISTANCE_SPEC,
) -> tuple[int, ...]:
    """Return the full ordered outgoing resistance profile from ``current``."""

    return tuple(resistance(current, candidate, spec) for candidate in universe)


def outgoing_profile_by_serialization(
    current: Node,
    universe: tuple[Node, ...],
    spec: ResistanceSpec = DEFAULT_RESISTANCE_SPEC,
) -> tuple[tuple[str, int], ...]:
    """Return ``(canonical serialization, resistance)`` pairs for audit output."""

    return tuple(
        (candidate.canonical_serialize(), resistance(current, candidate, spec))
        for candidate in universe
    )
