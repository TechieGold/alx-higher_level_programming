#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.

Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb as DB
import sys

if __name__ == '__main__':
    db_connect = DB.connect(host='localhost', port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], database=sys.argv[3])
    cursor = db_connect.cursor()
    sql = "SELECT * FROM `states` ORDER BY `id`"
    cursor.execute(sql)

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db_connect.close()
