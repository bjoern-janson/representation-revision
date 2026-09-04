from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from representation_revision.gamma_ordering import run_gamma_ordering


def canonical_json(payload) -> str:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ) + "\n"


def _parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Execute frozen Gamma ordering v1 assay")
    parser.add_argument("--scientific-source", required=True)
    parser.add_argument("--output", type=Path)
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = _parse_args(argv)
    if re.fullmatch(r"[0-9a-f]{40}", args.scientific_source) is None:
        raise SystemExit("--scientific-source must be a lowercase 40-hex commit SHA")

    result = run_gamma_ordering()
    result["scientific_source"] = args.scientific_source
    raw = canonical_json(result)
    if args.output is not None:
        args.output.write_text(raw, encoding="utf-8", newline="")
    sys.stdout.write(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
