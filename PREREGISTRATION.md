# L2 Representation-Revision Assay — Preregistration

**Status:** frozen before recorded scientific execution.

## Primary question
Does corrective evidence cause persistent revision of the representation generator itself?

## Frozen causal object
`RRA(S,e,G,U_rev) -> (G', pi, E_disc)` where `U_rev` is the frozen revision universe.

## Declared revision universe
`U_rev = {g0_surface, g1_complete, g2_redundant}`.

- `g0_surface`: retains only x0.
- `g1_complete`: retains x0 and x1.
- `g2_redundant`: retains x0 and OR(x0,x1).

Membership is fixed independently of the current generator. No post-outcome candidate expansion is permitted.

## Toy task
Inputs are two binary features `(x0, x1)`. Target is `y = x0 XOR x1`. A representation is sufficient when equal representations never correspond to different target values over the declared diagnostic domain.

## Discrimination
The probe pool is fixed to `(0,0), (0,1), (1,0), (1,1)`. Candidate subsets are searched exhaustively, deterministically, by increasing subset size then lexical combination order. Selection requires exactly one candidate to be sufficient on the selected probes.

## Adoption
The RRA result is one of `{current generator, unique supported successor, null}`. Null means insufficient evidence for a unique supported successor within the declared revision universe.

## Coverage status
Coverage is recorded separately from scientific result and may be `certified-complete`, `bounded-partial`, or `unknown`. `certified-complete` means complete for the explicitly declared finite universe only; it does not mean complete over all conceivable generator designs.

## Hypothesis
`g0_surface` is generator-inadequate on the diagnostic domain; `g1_complete` will be uniquely selected within the frozen universe.

## Primary success criterion
Persistent generator revision must be behaviorally observable on held-out future inputs: there exists a future input d such that the adaptive generator and fixed g0 shadow produce non-equivalent representations.

The adaptive and shadow branches receive exactly identical future `(S,e)` pairs.

## Exclusions
This assay makes no L3 claim. No revision-learning rule is itself adapted.
