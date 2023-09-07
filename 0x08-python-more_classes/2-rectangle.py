#!/usr/bin/python3
class Rectangle:
    """
    This class defines a Rectangle class with specified
    width and height attributes.
    Attributes:
        __width(int): the width of the rectangle.
        __height(int): the height of the rectangle.
    Methods:
        __init__(self, width=0, height=0)
            Initializes a new Rectangle instance
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
            Returns the rectangle area.
        perimeter(self):
        returns the rectangle perimeter.
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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
