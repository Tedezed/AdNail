def busqueda(appid,numpag,entrada):
    import requests
    import json
    from bottle import request, template, request, response

    url = 'http://svcs.ebay.com/services/search/FindingService/v1?'
    dicc = {'OPERATION-NAME':'findItemsByKeywords',
    'SERVICE-VERSION':'1.0.0',
    'SECURITY-APPNAME':'',
    'RESPONSE-DATA-FORMAT':'JSON',
    'keywords':'',
    'paginationInput.entriesPerPage':'',
    'paginationInput.pageNumber':''}
    dicc['SECURITY-APPNAME'] = appid

    if entrada == '':
        entrada = request.forms.get('entrada')
        response.set_cookie('entrada', entrada)

    dicc['keywords'] = entrada
    numresp = 15
    dicc['paginationInput.entriesPerPage'] = numresp
    dicc['paginationInput.pageNumber'] = numpag

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
    
