def AdNailResultado(appid,numpag,entrada):
	from bottle import template
	from ebay import busqueda
	from BrainSlug import BrainSlugMA
	from BrainSlug import BrainSlugTA
	try:
		dicebay = busqueda(appid,numpag,entrada)
	except KeyError:
		dicebay = ''
	dicma = BrainSlugMA(numpag,entrada)
	dicta = BrainSlugTA(numpag,entrada)

	if dicebay or dicma or dicta:
		listtitulo = []
		listlink = []
		listprecio = []
		listphoto =  []
		listmoneda = []
		listmetodo = []
		llave = 0
		while llave < 20:
			if not dicebay == '':
				listtitulo.append(dicebay['listtitulo_ebay'][llave])
				listlink.append(dicebay['listlink_ebay'][llave])
				listprecio.append(dicebay['listprecio_ebay'][llave])
				listphoto.append(dicebay['listphoto_ebay'][llave])
				listmoneda.append(dicebay['listmoneda_ebay'][llave])
				listmetodo.append(dicebay['listmetodo_ebay'][llave])

			if not dicma == '':
				listtitulo.append(dicma['listtitulo_ma'][llave])
				listlink.append(dicma['listlink_ma'][llave])
				listprecio.append(dicma['listprecio_ma'][llave])
				listphoto.append(dicma['listphoto_ma'][llave])
				listmoneda.append(dicma['listmoneda_ma'][llave])
				listmetodo.append(dicma['listmetodo_ma'][llave])

			if not dicta == '':
				listtitulo.append(dicta['listtitulo_ta'][llave])
				listlink.append(dicta['listlink_ta'][llave])
				listprecio.append(dicta['listprecio_ta'][llave])
				listphoto.append(dicta['listphoto_ta'][llave])
				listmoneda.append(dicta['listmoneda_ta'][llave])
				listmetodo.append(dicta['listmetodo_ta'][llave])

			llave += 1

		return template('resultado.html',listtituloh=listtitulo,listlinkh=listlink,listprecioh=listprecio,
			listphotoh=listphoto,listmonedah=listmoneda,listmetodoh=listmetodo)
	else:
		return template('busqueda_error.html',entradah=entrada)