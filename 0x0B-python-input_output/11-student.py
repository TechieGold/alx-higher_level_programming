#!/usr/bin/python3
""" This modulw defines a class Student.
    Attributes:
        first_name: student first name
        last_name: student last name.
        age: student age.

    Methods:
        __init__(self, first_name, last_name, age);
            initialize a new instance of Student.
        to_json(self):
            retrieves a dictionary representation of a Student instance.
        reload_from_json(self, json):
            that replaces all attributes of the Student instance.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """instantiates the public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
