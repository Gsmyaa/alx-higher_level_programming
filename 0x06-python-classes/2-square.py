#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    initialize object with private
    instances.
    """
    def __init__(self, size=0):
        """
        Args:
            size: size of the new square.
        """
        self.__size = size
        try:
            assert type(size) == int
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
