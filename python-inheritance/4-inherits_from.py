#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Arguments:
    obj -- The object to check.
    a_class -- The class to compare against.

    Returns:
    True if the object is an instance of a class that inherited from
    the specified class; False otherwise.
    """
    if (issubclass(type(obj), a_class)) and (type(obj) != a_class):
        return True
    else:
        return False
