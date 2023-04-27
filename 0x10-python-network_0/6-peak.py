#!/usr/bin/python3
def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        max = None
    else:
        max = list_of_integers[0]
        for i in list_of_integers:
            if i >= max:
                max = i
            else:
                pass
    return max