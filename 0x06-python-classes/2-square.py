#!/usr/bin/python3
"""A Square class with private attribute -size
   size must be an integer
   if size is less than 0 raises a ValueError
"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
