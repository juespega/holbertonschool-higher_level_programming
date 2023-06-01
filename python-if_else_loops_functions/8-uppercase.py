#!/usr/bin/python3
def uppercase(s):
    for char in s:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            uppercase_char = chr(ascii_val - 32)
            print("{}".format(uppercase_char), end='')
        else:
            print("{}".formta(char), end='')
