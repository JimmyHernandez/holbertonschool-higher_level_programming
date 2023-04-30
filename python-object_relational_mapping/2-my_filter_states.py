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
                         state=sys.argv[4],
                         port=3306)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name='{}' COLLATE utf8mb4_bin ORDER BY id ASC;".format(state))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
