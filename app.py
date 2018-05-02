from bottle import route, run, template, static_file, request, get, post
import os
import datetime
import sqlite3
import sys
@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='./static/')

@route('/')
def index():
	return template(index.tpl)
	
@route('/new', method=['GET','POST'])
def new_task():
	if request.POST.get('save', '').strip():
		todotitle = request.POST.get('task')
		tododesc = request.POST.get('desc')
		tododatetime = datetime.datetime.now()
		
		# CONNECT DATABASE
		con = sqlite3.connect('data\\todo.dat')
		cur = con.cursor()
		rec = cur.execute('INSERT INTO todo VALUES(null,?,?,?)', (todotitle,tododesc,tododatetime))
		con.commit()
		rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
		
		return template(index.tpl, rows = rows)
	else:
		return template(newtask.tpl)
	
	
	

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), app=my_session)
