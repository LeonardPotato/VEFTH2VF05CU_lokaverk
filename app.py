from bottle import route, run, template

@route('/')
def index():
	return template(index.tpl)

	
	
	
	

run(host='localhost', port=8080 debug="='true', reloader='True')