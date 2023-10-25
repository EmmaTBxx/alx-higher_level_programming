#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list as integers.

    Args:
        my_list: The list to print elements from.
        x: Number of elements to access in my_list.

    Returns: The real number of integers printed.
    """
    count = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print("{:d}".format(my_list[item]), end=' ')
                count += 1
            except (IndexError, ValueError):
                break
    print()
    return count
