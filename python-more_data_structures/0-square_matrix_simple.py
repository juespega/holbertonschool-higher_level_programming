#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Create a new matrix with the same size as the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    new_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    # Iterate over each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Compute the square value of the current element and store it in the result matrix
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
