#!/usr/bin/python3

"""this modulw contain a function that reads
a text file and print it to atdout"""


def read_file(filename=""):
    """ Reads a text file"""
    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            print(line, end='')
