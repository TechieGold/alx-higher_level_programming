#!/usr/bin/python3
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public Methods:
        printed_sorted(self): prints the list in ascendding sorted order.

    Attributes:
        Inherits all methods and attributes from the built-in list class.
    """
    def print_sorted(self):
        """ Prints element of the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
