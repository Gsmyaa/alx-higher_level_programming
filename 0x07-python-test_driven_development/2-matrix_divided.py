#!/usr/bin/python3
"""Defines a function that divides matrix."""


def matrix_divided(matrix, div):
    """Returns a new matrix, product of matrix division by int

    Matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError.

    div:
        can't be equal to 0, otherwise raise exception.

    All elements fo the matrix should be divided by div
    , rounded to 2 decimal places.
    """
    for i in matrix:
        for j in i:
            if (not isinstance(j, int) and not isinstance(j, float)):
                raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    row_len = []
    for i in matrix:
        row_len.append(len(i))
    for i in matrix:
        for j in row_len:
            if len(i) != j:
                raise TypeError("Each row of the \
matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_list = []
        for elem in row:
            num = round(elem / div, 2)
            new_list.append(num)
        new_matrix.append(new_list)
    return new_matrix
