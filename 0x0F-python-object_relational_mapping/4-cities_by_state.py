#!/usr/bin/python3
"""
2-my_filter_states module
A script that takes in arguments and displays all values in the states table
whare name matches the argument and the code is safe from SQL injections
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
    cursor.execute("""
    SELECT * FROM states
    ORDER BY id ASC
    """)
    rows = cursor.fetchall()
    for item in rows:
        print(item)

    cursor.close()
    connect.close()
