#!/usr/bin/python3
"""
Display all values in the states table of hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cur = db.cursor()
    cur.execute(
        "SHOW * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;")
    states = cur.fetchall()

    for state in states:
        print(state)
