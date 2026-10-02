#!/usr/bin/env python3
"""CLI for the Morse Code Toolkit.

Usage:
    python cli.py encode "hello world"
    python cli.py decode "... --- ..."
"""
import sys

from morse import decode, encode


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in ("encode", "decode"):
        print(__doc__.strip())
        return 2
    action, value = sys.argv[1], sys.argv[2]
    print(encode(value) if action == "encode" else decode(value))
    return 0


if __name__ == "__main__":
    sys.exit(main())
