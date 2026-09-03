# L2 Assay

The assay is intentionally isolated and deterministic.

Scientific execution is `representation_revision.assay.run_scientific_assay()`.

## Causal sequence

The repaired assay requires the observed trigger discrepancy to implicate the current generator before any follow-up discrimination occurs:

`corrective trigger -> observed discrepancy -> generator diagnosis -> fixed follow-up probes -> discriminating evidence -> persistent selected generator -> held-out future evaluation`

The follow-up probe pool is downstream of the trigger, while the revision universe remains fixed independently of the current generator.

## Checkpoints

The pre-certification checkpoint independently establishes:

1. finite deterministic enumeration and certified-complete coverage of the declared universe;
2. deterministic unique discrimination within that universe;
3. generator adoption from the same trigger path.

Only after those pass should the recorded adaptive-vs-shadow execution be produced.

## Shadow

The fixed-G shadow receives the identical held-out `(S_future, e_future)` event stream as the adaptive branch. The only intended treatment difference is persistent generator state: the adaptive branch carries the selected successor while the shadow remains `g0_surface`.

## Claim boundary

This assay targets L2: evidence-driven persistent revision of the representation generator. It does not adapt the generator-revision rule itself and therefore makes no L3 claim.
