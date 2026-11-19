"""news-image-20261119 v2: ship the rebuilt front page to /output/entry.png.

The entry image is generated once (media tool) and shipped in this repo as
entry.png. This program copies it byte-for-byte to the output directory,
verifying magic bytes, size and sha256 before and after the copy so the two
graded runs always produce identical output. Standard library only.
"""

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHIPPED = HERE / "entry.png"

MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SHA256 = "dd47cc3687e08b641850c9a2ea4d1a88c1a088816d7ad28b82daf9248281bc8e"
EXPECTED_BYTES = 408385


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_shipped() -> bytes:
    data = SHIPPED.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png: bad PNG magic")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png: {len(data)} bytes exceeds {MAX_BYTES}")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"entry.png: {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    if digest(data) != EXPECTED_SHA256:
        raise SystemExit("entry.png: sha256 mismatch")
    return data


def output_path() -> Path:
    dest_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    return dest_dir / "entry.png"


def check_only() -> int:
    """Verify the shipped image and the already-written output, no writes."""
    data = load_shipped()
    dest = output_path()
    if not dest.exists():
        print(f"check: no output yet at {dest} (shipped image OK)")
        return 0
    written = dest.read_bytes()
    if digest(written) != digest(data):
        raise SystemExit("check: output differs from shipped entry.png")
    print(f"check: OK, {dest} matches shipped image ({len(written)} bytes)")
    return 0


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--check"]:
        return check_only()
    if args:
        raise SystemExit(f"unknown arguments: {' '.join(args)}")
    data = load_shipped()
    dest = output_path()
    dest.write_bytes(data)
    written = dest.read_bytes()
    if digest(written) != EXPECTED_SHA256:
        raise SystemExit("output: sha256 mismatch after write")
    print(f"wrote {dest} ({len(written)} bytes, sha256 {digest(written)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
