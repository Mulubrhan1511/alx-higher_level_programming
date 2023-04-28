#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
from requests import post
import sys 

if __name__ == "__main__":
    pay = {'email': sys.argv[2]}
    result = post(sys.argv[1], data=pay)
    print(result.text)