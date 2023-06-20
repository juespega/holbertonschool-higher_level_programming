#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object:
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Argument:
    obj -- The object for which to retrieve the attributes and methods.

    Returns:
    A list containing the attributes and methods of the object.
    """
    return dir(obj)
