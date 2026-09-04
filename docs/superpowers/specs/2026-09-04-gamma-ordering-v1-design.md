# Gamma Ordering v1 Design

**Date:** 2026-09-04  
**Approved intent:** execute the previously proposed minimal Γ ordering assay after freezing it.  
**Scientific parent:** `preregister-gamma-t-v0@e154cd7d791a23d40463fc513e64e3d7b798d845`

## Goal

Test whether a deterministic second-order outgoing-profile displacement changes when the same composable directed transition multiset is reordered.

## Architecture

Add one isolated module, `representation_revision/gamma_ordering.py`, which consumes the existing certified syntax/semantic fixtures and the three already-frozen resistance functions. It enumerates every eligible center-plus-three-leaf motif, exhausts all six leaf orders, computes the frozen `Q_k`, and returns a deterministic JSON-serializable summary. It does not mutate predecessor code or create a new representation generator.

Add one runner, `run_gamma_ordering.py`, that verifies the certificate fixtures, calls the assay exactly once, prints canonical JSON, and optionally writes that exact JSON to a path supplied by the caller.

## Scientific controls

Every permutation holds fixed:

- four representation identities;
- semantic class;
- center/leaf visit counts;
- start/end state;
- full directed transition multiset;
- all static outgoing profiles and pairwise resistance values;
- all structural-complexity properties of the participating nodes.

Only leaf order changes.

## Statistic

For family `k`:

```math
P_k(G)=(R_k(G,G_r))_{r=1}^{77}
```

```math
L_k(i,j)=\sum_r|P_k(i)_r-P_k(j)_r|
```

```math
Q_k(c,\pi_1,c,\pi_2,c,\pi_3,c)=L_k(\pi_1,\pi_2)+L_k(\pi_2,\pi_3).
```

All six `S3` orders are evaluated. A family-positive motif has more than one distinct Q. The primary positive requires one same motif positive under all three families.

## Reversal limitation

Because `L_k` is symmetric, `Q_k` is unchanged by full sequence reversal. This design tests ordering/adjacency, not directionality or an arrow of time.

## Error handling

The assay must fail closed if fixture counts differ from 77 syntax members / 6 semantic classes, if fixture membership is inconsistent, if an eligible motif does not yield exactly six unique permutations, or if any result is non-integer/non-deterministic.

## Testing

Unit tests use toy profile matrices and toy motif identities only; they may not inspect certified-universe Γ outcomes before scientific-source freeze. Predecessor-surface tests may reproduce already-known v2 counts. After implementation freeze, the scientific runner is executed against the certified fixtures and its raw JSON is hashed before interpretation.

## Output boundary

The result object reports counts, ΔQ summaries, and the lexicographically earliest common witness. It contains no causal, temporal-direction, learning, prediction, or candidate-generation interpretation.
