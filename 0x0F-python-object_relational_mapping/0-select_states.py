#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv


def main():
    '''main'''
    database = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2],
        db=argv[3])
    cursor = database.cursor()
    cursor.excute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
