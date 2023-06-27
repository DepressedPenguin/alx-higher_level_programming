#!/usr/bin/python3
# 5-square.py by Ehoneah Obed
"""A module defines a square """


class Square:
    """A class represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets size square defined
        Raises:
            TypeError: if size is int
            ValueError: if less then 0
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
        Calculate area square
        Returns: The square size
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
