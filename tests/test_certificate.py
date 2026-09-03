from pathlib import Path

import boolean_world.generators as generators

from certificate.verify import load_verified_universe


ROOT = Path(__file__).resolve().parents[1]


def test_certificate_verifies_and_exposes_only_frozen_fixtures(monkeypatch):
    def forbidden_enumeration(*args, **kwargs):
        raise AssertionError("certificate consumer must not enumerate the universe")

    monkeypatch.setattr(generators, "enumerate_universe", forbidden_enumeration)
    verified = load_verified_universe(ROOT / "certificate")

    assert len(verified.syntax) == 77
    assert verified.certificate["source_commit"] == "df450d91d0b3acdd1c0937bd5d8b20bda98b20b4"
    assert verified.semantic["class_count"] == 6


def test_semantic_fixture_is_an_exact_partition_of_syntax_fixture():
    verified = load_verified_universe(ROOT / "certificate")
    members = [member for record in verified.semantic["classes"] for member in record["members"]]

    assert len(members) == len(verified.syntax) == 77
    assert len(set(members)) == 77
    assert set(members) == set(verified.syntax)


def test_consume_boundary_has_no_production_enumerator_dependency():
    source = (ROOT / "certificate" / "verify.py").read_text(encoding="utf-8")

    assert "enumerate_universe" not in source
