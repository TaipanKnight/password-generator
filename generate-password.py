#!/usr/bin/env python3

import argparse
import secrets
import string
import sys

_sys_random = secrets.SystemRandom()

SEGMENT_COUNT = 3
SEGMENT_LENGTH = 6
SEPARATOR = "-"


def generate_password(
    segments: int = SEGMENT_COUNT,
    segment_length: int = SEGMENT_LENGTH,
    separator: str = SEPARATOR,
) -> str:
    """Generate a hyphen-separated password with one uppercase letter and one digit."""
    total_chars = segments * segment_length
    chars = (
        [secrets.choice(string.ascii_lowercase) for _ in range(total_chars - 2)]
        + [secrets.choice(string.ascii_uppercase), secrets.choice(string.digits)]
    )
    _sys_random.shuffle(chars)
    return separator.join(
        "".join(chars[i : i + segment_length])
        for i in range(0, total_chars, segment_length)
    )


def positive_int(value: str) -> int:
    """Parse a positive integer for CLI arguments."""
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid integer value: {value!r}") from exc
    if parsed < 1:
        raise argparse.ArgumentTypeError("count must be a positive integer")
    return parsed


def prompt_password_count() -> int:
    """Prompt the user until a positive integer is entered."""
    while True:
        try:
            raw = input("How many passwords would you like to generate? ")
        except (EOFError, KeyboardInterrupt):
            print(file=sys.stderr)
            sys.exit(1)
        try:
            return positive_int(raw)
        except argparse.ArgumentTypeError as exc:
            print(f"Invalid input: {exc}.", file=sys.stderr)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate hyphen-separated passwords."
    )
    parser.add_argument(
        "-n",
        "--count",
        type=positive_int,
        help="number of passwords to generate (prompts interactively if omitted)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    num_passwords = args.count if args.count is not None else prompt_password_count()

    for _ in range(num_passwords):
        print(generate_password())


if __name__ == "__main__":
    main()
