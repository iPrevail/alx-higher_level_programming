#!/usr/bin/python3
"""Create a class that initializes a square and computes area"""


class Square:
    """Define a square"""
    def __init__(self, size=0):

        """Initialize the size of the square, raises TypeError
        if size is not an int
        Args:
            size: the size of the square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Compute the area of the square
        Return: the area of the square"""

        return self.__size**2
