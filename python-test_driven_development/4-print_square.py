#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """This function prints a square.
    Args:
        size (int)
    Returns:
        print a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
