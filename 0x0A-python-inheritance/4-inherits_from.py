#!/usr/bin/python3
def inherits_from(obj, a_class):
    """check if obj is an instance of a class that inherited
    (directly or indirectly) from a class.
    
    Args:
        obj: The object to be checked.
        a_class: The class to compare against.
        
    Returns:
        True if obj is an instance of a class that
        inherits from a_class.
    """
    for base_class in obj.__class__.mro():
        if base_class == a_class:
            return (True)
        return (False)