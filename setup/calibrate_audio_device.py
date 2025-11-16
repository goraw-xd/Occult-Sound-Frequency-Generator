#!/usr/bin/env python3
"""Audio device calibration placeholder.
Detects available audio devices and writes simple latency settings.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'data' / 'audio_calibration.json'


def calibrate():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = {
        'device': 'default',
        'latency_ms': 50,
    }
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print('Wrote calibration to', OUT)


if __name__ == '__main__':
    calibrate()
