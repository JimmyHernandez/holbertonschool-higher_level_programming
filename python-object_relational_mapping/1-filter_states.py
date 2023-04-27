#!/usr/bin/python3
"""
Lists all states with N names from
hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' COLLATE SQL_Latin1_General_CP1_CS_AS collation ORDER BY id ASC;")
    states = cur.fetchall()

    for state in states:
        print(state)
