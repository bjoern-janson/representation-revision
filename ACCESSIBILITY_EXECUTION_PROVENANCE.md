# Representational Accessibility v1 — Execution Provenance

## Status

The preregistered v1 accessibility comparison has now been executed on the frozen literal 77-member Boolean syntax universe.

The preregistration itself remains unchanged and retains its original status: `frozen_before_accessibility_execution`.

## Execution object

- Universe: `certificate/U_syntax.json`
- Syntax members: 77
- Semantic classes: 6
- Threshold: `tau = 3`
- Resistance specification: operator substitution 1; input-index substitution 1; node deletion 1 per node; node insertion 2 per node
- Resistance construction: future-blind and semantic-label-blind; no future outcomes were used
- Candidate-space regeneration: none
- Candidate-space expansion: none

## Observed result

There are 759 unordered pairs of semantically equivalent syntax members.

- Full outgoing resistance profiles differ for **759 / 759** semantically equivalent pairs.
- Thresholded reachable sets at `tau = 3` differ for **755 / 759** semantically equivalent pairs.
- The remaining **4 / 759** pairs have different weighted resistance profiles but the same thresholded reachable set at `tau = 3`.

Across all 5,852 ordered non-identical syntax pairs, the resistance relation is asymmetric for 1,884 pairs (32.1941216678058%).

Thresholded reachable-set sizes at `tau = 3` range from 2 to 51, with mean 31.64935064935065 across the 77 current representations.

## Interpretation

The preregistered alternative is supported:

> Within the certified finite Boolean universe, semantic equivalence does not imply equivalence of outgoing transition geometry under the preregistered structural resistance relation.

The stronger secondary observation is also supported:

> At `tau = 3`, semantically equivalent representations can have different thresholded reachable sets.

## Claim ceiling

This execution does **not** establish that the structural resistance relation is intrinsic or uniquely correct. It does not test future prediction, causal correction, behavioral consequences, open-ended representation discovery, or completeness over representation space.

The result is therefore a finite, relation-relative statement about the certified Boolean universe.

## Provenance

The certified universe remains bound to source commit `df450d91d0b3acdd1c0937bd5d8b20bda98b20b4` and the existing certificate hashes.

The recorded execution artifact is `RECORDED_ACCESSIBILITY_EXECUTION.json`.
Its canonical JSON SHA-256 is:

`c7cce848ebfcd064c4579085ffd4980ade0e27e9f18e9c1dcf4cbf1120a7ecc8`
