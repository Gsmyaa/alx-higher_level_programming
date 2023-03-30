#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Instantiation with size,
       by private instance size
    """
    def __init__(self, size):
        """Args:
                size(int): size of new square.
        """
        self.__size = size
