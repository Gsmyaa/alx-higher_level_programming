#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return str
    else:
        my_str = str.replace(str[n], "")
        return my_str
