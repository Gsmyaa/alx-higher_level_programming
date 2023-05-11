#!/usr/bin/python3
"""Defines module that writes a string to
a text file and returns the number
characters written.
"""


def write_file(filename="", text=""):
    """Defines a method that write a string
    to a text file(UTF8).
    arguments:
        filename - name of a file
        text - a string to be written
    returns:
        number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        num_char = int(f.write(text))
    return num_char
