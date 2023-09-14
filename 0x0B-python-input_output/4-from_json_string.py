#!/usr/bin/python3
"""This module function that returns an object
(Python data structure)represented by a JSON string"""


def from_json_string(my_str):
    """Returns an object representation of json string"""
    return eval(my_str)
