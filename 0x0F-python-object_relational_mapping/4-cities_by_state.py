#!/usr/bin/python3
"""displays where name matches"""
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
    veronic.execute("""SELECT t2.id, t2.name, t1.name
                    FROM cities AS t2
                    JOIN states as t1
                    ON t1.id = t2.state_id ORDER BY id ASC""")
    hussa = veronic.fetchall()
    for i in hussa:
        print(i)
    n.close()


if __name__ == "__main__":
    detectme()
