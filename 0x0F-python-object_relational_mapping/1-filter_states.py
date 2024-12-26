#!/usr/bin/python3
"""
1-filter_states module
A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cursor.fetchall()
    for item in rows:
        print(item)

    cursor.close()
    connect.close()
