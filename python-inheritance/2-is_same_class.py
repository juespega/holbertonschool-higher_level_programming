#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Arguments:
    obj -- The object to check.
    a_class -- The class to compare against.

    Returns:
    True if the object is exactly an instance of the specified class;
    False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
