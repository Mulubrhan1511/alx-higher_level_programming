#!/usr/bin/python3
def islower(c): #return true if c is lower
    "function that check if c is lower or upper case"
    x = int(ord(c))
    if x >= 97 and x <= 127:
        return True
    else:
        return False
