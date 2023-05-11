#!/usr/bin/python3
"""Defines module that returns JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """Defines a method that changes to json
    anguments:
        my_obj - javascript
    returns:
        string JSON
    """
    return json.dumps(my_obj)
