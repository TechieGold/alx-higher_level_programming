#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class that inherits from Rectangle class.

    methods:
        __init__(self, size): Initializes a size attribute.
    Attributes:
        __size(private): size of the square. must be an integer.
        must be validated by the integer validator method.
        area(self): calculates and returns the area of the rectangle.
        __str__(self) - should return a string representation of
        the square description.
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
