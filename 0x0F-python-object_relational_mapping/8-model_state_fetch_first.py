#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import MySQLdb
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)    
    cur = db.cursor()

    cur.execute("SELECT * FROM states")

    myresult = cur.fetchall()

    if len(myresult) == 0:
        pass
    else:
        print(myresult[0][0], end='')
        print(': ' + myresult[0][1])
