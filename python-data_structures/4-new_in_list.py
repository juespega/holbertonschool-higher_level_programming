#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # retorna una copia de la lista original
    new_list = my_list[:]  # crea una copia de la lista original
    new_list[idx] = element  # Se remplaza el elemento en el indice indicado
    return new_list
