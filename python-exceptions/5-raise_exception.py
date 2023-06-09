#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Example type exception")
    except TypeError as e:
        raise e
