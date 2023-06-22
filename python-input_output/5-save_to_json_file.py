#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Arguments:
    - my_obj: The object to be written to the file.
    - filename: The name of the file to write the object to.

    The function uses the `json` module to convert the object into
    its JSON representation and writes it to the file.

    Usage:
    - save_to_json_file(my_object, "file.json")  # Writes the object
    to the JSON file
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
