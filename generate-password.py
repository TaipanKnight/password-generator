#!/usr/local/bin/python3

import random
import string


def generate_password():
    # Create a pool of lowercase letters
    lowercase_letters = string.ascii_lowercase
    # Create a pool of uppercase letters and digits
    uppercase_letter = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)

    # Generate three sets of 6 random lowercase letters
    segments = [''.join(random.choice(lowercase_letters) for _ in range(6)) for _ in range(3)]
    password = '-'.join(segments)

    # Create a list of valid positions to insert the uppercase letter and digit
    valid_positions = [i for i in range(len(password)) if password[i] != '-']

    # Ensure that two distinct positions are chosen
    insert_positions = random.sample(valid_positions, 2)
    password_list = list(password)

    # Insert the uppercase letter and digit into the password
    password_list[insert_positions[0]] = uppercase_letter
    password_list[insert_positions[1]] = digit

    return ''.join(password_list)


def main():
    num_passwords = int(input("How many passwords would you like to generate? "))

    for _ in range(num_passwords):
        print(generate_password())


if __name__ == "__main__":
    main()
