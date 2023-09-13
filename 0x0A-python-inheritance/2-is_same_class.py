#!/usr/bin/python3
"""
Returns True if the object is exactly an instance
of a class otherwise False.

attr:
    obj: the object
    a_class: the class

meths:
    is_same_class(obj, a_class): checks if an obj is an instance of a_class.
"""


def is_same_class(obj, a_class):
    """Returns True if an object is an instance of a class, False otherwise."""
    return (type(obj) is a_class)
