#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    [print(city) for city in cur.fetchall()]
