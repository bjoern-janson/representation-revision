# L2 Representation-Revision Assay — Preregistration v2

**Status:** frozen before valid recorded scientific execution. The earlier draft reused diagnostic states in its future set and was discarded as an invalid rehearsal; no result from that rehearsal is part of the scientific record.

## Primary question
Does corrective evidence cause persistent revision of the representation generator itself?

## Frozen causal object
`RRA(S,e,G,U_rev) -> (G', pi, E_disc)` where `U_rev` is the frozen revision universe.

## Declared revision universe
`U_rev = {g0_surface, g1_complete, g2_redundant}`.

Membership is fixed independently of the current generator. No post-outcome candidate expansion is permitted.

## Toy task
Events are three binary coordinates `(x0, x1, mode)`. The target is `y = x0 XOR x1`; `mode` is an explicit held-out marker ignored by every candidate generator.

Diagnostic events have `mode=0`. Held-out future events have `mode=1`, so the future event set is disjoint from the diagnostic event set.

A representation is sufficient when equal representations never correspond to different target values over the declared diagnostic domain.

## Candidate generators
- `g0_surface`: retains only `x0`.
- `g1_complete`: retains `x0` and `x1`.
- `g2_redundant`: retains `x0` and `OR(x0,x1)`.

## Discrimination
The diagnostic probe pool is fixed to `(0,0,0), (0,1,0), (1,0,0), (1,1,0)`. Candidate subsets are searched exhaustively and deterministically, by increasing subset size then lexical combination order. Selection requires exactly one candidate to be sufficient on the selected probes.

## Adoption
The RRA result is one of `{current generator, unique supported successor, null}`. Null means insufficient evidence for a unique supported successor within the declared revision universe.

## Coverage status
Coverage is reported separately as `certified-complete`, `bounded-partial`, or `unknown`. Here `certified-complete` means complete for the explicitly declared finite universe only; it does not imply completeness over all conceivable generator designs.

## Hypothesis
`g0_surface` is generator-inadequate on the diagnostic domain and `g1_complete` will be uniquely selected within the frozen universe.

## Primary success criterion
Persistent generator revision must be behaviorally observable on held-out future events: at least one held-out future event must produce a representation non-equivalent to that produced by the fixed `g0_surface` shadow.

The adaptive and shadow branches receive exactly identical future `(S,e)` pairs.

## Exclusions
This assay makes no L3 claim. No revision-learning rule is itself adapted. No candidate-universe expansion is allowed after outcome observation.
