#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    Private instance attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        to retrieve private instance attribute size
        """
        return self.__size

    @property
    def position(self):
        """to retrieve private instance attribute position"""
        return self.__position

    @size.setter
    def size(self, value):
        """
        to set private instance attribute
        """
        self.__size = value
        try:
            assert type(value) == int
        except BaseException:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        """to set position, a tuple of two integers"""
        self.__position = value
        try:
            assert type(value) == tuple
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert type(value[0]) == int or type(value[1]) == int
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        print squre using #
        """
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print("\n")
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
