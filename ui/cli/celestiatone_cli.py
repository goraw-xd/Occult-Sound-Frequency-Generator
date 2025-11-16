"""Simple CLI entrypoint."""

import argparse
from . import cli_commands


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--intent', help='Intent text')
    args = parser.parse_args()
    print('CLI placeholder - intent:', args.intent)


if __name__ == '__main__':
    main()
