import requests
import json
import bottle

fil = open('Key.conf','r')
key = ''
for lin in fil:
	key = key + lin
key = key.replace("\n","")
fil.close()
exec key

url = 'http://svcs.ebay.com/services/search/FindingService/v1?'
dicc = {'OPERATION-NAME':'findItemsByKeywords',
'SERVICE-VERSION':'1.0.0',
'SECURITY-APPNAME':'',
'RESPONSE-DATA-FORMAT':'JSON',
'keywords':'',
'paginationInput.entriesPerPage':''}

dicc['SECURITY-APPNAME'] = appid

iphost = raw_input('Introduce IP Server: ')

@bottle.get('/')
def inicio():
	return bottle.template('index.tpl')

@bottle.post('/resultado')
def resultado():
	entrada = request.froms.get('busqueda')
	dicc['keywords'] = entrada
	dicc['paginationInput.entriesPerPage'] = 15
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
		
	return bottle.template('resultado.tpl',imagurg,title,moneda,precio)

bottle.run(host=iphost, port=8080)
