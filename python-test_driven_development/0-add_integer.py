#!/usr/bin/python3
"""

"""

def add_integer(a, b=98):
    """This function adds two integers.
    Args:
        a (int): The first number. b (int): The second number.
    Returns:
        Returns an integer: the addition of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
