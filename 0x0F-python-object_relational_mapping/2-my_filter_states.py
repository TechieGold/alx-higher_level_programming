#!/usr/bin/python3

"""
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the provided argument.


Usage: ./2-my_filter_states.py <mysql_username> <mysql_password>
<database_name> <state_to_find>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3])
    cur = db_connect.cursor()
    cur.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
