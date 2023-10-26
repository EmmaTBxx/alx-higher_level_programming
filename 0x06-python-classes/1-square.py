#!/usr/bin/python3

"""
This module defines a Square class for representing squares.
"""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square (1 side).
    """

    def __init__(self, size):
        """Initializes a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
