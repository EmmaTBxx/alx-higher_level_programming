#!/usr/bin/python3

class Square:
    """A class that defines a square."""

    def __init__(self, side_length):
        """
        Initializes a square with a given side length.

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
