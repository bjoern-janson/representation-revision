# Operational L2 v1 — Scientific Custody Record

**Status:** EXECUTED / STOPPED / FROZEN

This is a non-scientific custody/navigation record for the first operational L2 v1 execution. It indexes the already-frozen scientific source, execution, raw observation, primary adjudication, and post-hoc methodological characterization without rewriting any of them or authorizing L2-v2.

## Frozen authority chain

```text
operational preregistration
2f577515fa2933833d6a50fcf37b9b53e0b31a57
        ↓
pre-execution supplement
80b5c48135c293c4c5b57a654d6936c6b3aa0607
        ↓
scientific source
c171a0095e6d0d98cac10c998911bc8e506c4d0d
        ↓
one-shot scientific execution
Actions run 33849068772
        ↓
raw observation freeze
a60c07ffc9bb787a04c129a67e145b25a25aaf5e
        ↓
primary adjudication
65b2926ea977b1ec0790c7f52e2e44fffa269f7c
        ↓
post-hoc methodological characterization
eae168af0ea12389924076db97024b26fe025f2f
```

## Execution custody

```text
scientific workflow run number      1
pre-execution repository tests      48 passed in 0.70s
result/stdout comparison            byte-for-byte match
GitHub Actions artifact ID          9927624553
artifact ZIP SHA-256                37f5a68e8f9da9631a7c21712319cbe46d8c88e43edee40e9bcab59bb0fb4ea2
raw result SHA-256                  16b86262224dbf2ce6885bce7c4172d8ed1b1cd55280457c299eb28b696586a2
```

The scientific implementation/workflow bytes were not changed after the one-shot outcome. The two post-result commits froze the raw observation and primary adjudication; the later methodological characterization is explicitly post-hoc and non-authority-expanding.

## Frozen one-shot specimen

```text
target signature    1011
G0                  INPUT(0)
G0 signature        0011
fixed trigger       (1,1)

target(1,1)         1
G0(1,1)             1
D                   0
```

The preregistered stop therefore fired:

```text
STOP_NO_DISCREPANCY
```

and the scientific burden state is:

```text
C_U                     PASS
D                       0
W                       NOT_EVALUATED
C                       NOT_EVALUATED
P                       NOT_EVALUATED
E                       NOT_EVALUATED
G*                      NOT_SELECTED
```

No second seed, alternate trigger, or outcome-conditioned probe is authorized by this frozen specimen.

## Methodological characterization

The later note [`OPERATIONAL_L2_V1_METHODOLOGICAL_CHARACTERIZATION.md`](OPERATIONAL_L2_V1_METHODOLOGICAL_CHARACTERIZATION.md) is:

```text
FROZEN / POST-HOC / NON-AUTHORITY-EXPANDING
```

It records the methodological distinction:

```text
implemented != available != authorized != observed
```

and the estimand firewall:

```text
Pr(D = 1 | frozen exposure rule)
    !=
1[ exists x in X such that D(x) = 1 ]
```

The note does not authorize a new draw or any successor assay.

## Public status

```text
Operational L2-v1
    EXECUTED / STOPPED / FROZEN

C_U                     PASS
D                       0
W/C/P/E                 NOT_EVALUATED
second draw             NOT AUTHORIZED
L2-v2                   NOT OPENED
U_t -> U_(t+1)          UNESTABLISHED
```

## Scientific ceiling

The L2-v1 specimen provides:

> No evidence for or against operational representation revision under W/C/P/E in L2-v1, because the preregistered discrepancy prerequisite was absent.

Independently:

> `U_t -> U_(t+1)` remains completely untested and unestablished.

A future discrepancy-incidence design would be a new scientific object requiring its own preregistration, sampling distribution, stopping rule, estimand, and authorization. Even a successful future W/C/P/E result inside frozen `U` would not establish candidate-space expansion.

## Integration boundary

Main-line integration is a governance/custody event only. It does not rerun the scientific workflow, amend the frozen observation, re-adjudicate the result, or authorize L2-v2.
