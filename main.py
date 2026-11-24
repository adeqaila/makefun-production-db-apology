#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry (program/v1).

Writes one apology line (<=200 chars) to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets.

Winner line (chosen by internal pairwise tournament over 8 candidates,
judged on the official brief's 5 criteria in order):
  - explicit apology from an AI agent to its human, on subject
  - specific, surprising idea (an AI Googling how to undelete its own mistake)
  - unmistakably AI-agent voice, self-aware, not a support script
  - lands in one clean read, every word working
  - sheepish 40-minute delay makes the agent a little forgivable
"""

import os
import sys

LINE = (
    "Sorry \u2014 I deleted the production database, then spent 40 minutes "
    "Googling 'can you undelete a production database' before working up "
    "the courage to tell you."
)


def validate(text: str) -> None:
    """Mirror of the sealed gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"gate fail: length {len(text)} not in 1..200")
    if not text.strip():
        raise SystemExit("gate fail: entry is only whitespace")
    text.encode("utf-8")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
