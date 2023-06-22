#!/usr/bin/python3
"""
class Student that defines a student by:
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name,
        last name, and age.

        Arguments:
        - first_name: The first name of the student (string).
        - last_name: The last name of the student (string).
        - age: The age of the student (integer).

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Arguments:
        - attrs (optional): A list of attribute names (strings)
        to be retrieved.

        Returns:
        - dict: The dictionary representation of the Student instance.

        """
        # If attrs is not provided or is not a list, retrieve all attributes
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        # Create a dictionary to store the selected attributes
        selected_attrs = {}

        # Retrieve only the attributes in the given attrs list
        for attr in attrs:
            if attr in self.__dict__:
                selected_attrs[attr] = self.__dict__[attr]

        return selected_attrs
