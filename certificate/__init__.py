"""Frozen certificate artifacts and their verification boundary."""

from .verify import CertificateVerificationError, load_verified_universe, verify_certificate

__all__ = [
    "CertificateVerificationError",
    "load_verified_universe",
    "verify_certificate",
]
