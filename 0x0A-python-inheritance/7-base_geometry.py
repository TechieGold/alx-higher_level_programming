#!/usr/bin/python3
"""
This module contains a BaseGeometry class with public instance method.

methods:
    area(self): raises an Exception with a message.
    integer_validator(self, name, value): Validates a value.
        if value is not an integer, a TypeError is raised.
        if value is less than or equal to zero, a ValueError is raise.
Args:
    name: name of integer(string)
    value: of the integer (must be an integer)
"""


class BaseGeometry:
    """A BaseGeometry class with public instance methods."""
    def area(self):
        """Raise a Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a value is an integer or not"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
