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
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """instantiates the public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
