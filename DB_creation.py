#!/usr/bin/python3

import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('June_labCC.db')
print("Database creato correttamente")
# Create SITE table
conn.execute('''CREATE TABLE "SITE" (
	"WordID"	INTEGER,
	"Link"	TEXT NOT NULL,
	"Modulo"	TEXT,
	"Parent"	TEXT NOT NULL,
	"SQLJ"	INTEGER DEFAULT 0,
	"Notes"	TEXT,
	PRIMARY KEY("WordID" AUTOINCREMENT)
);''')

print("Table 'SITE' creata correttamente")
