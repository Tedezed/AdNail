def BrainSlugMA(numpag,entrada):
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import urllib2
    import re
    from bottle import template, request, response

    if entrada == '':
        entrada = request.forms.get('entrada')
        response.set_cookie('entrada', entrada)
    print "Busqueda del cliente:-", entrada, "-Pag.", numpag

    urlbusq = 'http://www.milanuncios.com/anuncios/'
    palabra = entrada
    palabra = palabra.replace(' ','-')
    url  = urlbusq + palabra + '.htm' + '?pagina=' + str(numpag)

    html = urllib2.urlopen(url)
    htmlread = html.read()
    html.close()

    error = re.findall('class="nohayanuncios"', htmlread)
    if error:
        return template('busqueda_error.html',entradah=entrada)
    else:
        resulhtml = re.findall('<div\ class=x1>[\s\S\w\W]*', htmlread)
        listahtml = resulhtml[0].split("<div class=x10>")
        del listahtml[30]

        listtitulo = []
        listprecio = []
        listlink = []
        listphoto = []
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
            listtitulo.append(titulo)

            precio = re.findall('<div\ class=pr>[0-9.]*', prodct)
            if precio:
                precio = precio[0].replace('<div class=pr>','')
            else:
                precio = 'N/A'
            listprecio.append(precio)

            link = re.findall('<div\ class=x7><a href=".*"', prodct)
            if link:
                link = link[0].replace('"','')
                link = link.replace('<div class=x7><a href=','')
            else:
                link = 'N/A'
            listlink.append('http://www.milanuncios.com' + link)

            ide = re.findall('<div\ class=x5>r[0-9A-Z]*', prodct)
            ide = ide[0].replace('<div class=x5>r','')
            strlong =  len(ide)
            cod2 =  ide[strlong - 5:strlong - 3]
            cod1 = ide[0:strlong - 5]
            photo = serverimg + cod1 + '/' + cod2 + '/' + ide + '_1.jpg'
            listphoto.append(photo)

        numlist = 0

    return template('resultado2.html',listtituloh=listtitulo,listphotoh=listphoto,listlinkh=listlink,listprecioh=listprecio)
