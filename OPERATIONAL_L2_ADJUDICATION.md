# Operational L2 v1 — Adjudication

**Status:** EXECUTED / STOPPED AT PREREGISTERED FIXED-TRIGGER GATE / FROZEN

This adjudication is downstream of the frozen v5 preregistration, the pre-execution implementation supplement, the scientific-source commit, and the one-shot custodied execution. It does not alter the protocol or authorize another draw.

## Authority chain

```text
frozen operational preregistration v5
2f577515fa2933833d6a50fcf37b9b53e0b31a57
        ↓
pre-execution supplement revision 2
80b5c48135c293c4c5b57a654d6936c6b3aa0607
        ↓
scientific source
c171a0095e6d0d98cac10c998911bc8e506c4d0d
        ↓
one-shot custody execution
run 33849068772
        ↓
raw observation freeze
a60c07ffc9bb787a04c129a67e145b25a25aaf5e
```

Raw result SHA-256:

`16b86262224dbf2ce6885bce7c4172d8ed1b1cd55280457c299eb28b696586a2`

Custody artifact:

- artifact ID: `9927624553`
- artifact ZIP SHA-256: `37f5a68e8f9da9631a7c21712319cbe46d8c88e43edee40e9bcab59bb0fb4ea2`
- scientific source: `c171a0095e6d0d98cac10c998911bc8e506c4d0d`
- full repository verification before execution: `48 passed in 0.70s`

## Frozen source-seeded specimen

The scientific-source SHA deterministically produced:

```text
target signature    1011
trigger index       3
trigger projection  (1,1)
```

The pre-trigger generator was frozen as:

```text
G0             INPUT(0)
G0 signature   0011
```

At the single source-seeded trigger probe `(1,1)`:

```text
G0 output      1
target output  1
```

Therefore the required corrective discrepancy was absent.

## Preregistered stop

The execution supplement prohibited scanning the four probes until a favorable discrepancy appeared. It required exactly one source-seeded trigger probe and specified:

```text
if target(trigger) == G0(trigger):
    STOP_NO_DISCREPANCY
```

That stop rule fired.

Observed trace:

```text
C_U          PASS
trigger      NO DISCREPANCY
diagnosis    NOT OPENED
T_t          EMPTY
G*           NOT SELECTED
C            NOT EVALUATED
W            NOT EVALUATED
P            NOT EVALUATED
E            NOT EVALUATED
primary      FALSE
```

This is a scientific stop, not a software failure. The workflow completed successfully, the repository tests passed before execution, the result/stdout byte comparison passed, the result was hashed, and the custody artifact was uploaded.

## Interpretation

The frozen v1 specimen does **not** support the positive operational L2 claim because the causal sequence never reached diagnosis, discriminating evidence, candidate selection, persistence, or held-out consequence.

It also does **not** establish that the downstream `C/W/P/E` burdens would fail conditional on a genuine discrepancy. They were not reached.

The earned statement is therefore:

> **In the first source-seeded operational L2 v1 specimen, the preregistered fixed trigger failed to produce a discrepancy between the frozen target and `G0`, so the assay stopped before diagnosis or candidate discrimination. No positive operational L2 result was obtained, and the downstream causal, change, persistence, and consequence burdens remain unevaluated in this specimen.**

## Permanent ceilings

This result does not establish or refute, in general:

- causal candidate selection conditional on a discrepancy;
- persistent representation revision;
- generator-specific held-out consequence;
- candidate-space expansion;
- arbitrary representation invention;
- `U_t -> U_(t+1)`;
- L3 adaptation or general intelligence.

The certified-universe boundary remains unchanged.

## Rerun boundary

**No automatic second seed, alternate trigger, or cherry-picked source commit is authorized.**

The first source-seeded draw is part of the scientific result. Replacing it because the trigger did not wound `G0` would convert the trigger gate into outcome-conditioned search.

A second execution would require a separately motivated and preregistered replication/sampling question with its own decision rule and authorization. It cannot be treated as a continuation of this one-shot specimen merely to reach the later gates.
