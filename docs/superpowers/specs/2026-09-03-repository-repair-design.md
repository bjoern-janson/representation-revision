# Repository Repair v1 Design

**Status:** approved implementation design  
**Date:** 2026-09-03  
**Branch:** `repo-repair-v1`

## Goal

Bring the repository's public/default state, custody, provenance, CI behavior, and governance documentation into alignment with the already-established scientific state without changing any frozen scientific object or designing new science.

## Scientific immutability boundary

The repair must not modify the content of:

- the frozen certificate fixtures or verifier;
- historical v1/v2/v3 preregistrations;
- frozen v1/v2/v3 scientific implementations;
- recorded v1/v2 result objects;
- the frozen v3 scientific source at `0eead840a1fc2f5de96d809b5e7b45ee14f7d726`;
- the current open `GAMMA_PREREGISTRATION.md` or `GAMMA_SCIENTIFIC_LEDGER.md`;
- resistance definitions or claim ceilings.

The repair may add archival evidence, provenance clarification, post-hoc methodological audit, repository-state documentation, metadata, and CI/governance changes. Such additions are non-authorizing and may not retroactively alter a historical result.

## Repository-history approach

Start from `preregister-gamma-t-v0@e154cd7d791a23d40463fc513e64e3d7b798d845`. Preserve the unique `main@47e432817f1e7791d70e16cc08263bd28f583151` custody-exposure commit in ancestry with a merge commit whose tree initially remains identical to the Γ tip. Do not squash or rewrite historical scientific branches.

## Durable v3 custody

The successful custody run is GitHub Actions run `33775722525`, observer/workflow SHA `47e432817f1e7791d70e16cc08263bd28f583151`, frozen scientific source `0eead840a1fc2f5de96d809b5e7b45ee14f7d726`, artifact `v3-structural-complexity-control-evidence` / artifact ID `9901478202`.

Archive under `evidence/v3/`:

- `structural_complexity_control_output.json` byte-for-byte;
- `structural_complexity_control_output.sha256`;
- `pytest.log`;
- `provenance.txt`;
- `CUSTODY_RECORD.md` binding run, artifact, scientific source, observer SHA, file hashes, and adjudication status.

The recorded JSON SHA-256 must remain:

`2ae420019c41bbce43e8e34246d787b26475dc5f3b86f197e01b516ca0b07f72`.

The archive supplements custody; it does not become a new scientific execution.

## v2 provenance clarification

Do not alter `RECORDED_RESISTANCE_ROBUSTNESS_EXECUTION.json`. Add a companion provenance clarification explaining that run `33764556701` successfully completed `python scripts/run_resistance_robustness.py` before the containing CI job failed in a later regression test due to exact floating-point equality in `tests/test_accessibility_record.py`. State that the assay output and the CI job conclusion are distinct facts.

## Post-hoc methodological audit

Add `METHODOLOGICAL_AUDIT.md`, explicitly marked `POST-HOC / NON-AUTHORIZING`. Record only demonstrated scope facts:

1. Full labeled outgoing profiles contain forced self-coordinate differences for distinct representations under positive-cost resistance families; therefore binary `D_k > 0` is partly identity-anchored by construction.
2. v3 exact conditioning is by `|Δz|` within the semantic-equivalent pair population, not by semantic-class identity plus absolute complexity-vector pair.
3. `R_v1`, `R_unit`, and `R_depth` vary cost conventions while sharing the same broad canonical-AST recursive edit ontology.
4. The 77-member destination universe includes `INPUT`/BIT nodes as well as BOOL-valued nodes; this is an explicit scope property of the measured outgoing geometry.

The audit must state that these facts do not mutate historical protocols or authorize a new bridge/Γ result.

## Public repository state

Add `RESEARCH_STATE.md` as the authoritative present-state index. Update `README.md` so the public landing surface accurately distinguishes:

- certified finite universe infrastructure;
- historical toy assay;
- unfired stronger operational W/C/P/E causal assay;
- v1 accessibility result;
- v2 resistance-cost robustness result with provenance clarification;
- v3 structural-complexity-control result supported at its preregistered ceiling with durable custody;
- Γ_t open/not frozen;
- candidate-space expansion unestablished.

Update `pyproject.toml` description to describe the repository rather than only the historical L2 toy assay. Preserve `LICENSE` and `CITATION.cff` already present in the scientific lineage. Add ordinary generated-file exclusions only if needed.

## CI separation

Separate these jurisdictions:

`regression CI != scientific execution != custody reproduction`.

Generic `tests` should run regression tests only. Historical resistance-robustness and structural-complexity scientific workflows must not execute automatically on unrelated pushes/PRs. Their reproducibility workflows may remain available through explicit/manual triggers and should pin or clearly identify the historical scientific source when they execute.

No CI repair may alter scientific implementation code or historical result files.

## Consolidation and governance

Open one `repo-repair-v1 -> main` pull request after verification. Use merge ancestry rather than squash/rebase so historical lineage remains inspectable. After consolidation, close obsolete historical PRs with explanatory comments rather than claiming they were independently merged.

The connector may not expose ruleset/tag writes. Where mechanical protection cannot be applied through the available interface, document the remaining manual protection actions precisely; do not claim they are complete.

## Verification requirements

Before completion:

- full pytest suite passes on repair head;
- certificate verification passes unchanged;
- frozen certificate fixture/verifier blob SHAs are unchanged from Γ tip;
- `GAMMA_PREREGISTRATION.md` and `GAMMA_SCIENTIFIC_LEDGER.md` blob SHAs are unchanged;
- frozen v3 scientific source remains unchanged and referenced by exact SHA;
- archived v3 raw JSON hash equals the recorded SHA-256;
- v2 provenance clarification matches the Actions log ordering;
- diff contains only custody/provenance/audit/docs/metadata/workflow/governance repair;
- no new scientific statistic, assay, resistance family, interpretation, or Γ design is introduced.

## Stop condition

After consolidation, governance cleanup, and a fresh ultra-parse, stop. New Γ_t design resumes only in a separate scientific step.