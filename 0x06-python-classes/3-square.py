#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    initializing Object of class
    """
    def __init__(self, size=0):
        self.__size = self
        """
        paramaters
        size: int else TypeError
        if size < 0, ValuError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    return square of an object
    """
    def area(self):
        return self.__size ** 2
