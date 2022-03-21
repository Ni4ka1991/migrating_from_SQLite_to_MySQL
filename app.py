#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error
import mysql.connector as mqlc
from config import *

path = f"data/{db_from_name}"

def create_connection_SQLite( path ):
    connection = None
    try:
        connection = sqlite3.connect( path )
        print("Connection to SQLite DB successful")
    except Error as err:
        print(f"The error '{err}' occurred")

    return connection


def create_connection_MySQL( host_name, user_name, user_password, database ):
    connection = None
    try:
        mydb = mqlc.connect( host_name, user_name, user_password, database )
        print("Connection to Mariadb DB successful")
        cursor = mydb.cursor()
        cursor.execute( "SELECT * FROM ALL_PLUGINS" )
    except mqlc.Error as err:
        print( f"Are you forget to srart mariadb server?: {err}" )
    
    return connection


def create_execute( connection, query ):
        cursor = connection.cursor()
        try:
            cursor.execute( query )
            print( f"\"{query}\" was successfully")
        except Error as err:
            print(f"The error '{err}' occurred")



'''
base_SQLite = create_connection_SQLite( path )
a = create_execute( base_SQLite, "SELECT name, dtype FROM domain" )
print( a )
'''
base_MySQL = create_connection_MySQL( host_name, user_name, user_password, "information_schema" )
