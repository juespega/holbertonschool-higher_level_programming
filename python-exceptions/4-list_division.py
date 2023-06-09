#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for item in range(list_length):
        try:
            divides = (my_list_1[item] / my_list_2[item])

        except TypeError:
            divides = 0
            print("wrong type")

        except ZeroDivisionError:
            divides = 0
            print("division by 0")

        except IndexError:
            divides = 0
            print("out of range")

        finally:
            result.append(divides)

    return result
