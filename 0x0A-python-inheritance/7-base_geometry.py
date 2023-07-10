#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """improve class"""
    def __init__(self):
        """init inti"""
        pass

    def area(self):
        """Integer validator"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
