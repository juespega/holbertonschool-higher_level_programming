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
        to retrieve.

        Returns:
        - dict: The dictionary representation of the Student instance.

        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values
        provided in the dictionary.

        Arguments:
        - json: A dictionary with the attributes and values to replace
        in the Student instance.

        """
        for attr, value in json.items():
            setattr(self, attr, value)
