#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    elif idx < 0 or idx >= len(my_list):
        return my_list[:] # Return a copy of the original list
    else:
        new_list = my_list[:]  # Create a copy of the original list
        new_list[idx] = element  # Replace the element at the specified index
        return new_list