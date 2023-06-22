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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
        - dict: The dictionary representation of the Student instance.

        """
        # Create a dictionary to store the student attributes
        student_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

        return student_dict
