#!/usr/bin/python3
"""check if obj is an instance of a class that inherited
    (directly or indirectly) from a class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that
        inherits from a_class.
    """


def inherits_from(obj, a_class):
    """Check if an object inherits from a specific class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
