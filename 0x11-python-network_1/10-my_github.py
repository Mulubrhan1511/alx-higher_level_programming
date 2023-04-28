#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    file = requests.auth.HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=file)
    print(r.json().get("id"))
