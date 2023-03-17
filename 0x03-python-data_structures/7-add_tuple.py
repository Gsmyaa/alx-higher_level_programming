#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplec = ()
    if len(tuple_b) == 2:
        tuplec = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_b) == 1:
        tuplec = (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif len(tuple_b) == 0:
        tuplec = (tuple_a[0], tuple_a[1])
    elif len(tuple_a) == 1:
        tuplec = (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_a) == 0:
        tuplec = (tuple_b[0], tuple_b[1])
    return tuplec
