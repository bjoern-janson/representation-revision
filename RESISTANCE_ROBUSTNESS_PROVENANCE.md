# Resistance Robustness Execution — v1

## Frozen question

> Does semantic-equivalent separation persist across independently justified resistance constructions?

No prediction, correction, candidate-space expansion, or `Γ_t`/future analysis is part of this rung.

## Frozen constructions

Three materially distinct structural resistance constructions were frozen before execution:

1. **R_v1** — the original preregistered directional structural convention: recursive canonical alignment, substitution cost 1, input-index substitution cost 1, deletion 1 per node, insertion 2 per node.
2. **R_unit** — unweighted unit-edit structural cost: substitution, insertion, and deletion all cost 1.
3. **R_depth** — hierarchy-weighted structural cost: local substitution and each node insertion/deletion cost increases with AST depth as `depth + 1`.

The family rationales, rules, parameters, and implementations are recorded in `ACCESSIBILITY_ROBUSTNESS_PREREGISTRATION.json`.

## Execution

The calculation was executed by GitHub Actions on commit `df7bdc7fb066c596d1944e9bd3731aefb601a43d`, using `scripts/run_resistance_robustness.py` in Python 3.11 CI.

Workflow run: `33764556701`

The script completed successfully before the subsequent repository regression suite. The later regression failure was a floating-point comparison in the pre-existing v1 accessibility provenance test; that assertion has since been replaced with a tolerance-based comparison and does not alter the scientific calculation.

## Result

The certified universe contains 77 syntax members in 6 semantic classes, giving 759 unordered semantic-equivalent pairs.

### Full outgoing profiles

```text
R_v1     |S_k_profile| = 759
R_unit   |S_k_profile| = 759
R_depth  |S_k_profile| = 759
```

Every one of the 759 semantic-equivalent pairs separates under every family.

Therefore:

```text
J_profile(R_v1, R_unit)  = 1.0
J_profile(R_v1, R_depth) = 1.0
J_profile(R_unit, R_depth)= 1.0
```

### Thresholded reachability, τ = 3

```text
R_v1     |S_k_reach| = 755
R_unit   |S_k_reach| = 755
R_depth  |S_k_reach| = 759
```

The separating sets for `R_v1` and `R_unit` are identical. Each has 755 pairs in common with `R_depth`, giving:

```text
J_reach(R_v1, R_unit)   = 1.0
J_reach(R_v1, R_depth)  = 0.994729907773386
J_reach(R_unit, R_depth) = 0.994729907773386
```

## Interpretation

The finite robustness result supports:

> **Within the certified finite Boolean universe, semantic-equivalent separation of outgoing transition geometry is not confined to the original `R_v1` resistance convention in this three-family assay.**

This weakens the explanation that the v1 phenomenon was created solely by one arbitrary cost convention.

It does **not** establish intrinsic or uniquely correct representation geometry. Nor does it establish future predictive value, behavioral causality, corrective accessibility, or completeness of the representation space.

## Frozen claim ceiling

```text
high cross-family stability
    => evidence against an R_v1-only artifact

high cross-family stability
    ≠ intrinsic geometry

low cross-family stability would instead have supported resistance-convention dependence.
```

The next rung remains separate from this one.
