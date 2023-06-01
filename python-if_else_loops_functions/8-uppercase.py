#!/usr/bin/python3
def uppercase(s):
    for char in s:  # recorrer el string caracter por caracter
        ascii_val = ord(char)  # asignar el valor en num entero del caracter
        # validar si el num está en el rango de min(ASCII range: 97-122)
        if 97 <= ascii_val <= 122:
            # conv a may, se resta 32 al val actual, lo que da la letra en may
            uppercase_char = chr(ascii_val - 32)
            print(uppercase_char, end='')
        else:
            print(char, end='')
    print()  # imprimir nueva línea
