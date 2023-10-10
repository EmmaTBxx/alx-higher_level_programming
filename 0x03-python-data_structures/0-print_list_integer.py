#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all intergers of a list
    don't import any module or cast integers into strings
    """
    if my_list:
        for integer in my_list:
            print("{:d}" .format(integer))
