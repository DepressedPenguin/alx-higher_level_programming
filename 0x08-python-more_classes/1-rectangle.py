#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """A class named Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
