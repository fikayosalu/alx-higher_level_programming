#!/usr/bin/python3
"""
2-my_filter_states module
A script that takes in an argument and displays all values
in the states table where name matches the argument
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
    state_name = sys.argv[4]
    cursor = connect.cursor()
    cursor.execute("\
    SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    rows = cursor.fetchall()
    if rows:
        for item in rows:
            print(item)
    else:
        print()

    cursor.close()
    connect.close()
