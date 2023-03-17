#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{:d}".format(i))
    else:
        print("{:d}".format(i) if i >= 10 else "0{:d}".format(i), end=", ")
