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
        self.__size = size

    @property
    def size(self):
        """Retrieve private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting private instance attrubute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    return square of an object
    """
    def area(self):
        return self.__size ** 2
