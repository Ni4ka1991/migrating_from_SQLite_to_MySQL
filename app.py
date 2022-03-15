#!/usr/bin/env python3

import sqlite3

base = sqlite3.connect( "new.db" )
cursor = base.cursor()
base.execute( "CREATE TABLE IF NOT EXISTS {} (login, password)".format( "data" ))
base.commit()

cursor.execute( "INSERT INTO data VALUES( ?, ? )", ( "antonii2014", "qwerty1234"))
base.commit()
cursor.execute( "INSERT INTO data VALUES( ?, ? )", ( "pawlik1981", "qwerty4321"))
base.commit()
