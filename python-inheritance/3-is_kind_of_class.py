#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or inherited from, a specified class.

    Arguments:
    obj -- The object to check.
    a_class -- The class to compare against.

    Returns:
    True if the object is an instance of, or inherited from, the specified
    class; False otherwise.
    """
    return isinstance(obj, a_class) or a_class in obj.__class__.__bases__
