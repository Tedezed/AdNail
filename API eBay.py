import webbrowser
import requests
import json
from lxml import etree

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

#key = raw_input('Clave API: ')
dicc['SECURITY-APPNAME'] = appid

#entrada = 'harry'
entrada = raw_input('Palabras clave a buscar: ')
dicc['keywords'] = entrada

#numresp = 3
numresp = int(raw_input('Numero de resultados: '))
dicc['paginationInput.entriesPerPage'] = numresp

respuesta = requests.get(url,params = dicc)
dicc = json.loads(respuesta.text.encode("utf-8"))

contador = 0
while numresp > contador:
	print dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['title'][0]
	print dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['@currencyId']
	print dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['__value__']
	contador = contador + 1
