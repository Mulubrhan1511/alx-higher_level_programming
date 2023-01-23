#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format('2'))
        return True
    except ValueError:
        return False
