#!/usr/bin/python3
"""Defines module that define student class"""


class Student:
    """Defines a class student"""
    def __init__(self, first_name, last_name, age):
        """inistatiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary"""
        return self.__dict__
