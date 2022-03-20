#!/usr/bin/env python3

import sqlite3
import mysql.connector as mqlc
from config import *


base = sqlite3.connect( f"data/{db_from_name}" )
cursor = base.cursor()
cursor.execute( "SELECT * FROM domain" )
request = cursor.fetchall()


k = 1
for row in request:
    print( f"id = {row[0]}; name = {row[1]}; dtype = {row[5]}" )
    k += 1


mydb = mqlc.connect( host="localhost", user="root", password="qwerty258", database="information_schema" )
cursor = mydb.cursor()
cursor.execute( "SELECT * FROM ALL_PLUGINS" )
request_mysql = cursor.fetchall()

'''
k = 1
for row in request_mysql:
    print( f"{k} >>> {row}" )
    k += 1
'''
