#!/usr/bin/python3
def uppercase(str):
        for i in range(len(str)):
            if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
                c = chr(ord(str[i]) - 32)
            else:
                c = str[i]
            print("{:}".format(c), end="")
        print()
