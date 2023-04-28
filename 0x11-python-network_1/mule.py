#!/usr/bin/python3
""" fetches from the url"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status/') as response:
    html = response.read()
    print(html)