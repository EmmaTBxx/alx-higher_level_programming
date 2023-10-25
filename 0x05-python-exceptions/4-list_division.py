#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides elements of two lists element-wise.

    Args:
        my_list_1: List 1
        my_list_2: List 2
        list_length: Length of lists

    Returns: New list with all the divisions
    """
    new_list = []

    for item in range(list_length):
        try:
            quotient = my_list_1[item] / my_list_2[item]
        except IndexError:
            print("Out of range")
            quotient = 0
        except TypeError:
            print("Wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("Division by 0")
            quotient = 0
        finally:
            new_list.append(quotient)
    return new_list
