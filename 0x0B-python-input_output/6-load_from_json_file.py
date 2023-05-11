#!/usr/bin/python3
"""Defines module that creates an object
from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """Defines method that loads from
    json file
    arguments:
        filename - name of file
    """
    with open(filename) as f:
        return json.load(f)
