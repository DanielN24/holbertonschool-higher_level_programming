#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa: """


if __name__ == '__main__':
    """ Module to select states"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    st = sys.argv[4].split('\'')
    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY \
states.id ASC".format(st[0])

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
