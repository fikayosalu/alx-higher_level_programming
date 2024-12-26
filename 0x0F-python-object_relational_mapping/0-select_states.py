#!/usr/bin/python3
"""
0-select_states module
A python script that lists all states from the database:
hbtn_0e_0_usa
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

    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()

    for items in result:
        print(items)

    cursor.close()
    connect.close()
