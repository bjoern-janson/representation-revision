from pathlib import Path

import boolean_world.generators as generators
import pytest

from certificate.verify import CertificateVerificationError, load_verified_universe


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_ROOT = ROOT / "certificate"


def test_certificate_verifies_and_exposes_only_frozen_fixtures(monkeypatch):
    def forbidden_enumeration(*args, **kwargs):
        raise AssertionError("certificate consumer must not enumerate the universe")

    monkeypatch.setattr(generators, "enumerate_universe", forbidden_enumeration)
    verified = load_verified_universe(CERTIFICATE_ROOT)

    assert len(verified.syntax) == 77
    assert verified.certificate["source_commit"] == "df450d91d0b3acdd1c0937bd5d8b20bda98b20b4"
    assert verified.semantic["class_count"] == 6


def test_certificate_binds_declared_reference_and_implementation_metadata():
    verified = load_verified_universe(CERTIFICATE_ROOT)
    certificate = verified.certificate

    assert certificate["reference_enumerator_git_blob_sha1"] == "89a0be89a1f223db035828446504a7e6d7e8ce81"
    assert certificate["implementation_manifest_sha256"] == "35817ef71f87215949b98d21943576ff33a591587bf851c30f3501c6f8d0e7bb"
    assert certificate["dsl_spec_hash_sha256"] == "64922dd1c329b62c326e95f6775a7ee34b6cd4783f91a576a82794362bf8c2dc"


def test_semantic_fixture_is_an_exact_partition_of_syntax_fixture():
    verified = load_verified_universe(CERTIFICATE_ROOT)
    members = [member for record in verified.semantic["classes"] for member in record["members"]]

    assert len(members) == len(verified.syntax) == 77
    assert len(set(members)) == 77
    assert set(members) == set(verified.syntax)


def test_consume_boundary_has_no_production_enumerator_dependency():
    source = (CERTIFICATE_ROOT / "verify.py").read_text(encoding="utf-8")

    assert "enumerate_universe" not in source


def test_source_binding_mismatch_is_a_hard_stop(tmp_path):
    for name in ("certificate.json", "U_syntax.json", "U_semantic.json", "verify.py"):
        (tmp_path / name).write_bytes((CERTIFICATE_ROOT / name).read_bytes())

    certificate = (tmp_path / "certificate.json").read_text(encoding="utf-8")
    certificate = certificate.replace(
        "df450d91d0b3acdd1c0937bd5d8b20bda98b20b4",
        "0000000000000000000000000000000000000000000000000000000000000000",
        1,
    )
    (tmp_path / "certificate.json").write_text(certificate, encoding="utf-8")

    with pytest.raises(CertificateVerificationError, match="source commit binding mismatch"):
        load_verified_universe(tmp_path)
