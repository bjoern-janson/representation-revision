# Γ Ordering v1 — Post-hoc Algebraic Characterization

**Status:** `FROZEN / POST-HOC / NON-AUTHORITY-EXPANDING`  
**Scientific rung:** `Γ_t` ordering / adjacency assay  
**Preregistration freeze:** `05f718cba12194a42c1578f790081cc9016a151f`  
**Scientific source:** `389969e510446450684402be3c1df4ececcf0ed7`  
**Frozen result / adjudication commit:** `0a648fad0ad3b23bfd4f9ecc4e8e3acaff4598ce`

This document was written **after** execution and adjudication of Γ ordering v1. It does not amend the preregistration, statistic, decision rule, raw observation, primary adjudication, or claim ceiling. Its sole purpose is to characterize algebraically why the preregistered positive result occurs.

## 1. Frozen thread and statistic

For an eligible motif with center `c` and distinct leaves `a,b,d`, every null ordering has the form

```math
\Gamma=(c,a,c,b,c,d,c)
```

up to permutation of the three leaves.

The preregistered statistic for resistance family `k` is

```math
Q_k(\Gamma)=\sum_{t=0}^{4}L_k(G_t,G_{t+2}),
```

where

```math
L_k(i,j)=\sum_r\left|R_k(G_i,G_r)-R_k(G_j,G_r)\right|.
```

Although the underlying resistance relation `R_k` may be directed, `L_k` is symmetric by construction:

```math
L_k(i,j)=L_k(j,i).
```

## 2. Exact reduction

Substituting

```math
(G_0,\ldots,G_6)=(c,a,c,b,c,d,c)
```

into the frozen statistic gives

```math
\begin{aligned}
Q_k(\Gamma)
&=L_k(c,c)+L_k(a,b)+L_k(c,c)+L_k(b,d)+L_k(c,c)\\
&=L_k(a,b)+L_k(b,d).
\end{aligned}
```

Therefore

```math
\boxed{Q_k(a,b,d)=L_k(a,b)+L_k(b,d).}
```

The center contributes no nonzero term. The statistic is exactly the length, under the frozen static `L_k` relation, of the two-edge path whose middle leaf is `b`.

## 3. Exhaustive S3 values

Write

```math
\ell_{ab}=L_k(a,b),\qquad
\ell_{ad}=L_k(a,d),\qquad
\ell_{bd}=L_k(b,d).
```

Across all six permutations of the leaves, `Q_k` can take only the three reversal-paired values

```math
\begin{aligned}
q_a &= \ell_{ab}+\ell_{ad},\\
q_b &= \ell_{ab}+\ell_{bd},\\
q_d &= \ell_{ad}+\ell_{bd}.
\end{aligned}
```

Each value occurs for a forward/reverse pair because `L_k` is symmetric.

Thus

```math
\boxed{Q_k(a,b,d)=Q_k(d,b,a)}
```

and similarly for the other two reversal pairs.

## 4. Exact condition for Γ positivity

The three candidate path sums are all equal iff the three static pairwise distances are all equal.

If

```math
q_a=q_b=q_d,
```

then pairwise subtraction gives

```math
\ell_{ad}=\ell_{bd},\qquad
\ell_{ab}=\ell_{bd},
```

hence

```math
\ell_{ab}=\ell_{ad}=\ell_{bd}.
```

The converse is immediate.

Therefore:

```math
\boxed{
Q_k\text{ is nonconstant over }S_3
\iff
L_k(a,b),L_k(a,d),L_k(b,d)\text{ are not all equal}.
}
```

Equivalently, Γ ordering v1 is positive for family `k` exactly when the leaf triple is non-equilateral under the frozen static `L_k` relation.

## 5. Characterization of the frozen prevalence

The primary preregistered result remains existential:

```math
\boxed{\text{common_positive_motifs}>0.}
```

The frozen exhaustive observation found:

```text
eligible motifs        116,664
common-positive        116,475
R_v1 positive          116,475
R_unit positive        116,475
R_depth positive       116,592
```

The post-hoc reduction therefore characterizes the descriptive `116,475 / 116,664 ≈ 99.838%` common-positive frequency as follows:

> Almost every eligible motif is non-equilateral under each of the three declared `L_k` relations simultaneously.

This is descriptive characterization only. It does not replace or enlarge the preregistered existential endpoint.

## 6. Tightened interpretation

The preregistered result remains true:

```math
\boxed{
\text{fixed transition multiset} + \text{different ordering}
\not\Rightarrow
\text{same }Q_k.
}
```

The post-hoc reduction shows why:

```math
\boxed{
\text{static }L_k\text{ relation} + \text{ordering}
\Rightarrow
Q_k
}
```

exactly.

Accordingly, Γ does **not** require an additional temporal state variable or latent dynamic mechanism to explain the observed effect. The order operation selects which two static leaf-to-leaf distances are composed.

The strongest explanatory compression is therefore:

```math
\boxed{
\text{semantic equivalence}\centernot\Rightarrow\text{relational equivalence},
\qquad
\text{relational heterogeneity}+\text{ordered composition}
\Rightarrow
\text{order-sensitive functional}.
}
```

## 7. Permanent guardrail

The frozen interpretive ladder is:

```math
\boxed{
\begin{aligned}
\text{transition multiset} &\not\Rightarrow Q_k,\\
Q_k\text{ order-sensitive} &\not\Rightarrow \text{orientation},\\
\text{orientation} &\not\Rightarrow \text{causality},\\
\text{causality} &\not\Rightarrow \text{adaptation},\\
\text{adaptation} &\not\Rightarrow U_t\rightarrow U_{t+1}.
\end{aligned}
}
```

No claim is earned about arrow of time, causal efficacy, prediction, learning, adaptation, intrinsic geometry, candidate-space expansion, future-relevant invariants, or open-ended representation invention.

## 8. Closure

Γ ordering v1 is a complete scientific rung:

```text
preregistration
→ execution
→ frozen positive result
→ frozen adjudication
→ post-hoc algebraic explanation
→ claim ceiling tightened, not enlarged
→ STOP
```

No `Γ+1`, directional statistic, or successor temporal object is authorized by this characterization. A successor experiment requires an independently motivated scientific question rather than a desire to extract a stronger interpretation from Γ.
