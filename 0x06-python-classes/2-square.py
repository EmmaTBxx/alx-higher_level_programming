#!/usr/bin/python3


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square (1 side).
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square (1 side).

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
