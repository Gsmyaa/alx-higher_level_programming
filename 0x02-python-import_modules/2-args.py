#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n - 1 == 0:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(n - 1))
    for i in range(1, n):
        print("{:d}: {}".format(i, str(sys.argv[i])))
