#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

# compute addition
    print("{} + {} = {}".format(a, b, add(a, b)))
# compute substraction
    print("{} - {} = {}".format(a, b, sub(a, b)))
# compute multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))
# compute division
    print("{} / {} = {}".format(a, b, div(a, b)))
