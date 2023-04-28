#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    repos = sys.argv[2]
    commit = sys.argv[1]
    url = 'https://api.github.com/repos/' + repos + '/' + commit + '/commits'
    r = requests.get(url)
    my_fiile = r.json()
    for i in range(10):
            print("{}: {}".format(
                my_fiile[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))