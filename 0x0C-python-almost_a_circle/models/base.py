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
        """
        Convert a list of dictionary into a JSON string.
        Args:
            list_dictionaries (list): A list of dictionary to be converted.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file.
        Args:
            list_objs(list): A list of instance to be saved.
        Raises:
            ValueError: if cls is not a subclass of Base.
        """
        if cls is not Base and not issubclass(cls, Base):
            raise ValueError("cls must be a subclass of Base")

        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(dict_list)

        with open(file_name, 'w') as f:
            f.write(json_str)

    def from_json_string(json_string):
        """
        Convert a JSON strint into a list of dictionaries.

        Args:
           json_string (str): JSON string representing a list of dictionaries.

       Returns:
           list: List of dictionaries represented my json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on a dictionary.
        Args:
            **dictionary: Dictionary containing attribute names and values.

        Returns:
            cls: An instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Unsupported class")

        # Use the update method to assign attributes from the dictionary
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.
        Returns:
            list: List of instances loaded from the file.
        """
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, 'r') as f:
                json_str = f.read()
        except FileNotFoundError:
            return []

        json_list = cls.from_json_string(json_str)
        instances = [cls.create(**item) for item in json_list]
        return instances
