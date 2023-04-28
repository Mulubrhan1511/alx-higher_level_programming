#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        payload = {'q': ''}
    else:
        payload = {'q': sys.argv[0]}
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        file = r.json()
        if file == {}:
            print('No result')
        else:
            print("[{}] {}".format(file.get("id"), file.get("name")))
    except ValueError:
        print("Not a valid JSON")