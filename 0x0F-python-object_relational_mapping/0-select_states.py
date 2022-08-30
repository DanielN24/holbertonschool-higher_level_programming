#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    """module to select states"""

    import MySQLdb
    from sys import argv

    database = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2],
        db=argv[3])
    cursor = database.cursor()
    cursor.excute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
