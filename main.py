"""A single picture carrying the whole planet's news for one Thursday.

Beside this script sits entry.png: a crowded front page for 19 November
2026, thirty-six items in all — six drawn large at the top, thirty
numbered underneath, and a small map tying each place to its story.
This script does nothing creative: it moves those exact bytes to the
folder the grader reads, then proves the copy matches byte for byte.
"""

import hashlib, os, sys
import pathlib


def _fingerprint(location):
    return hashlib.sha256(location.read_bytes()).hexdigest()


def _place_picture():
    repo = pathlib.Path(__file__).resolve().parent
    shipped = repo / "entry.png"
    out_folder = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_folder.mkdir(parents=True, exist_ok=True)
    target = out_folder / "entry.png"
    payload = shipped.read_bytes()
    target.write_bytes(payload)
    if target.stat().st_size != len(payload):
        raise RuntimeError("written file is not the same length as the shipped one")
    if _fingerprint(shipped) != _fingerprint(target):
        raise RuntimeError("written file bytes differ from the shipped ones")
    return target


def main(argv):
    if "--check" in argv:
        shipped = pathlib.Path(__file__).resolve().parent / "entry.png"
        if shipped.stat().st_size > 1048576:
            raise RuntimeError("shipped picture is over the one-mebibyte cap")
        print("check ok:", _fingerprint(shipped))
        return 0
    _place_picture()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
