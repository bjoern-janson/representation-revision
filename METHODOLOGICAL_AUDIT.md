# Methodological Audit of the Frozen Accessibility Ladder

**Status:** POST-HOC / NON-AUTHORIZING  
**Scope:** v1 accessibility, v2 resistance robustness, v3 structural-complexity control  
**Authority:** documentation of scope properties only

This audit was written after the historical v1-v3 objects were frozen. It does not amend a preregistration, rerun an assay, replace a recorded result, or authorize a new scientific rung.

## Permanent rule

```text
post-hoc audit finding != retroactive protocol mutation
```

The correct use of this document is to sharpen what the historical measurements do and do not establish.

## Audit finding 1 — labeled full profiles contain forced self-coordinate separation

For resistance family `k`, the v1-v3 full outgoing profile of representation `G_i` is the ordered vector

`P_i(r) = R_k(G_i, G_r)`

over the complete labeled 77-member destination universe.

All three frozen resistance implementations satisfy `R_k(G_i, G_i) = 0`. For distinct canonical ASTs in these implementations, a structural difference incurs positive cost. Therefore for any distinct `i` and `j`:

```text
P_i(i) = 0        while P_j(i) > 0
P_j(j) = 0        while P_i(j) > 0
```

Consequently the full-profile Hamming divergence used in v3 obeys

`D_k(i,j) >= 2`

for every distinct pair under the three frozen families.

### Effect on interpretation

The binary event `D_k > 0`, and therefore a `759/759` count of distinct labeled full profiles among 759 distinct semantic-equivalent pairs, is partly identity-anchored by the profile coordinate system itself. It should not be treated as an independent surprise that every distinct source has a different labeled full profile.

This observation does **not** imply that the full resistance profiles are meaningless. Their divergence magnitude, thresholded reachable sets, and variation beyond the forced self coordinates remain separate measured quantities. In particular, v1's `755/759` thresholded reachable-set separation is not forced by the same argument, and v3's preregistered decision depends on within-stratum variation in `D_k`, not merely on `D_k > 0`.

## Audit finding 2 — v3 conditions on pairwise `|Delta z|`, not absolute complexity identity

The frozen v3 preregistration defines the exact stratum key as the componentwise absolute pairwise difference

`|z(G_i) - z(G_j)|`.

The implementation first restricts the primary analysis to semantic-equivalent pairs and then groups those pairs solely by that difference vector. The stratum key does not additionally encode:

- the semantic-class identifier shared by `G_i` and `G_j`; or
- the unordered absolute pair `{z(G_i), z(G_j)}`.

Therefore the exact v3 result should be read as the preregistration itself states it:

> Within the semantic-equivalent pair population, `D_k` is not a deterministic function of the declared pairwise structural-complexity difference vector alone.

It is not equivalent to exact matching on semantic-class identity plus both absolute complexity vectors.

### Effect on interpretation

This narrows how the phrase "exact structural-complexity control" should be paraphrased, but it does not invalidate the frozen v3 adjudication at its actual preregistered claim ceiling.

## Audit finding 3 — the three v2 resistance families share a structural-edit ontology

`R_v1`, `R_unit`, and `R_depth` are materially different cost conventions, but they are not three ontologically independent geometries.

All operate on the same canonical AST representation and share the broad construction:

- equality gives zero cost;
- inputs receive index/substitution treatment;
- root/type/arity incompatibilities trigger subtree replacement-style cost;
- compatible non-input nodes are recursively aligned by canonical child position;
- differences accumulate through structural edits.

The principal changes are cost weighting and directionality conventions, including unit costs and hierarchy/depth weighting.

### Effect on interpretation

v2 supports robustness across three preregistered resistance **cost constructions within a shared canonical-AST structural-edit family**. It weakens the hypothesis that only the original `R_v1` weighting produced the observed separation. It does not establish robustness across unrelated representation geometries or an intrinsic/natural geometry.

## Audit finding 4 — the profile destination universe mixes BIT and BOOL nodes

The frozen 77-member syntax fixture includes `INPUT(0)` and `INPUT(1)`, whose DSL type is `BIT`, alongside Boolean-valued expressions produced by `EQ`, `NEQ`, `NOT`, `AND`, `OR`, and `XOR`.

The resistance-profile measurements use all 77 syntax members as labeled destinations. Thus the measured outgoing geometry includes structural resistance from Boolean-valued source representations to the two BIT-valued input nodes as well as to BOOL-valued nodes.

### Effect on interpretation

This is a scope property of the frozen structural measurement convention. The historical assays do not claim that every measured source-destination pair is a typed executable trajectory step in a later temporal process. Any future trajectory experiment must define its own admissibility/type contract rather than silently inheriting "all 77 profile destinations" as valid temporal transitions.

This statement does not redesign `Gamma_t`; the current Gamma ledger remains open.

## What this audit does not do

This document does not:

- alter `ACCESSIBILITY_PREREGISTRATION.json`;
- alter `ACCESSIBILITY_ROBUSTNESS_PREREGISTRATION.json`;
- alter `ACCESSIBILITY_COMPLEXITY_PREREGISTRATION.json`;
- alter any recorded execution object;
- alter any resistance implementation;
- alter the frozen v3 scientific source;
- re-adjudicate v1, v2, or v3;
- establish a bridge assay;
- establish temporal organization `Gamma_t`;
- establish prediction, causation, adaptation, intrinsic geometry, or candidate-space expansion.

## Historical ladder after audit

The audit leaves the scientific ledger as:

```text
certified finite universe                         historical / frozen
v1 accessibility                                 historical / frozen
v2 resistance-cost robustness                    historical / frozen
v3 declared |Delta z| complexity-control result  historical / frozen
Gamma_t                                           OPEN / NOT FROZEN
```

The purpose of the audit is precision, not revision.
