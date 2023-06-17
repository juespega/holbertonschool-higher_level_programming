#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """This function adds two integers.
    Args:
        matrix (int or float). div (int or float).
    Returns:
        Returns a new matrix"""
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(
            isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    """Check if each row of the matrix has the same size"""
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    """Check if div is a number"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """Check if div is not zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    # new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
