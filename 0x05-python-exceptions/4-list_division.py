#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
            new_list.insert(i, x)
        except ZeroDivisionError:
            print("zero")
            new_list.insert(i, 0)
        except TypeError:
            print("type error")
            new_list.insert(i, 0)
        except IndexError:
            print("Index error")
            new_list.insert(i, 0)
    return new_list
