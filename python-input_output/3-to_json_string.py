#!/usr/bin/python3
import json
"""
function that returns the JSON representation of an object (string):
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Argument:
    - my_obj: The object to be serialized to JSON.

    Returns:
    - str: The JSON representation of the object.

    """

    return json.dumps(my_obj)
