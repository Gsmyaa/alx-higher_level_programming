#!/usr/bin/python3
"""module that defines a class student"""


class Student:
    """represent a student"""
    def __init__(self, first_name, last_name, age):
        """initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        Student instance
        if attrs is list of strings, include only attributes
        """
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
