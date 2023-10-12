#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurences of an element in a new list
    my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
