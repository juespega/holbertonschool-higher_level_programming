#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # Si el diccionario está vacío
        return None

    # Inicializar la puntuación máxima con un valor muy pequeño
    max_score = float("-inf")
    best_key = None

    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_score:
            max_score = value
            best_key = key

    return best_key
