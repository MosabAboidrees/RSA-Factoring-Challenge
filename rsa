#!/usr/bin/python3
"""
This script factorizes numbers read from a file into
a product of two prime numbers. Each line in the file
should contain one number to be factorized.
"""

import sys


def factorize_numbers_from_file():
    """
    Reads a file specified by the command line argument
    and factorizes each number
    found in the file into two factors, where possible,
    ensuring at least one factor is a prime number.
    """
    try:
        # Retrieve the file name from command line arguments
        file_name = sys.argv[1]
        with open(file_name) as numbers_file:
            # Iterate through each line in the file
            for number_str in numbers_file:
                num = int(number_str)
                # Check if the number is even
                if num % 2 == 0:
                    print("{}={}*{}".format(num, num // 2, 2))
                    continue
                # Initialize factor search starting from 3 for odd numbers
                pot_fac = 3
                while pot_fac < numb // 2:
                    # If a factor is found, print it and break the loop
                    if num % pot_fac == 0:
                        print("{}={}*{}".format(num, num // pot_fac, pot_fac))
                        break
                    potential_factor += 2
                # If no factors found other than 1 and
                # the number itself, print as prime
                if potential_factor >= (number // 2) + 1:
                    print("{}={}*{}".format(number, number, 1))
    except IndexError:
        # Handle the case where no file name
        # is provided in the command line arguments
        print("Usage: {} <file>".format(sys.argv[0]), file=sys.stderr)


factorize_numbers_from_file()
