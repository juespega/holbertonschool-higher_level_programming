#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Completar con ceros si la tupla es menor a 2 elementos
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    # Sumar solo los primeros 2 elementos si la tupla es mayor a 2 elementos
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Sumar los elementos correspondientes
    suma_tuplas = tuple(x + y for x, y in zip(tuple_a, tuple_b))

    return suma_tuplas
