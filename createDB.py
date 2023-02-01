import sqlite3
con = sqlite3.connect("fblaproject.db")
cur = con.cursor() 
cur.execute("CREATE TABLE School(name, county, id, events, students, teachers, schoolStoreBool, schoolStore)")