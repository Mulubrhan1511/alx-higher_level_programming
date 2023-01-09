#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for idx, x in enumerate(my_list):
        if x % 2 == 0:
            my_list[idx] = True
        else:
            my_list[idx] = False
    return my_list
