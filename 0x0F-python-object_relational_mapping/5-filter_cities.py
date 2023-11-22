#!/usr/bin/python3

"""
This script displays all values in the cities table of hbtn_0e_0_usa
where the name matches the provided argument.


Usage: ./5-filter_cities.py <mysql_username> <mysql_password> \
                                    <database_name> <state_name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([city[2] for city in cur.fetchall()
                     if city[4] == sys.argv[4]]))
