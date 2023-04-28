#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)