#!/usr/bin/python3
"""module that defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student.

        Arguments:
            first_name (str) - first name of the student.
            last_name (str) - last name of the student.
            age (int) - age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that define dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Arguments:
            attrs (list) - The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Arguments:
            json (dict) - key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
