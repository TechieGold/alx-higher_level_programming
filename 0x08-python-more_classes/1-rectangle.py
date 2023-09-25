#!/usr/bin/python3
"""This module contains a Rectangle class"""


class Rectangle:
    """
    This class defines a Rectangle class with specified
    width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance
        with optional width and height attributes.

         Attributes:
        __width(int): the width of the rectangle.
        __height(int): the height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
