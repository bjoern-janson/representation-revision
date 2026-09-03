# Γ_t — Fresh Scientific Preregistration Ledger

**Status:** OPEN / NOT FROZEN  
**Scientific rung:** `Γ_t`  
**Purpose:** establish a new scientific object for testing whether an observed transition sequence contains directional or temporal organization beyond static transition geometry.

## Separation from v3

This document is a new scientific ledger. It is **not a v3 extension, amendment, or reinterpretation**.

The v3 scientific object remains historical and frozen. In particular:

```text
v3 protocol
v3 scientific source
v3 custody record
v3 observation
v3 adjudication
v3 claim ceiling
```

must not be changed by this rung.

The standing boundary is:

```math
\\boxed{\\text{residual transition structure}\\neq\\Gamma_t}
```

No temporal, directional, predictive, causal, or intrinsic interpretation is inherited from v3.

## Primary scientific question

> **Does an observed quantity depend on the ordering of transitions, rather than only on the multiset of those transitions?**

The conceptual object is an ordered transition thread:

```math
(\\Delta G_0,\\Delta G_1,\\ldots,\\Delta G_{T-1}).
```

A corresponding order-destroying transformation permutes the same transitions:

```math
(\\Delta G_{\\pi(0)},\\Delta G_{\\pi(1)},\\ldots,\\Delta G_{\\pi(T-1)}).
```

The permutation/null construction, statistic, matching constraints, and admissible sequence lengths are **not yet frozen here**. They must be specified before execution.

## Required preregistration components

The final frozen preregistration must independently specify:

1. **Temporal object:** exactly what constitutes a transition thread, its endpoints, ordering, length, and admissible transitions.
2. **Directional statistic:** a deterministic scalar or finite vector that is computed from the ordered thread.
3. **Ordering-destroying null:** a transformation that preserves the declared transition multiset and relevant marginals while destroying the ordering property under test.
4. **Static-geometry control:** an explicit control that distinguishes ordering effects from quantities already determined by static outgoing transition geometry.
5. **Null ensemble / comparison rule:** the exact finite comparison procedure, including all matching, stratification, or exhaustive enumeration rules.
6. **Failure condition:** a predeclared result under which the directional/temporal organization question is not supported.
7. **Claim ceiling:** the strongest finite statement that may be made if the preregistered criterion succeeds.
8. **Exclusions:** explicit prohibitions on prediction, causal correction, candidate-space expansion, intrinsic geometry, and generalization beyond the certified finite universe unless separately registered.

## Core falsifier

The central falsifier should operationalize the distinction:

```math
\\boxed{
\\text{same transition multiset} + \\text{different ordering}
\\not\\Rightarrow
\\text{same measured quantity}
}
```

A successful result must therefore survive the declared static-geometry controls and cannot be credited merely because different sequences contain different transitions.

## Provisional claim ceiling

No positive claim is currently registered beyond the following target form:

> **Within the declared finite experimental universe and under the preregistered controls, the measured quantity is sensitive to transition ordering rather than being fully determined by the preserved static transition multiset and declared static-geometry controls.**

This wording is **provisional** and becomes authoritative only after the complete protocol, statistic, null, controls, thresholds, and failure rule are frozen.

## Explicit exclusions

This rung does **not** by itself authorize claims about:

```text
future prediction
causal efficacy of correction
learning or adaptation
intrinsic / natural representational geometry
universal representation-space completeness
candidate-space expansion U_t → U_{t+1}
future-relevant invariants I_t
```

## Scientific ledger

```text
Protocol frozen                 ☐
Temporal object frozen          ☐
Directional statistic frozen   ☐
Ordering null frozen            ☐
Static-geometry control frozen ☐
Failure condition frozen       ☐
Claim ceiling frozen            ☐
Execution                        ☐
Custody                         ☐
Observation inspection          ☐
Adjudication                   ☐
```

Until all protocol elements are frozen, this document remains an **open design ledger** and no `Γ_t` result is established.