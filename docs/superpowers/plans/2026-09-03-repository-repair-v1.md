# Repository Repair v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the repository's public/default state, custody, provenance, CI behavior, and governance documentation faithfully represent the already-established scientific state without changing frozen science or redesigning Γ_t.

**Architecture:** Work on isolated branch `repo-repair-v1`. Preserve both the Γ lineage and the unique `main` custody-observer commit in merge ancestry, then make additive archival/provenance/audit/documentation repairs and narrow workflow changes. Consolidate through one reviewed PR to `main`; historical scientific branches remain untouched.

**Tech Stack:** Git/GitHub, GitHub Actions YAML, Python 3.11+, pytest, Markdown/JSON, SHA-256.

**Spec:** `docs/superpowers/specs/2026-09-03-repository-repair-design.md`

## Global Constraints

- Do not modify frozen certificate fixtures or `certificate/verify.py`.
- Do not modify historical v1/v2/v3 preregistrations, recorded result objects, resistance definitions, or scientific implementations.
- Do not modify `GAMMA_PREREGISTRATION.md` or `GAMMA_SCIENTIFIC_LEDGER.md`.
- Frozen v3 scientific source is `0eead840a1fc2f5de96d809b5e7b45ee14f7d726`.
- Successful v3 custody run is `33775722525`; observer/workflow SHA is `47e432817f1e7791d70e16cc08263bd28f583151`.
- Archived v3 JSON SHA-256 must be `2ae420019c41bbce43e8e34246d787b26475dc5f3b86f197e01b516ca0b07f72`.
- v2 recorded assay run is `33764556701`; its assay step succeeded before a later float-equality regression test failed.
- No new scientific statistic, assay, resistance family, Γ design, prediction, or causal interpretation may be introduced.

---

### Task 1: Preserve main custody ancestry

**Files:**
- No content changes.

**Interfaces:**
- Consumes: `repo-repair-v1` head descended from `e154cd7d791a23d40463fc513e64e3d7b798d845`; `main@47e432817f1e7791d70e16cc08263bd28f583151`.
- Produces: a merge commit with the repair branch tree unchanged and both commits in ancestry.

- [ ] **Step 1:** Fetch current repair head tree SHA and verify branch still descends from `e154cd7…`.
- [ ] **Step 2:** Create a two-parent merge commit using the current repair tree, first parent repair head and second parent `47e432817f1e7791d70e16cc08263bd28f583151`.
- [ ] **Step 3:** Fast-forward `repo-repair-v1` to the merge commit.
- [ ] **Step 4:** Compare pre/post merge trees; expected content diff is empty.

### Task 2: Permanently archive v3 custody evidence

**Files:**
- Create: `evidence/v3/structural_complexity_control_output.json`
- Create: `evidence/v3/structural_complexity_control_output.sha256`
- Create: `evidence/v3/pytest.log`
- Create: `evidence/v3/provenance.txt`
- Create: `evidence/v3/CUSTODY_RECORD.md`

**Interfaces:**
- Consumes: downloaded artifact ID `9901478202` from run `33775722525`.
- Produces: durable Git archive of the exact custodied bytes and human-readable binding record.

- [ ] **Step 1:** Extract the downloaded artifact locally and hash each file.
- [ ] **Step 2:** Verify raw JSON SHA-256 equals `2ae420019c41bbce43e8e34246d787b26475dc5f3b86f197e01b516ca0b07f72`; abort on mismatch.
- [ ] **Step 3:** Verify `provenance.txt` names scientific source `0eead840…`, observer SHA `47e432…`, run `33775722525`, attempt `1`, and workflow `v3 custody run`.
- [ ] **Step 4:** Commit the four artifact files byte-for-byte under `evidence/v3/` plus `CUSTODY_RECORD.md` documenting artifact ID, Actions artifact digest `sha256:cfa296287b4484d5ed5c13f2d9536032426ee0a38abad1ee101bf9cad094326c`, expiration of the transient copy, individual file hashes, `32 passed`, and the frozen adjudication ceiling.
- [ ] **Step 5:** Fetch the committed raw JSON and independently verify its SHA-256 against the custody record.

### Task 3: Clarify historical provenance without rewriting results

**Files:**
- Create: `V2_PROVENANCE_CLARIFICATION.md`
- Create: `METHODOLOGICAL_AUDIT.md`

**Interfaces:**
- Consumes: existing immutable v1/v2/v3 files and Actions logs.
- Produces: non-authorizing historical clarification/audit only.

- [ ] **Step 1:** Write `V2_PROVENANCE_CLARIFICATION.md` stating the exact execution order: robustness script success, then pytest failure in `test_recorded_threshold_reachability_summary_is_reproducible` on exact float equality; explicitly distinguish assay execution from containing job conclusion.
- [ ] **Step 2:** State that `RECORDED_RESISTANCE_ROBUSTNESS_EXECUTION.json` is not modified and that the clarification does not upgrade or weaken its claim ceiling.
- [ ] **Step 3:** Write `METHODOLOGICAL_AUDIT.md` with status `POST-HOC / NON-AUTHORIZING` and the four audited scope facts: self-coordinate anchoring, `|Δz|`-only v3 conditioning, common structural-edit ontology, and mixed BIT/BOOL destination universe.
- [ ] **Step 4:** Include explicit non-effects: no retroactive protocol mutation, no new v3 adjudication, no intrinsic-geometry claim, no bridge result, no Γ_t result.

### Task 4: Repair the public repository truth surface

**Files:**
- Create: `RESEARCH_STATE.md`
- Modify: `README.md`
- Modify: `pyproject.toml`
- Create: `.gitignore`

**Interfaces:**
- Consumes: historical records plus durable v3 archive and audit documents.
- Produces: authoritative present-state index and accurate landing metadata.

- [ ] **Step 1:** Create `RESEARCH_STATE.md` listing the certificate, historical toy assay, unfired operational W/C/P/E assay, v1, v2, v3, open Γ_t, and unestablished candidate-space expansion with exact status/claim boundaries and key SHAs/run IDs.
- [ ] **Step 2:** Replace README research-stack/status sections so v3 is represented as supported at the preregistered ceiling and Γ_t is explicitly open/not frozen; link the new custody/provenance/audit/state files.
- [ ] **Step 3:** Update `pyproject.toml` project description from the historical L2-only wording to `Certified finite representation-revision assays, accessibility geometry controls, and provenance-preserving research infrastructure` while leaving package/version/python/test configuration unchanged.
- [ ] **Step 4:** Add `.gitignore` entries for Python caches, virtual environments, pytest cache, build artifacts, and generated root assay outputs only; do not ignore `evidence/`.

### Task 5: Separate regression CI from scientific execution

**Files:**
- Modify: `.github/workflows/test.yml`
- Modify: `.github/workflows/robustness.yml`
- Modify: `.github/workflows/structural-complexity-control.yml`

**Interfaces:**
- Consumes: existing tests and historical runner scripts.
- Produces: ordinary CI that does not automatically re-execute historical assays; explicit manual reproduction workflows remain available.

- [ ] **Step 1:** Change `test.yml` so push/PR CI installs the package and runs only `python -m pytest`; remove `python scripts/run_resistance_robustness.py` from generic regression CI.
- [ ] **Step 2:** Change `robustness.yml` trigger to `workflow_dispatch` only, rename/display comments as historical reproduction, and pin checkout to `2807014156e50b86748750c258ebe400345621c9` so reproduction does not execute the moving branch head.
- [ ] **Step 3:** Change `structural-complexity-control.yml` trigger to `workflow_dispatch` only and pin checkout to frozen v3 scientific source `0eead840a1fc2f5de96d809b5e7b45ee14f7d726`.
- [ ] **Step 4:** Keep `.github/workflows/v3-custody.yml` unchanged; it already expresses the desired custody boundary.
- [ ] **Step 5:** Inspect workflow diffs and verify no scientific Python/JSON result files changed.

### Task 6: Verify frozen-object integrity and repaired branch

**Files:**
- No new scientific files.

**Interfaces:**
- Consumes: repair head and known Γ-tip blob SHAs.
- Produces: evidence that repair changed only allowed surfaces.

- [ ] **Step 1:** Verify blob SHA of `certificate/verify.py` remains `57c1e23fa53e586b082372da00a3fe37dd171f89`, `certificate/U_syntax.json` remains `a74165f547390a116caa47f0ea16679e54c025a8`, and `certificate/U_semantic.json` remains `dbeda59e6961eb7cc40672b8f336b1d62e8b793c`.
- [ ] **Step 2:** Verify `GAMMA_PREREGISTRATION.md` remains blob `0f145494b8434992205bf6ef36122a13ce133256` and `GAMMA_SCIENTIFIC_LEDGER.md` remains blob `c79f6b62c34c7a56938a041de135b806a3609994`.
- [ ] **Step 3:** Verify frozen result/preregistration/resistance source files have no content diff from `e154cd7…`.
- [ ] **Step 4:** Run/observe CI for the repair head and require full pytest success before consolidation.
- [ ] **Step 5:** Compare `main...repo-repair-v1`; inspect every changed path and reject anything outside approved repair scope.

### Task 7: Consolidate to main and clean historical PR state

**Files:**
- No additional repository content required before PR.

**Interfaces:**
- Consumes: fully verified repair branch.
- Produces: authoritative `main` history and non-misleading PR state.

- [ ] **Step 1:** Open a non-draft PR `repo-repair-v1 -> main` summarizing repair-only scope and frozen-science invariants.
- [ ] **Step 2:** Wait for/inspect PR checks; merge only if green and head SHA matches the verified repair head.
- [ ] **Step 3:** Merge using `merge` method, not squash or rebase.
- [ ] **Step 4:** Add explanatory comments to PR #2 and PR #3 that their scientific lineage is preserved in the consolidated main ancestry and that the PRs are superseded by repository consolidation; then close them without claiming standalone merge.
- [ ] **Step 5:** Re-fetch branches, `main`, open PRs, rulesets, README, evidence paths, and workflows for a final ultra-parse.
- [ ] **Step 6:** Report any remaining manual-only governance actions (archival tags/rulesets/branch protection) exactly; do not claim they are complete through the connector if no write tool exists.

## Self-review

- Spec coverage: all approved repair areas map to Tasks 1-7.
- Placeholder scan: no TBD/TODO/implementation placeholders.
- Boundary consistency: every task preserves frozen science and Γ_t documents.
- Execution concern: GitHub connector cannot currently create rulesets/tags or change repository default-branch settings directly; Task 7 records these as explicit manual follow-ups if still unsupported.