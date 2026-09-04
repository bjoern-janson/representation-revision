# Gamma Ordering v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement, freeze, execute, and custody the preregistered finite Γ ordering assay without altering any predecessor scientific object.

**Architecture:** Add one pure assay module that precomputes the three frozen outgoing-profile geometries, exhaustively enumerates the 116,664 eligible center/three-leaf motifs, and evaluates all six `S3` orders. Add one small runner that serializes the deterministic result. Keep interpretation and custody in separate post-execution artifacts.

**Tech Stack:** Python >=3.11, standard library, pytest, existing `boolean_world` and `representation_revision` modules.

**Spec:** `docs/superpowers/specs/2026-09-04-gamma-ordering-v1-design.md`

## Global Constraints

- Use exactly the certified 77-member syntax fixture and six semantic classes frozen on the parent branch.
- Use exactly `R_v1`, `R_unit`, and `R_depth`; do not add or tune a resistance family.
- Exhaust all six leaf permutations for every eligible motif.
- Do not inspect certified-universe Γ outcomes before the implementation/scientific-source commit is frozen.
- `Q_k` is reversal-invariant; do not claim directional asymmetry or an arrow of time.
- Primary success is `common_positive_motifs > 0`; do not replace it after execution.

---

### Task 1: Pure Γ ordering module and toy tests

**Files:**
- Create: `representation_revision/gamma_ordering.py`
- Create: `tests/test_gamma_ordering.py`

**Interfaces:**
- Consumes: `Node`, `parse_canonical`, `R_v1`, `R_unit`, `R_depth`, `certificate/U_syntax.json`, `certificate/U_semantic.json`.
- Produces: `run_gamma_ordering() -> dict[str, object]` and pure helpers used by the runner/tests.

- [ ] **Step 1: Write failing toy tests**

```python
from representation_revision.gamma_ordering import q_values_for_leaf_triple


def test_q_values_are_reversal_paired():
    labels = ("a", "b", "d")
    distance = {
        ("a", "b"): 2, ("b", "a"): 2,
        ("a", "d"): 5, ("d", "a"): 5,
        ("b", "d"): 7, ("d", "b"): 7,
    }
    rows = q_values_for_leaf_triple(labels, lambda x, y: distance[(x, y)])
    assert len(rows) == 6
    by_order = {tuple(row["order"]): row["q"] for row in rows}
    assert by_order[("a", "b", "d")] == by_order[("d", "b", "a")]
    assert len(set(by_order.values())) == 3


def test_equilateral_toy_is_order_invariant():
    rows = q_values_for_leaf_triple(("a", "b", "d"), lambda _x, _y: 4)
    assert {row["q"] for row in rows} == {8}
```

- [ ] **Step 2: Run the toy tests and verify they fail before implementation**

Run: `pytest tests/test_gamma_ordering.py -q`

Expected: import/function failure because `gamma_ordering.py` does not yet exist.

- [ ] **Step 3: Implement the pure permutation helper and full assay**

Core helper:

```python
def q_values_for_leaf_triple(leaves, distance_fn):
    return [
        {"order": list(order), "q": distance_fn(order[0], order[1]) + distance_fn(order[1], order[2])}
        for order in itertools.permutations(leaves)
    ]
```

Full assay requirements:

```python
FAMILIES = {
    "R_v1": resistance,
    "R_unit": unit_resistance,
    "R_depth": depth_resistance,
}
```

Precompute `77 x 77` outgoing-profile L1 matrices for all three families. Enumerate semantic-class members in sorted canonical-serialization order; for each center, enumerate `itertools.combinations` of three other members. Assert the final eligible count equals `116664`.

For each motif/family, compute six Q values, `distinct_q_count`, and `delta_q`. Accumulate per-family positive counts, `D in {1,2,3}` counts, positive `delta_q` samples, and common-positive count. Track the lexicographically earliest common-positive motif by `(center, leaf1, leaf2, leaf3)`.

- [ ] **Step 4: Add fixture/predecessor validation tests**

```python
def test_certified_fixture_shape_and_motif_count():
    result = run_gamma_ordering(dry_validate_only=True)
    assert result["syntax_members"] == 77
    assert result["semantic_classes"] == 6
    assert result["eligible_motifs"] == 116664
```

A predecessor-only check may recompute the already-frozen semantic-pair count `759`; it must not assert any Γ outcome.

- [ ] **Step 5: Run tests**

Run: `pytest tests/test_gamma_ordering.py -q`

Expected: PASS.

---

### Task 2: Deterministic scientific runner

**Files:**
- Create: `run_gamma_ordering.py`
- Test: `tests/test_gamma_ordering.py`

**Interfaces:**
- Consumes: `run_gamma_ordering()` from Task 1.
- Produces: canonical JSON on stdout and optional byte-identical JSON file.

- [ ] **Step 1: Add a failing serialization test**

```python
def test_canonical_json_is_repeatable(tmp_path):
    from run_gamma_ordering import canonical_json
    payload = {"b": 2, "a": 1}
    assert canonical_json(payload) == '{"a":1,"b":2}\n'
```

- [ ] **Step 2: Implement runner**

Use:

```python
def canonical_json(payload):
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
```

CLI:

```text
python run_gamma_ordering.py --scientific-source <commit-sha> --output <path>
```

The runner inserts only provenance metadata (`scientific_source`) after computation; it does not alter the statistic or decision rule.

- [ ] **Step 3: Run focused tests and full predecessor suite**

Run:

```text
pytest tests/test_gamma_ordering.py -q
pytest -q
```

Expected: all tests pass.

---

### Task 3: Freeze implementation, execute once, and custody result

**Files:**
- Create after execution: `GAMMA_ORDERING_RESULT.json`
- Create after execution: `GAMMA_ORDERING_ADJUDICATION.md`
- Modify after execution: `GAMMA_SCIENTIFIC_LEDGER.md`

**Interfaces:**
- Consumes: frozen implementation commit and preregistration.
- Produces: raw observation, SHA-256 custody hash, and bounded adjudication.

- [ ] **Step 1: Freeze implementation/scientific-source commit before certified outcome inspection**

The commit must contain the preregistration, module, tests, and runner. Record its SHA as `SCIENTIFIC_SOURCE`.

- [ ] **Step 2: Execute the certified assay exactly once**

Run:

```text
python run_gamma_ordering.py --scientific-source $SCIENTIFIC_SOURCE --output /tmp/GAMMA_ORDERING_RESULT.json
```

- [ ] **Step 3: Hash the raw result before interpretation**

Run:

```text
python - <<'PY'
from hashlib import sha256
from pathlib import Path
p = Path('/tmp/GAMMA_ORDERING_RESULT.json')
print(sha256(p.read_bytes()).hexdigest())
PY
```

- [ ] **Step 4: Adjudicate only against the frozen rule**

```python
positive = result["common_positive_motifs"] > 0
```

If positive, use the exact preregistered claim ceiling. If zero, record the preregistered failure without rescue analysis.

- [ ] **Step 5: Commit observation and adjudication separately from the scientific source**

The post-execution commit must identify the scientific-source SHA, raw-result SHA-256, execution environment, test status, primary criterion, and exclusions. It must not rewrite the frozen preregistration or predecessor objects.
