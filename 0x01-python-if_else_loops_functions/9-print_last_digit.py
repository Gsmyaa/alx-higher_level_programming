#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    la = number % 10
    print(la, end="")
    return la
