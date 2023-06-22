#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Argument:
    - filename (str): The name of the JSON file.

    Returns:
    - object: The Python object created from the JSON file.

    """

    with open(filename, 'r') as file:
        data = json.load(file)
        return data
