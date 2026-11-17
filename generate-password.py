#!/usr/bin/env python3

import argparse
import secrets
import string
import sys

_sys_random = secrets.SystemRandom()


def generate_password():
    """Generate a hyphen-separated password with at least one uppercase letter and one digit."""
    lowercase_letters = string.ascii_lowercase
    uppercase_letter = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)

    segments = [''.join(secrets.choice(lowercase_letters) for _ in range(6)) for _ in range(3)]
    password = '-'.join(segments)

    valid_positions = [i for i, ch in enumerate(password) if ch != '-']
    insert_positions = _sys_random.sample(valid_positions, 2)
    password_list = list(password)

    password_list[insert_positions[0]] = uppercase_letter
    password_list[insert_positions[1]] = digit

    return ''.join(password_list)


def positive_int(value):
    """Parse a positive integer for CLI arguments."""
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid integer value: {value!r}") from exc
    if parsed < 1:
        raise argparse.ArgumentTypeError("count must be a positive integer")
    return parsed


def prompt_password_count():
    """Prompt the user until a positive integer is entered."""
    while True:
        raw = input("How many passwords would you like to generate? ")
        try:
            count = int(raw)
        except ValueError:
            print("Please enter a valid positive integer.", file=sys.stderr)
            continue
        if count < 1:
            print("Please enter a number greater than 0.", file=sys.stderr)
            continue
        return count


def parse_args():
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


def main():
    args = parse_args()
    num_passwords = args.count if args.count is not None else prompt_password_count()

    for _ in range(num_passwords):
        print(generate_password())


if __name__ == "__main__":
    main()
