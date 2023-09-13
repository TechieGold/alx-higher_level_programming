#!/usr/bin/python3
"""This module function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="UTF-8") as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)
