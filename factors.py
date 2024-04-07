#!/usr/bin/python3

import math
import sys


def factorize(n):
    """Attempt to factorize n into two factors."""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1


def process_file(filename):
    """Read numbers from a file and factorize each."""
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            p, q = factorize(number)
            print(f"{number}={p}*{q}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
        sys.exit(1)

    process_file(sys.argv[1])
