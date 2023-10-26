#!/usr/bin/python3
"""
This module defines a Square class for representing squares.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of a side of the square.
        position (tuple): The position of the square in 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.

        Args:
            size (int): The size of a side of the square.
            position (tuple): The position of the square in 2D space.

        Raises:
TypeError: If size is of integer and position is not a tuple of two integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not (isinstance(position, tuple) and len(position) == 2 and
                all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be tuple of two positive integers")
        self.__size = size
        self.__position = position

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The size of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position of the square.

        Returns:
            tuple: The position of the square in 2D space.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Args:
            value (tuple): The position of the square in 2D space.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be tuple of two positive integers")
        self.__position = value
