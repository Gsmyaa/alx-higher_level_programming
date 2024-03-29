#!/usr/bin/python3
"""Defines functions that prints a square with #."""


def print_square(size):
    """Prints square with char '#'.
    Args:
        size: the size length of the square.
    Raises:
          TypeError: If size is not an integer.
          ValueError: If size if < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
