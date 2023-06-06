#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        square_row = []
        for item in row:
            square_row.append(item ** 2)
        new_matrix.append(square_row)
    return new_matrix
