#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class that inherits from Rectangle class.

    methods:
        __init__(self, size): Initializes a size attribute.
    Attributes:
        __size(private): size of the square. must be an integer.
        area(self): calculates and returns the area of the rectangle.
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
