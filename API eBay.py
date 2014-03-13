import webbrowser
import requests
from lxml import etree

fil = open('Key.conf','r')
key = ''
for lin in fil:
	key = key + lin
key = key.replace("\n","")
exec key

url = 'http://open.api.ebay.com/shopping?'
dicc = {'callname':'FindProducts','responseencoding':'XML',
'appid':'','siteid':'0','version':'525','QueryKeywords':'',
'AvailableItemsOnly':'true','MaxEntries':''}

#key = raw_input('Clave API: ')
dicc['appid'] = appid


entrada = raw_input('Palabras clave a buscar: ')
dicc['QueryKeywords'] = entrada

numresp = raw_input('Numero de resultados: ')
dicc['MaxEntries'] = numresp

respuesta = requests.get(url,params = dicc)
xml = etree.fromstring(respuesta.text.encode("utf-8"))
print etree.tostring(xml)
