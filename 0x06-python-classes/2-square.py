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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
