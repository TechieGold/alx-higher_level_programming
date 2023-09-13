#!/usr/bin/python3
"""
This module contains a  Rectangle class the inherits from BaseGeometry class.

Methods:
    __init__(self, width, height):
        Automatically instantiates  width and height attributes.
Attributes:
    __width(private): the rectangle width. must be an int.
    __height(private): the rectangle height. must be an int.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class the inherits from BaseGeometry class."""
    def __init__(self, width, height):
        """instantiates width and height atrributes."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
