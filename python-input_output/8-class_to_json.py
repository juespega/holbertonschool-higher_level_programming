#!/usr/bin/python3
"""
function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Arguments:
    - obj: An instance of a class.

    Returns:
    - dict: The dictionary description of the object.

    """
    # Create an empty dictionary to store the object attributes
    obj_dict = {}

    # Iterate over the object's attributes
    for attr in dir(obj):
        # Ignore private and special attributes
        if not attr.startswith('__'):
            # Get the attribute value
            value = getattr(obj, attr)

            # Check if the value is serializable
            if isinstance(value, (list, dict, str, int, bool)):
                # Add the serializable value to the dictionary
                obj_dict[attr] = value

    return obj_dict
