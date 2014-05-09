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
    'paginationInput.pageNumber':'',
    'StoreURL':''}
    dicc['SECURITY-APPNAME'] = appid

    if entrada == '':
        entrada = request.forms.get('entrada')
        response.set_cookie('entrada', entrada)

    dicc['keywords'] = entrada
    print "Busqueda Ebay del cliente:-", entrada, "-Pag.", numpag
    numresp = 29
    dicc['paginationInput.entriesPerPage'] = numresp
    dicc['paginationInput.pageNumber'] = numpag

    respuesta = requests.get(url,params = dicc)
    dicc = json.loads(respuesta.text.encode("utf-8"))

    listtitulo_ebay = []
    listprecio_ebay = []
    listlink_ebay = []
    listphoto_ebay = []
    listmoneda_ebay =  []
    listmetodo_ebay = []
    contador = 0
    while numresp > contador:
        listtitulo_ebay.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['title'][0])
        monedac = dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['@currencyId']
        monedac = monedac.replace("USD", "$")
        listmoneda_ebay.append(monedac)
        listlink_ebay.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['viewItemURL'][0])
        listprecio_ebay.append(dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['sellingStatus'][0]['currentPrice'][0]['__value__'])
        listmetodo_ebay.append('Ebay')
        photoebay = dicc['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][contador]['galleryURL'][0]
        if photoebay == '':
            photo = 'http://www.kerrdental.es/res/global/product_515_275_noPhoto.jpg'
        listphoto_ebay.append(photoebay)
        contador = contador + 1

    dicebay = {'listtitulo_ebay':listtitulo_ebay,'listprecio_ebay':listprecio_ebay,'listlink_ebay':listlink_ebay,'listphoto_ebay':listphoto_ebay,'listmoneda_ebay':listmoneda_ebay,'listmetodo_ebay':listmetodo_ebay}
    return dicebay
    
