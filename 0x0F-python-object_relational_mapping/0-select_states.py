#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

def main():
    database = MySQLdb.connect(
        host='localhost', username=argv[1], password=argv[2],
        database=argv[3])
    cursor = database.cursor()
    cursor.excute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


if __name__ == "__main__":
    main()

