from bottle import get, port, run, template, request

@get('/')
def inicio():
    return bottle.template('index.html')

@post('/resultado')
def resultado():
	
