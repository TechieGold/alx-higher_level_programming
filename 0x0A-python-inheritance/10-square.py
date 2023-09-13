#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
    This module contain a square class that inherits from Rectangle class.

    methods:
        __init__(self, size): Initializes a size attribute.
    Attributes:
        __size(private): size of the square. must be an integer.
    """


class Square(Rectangle):
    """square class that inherits from Rectangle class."""
    def __init__(self, size):
        """Initialises width and height attributes."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
