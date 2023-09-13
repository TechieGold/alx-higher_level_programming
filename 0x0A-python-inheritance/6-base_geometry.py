#!/usr/bin/python3
"""
This module contains BaseGeometry class with public instance method.

public instance method:
    area(self): raises an Exception with a message.
"""


class BaseGeometry:
    """BaseGeometry class."""
    def area(self):
        """Raise an Exception"""
        raise Exception("area() is not implemented")
