# L2 Representation-Revision Assay — Preregistration v4

**Status:** frozen before operational execution.

## Primary question

Within a certified finite Boolean generator universe, can corrective evidence causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs?

## Non-equivalence guard

The assay does not infer mechanism from behavioral similarity:

`behavioral equivalence != mechanistic equivalence`

Therefore `ΔB` is not sufficient evidence for `ΔG`, and `ΔG` is not by itself sufficient evidence that corrective evidence caused the change.

## Certified universe boundary

The candidate universe is supplied by the frozen certificate at `certificate/certificate.json` and is not regenerated during assay execution. The certificate is the upstream invariant:

`U_rev = Load(VerifiedCertificate)`

No post-trigger or post-outcome universe expansion is permitted. Completeness is asserted only relative to the declared Boolean DSL, `d=2`, `max_depth=2`, and canonicalization policy recorded by the certificate.

Operational machine-checkable details are frozen in `OPERATIONAL_PREREGISTRATION.json`.

## Four evidential burdens

### C_U — What candidate space is actually licensed?

**Measurement:** verify the certificate, its self-hash, both fixture hashes, declared counts, canonical syntax, and semantic partition before exposing the fixtures.

**Acceptance:** 77 unique canonical syntax members and 6 semantic classes; every syntax member appears exactly once in exactly one semantic class.

**Failure:** hard stop. No causal L2 claim may be made from an uncertified universe.

### W — What changed?

**Measurement:** compare the persistent adaptive generator identity and its generator-interface outputs with the pre-trigger `G0` generator.

**Acceptance:** `G_adaptive = G1`, `G1 != G0`, and at least one held-out generator-interface output differs from the fixed `G0` shadow.

**Failure:** generator-level change was not established; downstream behavioral differences are not sufficient.

### C — What caused the generator change?

The intended causal sequence is:

`observed discrepancy -> diagnosis -> discriminating evidence T_t -> unique candidate G1 -> adoption`

**Temporal lock:** `T_t` and the trigger outcome must be generated without access to `G1` identity or any post-selection generator metadata.

**Acceptance:** the trigger discrepancy precedes diagnosis; diagnosis precedes follow-up evidence; follow-up evidence is evaluated before adoption; `T_t` uniquely discriminates `G1` within the frozen universe; candidate identity does not leak into evidence generation.

**Failure:** any leakage, temporal inversion, or non-unique discrimination defeats causal attribution to the discriminating evidence.

### P — Did the change persist?

**Measurement:** record the generator identity used at every post-adoption held-out evaluation.

**Acceptance:** for every `x` in `H_post`, the adaptive branch uses the same selected `G1`; there is no reversion, mutation, or hidden replacement.

**Failure:** temporary selection is not persistent representation revision.

### E — What did the persistent change cause?

**Measurement:** compare the persistent `G1` branch with both the fixed-`G0` shadow and a compensation condition that can pursue the same useful behavior without changing `G0`.

The preferred dependent variable is a **held-out generator consequence**, not merely a generic behavioral consequence.

**Acceptance:** the observed held-out consequence is specific to `G1` at the generator interface and survives the shadow and compensation controls.

**Failure:** equivalent useful behavior produced while `G0` remains unchanged is evidence for downstream compensation, not for generator-specific consequence.

## Hypotheses and controls

### Revision hypothesis

`H_revision: G_adaptive = G1, G1 != G0`

### Compensation hypothesis

`H_comp: G_adaptive = G0` while a separate compensation path `K` produces the relevant useful behavior.

The compensation condition exists to test whether apparent L2 success is merely downstream behavioral rescue.

### Shadow control

`H_shadow: G_shadow = G0` while adaptive and shadow branches receive exactly the same future input/evidence stream.

The shadow controls for ordinary treatment-independent drift and generic future-input effects. The compensation control attacks mechanistic non-identifiability.

## Stop rules

The experiment must terminate without a positive L2 interpretation if any of the following occurs:

1. certificate verification fails;
2. the candidate universe is regenerated or expanded after the trigger/outcome;
3. candidate identity leaks into trigger, outcome, or pre-adoption evidence generation;
4. discrimination is non-unique;
5. the selected generator is not persistent across `H_post`;
6. adaptive and shadow future event streams differ;
7. the compensation control reproduces the claimed consequence while `G0` remains unchanged.

## Current toy-task legacy assay

The existing frozen toy assay remains the historical positive control and is not silently upgraded by this preregistration. Its hand-declared toy universe and recorded execution are retained as prior evidence. The new operational assay must satisfy the stricter W/C/P/E specification above before stronger generator-causal claims are made.

## Claim ceiling

A successful operational run supports only the following bounded proposition:

> Within the certified finite Boolean generator universe, corrective evidence can causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs under the declared shadow, compensation, and leakage controls.

It does not establish self-reference, recursion, consciousness, general intelligence, arbitrary representation invention, or completeness beyond the certified DSL.

## Exclusions

This assay makes no L3 claim. The generator-revision rule is not itself adapted. No post-outcome candidate expansion is allowed. The certificate is an upstream object and is not altered by assay outcomes.
