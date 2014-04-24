from bottle import get, post, route, request, run, template, static_file, response
from shift_local import shift_local
from ebay import busqueda

fil = open('Key.conf','r')
key = ''
for lin in fil:
    key = key + lin
key = key.replace("\n","")
fil.close()
exec key

@get('/css/<filename:re:.*\.css>')
def sever_static(filename):
    return static_file(filename, root='css')

@get('/images/<filename:re:.*>')
def sever_static(filename):
    return static_file(filename, root='images')

@route('/')
def index():
    return template('index.html')

@get('/busqueda')
def entrada():
    return template('busqueda.html')

@get('/contacto')
def contacto():
    return template('contacto.html')

@post('/resultado')
def resultado():
    try:
        entrada = ''
        numpag = 1
        response.set_cookie('busqueda', str(numpag))
        return busqueda(appid,numpag,entrada)
    except KeyError:
        return template('busqueda_error.html',entradah=entrada)

@route('/resultado+')
def resultado():
    entrada = request.cookies.get('entrada', 'entrada')
    numpag = int(request.cookies.get('busqueda', '1'))
    if numpag < 90:
        numpag = numpag + 1
    response.set_cookie('busqueda', str(numpag))
    return busqueda(appid,numpag,entrada)

@route('/resultado-')
def resultado():
    entrada = request.cookies.get('entrada', 'entrada')
    numpag = int(request.cookies.get('busqueda', '1'))
    if numpag > 1:
        numpag = numpag - 1
    response.set_cookie('busqueda', str(numpag))
    return busqueda(appid,numpag,entrada)

#Deteccion de entorno, OpenShift o local.
shift_local()
