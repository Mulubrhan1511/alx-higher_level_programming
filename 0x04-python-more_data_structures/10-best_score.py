#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        max = 0
        for i in a_dictionary:
            if a_dictionary[i] > max:
                max = a_dictionary[i]
            else:
                pass
        for i in a_dictionary:
            if a_dictionary[i] == max:
                return i
    return None
