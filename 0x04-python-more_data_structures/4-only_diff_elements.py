#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    comm_list = []
    odd_list = []
    for i in set_1:
        for j in set_2:
            if i == j:
                comm_list.append(i)
                break
    for n in set_1:
        test = True
        for i in comm_list:
            if n == i:
                test = False
                break
        if test:
            odd_list.append(n)
    for m in set_2:
        test2 = True
        for i in comm_list:
            if m == i:
                test2 = False
                break
        if test2:
            odd_list.append(m)
    odd_list = set(odd_list)
    return odd_list
