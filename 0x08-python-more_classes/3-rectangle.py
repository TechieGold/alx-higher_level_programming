#!/usr/bin/python3
class Rectangle:
    """
    This class defines a rectangle with specified width and height.
    Attributes:
        __width(int): width of the rectangle.
        __height(int): height of the rectangle.
    Methods:
        __init__(self, width=0, height=0):
            Initializes a new rectangle instance
            with optional width and height attributes.
        width(self):
            Retrieves the width of the rectangle.
        width(self, value):
            Sets the width of the rectangle.
        height(self):
            Retrieves the height of the rectangle.
        height(self, value):
            Sets the height of the rectangle.
        area(self):
            Calculates and returns the area of the rectangle.
        perimeter(self):
            Calculates and returns the perimeter of the rectangle.
        __str__(self):
            Returns a string representation of the rectangle using '#'.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(['#' * self.__width] * self.__height))
