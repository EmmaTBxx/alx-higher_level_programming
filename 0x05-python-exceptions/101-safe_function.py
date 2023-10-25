#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    Executes a function safely and handles exceptions.

    Args:
        fct: A function to be executed.
        *args: Any arguments to be passed to the function.

    Returns:
        The result of the function if it executes successfully.
        None if an exception occurs during the function execution, and
        the error message is printed to stderr.
    """
    try:
        result = fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
    return result
