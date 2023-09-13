#!/usr/bin/python3
"""
Lists the attribute and method of an object.

Args:
    obj(object): Object to inspect

Return:
    A list containing the methods and attributes of an object.
"""


def lookup(obj):
    """Returns the list of available methods
    and attributes of an object"""
    return (dir(type))
