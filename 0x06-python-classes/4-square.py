#!/usr/bin/python3
"""a class Square that defines a square

    Private instance attribute: size

    property def size(self): to retrieve it:
    property setter def size(self, value): to set it

    size must be an integer otherwise raise a TypeError
    size must be greater than 0otherwise rais a ValueError
"""


class Square:
    """Sqaure class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
