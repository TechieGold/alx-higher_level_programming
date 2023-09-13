#!/usr/bin/python3

"""Returns True if the object is an instance of,
or if the object is an instance of a class that inherited
fromspecified class, otherwise False is returned.

Args:
    obj: The object to be checked.
    a_class: The class to compare against.

Returns:
    True if obj is an instance of a_class or any of its subclasses,
    otherwise False.
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return (True)
    for base_class in obj.__class__.mro():
        if base_class == a_class:
            return (True)
    return (False)
