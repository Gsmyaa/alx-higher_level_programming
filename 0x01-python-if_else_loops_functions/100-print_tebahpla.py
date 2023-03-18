#!/usr/bin/python3
i = 122
j = 2
while i >= 97:
    if j % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i - 32)), end="")
    i = i - 1
    j = j + 1
