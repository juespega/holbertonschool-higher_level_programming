#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    result = sum(new_list)
    return result

# return (sum(set(my_list))
