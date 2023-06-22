#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Returns Pascal's triangle as a list of lists of integers.

    Arguments:
    - n: The number of rows in Pascal's triangle (integer).

    Returns:
    - list: Pascal's triangle represented as a list of lists
    of integers.

    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # Initialize each row with a 1 at the beginning
        if i > 0:
            prev_row = triangle[i-1]
            for j in range(len(prev_row) - 1):
                # Sum the adjacent values in the previous row
                row.append(prev_row[j] + prev_row[j+1])
            row.append(1)  # Add a 1 at the end of each row
        triangle.append(row)

    return triangle
