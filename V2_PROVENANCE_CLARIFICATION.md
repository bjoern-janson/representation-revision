# v2 Resistance-Robustness Provenance Clarification

**Status:** POST-HOC PROVENANCE CLARIFICATION / NON-AUTHORIZING  
**Historical result object:** unchanged  
**Recorded result:** `RECORDED_RESISTANCE_ROBUSTNESS_EXECUTION.json`

## Why this clarification exists

The immutable v2 execution record names GitHub Actions workflow run `33764556701` and job `100678990416`. GitHub records the overall containing job as `failure`.

That job-level conclusion must not be conflated with the status of the scientific assay step inside the job.

## Exact observed execution order

The Actions log shows the following order at head SHA `df7bdc7fb066c596d1944e9bd3731aefb601a43d`:

1. Repository checkout and environment setup succeeded.
2. `python scripts/run_resistance_robustness.py` completed successfully and printed the complete robustness output, including the recorded `759/759` full-profile counts and `755/755/759` threshold-reachability counts.
3. Only **after** that assay step completed, `python -m pytest` ran.
4. Pytest reported `1 failed, 26 passed`.
5. The single failure was `tests/test_accessibility_record.py::test_recorded_threshold_reachability_summary_is_reproducible`.
6. The failed assertion compared the freshly computed floating-point value `2437 / 77 = 31.649350649350648` by exact equality with the serialized recorded value `31.64935064935065`.

The later lineage repairs that regression check with `math.isclose(..., rel_tol=0.0, abs_tol=1e-12)`; the scientific resistance-robustness calculation itself is unchanged.

## Provenance interpretation

The accurate provenance statement is therefore:

```text
v2 assay step                         SUCCESS
containing CI job                     FAILURE
reason for containing-job failure     later exact-float regression assertion
scientific output produced first      YES
```

The containing workflow's failure is a real historical fact and must remain visible. It is not evidence that the v2 assay command failed or that its printed output was absent.

## No mutation of the historical result

`RECORDED_RESISTANCE_ROBUSTNESS_EXECUTION.json`, its recorded claim, its canonical JSON hash, the resistance implementations, and the preregistration are not changed by this clarification.

This document does not upgrade, weaken, re-adjudicate, or independently reproduce v2. It only makes the relationship between the successful assay step and the failed containing CI job explicit.

## Claim boundary

The historical v2 ceiling remains the recorded finite three-family robustness statement. This clarification does not establish intrinsic representational geometry, prediction, behavioral consequence, causation, candidate-space expansion, or `Gamma_t`.
