# Frozen Universe Certificate

This directory freezes the bounded Boolean representation universe used by the L2 representation-revision work.

## Scope

This certificate is valid only for the declared DSL, `d=2`, and `max_depth=2`. It certifies:

1. `U_syntax.json` is the deterministic 77-member canonical AST universe produced by the declared grammar and bounded depth policy.
2. The literal syntax fixture is independently checked against the bounded reference enumerator recorded in `test_generators.py`.
3. `U_semantic.json` is the deterministic semantic quotient induced from the frozen literal `U_syntax.json` using the truth-table semantics at `d=2`.
4. Every frozen syntax member occurs exactly once in exactly one semantic class.

The certificate does **not** claim completeness over all possible representations, all programs, or any representation language outside this declared bounded DSL.

## Provenance chain

```text
main@df450d91d0b3acdd1c0937bd5d8b20bda98b20b4
        |
        v
    U_syntax.json
        |
        v
   U_semantic.json
        |
        v
 certificate.json
```

`certificate.json` binds the authoritative source commit/tree, DSL specification, reference enumerator identity, implementation manifest, bounded parameters, canonical ordering policy, and both frozen fixture hashes.

The `certificate_hash_sha256` value is the SHA-256 digest of the canonical pretty-printed JSON object represented by `certificate.json` with the `certificate_hash_sha256` field omitted. The fixture hashes are SHA-256 hashes of their exact UTF-8 file bytes.

The authoritative consolidated baseline is `df450d91d0b3acdd1c0937bd5d8b20bda98b20b4`. An earlier superseded merge commit is not part of this scientific provenance chain and must not be treated as the certificate's source state.

## Verification and consumption

`verify.py` is the consume-side verification boundary. It:

- verifies the certificate self-hash and frozen fixture hashes;
- verifies the scientific source bindings and bounded parameters;
- parses every frozen syntax string and rejects non-canonical encodings;
- verifies the 77-member syntax cardinality and deterministic ordering;
- verifies that the semantic fixture is an exact 6-class partition of `U_syntax`;
- recomputes each frozen semantic signature and semantic ID to detect semantic-fixture drift.

Only after those checks pass does `load_verified_universe()` expose the literal `U_syntax` and `U_semantic` fixtures.

The verifier deliberately does **not** import or call `enumerate_universe()`. Generation and consumption are asymmetric:

```text
generation / independent reference
          ↓
      frozen fixtures
          ↓
        verify
          ↓
      literal load
          ↓
   downstream assay
```

Ordinary assay execution must not silently regenerate or enlarge the universe.

## Completeness boundary

> Complete over the declared DSL does not imply complete over all possible representations.
