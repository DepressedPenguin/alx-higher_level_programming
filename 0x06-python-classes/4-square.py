#!/usr/bin/python3
# 4-square.py by Zakaria Elaroussi
"""A module defines a square """


class Square:
    """A class represents a square"""

    def __init__(self, size=0):
        """Initializing square class
        Args:
            size: represnets Size of square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less then zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
