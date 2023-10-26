#!/usr/bin/python3
"""
This module defines a Square class for representing squares.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square (1 side).
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of a side of the square.

        Raises:
            TypeError: If the input size is not an integer.
            ValueError: If the input size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square using '#' symbols.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
