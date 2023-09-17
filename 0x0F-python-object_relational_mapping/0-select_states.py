#!/usr/bin/python3
"""List All states inside hbtn_0e_0_usa db """

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

db = MySQLdb.connect(host='localhost',
                     user=username,
                     passwd=password,
                     db=db_name,
                     port=3306)

cur = db.cursor()

cur.execute("SELECT id, name FROM states ORDER BY id ASC")

result = cur.fetchall()
for sta in result:
    print(sta)

cur.close()
