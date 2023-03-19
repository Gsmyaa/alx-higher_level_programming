#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in matrix:
        matrix_row = []
        for j in i:
            matrix_row.append(j**2)
        matrix2.append(matrix_row)
    return matrix2
