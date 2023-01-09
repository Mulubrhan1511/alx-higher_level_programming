#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        for idx, num in enumerate(elem):
            open_string = "{}"
            if idx != len(elem) - 1:
                print(open_string.format(num), end=' ')
            else:
                print(open_string.format(num), end='')
        print()
