from __future__ import annotations

import argparse
import json
from pathlib import Path

from representation_revision.operational_l2 import run_operational_l2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--out", default="OPERATIONAL_L2_RESULT.json")
    args = parser.parse_args()

    result = run_operational_l2(source_commit=args.source_commit)
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n"
    Path(args.out).write_text(payload, encoding="utf-8", newline="\n")
    print(payload, end="")


if __name__ == "__main__":
    main()
