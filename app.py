#!/usr/bin/env python3

import sqlite3
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
