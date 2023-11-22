#!/usr/bin/python3

"""
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the provided argument.

Usage: ./2-my_filter_states.py <mysql_username> <mysql_password>
<database_name> <state_to_find>
"""
import MySQLdb as DB
import sys

if __name__ == '__main__':
    db_connect = DB.connect(host='localhost', port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], database=sys.argv[3])
    cursor = db_connect.cursor()
    sql = "SELECT * FROM `states` WHERE `name` = %s ORDER BY `id`"
    state_to_find = sys.argv[4]
    cursor.execute(sql, (state_to_find,))

    matching_states = cursor.fetchall()

    for state in matching_states:
        print(state)
    cursor.close()
    db_connect.close()
