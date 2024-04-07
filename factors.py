#!/usr/bin/python3

import math


def print_factors(number):
    """ Finds and prints a factorization of 'number'
    where one factor is as large as possible.
    This prints the first such factorization found, starting from 1.
    Args:
        number (int): The number to find a factorization for.
    """
    # Start with the smallest possible factor.
    factor_candidate = 1
    while factor_candidate * factor_candidate <= number:
        if (number % factor_candidate == 0):
            # If 'factor_candidate' is a factor,
            # calculate the corresponding factor.
            corr_fac = number // factor_candidate
            # Print the factorization in the format
            # "number=factor*corr_fac".
            print("{:d}={:d}*{:d}".format(number, corr_fac, factor_candidate))
            # Exit after finding the first factorization.
            break
    factor_candidate += 1


def main():
    from sys import argv, exit, stderr

    # Check if the script was called with the correct number of arguments.
    if len(argv) != 2:
        # If not, print the correct usage of the script to stderr.
        stderr.write("Usage: ./factors <file>\n")
        exit(1)
    try:
        # Attempt to open the specified file.
        file_handle = open(argv[1], "r")
    except FileNotFoundError:
        # If the file cannot be found, print an error message to stderr.
        stderr.write("Could not find file {}\n".format(argv[1]))
    else:
        # Read and process each line in the file until there are no more.
        while (True):
            line = file_handle.readline()
            if (not line):
                break
            # Convert the line from a string to an integer.
            number = int(line)
            # Call the function to print the factorization of the number.
            print_factors(number)
    # Close the file.
    file_handle.close()


main()
