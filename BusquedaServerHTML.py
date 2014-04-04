from bottle import get, port, run, template, request
import os
interfaz = raw_input('Introduce la interfaz que deseas utilizar: (eth0,wlan0,..)')
iphost = os.system('ifconfig ',interfaz,' | grep -o "inet\ addr\:[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" | grep -o "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}"')

@get('/')
def inicio():
    return bottle.template('index.tpl')

@post('/resultado')
def resultado():
	busqueda = request.froms.get('busqueda')
	return bottle.template('resultado.tpl', )

bottle.run(host=iphost, port=8080)
