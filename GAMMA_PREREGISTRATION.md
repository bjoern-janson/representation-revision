# Γ_t — Frozen Ordering Preregistration v1

**Status:** `FROZEN / UNEXECUTED`  
**Scientific rung:** `Γ_t`  
**Parent open-ledger commit:** `e154cd7d791a23d40463fc513e64e3d7b798d845`  
**Scope:** finite ordering/adjacency assay only; no directional arrow-of-time claim.

This freeze closes the open design ledger before any Γ outcome is inspected. It does not modify or reinterpret v1–v3.

## 1. Primary question

> **Within a fixed composable transition inventory, can the preregistered measured quantity change when only the ordering of those transitions changes?**

The target separation is:

```math
\boxed{
\text{same directed transition multiset}
+
\text{different ordering}
\not\Rightarrow
\text{same }Q_k
}
```

This assay tests **ordering / adjacency sensitivity**. Because the statistic below is reversal-invariant, it does **not** test an arrow of time or directional asymmetry.

## 2. Frozen universe

Use the certified 77-member Boolean universe already present on the parent branch:

- `certificate/U_syntax.json` blob `a74165f547390a116caa47f0ea16679e54c025a8`
- `certificate/U_semantic.json` blob `dbeda59e6961eb7cc40672b8f336b1d62e8b793c`
- syntax members: `77`
- semantic classes: `6`
- class sizes: `[27, 1, 1, 12, 12, 24]`

Certification remains relative to the declared DSL. No representation-space completeness claim is inherited.

## 3. Frozen resistance families

Use exactly the three predecessor resistance constructions already frozen in v2/v3:

1. `R_v1` = `representation_revision.accessibility.resistance`
2. `R_unit` = `representation_revision.resistance_robustness.unit_resistance`
3. `R_depth` = `representation_revision.resistance_robustness.depth_resistance`

Relevant parent-branch blobs:

- `representation_revision/accessibility.py`: `0f15545056800775d1be1d0b412cbb153c4c3089`
- `representation_revision/resistance_robustness.py`: `59a50b4de372bdc7b4100707568d9c804ab89355`

These families share a broad canonical-AST structural-edit ontology. A cross-family result is therefore robustness within this declared family, not evidence for intrinsic geometry.

## 4. Temporal object

An eligible motif is:

```math
M=(c,\{a,b,d\})
```

such that:

- `c`, `a`, `b`, and `d` are four distinct certified syntax members;
- all four belong to the same certified semantic class;
- `c` is the center;
- `{a,b,d}` is an unordered 3-leaf set.

For each permutation `π=(π1,π2,π3)` of the three leaves, construct the composable seven-state thread:

```math
\Gamma_\pi=(c,\pi_1,c,\pi_2,c,\pi_3,c).
```

Its six directed transitions are:

```text
c -> π1
π1 -> c
c -> π2
π2 -> c
c -> π3
π3 -> c
```

Across all six `S3` permutations, the directed transition multiset is exactly:

```text
{c->a, a->c, c->b, b->c, c->d, d->c}
```

with every transition appearing once.

From the frozen semantic class sizes, the eligible motif count is fixed before execution as:

```math
\sum_s n_s\binom{n_s-1}{3}=116664.
```

## 5. Identity / reuse control

Every null thread preserves exactly:

- the same center identity `c`;
- center visit count = `4`;
- each leaf identity and leaf visit count = `1`;
- the same start state and end state (`c`);
- the same four participating representations;
- the same semantic class;
- the same directed transition multiset;
- the same complete static outgoing resistance profiles of all four representations;
- the same complete pairwise resistance matrix among the four representations for each family;
- the same complexity vectors of all four representations.

Thus different reuse counts, different participating identities, different endpoints, or different transition inventories cannot explain a within-motif Γ difference.

## 6. Frozen outgoing-profile displacement

For family `k`, define the full outgoing profile over the certified 77-member universe:

```math
P_k(G)=(R_k(G,G_r))_{r=1}^{77}.
```

Define symmetric profile displacement:

```math
L_k(i,j)=\sum_{r=1}^{77}|R_k(G_i,G_r)-R_k(G_j,G_r)|.
```

The destination universe intentionally remains the same mixed BIT/BOOL 77-member universe used by the predecessor profile assays. No new semantic interpretation is attached to that choice.

## 7. Frozen ordering statistic

For a seven-state thread `Γ=(G0,...,G6)`, define:

```math
\boxed{
Q_k(\Gamma)=\sum_{t=0}^{4}L_k(G_t,G_{t+2})
}
```

For the center-return excursion construction this simplifies exactly to:

```math
\boxed{
Q_k(\Gamma_\pi)=L_k(\pi_1,\pi_2)+L_k(\pi_2,\pi_3).
}
```

`Q_k` is integer-valued and deterministic.

Because `L_k` is symmetric:

```math
Q_k(\pi_1,\pi_2,\pi_3)=Q_k(\pi_3,\pi_2,\pi_1).
```

Therefore this statistic is **reversal-invariant**. At most three distinct `Q_k` values can occur over the six permutations. A positive result is an ordering/adjacency result, not a directionality result.

## 8. Exact ordering-destroying null

For every eligible motif, exhaust all `3! = 6` leaf permutations. There is no stochastic permutation sample and no p-value threshold.

For family `k`, define:

```math
D_k(M)=|\{Q_k(\Gamma_\pi):\pi\in S_3\}|.
```

A motif is order-sensitive under family `k` iff:

```math
\boxed{D_k(M)>1.}
```

Also report:

```math
\Delta Q_k(M)=\max_\pi Q_k(\Gamma_\pi)-\min_\pi Q_k(\Gamma_\pi).
```

## 9. Primary decision rule

Let:

```math
C=\{M:D_{v1}(M)>1\land D_{unit}(M)>1\land D_{depth}(M)>1\}.
```

**Positive criterion:**

```math
\boxed{|C|>0.}
```

**Failure criterion:**

```math
\boxed{|C|=0.}
```

The same motif must be order-sensitive under all three resistance constructions. Family-specific positives without a common motif do not satisfy the primary criterion.

## 10. Frozen reporting

Report, without changing the decision rule:

- eligible motif count;
- per-family order-sensitive motif count;
- common-positive motif count `|C|`;
- per-family counts for `D_k(M) in {1,2,3}`;
- per-family `ΔQ_k` minimum/median/maximum among positive motifs;
- one deterministic lexicographically earliest common witness, if one exists;
- its six permutation threads and exact `Q_k` values for all three families.

The witness is descriptive after the exhaustive primary result; it is not selected to define success.

## 11. Positive claim ceiling

If and only if `|C|>0`, the strongest authorized statement is:

> **Within the certified finite Boolean universe, there exists a semantically invariant, exactly transition-matched composable thread for which the preregistered second-order outgoing-profile displacement depends on transition ordering across all three frozen resistance conventions. Thus this measured quantity is not determined by the preserved directed transition multiset and declared static controls alone.**

The result would establish only order/adjacency sensitivity of this declared finite statistic.

## 12. Explicit exclusions

No result from this assay, positive or negative, establishes:

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

A positive result also does not show that order contains information beyond the complete static profile geometry plus the ordering operation; `Q_k` is constructed from those frozen profiles. The claim is specifically that the preserved transition multiset and declared static controls do not by themselves determine `Q_k` without order.

## 13. Execution gate

Before any certified-universe Γ outcome is inspected:

```text
Protocol frozen                 YES
Temporal object frozen          YES
Ordering statistic frozen       YES
Ordering null frozen            YES
Static / identity controls      YES
Failure condition frozen        YES
Claim ceiling frozen            YES
Execution                       NO
Observation inspection          NO
Adjudication                    NO
```

Any implementation tests executed before the scientific run must use toy fixtures or predecessor-result checks only; they may not inspect certified-universe Γ outcomes.
