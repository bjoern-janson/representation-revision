# L2 Assay

The repository contains a historical deterministic toy assay and a separately frozen Boolean universe for the next operational assay. These are intentionally not conflated.

## Causal target

The operational L2 target is:

```text
fixed certified universe
  -> observed discrepancy
  -> generator diagnosis
  -> discriminating evidence
  -> unique candidate
  -> persistent generator adoption
  -> G1-specific held-out consequence
```

The four causal burdens are:

- **W — What changed?** `G0 != G1` at the generator interface.
- **C — What caused the change?** corrective evidence preceded and causally discriminated the selected candidate, without candidate-identity leakage.
- **P — Did it persist?** the selected generator remains the generator used throughout the post-adoption held-out set.
- **E — What did persistence cause?** the held-out consequence is specific to `G1` and survives shadow and compensation controls.

The full operational specification is frozen in [`OPERATIONAL_PREREGISTRATION.json`](OPERATIONAL_PREREGISTRATION.json) and [`PREREGISTRATION.md`](PREREGISTRATION.md).

## Certified universe boundary

The bounded Boolean candidate space is frozen in [`certificate/`](certificate/). A consumer must verify that certificate and load the literal fixtures. Ordinary assay execution must not regenerate or enlarge the universe.

```text
certificate -> verify -> literal U_syntax / U_semantic -> operational L2 consumer
```

The certificate proves only bounded completeness for its declared DSL and parameters. It does not prove completeness over all possible representations.

## Historical toy assay

`representation_revision.assay.run_scientific_assay()` is retained as a historical positive control. It uses the original three-generator toy `GeneratorSpec` universe and its recorded artifacts. The certificate is deliberately not retrofitted into that historical execution, because doing so would silently change the experimental object.

The historical sequence remains:

`corrective trigger -> observed discrepancy -> generator diagnosis -> fixed follow-up probes -> discriminating evidence -> persistent selected generator -> held-out future evaluation`

Its recorded result is documented in [`RECORDED_EXECUTION.json`](RECORDED_EXECUTION.json) and its provenance in [`EXECUTION_PROVENANCE.md`](EXECUTION_PROVENANCE.md).

## Shadow and compensation controls

The **shadow** receives the identical held-out future `(S,e)` stream while retaining `G0`.

The **compensation** control is a separate future condition permitted to reproduce useful behavior while retaining `G0`. It exists to test the residual alternative that apparent L2 success is downstream behavioral rescue rather than representation revision.

## Claim boundary

The experiment targets evidence-driven persistent revision of the representation generator. It makes no L3 claim and no claim that self-reference, recursion, consciousness, or general intelligence is necessary for the observed effect.
