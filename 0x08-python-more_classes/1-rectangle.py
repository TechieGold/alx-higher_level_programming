#!/usr/bin/python3
class Rectangle:
    """
    This class defines an rectangle with a specified width and height.
    Attributes:
        __width(int): The width of the rectangle
        __height(int): The height of the rectangle.
    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle instance with
            optional width and height.
        width(self):
            Retrieves the with of the rectangle.
        width(self, value):
            Sets the width of the rectangle.
        height(self):
            Retrieves the height of the rectangle.
        height(self, value):
            Sets the heigth of the rectangle.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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
