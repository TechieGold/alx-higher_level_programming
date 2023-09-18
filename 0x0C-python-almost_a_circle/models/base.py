#!/usr/bin/python3
"""
This module contains a base class with attribute and constructor.
Attributes:
    __nb_objects: A private class attribute.
    id: constructor attribute.
Methods:
    __init__(self, id=None): class constructor.
"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
