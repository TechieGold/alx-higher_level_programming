#!/usr/bin/python3
"""
This module contains a base class with attribute and constructor.
Attributes:
    __nb_objects: A private class attribute.
    id: constructor attribute.
Methods:
    __init__(self, id=None): class constructor.
    def to_json_string(list_dictionaries):
        Convert and return a list of dictionaries to a JSON string.
"""
import json


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

    def to_json_string(list_dictionaries):
        """Convert a list of dictionary into a JSON string.
        Args:
            list_dictionaries (list): A list of dictionary to be converted.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file.
        Args:
            list_objs(list): A list of instance to be saved.
        Raises:
            ValueError: if cls is not a subclass of Base.
        """
        if not isinstance(cls, Base):
            raise ValueError("cls must be a subclass of Base")

        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.json"
        json_str = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])

        with open(file_name, 'w') as f:
            f.write(json_str)
