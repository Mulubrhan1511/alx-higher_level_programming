#!/usr/bin/python3
""" takes URL, email and  encodes the email """
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    filee = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, filee)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))