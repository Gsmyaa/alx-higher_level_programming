#!/usr/bin/python3
def uppercase(str):
    if str:
        my_str = []
        for i in range(len(str)):
            if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
                my_str.append(chr(ord(str[i]) - 32))
            else:
                my_str.append(str[i])
            print("{}".format(my_str[i]), end="")
        print()
