from bottle import get, post, route, request, run, template, static_file
import requests
import requests
import json
import commands

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
def salida():
    try:
        url = 'http://svcs.ebay.com/services/search/FindingService/v1?'
        dicc = {'OPERATION-NAME':'findItemsByKeywords',
        'SERVICE-VERSION':'1.0.0',
        'SECURITY-APPNAME':'',
        'RESPONSE-DATA-FORMAT':'JSON',
        'keywords':'',
        'paginationInput.entriesPerPage':''}

        dicc['SECURITY-APPNAME'] = appid
        entrada = request.forms.get('entrada')
        dicc['keywords'] = entrada
        numresp = 15
        dicc['paginationInput.entriesPerPage'] = numresp

        respuesta = requests.get(url,params = dicc)
        dicc = json.loads(respuesta.text.encode("utf-8"))

        imagurg = []
        title = []
        moneda = []
        precio = []
        contador = 0
        while numresp > contador:
            imagurg.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['galleryURL'][0])
            title.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['title'][0])
            monedac = dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['@currencyId']
            monedac = monedac.replace("USD", "$")
            moneda.append(monedac)
            precio.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['__value__'])
            contador = contador + 1
        return template('resultado.html',imagurgh=imagurg,titleh=title,monedah=moneda,precioh=precio)
    except KeyError:
        return template('busqueda_error.html',entradah=entrada)

print "AdNail - Interfaces disponibles: "
print commands.getoutput("/sbin/ifconfig | egrep -o '^[a-z].......'")
intfz = raw_input('Introduce la interfaz a utilizar: ')
comand = "/sbin/ifconfig "+intfz+" | egrep -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | egrep -v '*(0|255)$'"
iphost = commands.getoutput(comand)
print "La IP del Servidor es: ", iphost

run(host=iphost, port=8080, debug=True)
