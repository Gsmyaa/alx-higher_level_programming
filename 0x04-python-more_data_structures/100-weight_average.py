#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        tot = 0
        num = 0
        for i in my_list:
            num = num + i[1]
            pro = 1
            for j in i:
                pro = j * pro
            tot += pro
        return tot / num
    else:
        return 0
