#!/usr/bin/python3
"""
models.square
=============

This modules defines a Square class which represents
a Square with width, height and positions
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object
        Args:
            size (int): The size of the square.
            y (int, optional): The y-coordinate of the square's position.
            x (int, optional): The  x coordinate of the square's position.
            id(int, optional): The y=unique identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return (
            f"[Square] ({self.id})"
            f" {self.x}/{self.y} - {self.width}"

        )

    def update(self, *args, **kwargs):
        """
        Update the Square attributes based on the provided
        arguments or keyword arguments.

        Args:
            *args: Variable number of positional arguments (id, size, x, y).
            **kwargs: Variable number of keyword arguments
            representing attribute-value pairs.
        """
        if args:
            arg_order = ['id', 'size', 'x', 'y']
            for i, arg_value in enumerate(args):
                setattr(self, arg_order[i], arg_value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
