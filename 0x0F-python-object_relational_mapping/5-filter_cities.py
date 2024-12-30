#!/usr/bin/python3
"""
5-filter_cities
A script that takes in the name of a state as a argument
and lists all cities of that state using database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    connect = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
            )
    cursor = connect.cursor()
    cursor.execute(
            """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            """,
            (sys.argv[4],)
            )
    rows = cursor.fetchall()
    cursor.close()
    connect.close()
    index = 0
    if len(rows) >= 1:
        for row in rows:
            if index < len(rows) - 1:
                print(row[0], end=', ')
            else:
                print(row[0])
            index += 1
    else:
        print()
