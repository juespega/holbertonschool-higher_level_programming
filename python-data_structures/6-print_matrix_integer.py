#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for indx, val in enumerate(row):
            if indx != len(row) - 1:
                print(val, end=" ")
            else:
                print("{:d}".format(val), end="")
        print()
