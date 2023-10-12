#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurences of an element in a new list
    my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    You are not allowed to import any module
    """
    new_list = my_list.copy()
    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace

            return new_list
