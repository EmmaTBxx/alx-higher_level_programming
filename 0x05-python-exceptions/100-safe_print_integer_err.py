#!/usr/bin/python3

import sys


def safe_print_integer_err(value):

    """
    Function that prints an integer or handles errors.

    Args:
        value: The value to print.

    Returns:
        True if value is an integer and is correctly printed.
        False if there is an error, and the error message is printed to stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
