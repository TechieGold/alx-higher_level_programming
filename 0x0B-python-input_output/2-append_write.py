#!/usr/bin/python3
"""This module contain a function that appends a string
to a file and return the number of characters added"""


def append_write(filename="", text=""):
    """appends a string to a text file and
    returns the number of chars added"""
    with open(filename, "a", encoding="UTF-8") as file:
        nb_chars = file.write(text)
    return nb_chars
