#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    else:
        # return [num % 2 == 0 for num in my_list]
        list_result = []
        for item in my_list:
            if item % 2 == 0:
                list_result.append(True)
            else:
                list_result.append(False)
        return list_result
