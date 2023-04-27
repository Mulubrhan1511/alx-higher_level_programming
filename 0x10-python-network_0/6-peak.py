#!/usr/bin/python3
""" Test function find_peak """

def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers[0],list_of_integers[1])
    if size == 3:
        return max(list_of_integers[0], list_of_integers[1],list_of_integers[2])
    for i in range(size):
        if list_of_integers[i] < list_of_integers[i + 1] >list_of_integers[i + 2]:
            return list_of_integers[i + 1]