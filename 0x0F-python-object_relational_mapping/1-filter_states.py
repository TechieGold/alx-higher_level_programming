#!/usr/bin/python3

"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")

    [print(state_with_n) for state_with_n in cur.fetchall()]

    cur.close()
    db.close()
