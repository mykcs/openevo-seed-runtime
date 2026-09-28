#!/usr/bin/env python3
"""Validate the public OpenEvo SEED runtime identity without pulling image layers."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

IMAGE_RE = re.compile(r"^\| Image \| `(?P<value>ghcr\.io/[^\`]+)` \|$", re.MULTILINE)
TAG_RE = re.compile(r"^\| Tag \| `(?P<value>[^\`]+)` \|$", re.MULTILINE)
DIGEST_RE = re.compile(r"^\| Digest \| `(?P<value>sha256:[0-9a-f]{64})` \|$", re.MULTILINE)


def extract(pattern: re.Pattern[str], text: str, label: str) -> str:
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"README missing canonical {label} field")
    return match.group("value")


def read_contract() -> tuple[str, str, str]:
    text = README.read_text(encoding="utf-8")
    image = extract(IMAGE_RE, text, "image")
    tag = extract(TAG_RE, text, "tag")
    digest = extract(DIGEST_RE, text, "digest")

    if f"docker pull {image}:{tag}" not in text:
        raise SystemExit("README readable-tag pull command disagrees with Metadata")
    if f"docker pull {image}@{digest}" not in text:
        raise SystemExit("README digest-pinned pull command disagrees with Metadata")
    if "| Visibility | Public |" not in text:
        raise SystemExit("runtime identity qualification expects a public GHCR image")
    return image, tag, digest


def inspect_remote(image: str, tag: str, expected_digest: str) -> None:
    ref = f"{image}:{tag}"
    result = subprocess.run(
        ["docker", "buildx", "imagetools", "inspect", ref],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    print(result.stdout, end="")
    match = re.search(r"^Digest:\s+(sha256:[0-9a-f]{64})\s*$", result.stdout, re.MULTILINE)
    if not match:
        raise SystemExit("remote manifest inspection did not expose a canonical digest")
    actual = match.group(1)
    if actual != expected_digest:
        raise SystemExit(
            f"GHCR tag drift: {ref} resolves to {actual}, README pins {expected_digest}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--remote",
        action="store_true",
        help="Query the public GHCR manifest without pulling image layers.",
    )
    args = parser.parse_args()

    image, tag, digest = read_contract()
    print(f"README identity: {image}:{tag} -> {digest}")
    if args.remote:
        inspect_remote(image, tag, digest)
    print("PASS: runtime identity contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
