# Operational L2-v1 — Main-Line Integration Record

**Status:** NON-SCIENTIFIC GOVERNANCE / CUSTODY INTEGRATION  
**Date:** 2026-09-04

This record documents the later integration of the closed Operational L2-v1 lineage into the public `main` history. It does not amend the preregistration, alter the scientific source, rerun the assay, change the frozen observation, re-adjudicate the result, expand the methodological characterization, authorize a second draw, or open L2-v2.

## Authorization

Operational L2-v1 was kept separate through preregistration, implementation freeze, one-shot execution, raw observation freeze, primary adjudication, post-hoc methodological characterization, and custody. After the specimen was explicitly closed as `EXECUTED / STOPPED / FROZEN`, main-line integration was authorized as a repository-governance operation.

## Integration shape

The integration commit has two historical parents:

```text
parent 1: current public main before L2 integration
  0f2856a89653f941c5bae60ec473205c6498552b

parent 2: verified L2-v1 custody/navigation head
  1e020c8c8c5bd71f52067b67ed8d583510a9c350
```

The merge commit is a routing/governance object, not a scientific-source identity.

## Scientific ancestry that must remain reachable

```text
2f577515fa2933833d6a50fcf37b9b53e0b31a57  operational preregistration
80b5c48135c293c4c5b57a654d6936c6b3aa0607  pre-execution supplement
c171a0095e6d0d98cac10c998911bc8e506c4d0d  scientific source
a60c07ffc9bb787a04c129a67e145b25a25aaf5e  raw observation freeze
65b2926ea977b1ec0790c7f52e2e44fffa269f7c  primary adjudication
eae168af0ea12389924076db97024b26fe025f2f  post-hoc methodological characterization
529f282291bf61ae3b8925059ccd6773480291c7  custody record
1e020c8c8c5bd71f52067b67ed8d583510a9c350  custody/navigation head
```

## Frozen scientific observation

```text
C_U                     PASS
D                       0
W                       NOT_EVALUATED
C                       NOT_EVALUATED
P                       NOT_EVALUATED
E                       NOT_EVALUATED
G*                      NOT_SELECTED
stop                     STOP_NO_DISCREPANCY
```

The correct closure remains:

> **No evidence for or against operational representation revision under W/C/P/E was obtained in L2-v1, because the preregistered discrepancy prerequisite was absent.**

And independently:

> **Candidate-space expansion `U_t -> U_(t+1)` remains completely untested and unestablished by L2-v1.**

## Custody bindings

```text
scientific Actions run            33849068772
scientific workflow run number    1
pre-execution repository tests    48 passed in 0.70s
artifact ID                       9927624553
artifact ZIP SHA-256              37f5a68e8f9da9631a7c21712319cbe46d8c88e43edee40e9bcab59bb0fb4ea2
raw result SHA-256                16b86262224dbf2ce6885bce7c4172d8ed1b1cd55280457c299eb28b696586a2
```

## Byte-preservation requirements

The following science-bearing L2 files are imported exactly from the verified custody/navigation head:

```text
.github/workflows/operational-l2.yml
OPERATIONAL_L2_EXECUTION_PROTOCOL.json
OPERATIONAL_L2_RESULT.json
OPERATIONAL_L2_ADJUDICATION.md
OPERATIONAL_L2_V1_METHODOLOGICAL_CHARACTERIZATION.md
OPERATIONAL_L2_V1_CUSTODY.md
representation_revision/operational_l2.py
run_operational_l2.py
tests/test_operational_l2.py
```

`README.md` and `RESEARCH_STATE.md` are explicitly governance/navigation files and were reconciled after scientific closure. Those documentation edits do not become new evidence.

## Workflow boundary

The frozen Operational L2-v1 custody workflow is branch-scoped:

```text
push branch = freeze-operational-l2-v1
```

and path-scoped to the scientific implementation/runner/workflow files. Therefore importing the frozen lineage onto `main` does not execute the scientific assay. Ordinary regression CI may run on the integration commit; that is repository verification only.

## Acceptance invariants

The integration is acceptable only if all of the following hold:

```text
ordinary CI passes on the staged two-parent integration commit
L2 scientific implementation blob unchanged
L2 raw-result blob unchanged
raw result SHA-256 remains 16b86262224dbf2ce6885bce7c4172d8ed1b1cd55280457c299eb28b696586a2
primary adjudication unchanged
post-hoc methodological characterization unchanged
scientific workflow run count remains 1
2f577515..., 80b5c481..., c171a009..., a60c07ff..., 65b2926e..., eae168af... remain ancestors
Gamma lineage and prior main custody remain reachable
second L2-v1 draw remains NOT AUTHORIZED
L2-v2 remains NOT OPENED
Gamma+1 remains NOT AUTHORIZED
U_t -> U_(t+1) remains UNESTABLISHED
```

## Scientific boundary after integration

```text
Operational L2-v1            EXECUTED / STOPPED / FROZEN
C_U                           PASS
D                             0
W/C/P/E                       NOT_EVALUATED
second draw                   NOT AUTHORIZED
L2-v2                         NOT OPENED
U_t -> U_(t+1)                UNESTABLISHED
```

Main-line integration improves discoverability and ancestry without reopening the science.
