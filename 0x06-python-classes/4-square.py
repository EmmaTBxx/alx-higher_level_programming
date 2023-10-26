#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ Square class defined by geometric shape

        Attributes:
            size (int): Size of square
    """
    def __init__(self, size=0):
        """ Initializes the square

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        self.__size = size

    def area(self):
        """ Calculates square area

        Returns:
            The current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter for size

        Returns:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size

        Args:
            size (int): size of a side of the square

        Raises:
            TypeError: if size is not int
            ValueError: size less than 0

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:

            raise ValueError("size must be >= 0")
        else:
            self.__size = value
