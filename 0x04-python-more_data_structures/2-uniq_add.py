#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    result = 0
    for i in new_list:
        result += i
    return result
