# Representational Accessibility — v1

## Status

**Frozen design; implementation present; no future-prediction claim is made.**

This experiment is downstream of the certified Boolean universe and deliberately separate from the historical generator-revision execution and from the open-ended candidate-space expansion problem.

## Research question

For semantically equivalent representations in the certified finite universe, does semantic equivalence imply equivalence of representational transition geometry?

Formally:

```text
G_i ≡_semantic G_j  ?⇒  Geom(G_i) = Geom(G_j)
```

The negative result is the interesting case:

```text
G_i ≡_semantic G_j
and
Geom(G_i) ≠ Geom(G_j)
```

which would establish only that semantic identity does not exhaust transition identity under the declared resistance relation.

## Scope

The experiment uses only the frozen `certificate/U_syntax.json` universe and its verified semantic partition. The certified universe is exactly 77 canonical syntax members at `d=2`, `max_depth=2`, with 6 semantic classes.

No runtime regeneration or post-observation expansion of the universe is permitted.

The experiment does not test prediction, causal correction, agent learning, or open-ended representation discovery.

## Frozen resistance relation

The v1 relation is a deliberately primitive structural proxy over typed canonical ASTs:

```text
operator substitution       cost 1
input-index substitution    cost 1
node deletion               cost 1 per deleted subtree node
node insertion              cost 2 per inserted subtree node
```

For matching non-input roots, costs are accumulated recursively over corresponding canonical children. If the root kind/arity changes, the source subtree is deleted and the target subtree is inserted.

The unequal insertion/deletion costs make the relation directional in general:

```text
R(G_i → G_j) may differ from R(G_j → G_i).
```

This relation is a measurement convention, not a claim that it is an intrinsic or uniquely correct geometry of representation.

## Reachability

For a fixed threshold `τ`:

```text
A_i(τ) = { G_j : R(G_i → G_j) ≤ τ }
```

The current node is included because `R(G_i → G_i) = 0`.

The full outgoing profile

```text
R_i(j) = R(G_i → G_j)
```

is retained separately from thresholded reachability so that equal reachable sets do not hide different edge costs.

## Controls and ordering

The protocol is:

```text
1. freeze resistance specification
2. freeze threshold τ
3. verify and load literal certified U_syntax
4. compute full resistance profiles
5. derive thresholded reachable sets
6. load verified semantic partition
7. compare geometry within semantic classes
8. interpret only after the comparison is complete
```

The resistance specification must not be chosen or modified after inspecting the semantic-class result.

## Outcome classes

### Geometry invariant

For a semantic-equivalent pair:

```text
R_i = R_j
```

and therefore their thresholded neighborhoods are identical.

### Cost-geometry divergence without threshold divergence

```text
R_i ≠ R_j
but
A_i(τ) = A_j(τ)
```

This indicates different weighted transition structure even when a chosen threshold hides the difference.

### Reachability divergence

```text
A_i(τ) ≠ A_j(τ)
```

This is the strongest v1 result because semantically equivalent current representations have different cheaply reachable representational futures under the frozen relation.

## Claim ceiling

A positive v1 result supports only:

> Within the certified finite Boolean universe, semantic equivalence does not necessarily imply equivalence of transition accessibility under the preregistered structural resistance relation.

It does **not** establish that the resistance relation is natural, that accessibility predicts future outcomes, that accessibility is causally relevant to behavior, or that the finite universe is complete over representation space.

## Permanent boundary

```text
candidate evaluation ≠ candidate generation
revision within U_t ≠ expansion of U_t
certified U_t ≠ complete representation space
```

The open-ended discovery problem remains separate:

```text
U_t → evidence of inadequacy → U_{t+1} ⊃ U_t
```
