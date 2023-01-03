#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 127:
            num = 32
            print(f"{chr(ord(str[i]) - num)}", end='')
        else:
            print(f"{chr(ord(str[i]))}", end='')
    print()
