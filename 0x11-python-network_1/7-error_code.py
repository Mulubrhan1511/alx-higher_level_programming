#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    m = r.status_code
    if m >= 400:
        print("Error code: {}".format(m))
    else:
        print(r.text)
