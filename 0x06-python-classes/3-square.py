#!/usr/bin/python3
# 0-square.py by zakaria_Elaroussi
"""A module defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing class square
        Args:
            size: represnets size of square
        Raises:
            TypeError: if size is not int
            ValueError: if size less then 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate the square
        Returns: The square size
        """

        return (self.__size ** 2)
