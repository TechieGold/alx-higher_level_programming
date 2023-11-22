#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the provided argument (safe from MySQL injection).

Usage: ./ 3-my_safe_filter_states.py <mysql_username> <mysql_password>\
    <database_name> <state_name_searched>
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    state_name_searched = sys.argv[4]

    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")

    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
