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
        """Initialises width and height attributes."""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """Calculates and returns the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the string in this form [Rectangle] <width>/<height>"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
