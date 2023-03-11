#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n - 1 == 0:
        print("{} arguments.".format(n - 1))
    if n - 1 > 0:
        print("{} arguments:".format(n - 1))
    for i in range(1, n):
        print("{}: {}".format(i, str(sys.argv[i])))
