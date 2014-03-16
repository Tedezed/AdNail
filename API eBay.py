import webbrowser
import requests
import json
from jinja2 import Template

fil = open('Plantilla.html','r')
html = ''
for linea in fil:
	html = html + linea
Plantilla = Template(html)
fil.close()

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
entrada = raw_input('Palabras clave a buscar: ')
dicc['keywords'] = entrada
numresp = int(raw_input('Numero de resultados: '))
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
	moneda.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['@currencyId'])
	precio.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['__value__'])
	contador = contador + 1

Plantilla_sal = Plantilla.render(imagurgh=imagurg,titleh=title,monedah=moneda,precioh=precio)
archi=open('Plantilla_sal.html','w')
archi.write(Plantilla_sal)
archi.close()
webbrowser.open("Plantilla_sal.html")
