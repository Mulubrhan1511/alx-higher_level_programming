#!/usr/bin/python3
""" takes URL, email and  encodes the email """
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":

    filee = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    request = urllib.request.Request(sys.argv[1], filee)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))