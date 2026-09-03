# Frozen Universe Certificate

This directory freezes the bounded Boolean representation universe used by the
L2 representation-revision work.

## Scope

This certificate is valid only for the declared DSL, `d=2`, and
`max_depth=2`. It certifies:

1. `U_syntax.json` is the deterministic 77-member canonical AST universe
   produced by the declared grammar and bounded depth policy.
2. The literal syntax fixture is independently checked against the bounded
   reference enumerator recorded in `test_generators.py`.
3. `U_semantic.json` is the deterministic semantic quotient induced from the
   frozen literal `U_syntax.json` using the truth-table semantics at `d=2`.
4. Every frozen syntax member occurs exactly once in exactly one semantic class.

The certificate does **not** claim completeness over all possible
representations, all programs, or any representation language outside this
declared bounded DSL.

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

`certificate.json` binds the authoritative source commit/tree, DSL
specification, reference enumerator identity, implementation manifest,
bounded parameters, canonical ordering policy, and both frozen fixture hashes.

The authoritative consolidated baseline is `df450d91d0b3acdd1c0937bd5d8b20bda98b20b4`.
An earlier superseded merge commit is not part of this scientific provenance
chain and must not be treated as the certificate's source state.

## Consumption rule

A downstream consumer must treat the frozen fixtures as the certified
universe. It may verify the recorded hashes and structural predicates, but it
must not silently enlarge or regenerate the universe as part of ordinary
assay execution.

## Completeness boundary

> Complete over the declared DSL does not imply complete over all possible
> representations.
