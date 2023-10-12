#!/usr/bin/python3

def uniq_add(my_list=[]):
    """You are not allowed to import any module
    """
    # return [result := result + num for num in new_list][-1]

    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
