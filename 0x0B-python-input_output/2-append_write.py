#!/usr/bin/python3
"""Defines module that appends a string
at the end of a text file and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """Defines a method that append a string
    to a file(UTF8).
    argument:
        filename - name of file
        text - strings to be appended
    returns:
        number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        num_char = f.write(text)
    return num_char
