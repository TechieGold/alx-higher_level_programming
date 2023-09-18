#!usr/bin/python3
"""
models.rectangle
===============

This modules defines the Rectangle class, which represents
a rectangle with width, height and positions.
"""
from models.base import Base


class Rectangle(Base):
    """A clas representing arectangle with width, height and position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.
            x(int, optional): The x-coordinate of the rectangle's position.
            y(int, optional): The y-coordinate of the rectangle's position.
            id(int, optional): The unique identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError(" height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError(" x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the triangle."""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using '#' charaters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
