#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary.pop(i)
                return a_dictionary
