#!/usr/bin/python3
"""
Crate a base class.
"""


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
