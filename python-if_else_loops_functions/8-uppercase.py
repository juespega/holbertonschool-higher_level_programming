#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            ascii_val = chr(ascii_val - 32)
        print("{}".format(ascii_val), end='')
    print()
