#!/usr/bin/python3
"""Defines module that writes an object
to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Defines method that save to JSON file
    arguments:
        my_obj - JSON object
        filename - name of file
    returns: nothing
    """
    with open(filename, encoding='utf-8', mode='w') as f:
        json.dump(my_obj, f)
