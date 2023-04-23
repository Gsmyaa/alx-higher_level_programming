#!/usr/bin/python3
"""Defines module returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Returns list of attributes and methods"""
    return dir(obj)
