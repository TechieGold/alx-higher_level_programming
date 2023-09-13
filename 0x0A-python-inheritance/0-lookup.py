#!/usr/bin/python3
"""
Lists the attribute and method of an object.

Args:
    obj(object): Object to inspect

Return:
    A list containing the methods and attributes of an object.
"""


def lookup(obj):
    attributes_and_methods = dir(obj)

    return (list(attributes_and_methods))
