#!/usr/bin/python
class Rectangle:
    """
    This class defines a rectangle class
    with specified width and height attributes.
    Attributes:
        width(int): Width of the rectangle.
        height(int): Height of the rectangle.
    Method:
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
            Returns a string representation of the rectangle.
        __repr__(self):
            Returns a string representation of recreating the instances.
        __del__(self):
            Destructor method that prints "Bye rectangle..."
            when an instance is deleted.
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
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join['#' * self.__width] * self.__height)

    def __repr__(self):
        return (f"Represent{self.__width}, {self.__height}")

    def __del__(self):
        print("Bye rectangle...")
