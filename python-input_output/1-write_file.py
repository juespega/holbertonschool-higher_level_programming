#!/usr/bin/python3
"""
unction that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.

    Arguments:
    - filename (str): The name of the file to write to (optional).
    If not provided,
      an empty string is assumed.
    - text (str): The string to write to the file (optional).
    If not provided,
      an empty string is assumed.

    The function creates the file if it doesn't exist and overwrites
    the content of the file if it already exists.

    Usage:
    - write_file('file.txt', 'Hello, world!')  # Writes the string to the file

    Returns:
    - int: The number of characters written to the file.

    """

    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
        return num_characters
