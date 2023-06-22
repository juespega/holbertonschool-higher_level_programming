#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and
    returns the number of characters added.

    Arguments:
    - filename (str): The name of the file to append to (optional).
    If not provided, an empty string is assumed.
    - text (str): The string to append to the file (optional).
    If not provided, an empty string is assumed.

    If the file doesn't exist, it will be created.

    Usage:
    - append_write('file.txt', 'Hello, world!')  # Appends the string
    to the file

    Returns:
    - int: The number of characters added to the file.

    """

    with open(filename, 'a', encoding='utf-8') as file:
        num_character = file.write(text)
        return num_character
