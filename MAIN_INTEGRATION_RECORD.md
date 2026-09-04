# Main-Line Integration Record

**Status:** NON-SCIENTIFIC GOVERNANCE / CUSTODY INTEGRATION  
**Date:** 2026-09-04

This record documents the later integration of the closed Γ lineage into the public `main` history. It does not amend a preregistration, rerun an assay, re-adjudicate a result, expand a claim ceiling, or authorize successor science.

## Authorization

The scientific Γ lineage was first kept separate during design, execution, adjudication, post-hoc explanation, and closure. After Γ was explicitly frozen as a complete rung with `Γ+1 = NOT AUTHORIZED`, main-line integration was separately authorized as a repository-governance operation.

The earlier `SCIENTIFIC_CUSTODY_MANIFEST.json` is intentionally preserved byte-for-byte. Its `main_merge_authorized: false` field records the state at the time that custody index was frozen and is not retroactively rewritten.

## Integration shape

The integration commit must have exactly two historical parents:

```text
parent 1: repaired main
  3dc4ee1749c0c884505d1b446e0ec0c91138a394

parent 2: frozen Gamma custody head
  ebe9d6e7d47003e8aa91197aa450609c37770156
```

The merge commit is a routing/governance object, not a scientific-source identity.

## Scientific ancestry that must remain reachable

```text
05f718cba12194a42c1578f790081cc9016a151f  Gamma preregistration freeze
389969e510446450684402be3c1df4ececcf0ed7  Gamma scientific source
0a648fad0ad3b23bfd4f9ecc4e8e3acaff4598ce  Gamma result/adjudication
18433568be5c8e211060f326140f8c6b4650e648  Gamma post-hoc algebraic explanation
ad46551e8ce4758e8608738007380a604e77eaf9  Gamma scientific closure
```

## Byte-preservation requirements

The following frozen Γ files are imported using the exact blob identities from `freeze-gamma-ordering-v1@ebe9d6e7d47003e8aa91197aa450609c37770156`:

```text
.github/workflows/gamma-ordering.yml
GAMMA_ORDERING_ADJUDICATION.md
GAMMA_ORDERING_PREREGISTRATION.json
GAMMA_ORDERING_RESULT.json
GAMMA_POSTHOC_ALGEBRAIC_CHARACTERIZATION.md
GAMMA_PREREGISTRATION.md
GAMMA_SCIENTIFIC_LEDGER.md
SCIENTIFIC_CUSTODY_MANIFEST.json
representation_revision/gamma_ordering.py
run_gamma_ordering.py
tests/test_gamma_ordering.py
```

The Γ design/plan records are also preserved from that head. Existing repaired-main v3 custody evidence, v2 clarification, methodological audit, generic CI, packaging, and repository-repair files are retained from `main` unless explicitly reconciled as governance text.

`README.md` and `RESEARCH_STATE.md` are intentionally reconciled as present-state navigation/governance documents. Their merge-time edits are not scientific evidence.

## Workflow boundary

The frozen Γ custody workflow is branch-scoped:

```text
push branch = freeze-gamma-ordering-v1
```

Therefore importing that workflow onto `main` does not execute Γ. Ordinary regression CI may run on integration/main commits; that is repository verification, not new scientific evidence.

## Acceptance invariants

The integration is acceptable only if all of the following hold:

```text
ordinary CI passes
Gamma implementation blob unchanged
Gamma result blob unchanged
Gamma result SHA-256 remains abc55c8d63f055e9681b6feeef926f8bbe9e026368d974f3f0fbb18b70ca01f5
Gamma post-hoc characterization blob unchanged
SCIENTIFIC_CUSTODY_MANIFEST.json blob unchanged
v3 durable evidence retained from repaired main
05f718..., 389969..., 0a648f..., 184335..., ad4655... remain ancestors
Gamma scientific workflow is not re-executed by the integration
Gamma+1 remains NOT AUTHORIZED
candidate-space expansion remains UNESTABLISHED
```

## Scientific boundary after integration

```text
observation != explanation != causal interpretation != future authorization
```

and:

```text
Gamma supported / frozen
Gamma post-hoc explanation frozen / non-authority-expanding
orientation not established
causality not established
adaptation not established
Gamma+1 not authorized
U_t -> U_(t+1) unestablished
```

Main-line integration improves discoverability and ancestry without reopening the science.
