from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from boolean_world.ast import parse_canonical
from boolean_world.semantics import semantic_id, semantic_signature

EXPECTED_SOURCE_COMMIT = "df450d91d0b3acdd1c0937bd5d8b20bda98b20b4"
EXPECTED_SOURCE_TREE = "df357dac8553979dc281b149ec21c211e01e6a4b"


class CertificateVerificationError(ValueError):
    """Raised when the frozen universe certificate cannot be trusted."""


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_json_bytes(path: Path) -> tuple[Any, bytes]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateVerificationError(f"invalid JSON: {path}") from exc
    return value, raw


def _certificate_digest(certificate: dict[str, Any]) -> str:
    payload = dict(certificate)
    try:
        payload.pop("certificate_hash_sha256")
    except KeyError as exc:
        raise CertificateVerificationError("certificate_hash_sha256 is missing") from exc
    canonical = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    return _sha256_bytes(canonical.encode("utf-8"))


@dataclass(frozen=True)
class VerifiedUniverse:
    """Literal certified fixtures exposed only after complete verification."""

    certificate: dict[str, Any]
    syntax: tuple[str, ...]
    semantic: dict[str, Any]


def verify_certificate(root: Path | None = None) -> VerifiedUniverse:
    """Verify the frozen certificate and return its literal fixtures.

    This function never calls the production Boolean enumerator. The certified
    universe is loaded from the frozen JSON fixtures and checked in place.
    """
    base = Path(root) if root is not None else Path(__file__).resolve().parent
    certificate, certificate_raw = _read_json_bytes(base / "certificate.json")
    syntax, syntax_raw = _read_json_bytes(base / "U_syntax.json")
    semantic, semantic_raw = _read_json_bytes(base / "U_semantic.json")

    if not isinstance(certificate, dict):
        raise CertificateVerificationError("certificate root must be an object")
    if not isinstance(syntax, list) or not all(isinstance(item, str) for item in syntax):
        raise CertificateVerificationError("U_syntax must be a JSON string array")
    if not isinstance(semantic, dict):
        raise CertificateVerificationError("U_semantic root must be an object")

    if certificate.get("source_commit") != EXPECTED_SOURCE_COMMIT:
        raise CertificateVerificationError("certificate source commit binding mismatch")
    if certificate.get("source_tree") != EXPECTED_SOURCE_TREE:
        raise CertificateVerificationError("certificate source tree binding mismatch")
    if certificate.get("d") != 2 or certificate.get("max_depth") != 2:
        raise CertificateVerificationError("unsupported certificate bounds")

    recorded_cert_hash = certificate.get("certificate_hash_sha256")
    if recorded_cert_hash != _certificate_digest(certificate):
        raise CertificateVerificationError("certificate self-hash mismatch")

    if certificate.get("U_syntax_sha256") != _sha256_bytes(syntax_raw):
        raise CertificateVerificationError("U_syntax hash mismatch")
    if certificate.get("U_semantic_sha256") != _sha256_bytes(semantic_raw):
        raise CertificateVerificationError("U_semantic hash mismatch")

    expected_count = certificate.get("syntax_count")
    if expected_count != len(syntax) or len(syntax) != 77:
        raise CertificateVerificationError("U_syntax cardinality mismatch")
    if syntax != sorted(syntax) or len(set(syntax)) != len(syntax):
        raise CertificateVerificationError("U_syntax is not unique sorted canonical text")

    parsed = []
    for text in syntax:
        try:
            node = parse_canonical(text)
        except (TypeError, ValueError) as exc:
            raise CertificateVerificationError(f"invalid frozen AST: {text}") from exc
        if node.canonical_serialize() != text:
            raise CertificateVerificationError(f"non-canonical frozen AST: {text}")
        parsed.append(node)

    classes = semantic.get("classes")
    class_count = semantic.get("class_count")
    if not isinstance(classes, list) or class_count != len(classes) or class_count != 6:
        raise CertificateVerificationError("U_semantic class cardinality mismatch")
    if semantic.get("d") != 2 or semantic.get("syntax_member_count") != len(syntax):
        raise CertificateVerificationError("U_semantic parameter binding mismatch")

    members_seen: list[str] = []
    semantic_ids: set[str] = set()
    signatures: set[str] = set()
    syntax_set = set(syntax)
    for record in classes:
        if not isinstance(record, dict):
            raise CertificateVerificationError("semantic class must be an object")
        members = record.get("members")
        if not isinstance(members, list) or not all(isinstance(item, str) for item in members):
            raise CertificateVerificationError("semantic class members must be strings")
        if members != sorted(members) or len(set(members)) != len(members):
            raise CertificateVerificationError("semantic class members are not unique sorted text")
        signature = record.get("signature")
        sid = record.get("semantic_id")
        if not isinstance(signature, str) or not isinstance(sid, str):
            raise CertificateVerificationError("semantic class identity is malformed")
        if signature in signatures or sid in semantic_ids:
            raise CertificateVerificationError("duplicate semantic class identity")
        signatures.add(signature)
        semantic_ids.add(sid)
        for member in members:
            if member not in syntax_set:
                raise CertificateVerificationError(f"semantic member absent from U_syntax: {member}")
        members_seen.extend(members)

    if len(members_seen) != len(syntax) or set(members_seen) != syntax_set:
        raise CertificateVerificationError("semantic quotient does not partition U_syntax exactly once")

    nodes_by_text = dict(zip(syntax, parsed))
    for record in classes:
        for text in record["members"]:
            node = nodes_by_text[text]
            actual_signature = semantic_signature(node, d=2)
            actual_id = semantic_id(node, d=2)
            if actual_signature != record["signature"] or actual_id != record["semantic_id"]:
                raise CertificateVerificationError(f"semantic fixture mismatch: {text}")

    return VerifiedUniverse(
        certificate=certificate,
        syntax=tuple(syntax),
        semantic=semantic,
    )


def load_verified_universe(root: Path | None = None) -> VerifiedUniverse:
    """Alias emphasizing the consume-only boundary for downstream callers."""
    return verify_certificate(root=root)
