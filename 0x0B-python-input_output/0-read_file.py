#!/usr/bin/python3
"""Defines module that reads a text file
and prints it to stdout
"""


def read_file(filename=""):
    """Defines function read file
    arguments:
        filename = object that handle filename
    """
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read(), end="")
