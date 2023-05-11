#!/usr/bin/python3
"""Defines module that returns object(python)
"""
import json


def from_json_string(my_str):
    """Defines method that change JSON to python object
    arguments:
        my_str - JSON string
    returns: python object
    """
    return json.loads(my_str)
