import sqlite3

connection=sqlite3.connect('database.db')

with open('student_content.sql') as f:
	connection.executescript(f.read())
	
cur=connection.cursor()

cur.execute("insert into student (username,name,pwd,due) values ('B200712CS','Ananthakrishnan M','B200712CS',0)")
cur.execute("insert into student (username,name,pwd,due) values ('B200744CS','Livin K L','B200744CS',0)")
cur.execute("insert into student (username,name,pwd,due) values ('B200722CS','Muhammed Roshan H','B200722CS',0)")
cur.execute("insert into student (username,name,pwd,due) values ('B200764CS','Bharath Ram','B200764CS',0)")

cur.execute("insert into admin (username,name,pwd) values ('A01','Karthik B','A01')")
connection.commit()
connection.close()
