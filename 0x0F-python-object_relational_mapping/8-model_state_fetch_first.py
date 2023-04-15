#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import MySQLdb
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], charset="utf8", port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states")

    myresult = cur.fetchall()

    if len(myresult) == 0:
        pass
    else:
        print(myresult[0][0], end='')
        print(': ' + myresult[0][1])
