# L2 Representation-Revision Assay — Preregistration v5

**Status:** frozen before operational execution.

## Primary question

Within a certified finite Boolean generator universe, can corrective evidence causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs?

## Permanent guardrails

**Candidate-space:** complete over the declared DSL does not imply complete over all possible representations.

**Mechanistic:** behavioral equivalence does not imply mechanistic equivalence. Therefore `ΔB` is not sufficient evidence for `ΔG`; `ΔG` is not by itself evidence that corrective evidence caused the change; and neither is sufficient evidence of a generator-specific held-out consequence.

## Certified universe boundary

The operational candidate universe is supplied only by the frozen certificate at `certificate/certificate.json`:

`U_rev = Load(VerifiedCertificate)`

The assay must not call `enumerate_universe()`, regenerate the universe, or expand it after trigger/outcome observation. Completeness is asserted only relative to the declared Boolean DSL, `d=2`, `max_depth=2`, and canonicalization policy recorded by the certificate.

## Four evidential burdens

### C_U — What candidate space is actually licensed?

**Measurement:** verify the certificate self-hash, fixture hashes, source bindings, bounded parameters, canonical syntax, and semantic partition before exposing the literal fixtures.

**Acceptance:** 77 unique canonical syntax members; 6 semantic classes; each syntax member appears exactly once in exactly one class.

**Negative/control:** any verification failure is a hard stop.

**Failure interpretation:** the candidate universe is not certified for this run; no causal L2 claim is permitted.

**Claim ceiling:** bounded completeness only for the certified Boolean DSL.

### W — What changed?

Let `G0` be the pre-trigger generator and `G*` the candidate actually selected by the evidence.

**Measurement:** compare persistent adaptive generator identity and generator-interface outputs with `G0` on held-out inputs.

**Acceptance:** `G* != G0`, the adaptive branch persistently uses `G*`, and at least one held-out generator-interface output differs from the fixed-`G0` shadow.

**Negative/control:** the shadow receives the identical future event/evidence stream and remains `G0`.

**Failure interpretation:** no generator-level change has been established; downstream behavioral differences cannot support the L2 claim.

**Claim ceiling:** generator-level divergence only; causal attribution remains unestablished.

### C — What caused the generator change?

The preregistered sequence is:

`observed discrepancy -> diagnosis -> discriminating evidence T_t -> unique candidate G* -> adoption`

**Temporal lock:** the trigger outcome and `T_t` must be generated and fixed without access to `G*` identity, selected-generator metadata, or any post-selection state.

**Acceptance:** discrepancy precedes diagnosis; diagnosis precedes follow-up evidence; follow-up evidence is evaluated before adoption; `T_t` uniquely identifies `G*` within the frozen universe; no selected-candidate identity leaks into trigger/outcome/evidence generation.

**Negative/control:** any leakage, temporal inversion, or non-unique discrimination is a causal-identification failure.

**Failure interpretation:** candidate selection may be contaminated or non-identifying; no claim that evidence caused the generator change.

**Claim ceiling:** corrective evidence can causally discriminate and select a candidate within the certified finite universe, subject to the declared controls.

### P — Did the change persist?

**Measurement:** record the generator identity used at every post-adoption held-out evaluation.

**Acceptance:** for every `x` in `H_post`, the adaptive branch uses the same selected `G*`; there is no reversion, mutation, or hidden replacement.

**Negative/control:** shadow remains `G0` throughout.

**Failure interpretation:** temporary candidate selection is not persistent representation revision.

**Claim ceiling:** persistent adoption of `G*`; no outcome claim follows from persistence alone.

### E — What did the persistent change cause?

**Measurement:** compare persistent `G*` against the fixed-`G0` shadow and a compensation condition that can pursue the same useful behavior while retaining `G0`.

The preferred dependent variable is a **G*-specific held-out generator consequence**, not merely a generic behavioral improvement.

**Acceptance:** the consequence is specific to `G*` at the generator interface and survives both shadow and compensation controls.

**Negative/control:** if compensation reproduces the claimed useful consequence while `G0` remains unchanged, the generator-specific interpretation fails.

**Failure interpretation:** the observation is explainable by downstream compensation or behavioral rescue rather than generator revision.

**Claim ceiling:** a persistent selected generator produces generator-specific consequences on held-out inputs under the declared controls.

## Hypotheses

### Revision

`H_revision: G_adaptive = G* and G* != G0`

`G*` is not fixed in advance; it is the unique candidate selected by the preregistered discriminating evidence, if one exists.

### Compensation

`H_comp: G_adaptive = G0` while a separate compensation path `K` produces the relevant useful behavior.

This tests whether apparent L2 success can be produced without the claimed representational mechanism.

### Shadow

`H_shadow: G_shadow = G0` with the adaptive and shadow branches receiving exactly the same future input/evidence stream.

## Controls

- **Universe control:** only the verified literal certificate fixtures are exposed; no runtime enumeration or post-outcome expansion.
- **Leakage control:** selected-candidate identity and post-selection metadata are unavailable to trigger/outcome/evidence generation.
- **Shadow control:** adaptive and shadow receive identical held-out streams; only persistent generator state differs.
- **Compensation control:** useful behavior is pursued while `G0` remains unchanged.

## Stop rules

The experiment terminates without a positive operational L2 interpretation if any of the following occurs:

1. certificate verification fails;
2. runtime enumeration or candidate-space expansion occurs;
3. candidate identity leaks into pre-adoption evidence generation;
4. discrimination is non-unique;
5. the selected generator is not persistent across `H_post`;
6. adaptive and shadow future event/evidence streams differ;
7. compensation reproduces the claimed consequence while `G0` remains unchanged.

A stop-rule failure is an epistemic disqualification of the run, not merely a software error.

## Historical toy assay

The existing three-generator toy assay remains separate historical evidence. Its `g0_surface`, `g1_complete`, and `g2_redundant` identities are not the operational candidate nomenclature and are not substituted into the 77-AST experiment.

## Claim ceiling

A successful operational run may support only:

> **Within the certified finite Boolean generator universe, corrective evidence can causally discriminate and persistently select a revised representation generator, producing generator-specific consequences on held-out inputs under the declared shadow, compensation, leakage, and universe controls.**

The result would not establish arbitrary representation invention, universal representation completeness, self-reference, recursion, consciousness, general intelligence, or L3 adaptation.

## Exclusions

The generator-revision rule is not itself adapted. The certificate is upstream of the treatment and cannot be modified by assay outcomes.
