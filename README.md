# Representation Revision — L2 Causal Assay

This repository isolates a narrow empirical question:

> **Within a certified finite Boolean generator universe, can corrective evidence causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs?**

The repository is deliberately split between a **historical toy assay**, a **certified finite-universe operational assay**, and a **representational-accessibility assay**. The historical toy assay is executed evidence; the stronger operational causal assay remains unfired; the accessibility assay is now executed evidence from a separate preregistered finite test of transition structure that does not use future outcomes.

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

### Frontier guardrail

> **Candidate evaluation is not candidate generation.**

A frozen candidate space can certify selection and transition structure **within that space**. It cannot establish that the space contains every causally relevant representation.

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
 ├─────────────────────────────────────┐
 ↓                                     ↓
L2 operational causal assay            v1 representational accessibility
W/C/P/E                                R → A_t → geometry comparison
 ↓                                     ↓
held-out generator consequence         ✅ executed semantic-equivalence test
                                       ↓
                                       future navigation (not yet tested)

Open frontier: U_t → U_{t+1} (candidate-space expansion)
```

## Repository map

| Path | Role |
| --- | --- |
| [`ASSAY.md`](ASSAY.md) | Historical/operational assay protocol and causal boundaries |
| [`PREREGISTRATION.md`](PREREGISTRATION.md) | Frozen operational L2 preregistration |
| [`OPERATIONAL_PREREGISTRATION.json`](OPERATIONAL_PREREGISTRATION.json) | Machine-checkable W/C/P/E contract and stop rules |
| [`ACCESSIBILITY_PREREGISTRATION.json`](ACCESSIBILITY_PREREGISTRATION.json) | Frozen v1 accessibility resistance specification and claim ceiling |
| [`REPRESENTATIONAL_ACCESSIBILITY.md`](REPRESENTATIONAL_ACCESSIBILITY.md) | Accessibility assay protocol, controls, and outcome classes |
| [`RECORDED_ACCESSIBILITY_EXECUTION.json`](RECORDED_ACCESSIBILITY_EXECUTION.json) | Immutable v1 accessibility execution record |
| [`ACCESSIBILITY_EXECUTION_PROVENANCE.md`](ACCESSIBILITY_EXECUTION_PROVENANCE.md) | Accessibility execution provenance and claim ceiling |
| [`certificate/`](certificate/) | Frozen bounded universe, semantic quotient, and consume-side verifier |
| [`boolean_world/`](boolean_world/) | Typed AST, bounded reference implementation, and pure semantics |
| [`representation_revision/`](representation_revision/) | Historical three-generator toy assay plus accessibility primitives |
| [`PRECERTIFICATION.json`](PRECERTIFICATION.json) | Historical pre-certification checkpoint |
| [`RECORDED_EXECUTION.json`](RECORDED_EXECUTION.json) | Historical toy execution record |
| [`EXECUTION_PROVENANCE.md`](EXECUTION_PROVENANCE.md) | Historical provenance and claim ceiling |
| [`tests/`](tests/) | Regression, certificate, L2, and accessibility contract tests |
| [`.github/workflows/test.yml`](.github/workflows/test.yml) | Continuous pytest regression workflow |

## Frozen state model

The conceptual state decomposition is deliberately kept distinct:

```text
G_t       current representation
A_t       cheaply reachable representations
Γ_t       temporal organization of accessibility
I_t       future-relevant invariant
X_{>t}    future observations / transitions
```

A candidate representation dimension earns dynamic relevance only under intervention if varying it, with the relevant controls held fixed, changes transition accessibility. This is a criterion for **candidate dynamic relevance**, not a completeness criterion for representation space.

A separate resource coordinate may be tracked as `r_t`; no inference is made that more resources necessarily increase representational reach.

## Two distinct incompletenesses

```text
U_t-internal incompleteness
    candidate exists in U_t but is inaccessible, unselected, or non-persistent

U_t-external incompleteness
    the relevant candidate/dimension is not expressible in U_t at all
```

These require different interventions and must not inherit one another's evidential credit.

## Accessibility assay — executed result

The v1 accessibility experiment used the frozen, future-blind structural resistance relation over the literal certified 77-member syntax universe, with the preregistered threshold `τ = 3`.

The execution found:

```text
semantic-equivalent pairs:                       759
full resistance-profile divergence:              759 / 759
thresholded reachable-set divergence (τ = 3):   755 / 759
weighted divergence without set divergence:        4 / 759
```

Across all `77 × 76 = 5852` ordered non-identical syntax pairs, `1884` were asymmetric under the preregistered directed relation.

Therefore the preregistered alternative is supported:

> **Within the certified finite Boolean universe, semantic equivalence does not imply equivalence of outgoing transition geometry under the preregistered structural resistance relation.**

The stronger thresholded observation is also supported:

> **At `τ = 3`, semantically equivalent representations can have different thresholded reachable sets.**

This is a finite, relation-relative result. It does not establish that the resistance relation is intrinsic or uniquely correct, that accessibility predicts future outcomes, that accessibility causes behavior, or that the certified finite universe is complete over representation space.

The complete execution record and provenance are frozen in [`RECORDED_ACCESSIBILITY_EXECUTION.json`](RECORDED_ACCESSIBILITY_EXECUTION.json) and [`ACCESSIBILITY_EXECUTION_PROVENANCE.md`](ACCESSIBILITY_EXECUTION_PROVENANCE.md).

## Two distinct experimental frontiers

**Within-space:**

```text
U_t → R → A_t → Γ_t → I_t → held-out future
```

asks whether transition accessibility has structure and whether that structure later constrains future transitions.

**Space-expansion:**

```text
U_t → evidence of inadequacy → U_{t+1} ⊃ U_t
```

asks whether corrective evidence can generate a representation/candidate family that was not available as a candidate beforehand.

The second problem is deliberately not claimed by the first.

## Two distinct experimental objects

**Historical assay:** three hand-declared `GeneratorSpec` candidates. Its execution is retained unchanged as prior evidence.

**Operational assay:** 77 certified Boolean AST candidates partitioned into 6 semantic classes. It has a frozen certificate and preregistration, but no operational causal execution has been performed.

**Accessibility assay:** a frozen future-blind resistance relation over the same certified 77 syntax members. Its v1 execution is complete and tests whether semantic equivalence is sufficient to determine transition geometry. No future prediction or open-ended representation discovery is part of v1.

The operational certificate is **not** retrofitted into the historical result.

## Provenance

The authoritative scientific source baseline is [`main@df450d91`](https://github.com/bjoern-janson/representation-revision/commit/df450d91d0b3acdd1c0937bd5d8b20bda98b20b4).

The certificate-containing state derives from that baseline. The certificate records the source commit/tree and fixture hashes explicitly.

The accessibility execution record has canonical JSON SHA-256:

`c7cce848ebfcd064c4579085ffd4980ade0e27e9f18e9c1dcf4cbf1120a7ecc8`

## Local verification

The project targets Python 3.11+ and uses pytest:

```bash
python -m pytest
```

The certificate consumer verifies the certificate and literal fixtures without calling `enumerate_universe()` during consumption.

## Claim ceiling

The current repository establishes certified finite candidate-space infrastructure, a historical toy generator-revision demonstration, and an executed v1 accessibility result under the frozen structural resistance relation. The stronger operational causal proposition remains reserved for the unfired L2 assay, and the open-ended candidate-space-expansion problem remains outside the certified finite scope.

No claim is made here about arbitrary representation invention, universal representation completeness, consciousness, self-reference, recursion, general intelligence, or L3 adaptation.
