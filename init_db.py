import sqlite3

connection=sqlite3.connect('database.db')

with open('student_content.sql') as f:
	connection.executescript(f.read())
	
cur=connection.cursor()

cur.execute("insert into student (username,name,pwd) values ('B200712CS','Ananthakrishnan M','B200712CS')")
cur.execute("insert into student (username,name,pwd) values ('B200744CS','Livin K L','B200744CS')")
cur.execute("insert into student (username,name,pwd) values ('B200722CS','Muhammed Roshan H','B200722CS')")
cur.execute("insert into student (username,name,pwd) values ('B200764CS','Bharath Ram','B200764CS')")
cur.execute("insert into student (username,name,pwd) values ('B200758CS','Yadunandan','B200758CS')")
cur.execute("insert into student (username,name,pwd) values ('B200728CS','Visakh Vijayan','B200728CS')")
cur.execute("insert into student (username,name,pwd) values ('B200686CS','Aleena Siby','B200686CS')")
cur.execute("insert into student (username,name,pwd) values ('B200718CS','Karthik B','B200718CS')")
cur.execute("insert into student (username,name,pwd) values ('B200714CS','Arjun T K','B200714CS')")
cur.execute("insert into student (username,name,pwd) values ('B200692CS','Abhina Sunny','B200692CS')")
cur.execute("insert into student (username,name,pwd) values ('B200698CS','Shyama V Chandran','B200698CS')")
cur.execute("insert into student (username,name,pwd) values ('B200690CS','Nooshin V','B200690CS')")
cur.execute("insert into student (username,name,pwd) values ('B200752CS','Sami P S','B200752CS')")
cur.execute("insert into student (username,name,pwd) values ('B200740CS','Gokul Praveen','B200740CS')")


cur.execute("insert into mess (name,capacity,owner,category) values ('PGII',3,'Shaju V','B')")
cur.execute("insert into mess (name,capacity,owner,category) values ('A',2,'Biju B','B')")
cur.execute("insert into mess (name,capacity,owner,category) values ('OldMega',4,'Vijayan T K','M')")
cur.execute("insert into mess (name,capacity,owner,category) values ('G',3,'Gopinath','G')")
cur.execute("insert into mess (name,capacity,owner,category) values ('MLH',3,'Mohanan P','G')")


cur.execute("insert into admin (username,name,pwd) values ('A01','Karthik B','A01')")
connection.commit()
connection.close()
