#!/usr/bin/python3
"""This module contains a class (MyInt)that inherits
    from the built-in int class
    But override the behaviour of the equality(==)
    and inequality (!=)
    to provide inverted result

    methods:
        __equal__ : "Override the equality operator (!=)
        to return the inverted result.
        __notequal__: "Override the inequality operator (!=)
        to return the inverted result
"""


class MyInt(int):
    """A class that inherits from the built-int int class"""
    def __equal__(self, other):
        """Overides the equality operator to return the inverted result."""
        return super().__ne__(other)

    def __notequal__(self, other):
        """Override the inequality operator (!=)
        to return the inverted result."""
        return super().__eq__(other)
