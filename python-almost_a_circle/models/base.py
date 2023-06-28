#!/usr/bin/python3
"""
Crate a base class.
"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        """
        if id is not None:
            """If an "id" value is provided, assign it to the "id"
            instance variable"""
            self.id = id
        else:
            # Increment the object counter for the class
            Base.__nb_objects += 1
            # Assign the current counter value to the "id" instance variable
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries to
            convert to JSON.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

