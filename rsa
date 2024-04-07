#!/usr/bin/python3

import random
import math


def modular_pow(base, exponent, modulus):
    """
    Efficiently computes (base^exponent) % modulus
    using the right-to-left binary method.
    Args:
        base (int): The base of the exponentiation.
        exponent (int): The exponent.
        modulus (int): The modulus.
    Returns:
        int: The result of (base^exponent) % modulus.
    """
    result = 1
    while (exponent > 0):
        # If exponent is odd, multiply the result
        # by the current base mod modulus
        if (exponent % 2 != 0):
            result = (result * base) % modulus
        # Divide exponent by 2
        exponent = int(exponent / 2)
        # Square the base and mod by modulus
        base = (base * base) % modulus
    return result


def prime_divisor(n):
    """
    Attempts to find a prime divisor of n using a variation
    of Pollard's Rho algorithm.
    Args:
        n (int): The number to find a prime divisor for.
    Returns:
        int: A divisor of n. Returns n if no divisor found.
    """
    if (n == 1):
        return n
    if (n % 2 == 0):
        return 2

    # Randomly initialize x, y, and the constant c within bounds
    x = random.randint(0, n - 2)
    y = x
    c = random.randint(1, n - 1)

    d = 1
    while (d == 1):
        # Move x and y according to the function and
        # calculate the gcd of |x-y| and n
        x = (modular_pow(x, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        d = math.gcd(abs(x - y), n)

        # If d equals n, retry with different x, y, c
        if (d == n):
            return prime_divisor(n)
    return d


def print_factors(number):
    """
    Prints factors of a given number using the prime_divisor function.
    Args:
        number (int): The number to factorize.
    """
    divisor = prime_divisor(number)
    complementary_divisor = int(number / divisor)
    # Ensure divisor is the smaller factor
    if divisor >= complementary_divisor:
        print("{:d}={:d}*{:d}".format(number, divisor, complementary_divisor))
    else:
        print("{:d}={:d}*{:d}".format(number, complementary_divisor, divisor))


def main():
    """
    Main function to read numbers from a file and print their factors.
    """
    from sys import argv, exit, stderr

    # Check for correct usage
    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit()

    try:
        # Attempt to open the specified file
        file_handle = open(argv[1], "r")
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
    else:
        # Read each line, convert to an integer, and print its factors
        while (True):
            line = file_handle.readline()
            if (not line):
                break
            number = int(line)
            print_factors(number)

    file_handle.close()


main()
