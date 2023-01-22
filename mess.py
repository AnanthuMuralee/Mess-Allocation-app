import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def connect_db():
	conn=sqlite3.connect('database.db')
	conn.row_factory=sqlite3.Row
	return conn
	
def get_post_student(username):
	conn=connect_db()
	post=conn.execute('SELECT * FROM student where username = ?',(username,)).fetchone()
	conn.close()
	if post is None:
		abort(404)
	return post

def get_post_admin(username):
	conn=connect_db()
	post=conn.execute('SELECT * FROM admin where username = ?',(username,)).fetchone()
	conn.close()
	if post is None:
		abort(404)
	return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your key bleh'


@app.route('/',methods=('GET', 'POST'))
def index():
	
	if request.method == 'POST':
	
		username = request.form['username']
		pwd = request.form['pwd']
		adorstu = request.form.get('utype')
		
		if adorstu == "student":
			conn = connect_db()
			user = conn.execute("SELECT id FROM student WHERE username = ? AND pwd = ?",(username,pwd)).fetchall()
			if user == []:
				flash("Username&Password not found!!!")
			else:
				user = get_post_student(username)
				if user['hostel'] is None:
					return redirect(url_for('create_profile',username=username))
				else:
					return redirect(url_for('show_profile',username=username))
		else:
			conn = connect_db()
			user = conn.execute("SELECT id FROM admin WHERE username = ? AND pwd = ?",(username,pwd)).fetchall()
			if user == []:
				flash("Username&Password not found!!!")
			else:
				return redirect(url_for('admin',username=username))
	return render_template('index.html')
	
@app.route('/<username>/create_profile',methods=('GET','POST'))
def create_profile(username):

	if request.method == 'POST':
		if request.form['action'] == 'save':
			gender = request.form['gender']
			hostel = request.form['hostel']
			room = request.form['room']
			if gender == "None" or hostel == "None" or room == "None":
				flash("Fill the options and Click Save Changes to Continue")
			else:	
				conn = connect_db()
				conn.execute("UPDATE student SET gender = ?, hostel = ?, room = ? WHERE username = ?",(gender,hostel,room,username))
				conn.commit()
				conn.close()
				return redirect(url_for('show_profile',username=username))		

	user = get_post_student(username)
	name=user['name']
	fname=name.split()
	email=fname[0].lower()+'_'+username.lower()+'@nitc.ac.in'
	return render_template('profile_student.html',user=user,email=email)
	
@app.route('/<username>/profile',methods=('GET','POST'))
def show_profile(username):
	user = get_post_student(username)
	name=user['name']
	fname=name.split()
	email=fname[0].lower()+'_'+username.lower()+'@nitc.ac.in'
	if request.method == 'POST':
		if request.form['action'] == 'continue':
			return redirect(url_for('mess_preference',username=username))
	return render_template('show_profile.html',user=user,email=email)
	
@app.route('/<username>/profile/mess_preference')
def mess_preference(username):
	user = get_post_student(username)
	
	return render_template('mess_preference.html',user=user)

@app.route('/<username>/admin')
def admin(username):
	user = get_post_admin(username)
	return render_template('admin.html',user=user)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
