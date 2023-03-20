#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_key = sorted(list(a_dictionary.keys()))
    for i in list_of_key:
        print("{}: {}".format(i, a_dictionary.get(i)))
