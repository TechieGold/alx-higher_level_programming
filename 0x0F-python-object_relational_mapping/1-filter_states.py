#!/usr/bin/python3

"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb as DB
import sys

if __name__ == '__main__':
    db_connect = DB.connect(host='localhost', port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], database=sys.argv[3])
    cursor = db_connect.cursor()
    sql = "SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`"
    cursor.execute(sql)

    states_with_n = cursor.fetchall()

    for state in states_with_n:
        print(state)
    cursor.close()
    db_connect.close()
