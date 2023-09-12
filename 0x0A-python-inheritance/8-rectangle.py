#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
A Rectangle class the inherits from BaseGeometry class

Methods:
    __init__(self, width, height):
        Automatically instantiates  width and height attributes.
Attributes:
    __width(private): the rectangle width. must be an int.
    __height(private): the rectangle height. must be an int.
"""
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)