#!/usr/bin/python3
"""List All states inside hbtn_0e_0_usa db """

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # name_search = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    query_s = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query_s = query_s.format(argv[4])
    cur.execute(query_s)

    result = cur.fetchall()
    for sta in result:
        print(sta)

    cur.close()
    db.close()
