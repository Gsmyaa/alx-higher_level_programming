#!/usr/bin/python3
def uppercase(str):
    if str:
        n = len(str) - 1
        for i in range(len(str)):
            if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
                c = chr(ord(str[i]) - 32)
            else:
                c = str[i]
            print("{}".format(c) if i == n else "{}".format(c), end="")
#print()
    else:
        print()
