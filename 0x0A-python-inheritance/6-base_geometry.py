#!/usr/bin/python3
"""
A BaseGeometry class with public instance method.

    meth:
        area(self): raises an Exception with a message.
"""


class BaseGeometry:
    def area(self):
        """Raise a Exception"""
        raise Exception("area() is not implemented")
