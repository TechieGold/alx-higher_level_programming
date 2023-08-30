#!/usr/bin/python3
"""Defines a Square class with size attribute

   size must be an integer, otherwise raises a TypeError
   size must be greater thab 0 otherwise raises a ValueError

   public instance methode that returns the current square area.
"""


class Square:
    """Sqaure Class definition"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
