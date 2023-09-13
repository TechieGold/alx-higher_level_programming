#!/usr/bin/python3
"""This module contain function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from json file"""
    with open(filename, "r", encoding="UTF-8") as file:
        json_str = file.read()
        file_obj = json.loads(json_str)
        return (file_obj)
