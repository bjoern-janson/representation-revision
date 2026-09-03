# Representation Revision — L2 Causal Assay

This repository isolates a narrow empirical question:

> **Within a certified finite Boolean generator universe, can corrective evidence causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs?**

The repository is deliberately split between a **historical toy assay** and a **stronger operational assay**. The former is executed evidence; the latter is certified infrastructure plus a frozen preregistration and remains unfired.

## Permanent epistemic guardrails

### Candidate-space guardrail

> **Complete over the declared DSL does not imply complete over all possible representations.**

The frozen certificate certifies only the declared Boolean DSL at `d=2`, `max_depth=2`, with its stated canonicalization policy.

### Mechanistic guardrail

> **Behavioral equivalence does not imply mechanistic equivalence.**

Therefore:

```text
ΔB  ↛  ΔG  ↛  Cause(e, ΔG)  ↛  ΔG-specific held-out consequence
```

A behavioral change is not sufficient evidence of generator change; generator change is not sufficient evidence that corrective evidence caused it; and neither establishes a generator-specific held-out consequence by itself.

## Research stack

```text
L0  Boolean ontology
 ↓
L1  bounded syntactic universe (77 members)
 ↓
L1.5 semantic quotient (6 classes)
 ↓
🔒 frozen universe certificate
 ↓
consume-side verification / literal fixture loading
 ↓
L2 operational causal assay (W/C/P/E)
 ↓
held-out generator-specific consequence
```

## Repository map

| Path | Role |
| --- | --- |
| [`ASSAY.md`](ASSAY.md) | Assay protocol and causal boundaries |
| [`PREREGISTRATION.md`](PREREGISTRATION.md) | Frozen operational L2 preregistration |
| [`OPERATIONAL_PREREGISTRATION.json`](OPERATIONAL_PREREGISTRATION.json) | Machine-checkable W/C/P/E contract and stop rules |
| [`certificate/`](certificate/) | Frozen bounded universe, semantic quotient, and consume-side verifier |
| [`boolean_world/`](boolean_world/) | Typed AST, bounded reference implementation, and pure semantics |
| [`representation_revision/`](representation_revision/) | Historical three-generator toy assay |
| [`PRECERTIFICATION.json`](PRECERTIFICATION.json) | Historical pre-certification checkpoint |
| [`RECORDED_EXECUTION.json`](RECORDED_EXECUTION.json) | Historical toy execution record |
| [`EXECUTION_PROVENANCE.md`](EXECUTION_PROVENANCE.md) | Historical provenance and claim ceiling |
| [`tests/`](tests/) | Regression and contract tests |

## Two distinct experimental objects

**Historical assay:** three hand-declared `GeneratorSpec` candidates. Its execution is retained unchanged as prior evidence.

**Operational assay:** 77 certified Boolean AST candidates partitioned into 6 semantic classes. It has a frozen certificate and preregistration, but no operational causal execution has been performed.

The operational certificate is **not** retrofitted into the historical result.

## Provenance

The authoritative scientific source baseline is [`main@df450d91`](https://github.com/bjoern-janson/representation-revision/commit/df450d91d0b3acdd1c0937bd5d8b20bda98b20b4).

The certificate-containing state derives from that baseline. The certificate records the source commit/tree and fixture hashes explicitly.

## Local verification

The project targets Python 3.11+ and uses pytest:

```bash
pytest
```

The certificate consumer verifies the certificate and literal fixtures without calling `enumerate_universe()` during consumption.

## Claim ceiling

The current repository establishes certified finite candidate-space infrastructure and a historical toy generator-revision demonstration. The stronger causal proposition is reserved for the unfired operational assay:

> **Within the certified finite Boolean generator universe, corrective evidence can causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs under the declared shadow, compensation, leakage, and universe controls.**

No claim is made here about arbitrary representation invention, universal representation completeness, consciousness, self-reference, recursion, general intelligence, or L3 adaptation.
