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
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square (1 side).

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
