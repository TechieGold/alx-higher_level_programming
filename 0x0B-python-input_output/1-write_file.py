#!/usr/bin/python3
"""This modulw contain a function that writes a string
to a file and return the number of chatacters written"""


def write_file(filename="", text=""):
    """writes a string to a text file and
    returns the number of chars written"""
    with open(filename, "w", encoding="UTF-8") as file:
        nb_chars = file.write(text)
    return nb_chars
