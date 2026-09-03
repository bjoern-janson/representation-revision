# Representation Revision — L2 Causal Assay

This repository isolates a narrow empirical question:

> **Within a certified finite Boolean generator universe, can corrective evidence causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs?**

The project is deliberately layered. It does not claim that behavioral change proves representation change, that representation change proves causal dependence on corrective evidence, or that either requires self-reference, recursion, or general intelligence.

## Research stack

```text
L0  Boolean ontology
 ↓
L1  bounded syntactic universe
 ↓
L1.5 semantic quotient
 ↓
🔒 frozen universe certificate
 ↓
operational verification / literal fixture loading
 ↓
L2 causal representation revision
 ↓
held-out generator consequence
```

The certificate freezes a 77-member canonical syntax universe and its 6-class semantic quotient for the declared Boolean DSL at `d=2`, `max_depth=2`. Its claim is bounded: complete over the declared DSL, not complete over all possible representations.

## Causal burden

The operational preregistration separates four evidential burdens:

```text
C_U  certified candidate universe
 W   what changed?                         G0 ≠ G1
 C   what caused the change?               evidence → discrimination → G1
 P   did the change persist?               G1 throughout H_post
 E   what did persistence cause?           G1-specific held-out consequence
```

The key non-equivalence guard is:

```text
behavioral equivalence ≠ mechanistic equivalence
```

So `ΔB` is never treated as sufficient evidence for `ΔG`.

## Repository map

| Path | Role |
| --- | --- |
| [`ASSAY.md`](ASSAY.md) | Causal assay protocol and boundaries |
| [`PREREGISTRATION.md`](PREREGISTRATION.md) | Frozen operational L2 preregistration |
| [`OPERATIONAL_PREREGISTRATION.json`](OPERATIONAL_PREREGISTRATION.json) | Machine-checkable W/C/P/E specification and stop rules |
| [`certificate/`](certificate/) | Frozen bounded universe, semantic quotient, and verifier |
| [`boolean_world/`](boolean_world/) | Typed AST, bounded enumerator, and pure semantics |
| [`representation_revision/`](representation_revision/) | Historical toy L2 assay implementation |
| [`PRECERTIFICATION.json`](PRECERTIFICATION.json) | Recorded pre-certification checkpoint |
| [`RECORDED_EXECUTION.json`](RECORDED_EXECUTION.json) | Recorded historical scientific execution |
| [`EXECUTION_PROVENANCE.md`](EXECUTION_PROVENANCE.md) | Provenance and discarded-rehearsal record |
| [`tests/`](tests/) | Regression and causal-contract tests |

## Two distinct finite-universe objects

The repository intentionally keeps two layers separate:

1. The historical toy assay uses its own three-generator `GeneratorSpec` universe so the previously recorded L2 result remains reproducible and unchanged.
2. The Boolean certificate freezes a mechanically enumerated bounded AST universe for the next, stronger operational assay.

The current certificate is therefore **not silently substituted into the historical assay**. Any future connection must be an explicit experimental change with its own preregistration and evidence.

## Provenance

The consolidated research baseline is [`main@df450d91`](https://github.com/bjoern-janson/representation-revision/commit/df450d91d0b3acdd1c0937bd5d8b20bda98b20b4).

The certificate-containing state derives from that baseline and records it explicitly. The later commits add the frozen certificate, operational preregistration, and consume-only verification layer; they do not rewrite the historical causal result.

## Local verification

The project targets Python 3.11+ and uses pytest. The intended verification command is:

```bash
pytest
```

The certificate consumer verifies the certificate self-hash, fixture hashes, source bindings, canonical syntax, semantic partition, and semantic identities before exposing the literal fixtures. It does **not** call `enumerate_universe()` during ordinary consumption.

## Claim ceiling

The central claim remains deliberately narrow:

> Corrective evidence can causally discriminate and persistently select a revised representation generator within a certified finite universe, with generator-specific held-out consequences under the declared controls.

That is an empirical L2 claim. It is not a claim of arbitrary representation invention, universal representation completeness, consciousness, self-reference, or L3 adaptation.
