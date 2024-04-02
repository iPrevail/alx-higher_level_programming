#!/usr/bin/python3
""" Create a class that raise errors"""


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
