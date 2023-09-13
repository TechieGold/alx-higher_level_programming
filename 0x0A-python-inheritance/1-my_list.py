#!/usr/bin/python3
"""
    This module create custom list class
    that inherits from the built-in list class.

    class: MyList(list)

    Public Methods:
        printed_sorted(self): prints the list in ascendding sorted order.

    Attributes:
        Inherits all methods and attributes from the built-in list class.
    """


class MyList(list):
    """custom list class that inherits from the built-in list class"""

    def print_sorted(self):
        """ Prints element of the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
