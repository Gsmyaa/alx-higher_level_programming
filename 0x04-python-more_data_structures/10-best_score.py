#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        bigvl = 0
        for i in a_dictionary:
            if a_dictionary[i] > bigvl:
                bigvl = a_dictionary[i]
        for i in a_dictionary:
            if a_dictionary[i] == bigvl:
                return i
