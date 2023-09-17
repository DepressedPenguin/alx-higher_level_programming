#!/usr/bin/python3
"""script that takes in an argument and displays where name matches"""
import MySQLdb
import sys


def detectme():

    argvv = sys.argv
    n = MySQLdb.connect(user=argvv[1],
                        host='localhost',
                        port=3306,
                        passwd=argvv[2],
                        db=argvv[3])

    veronic = n.cursor()
    v = """SELECT t2.name FROM cities AS t2
    JOIN states as t1
    ON t1.id = t2.state_id AND t1.name = %s"""
    veronic.execute(v, (argvv[4],))
    hussa = veronic.fetchall()
    for index, i in enumerate(hussa):
        print(i[0], end=", " if index < len(hussa) - 1 else "")
    print()
    n.close()


if __name__ == "__main__":
    detectme()
