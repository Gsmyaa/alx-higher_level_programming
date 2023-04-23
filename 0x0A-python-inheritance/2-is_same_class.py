#!/usr/bin/python3
"""Defines modules if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """checks if obj is instance of a_class
    Args:
        obj : the object to check.
	a_class: the class to check for obj.
    Returns:
	  True, if obj is an instance of a_class
          False, otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
