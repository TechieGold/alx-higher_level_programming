#!/usr/bin/python3

""" 
This script lists all states from the database hbtn_0e_0_usa.

Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb as DB
import os

if __name__ == '__main__':
    
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')
    host =  os.getenv(' DB_HOST')
    port = int(os.getenv('DB_PORT'))
    database = os.getenv('DB_DATABASE')
    
    db_connect = DB.connect(host="127.0.0.1", port=port, user=user, passwd=password, db=database, charset='uft8')
    cursor = db_connect.cursor()
    sql = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(sql)
    
    selected_rows = cursor.fetchall()
    
    for row in selected_rows:
        print(row)
    cursor.close()
    db_connect.close()
    
    print('All good.....')
    