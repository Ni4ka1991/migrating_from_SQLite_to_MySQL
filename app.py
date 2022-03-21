#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error
import mysql.connector as mqlc
from config import *

path = f"data/{db_from_name}"

def create_connection( path ):
    connection = None
    try:
        connection = sqlite3.connect( path )
        print("Connection to SQLite DB successful")
    except Error as err:
        print(f"The error '{err}' occurred")

    return connection

base = create_connection( path )
cursor = base.cursor()
a = cursor.execute( "SELECT name, dtype FROM domain" )
#cursor.execute( "SELECT * FROM record" )
print( a.fetchall() )




###### mysql ###
try:
    mydb = mqlc.connect( host="localhost", user="root", password="qwerty258", database="information_schema" )
    print("Connection to Mariadb DB successful")
    cursor = mydb.cursor()
    cursor.execute( "SELECT * FROM ALL_PLUGINS" )
except mqlc.Error as err:
    print( f"Are you forget to srart mariadb server?: {err}" )


