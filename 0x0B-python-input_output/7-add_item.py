#!/usr/bin/python3

"""This module contain script that adds all arguments to a Python list,
and save them to a file"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

lst = load_from_json_file("add_item.json")
lst.extend(sys.argv[1:])
save_to_json_file(lst, "add_item.json")
