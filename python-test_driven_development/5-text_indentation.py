#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """
    Check if text is a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for chars in ".:?":
        text = (chars + "\n\n").join(
            [line.strip(" ") for line in text.split(chars)])

    print("{}".format(text), end="")
