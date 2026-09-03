# Representation Revision

This repository is an evidence-first finite research program about representation revision, accessibility, and the boundary between **what a system can represent**, **what is reachable within a frozen representation space**, and **what remains unestablished beyond that space**.

The authoritative present-state index is [`RESEARCH_STATE.md`](RESEARCH_STATE.md).

## Current scientific state

```text
historical L2 toy assay                 EXECUTED / HISTORICAL
certified Boolean universe              FROZEN ✅
stronger operational W/C/P/E assay      PREREGISTERED / UNFIRED
v1 representational accessibility       EXECUTED / FROZEN ✅
v2 resistance-cost robustness           EXECUTED / FROZEN ✅
v3 structural-complexity control        SUPPORTED / FROZEN ✅
Gamma_t temporal-organization rung      OPEN / NOT FROZEN ☐
candidate-space expansion U_t->U_t+1   UNESTABLISHED
```

The repository is deliberately conservative about what each rung earns. Later custody, documentation, or repository-repair commits do not retroactively become scientific-source commits.

## Permanent epistemic guardrails

### Candidate-space guardrail

> **Complete over the declared DSL does not imply complete over representation space.**

The certificate covers only the declared Boolean DSL at `d=2`, `max_depth=2`.

### Mechanistic guardrail

> **Behavioral equivalence does not imply mechanistic equivalence.**

```text
Delta B  -/->  Delta G  -/->  Cause(e, Delta G)  -/->  generator-specific held-out consequence
```

### Search-space guardrail

> **Candidate evaluation is not candidate generation.**

A finite certified universe can support claims about selection or transition structure **within that universe**. It cannot establish open-ended representation invention.

### Dynamic-state guardrail

```text
G_t != A_t != Gamma_t != I_t
```

and, permanently:

```text
residual transition structure != Gamma_t
```

## Certified finite universe

The consume-side certificate freezes:

```text
syntax members      77
semantic classes      6
d                     2
max depth             2
```

[`certificate/verify.py`](certificate/verify.py) validates the literal frozen fixtures, source/tree bindings, DSL specification hash, implementation manifest, fixture hashes, canonical AST text, exact semantic partition, and recomputed semantic signatures. Certificate consumption does **not** regenerate the universe.

The certificate is finite infrastructure, not evidence that all relevant representations have been enumerated.

## Experimental objects

### Historical three-generator toy assay

The original small `GeneratorSpec` assay is retained unchanged as historical evidence. The later 77-member certificate is **not** retrofitted into that execution.

Relevant records:

- [`ASSAY.md`](ASSAY.md)
- [`PRECERTIFICATION.json`](PRECERTIFICATION.json)
- [`RECORDED_EXECUTION.json`](RECORDED_EXECUTION.json)
- [`EXECUTION_PROVENANCE.md`](EXECUTION_PROVENANCE.md)

### Stronger operational W/C/P/E causal assay

The certified 77-member operational causal assay is preregistered but **unfired**. Its stronger causal proposition therefore remains unearned.

Relevant records:

- [`PREREGISTRATION.md`](PREREGISTRATION.md)
- [`OPERATIONAL_PREREGISTRATION.json`](OPERATIONAL_PREREGISTRATION.json)

## v1 — representational accessibility

The preregistered future-blind structural resistance relation was evaluated over the literal certified 77-member syntax universe at `tau = 3`.

Recorded result:

```text
semantic-equivalent unordered pairs                759
full labeled resistance-profile divergence         759 / 759
thresholded reachable-set divergence, tau=3       755 / 759
profile divergence with equal reachable sets         4 / 759
```

Historical claim ceiling:

> **Within the certified finite Boolean universe, semantic equivalence does not imply equivalence of outgoing transition geometry under the preregistered structural resistance relation.**

At `tau=3`, semantically equivalent representations can also have different thresholded reachable sets.

Relevant records:

- [`ACCESSIBILITY_PREREGISTRATION.json`](ACCESSIBILITY_PREREGISTRATION.json)
- [`REPRESENTATIONAL_ACCESSIBILITY.md`](REPRESENTATIONAL_ACCESSIBILITY.md)
- [`RECORDED_ACCESSIBILITY_EXECUTION.json`](RECORDED_ACCESSIBILITY_EXECUTION.json)
- [`ACCESSIBILITY_EXECUTION_PROVENANCE.md`](ACCESSIBILITY_EXECUTION_PROVENANCE.md)

## v2 — resistance-cost robustness

Three preregistered resistance families were tested: `R_v1`, `R_unit`, and `R_depth`.

```text
full-profile separation
R_v1      759 / 759
R_unit    759 / 759
R_depth   759 / 759

thresholded reachability separation at tau=3
R_v1      755 / 759
R_unit    755 / 759
R_depth   759 / 759
```

Historical narrow conclusion:

> **The observed semantic-equivalent separation is not confined to the original `R_v1` cost convention within this finite three-family assay.**

The three families share the broad canonical-AST recursive structural-edit ontology while varying cost and directionality conventions. This is not evidence for an intrinsic or uniquely correct representational geometry.

The recorded assay command in workflow run `33764556701` succeeded before the containing CI job later failed on an exact floating-point regression assertion. That distinction is documented without altering the historical result in [`V2_PROVENANCE_CLARIFICATION.md`](V2_PROVENANCE_CLARIFICATION.md).

Relevant records:

- [`ACCESSIBILITY_ROBUSTNESS_PREREGISTRATION.json`](ACCESSIBILITY_ROBUSTNESS_PREREGISTRATION.json)
- [`RECORDED_RESISTANCE_ROBUSTNESS_EXECUTION.json`](RECORDED_RESISTANCE_ROBUSTNESS_EXECUTION.json)
- [`RESISTANCE_ROBUSTNESS_PROVENANCE.md`](RESISTANCE_ROBUSTNESS_PROVENANCE.md)
- [`V2_PROVENANCE_CLARIFICATION.md`](V2_PROVENANCE_CLARIFICATION.md)

## v3 — declared structural-complexity control

v3 asked whether the measured semantic-equivalent outgoing-profile divergence was fully explained by a preregistered nine-component structural-complexity vector:

```text
z(G) = (
  AST size,
  depth,
  n_INPUT,
  n_NOT,
  n_AND,
  n_OR,
  n_XOR,
  n_EQ,
  n_NEQ
)
```

The exact control key is componentwise pairwise `|Delta z|` within the semantic-equivalent pair population.

Custodied primary counts:

```text
family   N_eligible   N_matched   N_separated   matched strata   nonconstant matched strata
R_depth       759          759           759          26                    10
R_unit        759          759           759          26                    11
R_v1          759          759           759          26                    11
```

The all-zero `|Delta z|` stratum has multiple `D_k` values for all three families, directly satisfying the preregistered positive decision rule.

Frozen claim ceiling:

> **Within the certified finite Boolean universe and across all three preregistered resistance constructions, semantic-equivalent representations remain separated in outgoing transition geometry under exact matching on the declared nine-component structural-complexity difference vector; therefore the observed separation is not fully explained by those declared controls.**

This does **not** establish intrinsic geometry, semantic causality, temporal organization, prediction, behavioral consequence, candidate-space expansion, or `I_t`.

Frozen scientific source used for the custodied execution:

`0eead840a1fc2f5de96d809b5e7b45ee14f7d726`

Successful custody run:

```text
run                         33775722525
observer/workflow SHA       47e432817f1e7791d70e16cc08263bd28f583151
pytest                      32 passed in 0.46s
raw JSON SHA-256            2ae420019c41bbce43e8e34246d787b26475dc5f3b86f197e01b516ca0b07f72
```

The exact GitHub Actions artifact is durably archived under [`evidence/v3/`](evidence/v3/). See [`evidence/v3/CUSTODY_RECORD.md`](evidence/v3/CUSTODY_RECORD.md).

The frozen v3 preregistration is [`ACCESSIBILITY_COMPLEXITY_PREREGISTRATION.json`](ACCESSIBILITY_COMPLEXITY_PREREGISTRATION.json).

## Post-hoc methodological audit

[`METHODOLOGICAL_AUDIT.md`](METHODOLOGICAL_AUDIT.md) is explicitly **POST-HOC / NON-AUTHORIZING**. It records scope facts that sharpen interpretation without changing historical science:

- labeled full profiles contain forced self-coordinate differences for distinct sources;
- v3 conditions on pairwise `|Delta z|`, not absolute complexity-pair identity plus semantic-class identity;
- the three v2 resistance families share a structural-edit ontology;
- the 77-node profile destination universe includes both BIT and BOOL syntax nodes.

The audit does not rerun or re-adjudicate v1-v3 and does not establish a bridge or `Gamma_t` result.

## Current open frontier — `Gamma_t`

The fresh Γ ledger is intentionally open:

- [`GAMMA_PREREGISTRATION.md`](GAMMA_PREREGISTRATION.md)
- [`GAMMA_SCIENTIFIC_LEDGER.md`](GAMMA_SCIENTIFIC_LEDGER.md)

Standing question:

> **Does ordering of a fixed finite transition inventory contain measurable structure not determined by its preregistered order-free control?**

No statistic, composability control, permutation family, sequence construction, threshold, execution, custody, or adjudication is frozen yet.

No `Gamma_t` result exists.

## Candidate-space expansion remains separate

```text
U_t -> evidence of inadequacy -> U_{t+1} superset U_t
```

Nothing in v1-v3 demonstrates this. Absence, inaccessibility, non-selection, and non-persistence remain distinct failure modes.

## Repository map

| Path | Role |
| --- | --- |
| [`RESEARCH_STATE.md`](RESEARCH_STATE.md) | Authoritative present-state index |
| [`certificate/`](certificate/) | Frozen finite universe and consume-side verifier |
| [`boolean_world/`](boolean_world/) | Typed AST and pure Boolean semantics |
| [`representation_revision/`](representation_revision/) | Historical assay and frozen accessibility/robustness/control implementations |
| [`evidence/v3/`](evidence/v3/) | Durable v3 custody archive |
| [`V2_PROVENANCE_CLARIFICATION.md`](V2_PROVENANCE_CLARIFICATION.md) | Historical Actions-run clarification |
| [`METHODOLOGICAL_AUDIT.md`](METHODOLOGICAL_AUDIT.md) | Post-hoc, non-authorizing scope audit |
| [`GAMMA_PREREGISTRATION.md`](GAMMA_PREREGISTRATION.md) | Open Γ preregistration ledger |
| [`GAMMA_SCIENTIFIC_LEDGER.md`](GAMMA_SCIENTIFIC_LEDGER.md) | Open Γ state ledger |
| [`tests/`](tests/) | Regression and contract tests |
| [`.github/workflows/`](.github/workflows/) | Regression CI and explicit historical reproduction/custody workflows |

## Verification

The ordinary regression surface is:

```bash
python -m pytest
```

Historical scientific reproduction is intentionally kept separate from generic push/PR regression CI.

## Overall claim boundary

The repository currently establishes finite certified infrastructure plus frozen historical observations about representation-relative transition structure under declared structural resistance constructions and controls.

It does **not** establish:

```text
universal representation completeness
open-ended candidate generation
intrinsic / natural representational geometry
future prediction
causal behavioral efficacy of accessibility
persistent temporal organization Gamma_t
a future-relevant invariant I_t
general intelligence or consciousness
```
