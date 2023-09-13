#!/usr/bin/python3
"""that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """Returns the dictionary description"""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    elif isinstance(obj, (int, str, bool, list, dict)):
        return obj
