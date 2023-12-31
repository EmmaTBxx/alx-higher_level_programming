#!/usr/bin/python3

"""
This module defines a Square class and ways to calc its area and perimeter.
"""


class Square:
    """
    A class representing a square.

    This class defines a square and way  to calculate its area and perimeter.

    Attributes:
        side_length (int): The length of each side of the square.
    """

    def __init__(self, side_length):
        """
        Initializes a Square instance.

        Args:
            side_length (int): The length of each side of the square.
        """
        self.side_length = side_length

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.side_length ** 2

    def perimeter(self):
        """
        Calculates and returns the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.side_length
