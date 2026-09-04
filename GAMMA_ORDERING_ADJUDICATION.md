# Γ Ordering v1 — Adjudication

**Status:** `SUPPORTED / FROZEN`  
**Scientific rung:** `Γ_t` ordering / adjacency assay  
**Preregistration commit:** `05f718cba12194a42c1578f790081cc9016a151f`  
**Scientific-source commit:** `389969e510446450684402be3c1df4ececcf0ed7`  
**Custody run:** GitHub Actions `33844036424`  
**Custody job:** `100931989081`  
**Artifact ID:** `9925862074`

This document adjudicates only the result of the frozen Γ ordering v1 assay. It does not amend the preregistration, implementation, v1–v3 results, or the certified universe.

## 1. Pre-outcome freeze

The scientific sequence was:

```text
open Γ ledger
→ freeze exact temporal object / statistic / null / controls / failure rule / claim ceiling
→ freeze implementation and custody workflow
→ run full repository tests
→ execute certified Γ assay once
→ hash and archive raw result
→ inspect / adjudicate
```

The preregistered primary rule was:

```math
\boxed{\text{common_positive_motifs}>0}
```

where a common-positive motif is the **same** center-plus-three-leaf motif whose six exact `S3` orderings produce nonconstant `Q_k` under all three frozen resistance families `R_v1`, `R_unit`, and `R_depth`.

The preregistered failure condition was:

```math
\boxed{\text{common_positive_motifs}=0.}
```

Neither rule was changed after execution.

## 2. Execution and custody

The scientific-source checkout was exactly:

```text
389969e510446450684402be3c1df4ececcf0ed7
```

The GitHub Actions custody run used:

```text
OS:                 Ubuntu 24.04.4 LTS
runner image:       ubuntu-24.04 / 20260823.283.1
Python:             CPython 3.11.16
Git:                2.55.0
full test suite:    41 passed in 0.68s
```

Only after the test suite passed did the workflow execute:

```text
python run_gamma_ordering.py \
  --scientific-source 389969e510446450684402be3c1df4ececcf0ed7 \
  --output gamma-ordering-result.json
```

The workflow compared file output against stdout byte-for-byte before hashing and upload.

Raw observation SHA-256:

```text
abc55c8d63f055e9681b6feeef926f8bbe9e026368d974f3f0fbb18b70ca01f5
```

The independently downloaded artifact copy reproduced that exact SHA-256.

Uploaded artifact ZIP digest:

```text
sha256:888be3d02498d89233a2223cecf0bdb45328bcdabe42e08e9e2177ec104e63b5
```

The durable repository copy is `GAMMA_ORDERING_RESULT.json` and is byte-identical to the raw result object produced in the custody run.

## 3. Primary result

Frozen eligible motifs:

```text
116,664
```

Common-positive motifs across all three frozen resistance families:

```text
116,475
```

Therefore:

```math
\boxed{116475>0}
```

and the preregistered primary criterion is satisfied.

Machine result:

```text
primary_positive = true
```

The common-positive fraction is approximately `99.838%`. This prevalence is **descriptive only**: the preregistered decision rule was existential, not a prevalence threshold.

## 4. Per-family result

| Family | Order-sensitive motifs | D=1 | D=2 | D=3 | positive ΔQ min | median | max |
|---|---:|---:|---:|---:|---:|---:|---:|
| `R_v1` | 116,475 | 189 | 24,150 | 92,325 | 2 | 63 | 1,057 |
| `R_unit` | 116,475 | 189 | 24,150 | 92,325 | 2 | 63 | 598 |
| `R_depth` | 116,592 | 72 | 22,686 | 93,906 | 1 | 208.0 | 1,438 |

Here `D` is the number of distinct `Q_k` values over the six exact permutations. Because `Q_k` is reversal-invariant, `D≤3` by construction.

The common-positive count equals the full positive count of both `R_v1` and `R_unit`; thus every motif positive under those two families is also positive under `R_depth` in this frozen result. This is a descriptive set-containment fact of the exhaustive observation, not an additional preregistered hypothesis.

## 5. Deterministic earliest common witness

Center:

```text
AND(EQ(INPUT(0),INPUT(0)),EQ(INPUT(0),INPUT(0)))
```

Leaves:

```text
A = AND(EQ(INPUT(0),INPUT(0)),EQ(INPUT(1),INPUT(1)))
B = AND(EQ(INPUT(1),INPUT(1)),EQ(INPUT(1),INPUT(1)))
D = EQ(INPUT(0),INPUT(0))
```

For the six `S3` leaf orders, the frozen `Q_k` values occur in reversal-paired triples:

```text
R_v1:    887, 1630, 911, 1630, 911, 887      ΔQ = 743
R_unit:  497,  850, 521,  850, 521, 497      ΔQ = 353
R_depth: 1236, 2040, 1308, 2040, 1308, 1236 ΔQ = 804
```

The exact permutation labels and values are preserved in `GAMMA_ORDERING_RESULT.json`.

## 6. Adjudication

The frozen positive claim ceiling is earned exactly as preregistered:

> **Within the certified finite Boolean universe, there exists a semantically invariant, exactly transition-matched composable thread for which the preregistered second-order outgoing-profile displacement depends on transition ordering across all three frozen resistance conventions. Thus this measured quantity is not determined by the preserved directed transition multiset and declared static controls alone.**

The result is stronger descriptively than the existential criterion because the effect appears in 116,475 of 116,664 eligible motifs across the same three-family intersection. That frequency does **not** enlarge the claim ceiling.

## 7. Interpretation boundary

This assay establishes **ordering / adjacency sensitivity of the declared finite statistic**.

It does not establish directional temporal organization because:

```math
Q_k(\pi_1,\pi_2,\pi_3)=Q_k(\pi_3,\pi_2,\pi_1).
```

Therefore full sequence reversal leaves `Q_k` unchanged.

The result also does not show that a new dynamic state variable exists beyond the frozen static outgoing-profile geometry. `Q_k` is constructed from static profile distances plus an ordering operation. The narrow result is that the **transition multiset alone**, even with the frozen identity/reuse/static controls, does not determine this sequence functional without order.

No claim is earned about:

```text
arrow of time
causal efficacy
future prediction
learning or adaptation
beneficial correction
intrinsic / natural representational geometry
universal representation-space completeness
candidate-space expansion U_t -> U_(t+1)
future-relevant invariants I_t
open-ended representation invention
```

The three resistance families continue to share a broad canonical-AST structural-edit ontology. Cross-family agreement is therefore robustness within that declared family, not independent evidence for an intrinsic geometry.

## 8. Final frozen state

```text
Γ ordering v1 protocol             FROZEN
Γ ordering v1 scientific source    FROZEN
Γ ordering v1 execution            COMPLETE
Γ ordering v1 custody              FROZEN
Γ ordering v1 observation          FROZEN
Γ ordering v1 adjudication         SUPPORTED / FROZEN
```

No successor Γ statistic, directional assay, predictive interpretation, or new theoretical object is authorized by this adjudication.
