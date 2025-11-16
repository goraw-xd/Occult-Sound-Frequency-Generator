#!/usr/bin/env python3
"""Create initial user config file and prompt for API keys.
This script should NOT write secrets to git-tracked files; use .env instead.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / 'data' / 'user_profiles' / 'default_user.json'


def init():
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    if CONFIG.exists():
        print('User config already exists:', CONFIG)
        return
    default = {
        'username': 'default_user',
        'preferences': {},
    }
    with open(CONFIG, 'w', encoding='utf-8') as f:
        json.dump(default, f, indent=2)
    print('Created default user config at', CONFIG)


if __name__ == '__main__':
    init()
