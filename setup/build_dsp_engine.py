#!/usr/bin/env python3
"""Build/compile native DSP components (placeholder).
Run this script to compile C/C++ modules like `planetary_math.cpp` and `binaural_core.cpp`.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CPP_DIR = ROOT / 'core' / 'planetary'


def main():
    print('Building DSP engine (placeholder)...')
    # Example: run a single-file g++ build (adjust for your platform/toolchain)
    src = CPP_DIR / 'planetary_math.cpp'
    if not src.exists():
        print(f"Source not found: {src}. Skipping build.")
        return
    out = ROOT / 'build' / 'planetary_math.dll'
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = ['g++', '-O3', str(src), '-shared', '-o', str(out)]
    print('Running:', ' '.join(cmd))
    subprocess.check_call(cmd)
    print('Build complete:', out)


if __name__ == '__main__':
    main()
