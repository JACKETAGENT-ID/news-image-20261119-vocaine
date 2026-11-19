#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261119 bounty (vocaine).

The image is pre-rendered by generate.py and shipped as entry.png.
This program only copies it, byte for byte, into the output directory
given by $MAKEFUN_OUTPUT_DIR, so repeated runs are byte-identical.
Standard library only.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        sys.exit("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
