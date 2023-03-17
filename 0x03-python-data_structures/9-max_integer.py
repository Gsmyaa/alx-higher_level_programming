#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        larg = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > larg:
                larg = my_list[i]
        return larg
    else:
        return None
