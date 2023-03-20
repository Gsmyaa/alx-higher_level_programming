#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_set = []
    for i in set_1:
        tes = True
        for j in set_2:
            if i == j:
                my_set.append(i)
                break
    my_set = set(my_set)
    return my_set
