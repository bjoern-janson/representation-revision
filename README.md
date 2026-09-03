# Representation Revision — L2 Causal Assay

This repository isolates a narrow empirical question:

> **Within a certified finite Boolean generator universe, can corrective evidence causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs?**

The repository is deliberately split between a **historical toy assay**, a **certified finite-universe operational assay**, and a new **representational-accessibility assay**. The historical toy assay is executed evidence; the stronger operational causal assay is certified infrastructure plus a frozen preregistration and remains unfired. The accessibility assay is a separate, earlier finite test of transition structure and does not use future outcomes.

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
 ├───────────────────────────────┐
 ↓                               ↓
L2 operational causal assay     v1 representational accessibility
W/C/P/E                           R → A_t → geometry comparison
 ↓                               ↓
held-out generator consequence   semantic-equivalence test
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
| [`REPRESENTATIONAL_ACCESSIBILITY.md`](REPRESENTATIONAL_ACCESSIBILITY.md) | Accessibility assay protocol and outcome classes |
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

## Accessibility assay status

The v1 accessibility experiment uses a fixed, future-blind structural resistance relation over the literal certified 77-member syntax universe. It deliberately precedes any prediction experiment.

The protocol is:

```text
freeze R
 ↓
freeze τ
 ↓
verify literal certificate fixtures
 ↓
compute full directed resistance profiles
 ↓
derive A_i(τ)
 ↓
compare geometry within semantic classes
 ↓
interpret
```

A positive result would support only:

> **Within the certified finite Boolean universe, semantic identity does not necessarily exhaust transition accessibility under the frozen resistance relation.**

It would not establish that the resistance relation is intrinsic, that accessibility predicts future outcomes, or that the finite universe is complete over possible representations.

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

**Accessibility assay:** a frozen future-blind resistance relation over the same certified 77 syntax members. Its purpose is to test whether semantic equivalence is sufficient to determine transition geometry. No future prediction or open-ended representation discovery is part of v1.

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

The current repository establishes certified finite candidate-space infrastructure, a historical toy generator-revision demonstration, and a frozen v1 accessibility assay design. The stronger operational causal proposition remains reserved for the unfired assay, and the open-ended candidate-space-expansion problem remains outside the certified finite scope.

No claim is made here about arbitrary representation invention, universal representation completeness, consciousness, self-reference, recursion, general intelligence, or L3 adaptation.
