#!/usr/bin/env python3

import sqlite3
import mysql.connector


#from config import *

base = sqlite3.connect( "data/dnsmgr.db" )
cursor = base.cursor()

#base.execute( "CREATE TABLE IF NOT EXISTS {} (login, password)".format( "data" ))
#base.commit()

#cursor.execute( "INSERT INTO data VALUES( ?, ? )", ( "antonii2014", "qwerty1234"))
#base.commit()

#cursor.execute( "INSERT INTO data VALUES( ?, ? )", ( "pawlik1981", "qwerty4321"))
#base.commit()

request = cursor.execute( "SELECT * FROM record" ).fetchall()
print( request )


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rekt,zrf_2020",
        database="new.bd"
        )

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute( sql, val )

mydb.commit()

print( mycursor.rowcount, "record inserted." )
