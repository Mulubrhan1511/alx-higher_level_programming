#!/usr/bin/python3
"""
python script
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], charset="utf8", port=3306)
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s;', ('{}'.format(argv[4]),))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
