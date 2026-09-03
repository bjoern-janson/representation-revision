# L2 Representation-Revision Assay — Preregistration v3

**Status:** frozen before the repaired scientific execution.

## Primary question
Does corrective evidence cause persistent revision of the representation generator itself?

## Frozen causal object
`RRA(S,e,G,U_rev) -> (G', pi, E_disc)` where `U_rev` is the frozen revision universe.

## Declared revision universe
`U_rev = {g0_surface, g1_complete, g2_redundant}`.

Membership is fixed independently of the current generator. No post-outcome candidate expansion is permitted.

## Toy task
Events are three binary coordinates `(x0, x1, mode)`. The target is `y = x0 XOR x1`; `mode` is an explicit held-out marker ignored by every candidate generator.

The corrective trigger is `(1,1,0)`. Under `g0_surface`, the representation contains only `x0`, so its declared toy decoder predicts `1`; the observed target is `0`. This observed discrepancy is the causal trigger for generator diagnosis.

After generator-failure is diagnosed from the trigger, the fixed follow-up probe pool `(1,0,0), (1,1,0)` is entered to discriminate the predeclared successor candidates. The follow-up pool is therefore downstream of the corrective event, but cannot expand the revision universe.

Held-out future events have `mode=1`, so the future event set is disjoint from the trigger and follow-up diagnostic probes.

## Candidate generators
- `g0_surface`: retains only `x0`.
- `g1_complete`: retains `x0` and `x1`.
- `g2_redundant`: retains `x0` and `OR(x0,x1)`.

## Discrimination
The fixed follow-up probe pool is searched exhaustively and deterministically, by increasing subset size then lexical combination order. Selection requires exactly one candidate to be sufficient on the selected probes.

## Adoption and persistence
The RRA result is one of `{current generator, unique supported successor, null}`. Null means insufficient evidence for a unique supported successor within the declared revision universe.

The selected `GeneratorSpec` is the persistent adaptive generator state carried unchanged into held-out future evaluation. The shadow retains the initial `g0_surface` generator.

## Coverage status
Coverage is reported separately as `certified-complete`, `bounded-partial`, or `unknown`. Here `certified-complete` means complete for the explicitly declared finite universe only; it does not imply completeness over all conceivable generator designs.

## Primary success criterion
Persistent generator revision must be behaviorally observable on held-out future events: at least one held-out future event must produce a representation non-equivalent to that produced by the fixed `g0_surface` shadow.

The adaptive and shadow branches receive exactly identical future `(S,e)` pairs.

## Causal criterion
The intended positive signature is:

`corrective discrepancy e_t -> generator-failure diagnosis pi_t -> selected persistent G1 != G0 -> future representational divergence.`

The diagnosis must consume the observed trigger discrepancy; it may not be established solely from a preloaded diagnostic universe.

## Exclusions
This assay makes no L3 claim. No revision-learning rule is itself adapted. No candidate-universe expansion is allowed after outcome observation.
