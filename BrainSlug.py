def BrainSlugMA(numpag,entrada):
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import urllib2
    import re
    from bottle import template, request, response

    if entrada == '':
        entrada = request.forms.get('entrada')
        response.set_cookie('entrada', entrada)
    print "Busqueda MilAnuncios del cliente:-", entrada, "-Pag.", numpag

    urlbusq = 'http://www.milanuncios.com/anuncios/'
    palabra = entrada
    palabra = palabra.replace(' ','-')
    url  = urlbusq + palabra + '.htm' + '?pagina=' + str(numpag)

    html = urllib2.urlopen(url)
    htmlread = html.read()
    html.close()

    error = re.findall('class="nohayanuncios"', htmlread)
    if error:
        return ''
    else:
        resulhtml = re.findall('<div\ class=x1>[\s\S\w\W]*', htmlread)
        listahtml = resulhtml[0].split("<div class=x10>")
        del listahtml[30]

        listtitulo_ma = []
        listprecio_ma = []
        listlink_ma = []
        listphoto_ma = []
        listmoneda_ma =  []
        listmetodo_ma = []
        serverimg = 'http://91.229.239.12/fg/'
        for prodct in listahtml:
            titulo = re.findall('<div\ class=x4>.*', prodct)
            if titulo:
                titulo = titulo[0].replace('<div class=x4>','')
                titulo = titulo.replace('</div>','')
                titulo = titulo.replace("<b class='sub2'>","")
                titulo = titulo.replace("</b>","")
                titulo = titulo.decode("utf-8", "replace")
            else:
                titulo = 'Producto'
            listtitulo_ma.append(titulo)

            precio = re.findall('<div\ class=pr>[0-9.]*', prodct)
            if precio:
                precio = precio[0].replace('<div class=pr>','')
            else:
                precio = 'N/A'
            listprecio_ma.append(precio)

            link = re.findall('<div\ class=x7><a href=".*"', prodct)
            if link:
                link = link[0].replace('"','')
                link = link.replace('<div class=x7><a href=','')
            else:
                link = 'N/A'
            listlink_ma.append('http://www.milanuncios.com' + link)

            ide = re.findall('<div\ class=x5>r[0-9A-Z]*', prodct)
            ide = ide[0].replace('<div class=x5>r','')
            strlong =  len(ide)
            cod2 =  ide[strlong - 5:strlong - 3]
            cod1 = ide[0:strlong - 5]
            photo = serverimg + cod1 + '/' + cod2 + '/' + ide + '_1.jpg'
            listphoto_ma.append(photo)

            listmoneda_ma.append('&euro;')
            listmetodo_ma.append('MilAnuncios')

    dicma = {'listtitulo_ma':listtitulo_ma,'listlink_ma':listlink_ma,'listprecio_ma':listprecio_ma,'listphoto_ma':listphoto_ma,'listmoneda_ma':listmoneda_ma,'listmetodo_ma':listmetodo_ma}

    return dicma

def BrainSlugTA(numpag,entrada):
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import urllib2
    import re
    from bottle import template, request, response

    if entrada == '':
        entrada = request.forms.get('entrada')
        response.set_cookie('entrada', entrada)
    print "Busqueda TusAnuncios del cliente:-", entrada, "-Pag.", numpag

    urlbusq = 'http://www.tusanuncios.com/clasificados/query='
    palabra = entrada
    palabra = palabra.replace(' ','-')
    url  = urlbusq + palabra + '/' + str(numpag)

    html = urllib2.urlopen(url)
    htmlread = html.read()
    html.close()

    error = re.findall('<div id="EmptyContent">', htmlread)
    if error:
        return ''
    else:
        htmlread = re.findall('<div class="grid_product "[\s\S\w\W]*',htmlread)
        htmlread = htmlread[0].replace('\r','')
        htmlread = htmlread.replace('\n','')
        listahtml = htmlread.split('<div class="ad_textlink_search">')
        del listahtml[20]

        listtitulo_ta = []
        listprecio_ta = []
        listlink_ta = []
        listphoto_ta = []
        listmoneda_ta =  []
        listmetodo_ta = []
        for prodct in listahtml:
            titulo = re.findall(';tipo=5"\ >[0-9A-Za-z .*]*', prodct)
            if titulo:
                titulo = titulo[0].replace(';tipo=5" >                                            ','')
                titulo = titulo.decode("utf-8", "replace")
            else:
                titulo = 'Producto'
            listtitulo_ta.append(titulo)

            precio = re.findall('<div\ class="price">[0-9 .]*', prodct)
            if precio:
                precio = precio[0].replace('<div class="price">                                    ','')
            else:
                precio = 'N/A'
            listprecio_ta.append(precio)

            link = re.findall("window.location='[0-9A-Za-z/?=&;]*", prodct)
            if link:
                link = link[0].replace("window.location='",'')
                link = link.replace('&amp;','&')
                link = 'http://www.tusanuncios.com' + link
            else:
                link = 'N/A'
            listlink_ta.append(link)

            photo = re.findall('class="thumbnail" src="http://[0-9A-Za-z._/-]*"', prodct)
            if photo:
                photo = photo[0].replace('class="thumbnail" src=','')
                photo = photo.replace('"','')
                photo = photo.replace('_2.jpg','_3.jpg')
            else:
                photo = 'http://www.kerrdental.es/res/global/product_515_275_noPhoto.jpg'
            listphoto_ta.append(photo)

            listmoneda_ta.append('&euro;')
            listmetodo_ta.append('TusAnuncios')

    dicta = {'listtitulo_ta':listtitulo_ta,'listlink_ta':listlink_ta,'listprecio_ta':listprecio_ta,'listphoto_ta':listphoto_ta,'listmoneda_ta':listmoneda_ta,'listmetodo_ta':listmetodo_ta}

    return dicta
