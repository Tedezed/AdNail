def shift_local():
    import os
    from bottle import TEMPLATE_PATH, default_app

    ON_OPENSHIFT = False
    if os.environ.has_key('OPENSHIFT_REPO_DIR'):
        ON_OPENSHIFT = True

    if ON_OPENSHIFT:
        TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],
                                      'runtime/repo/wsgi/views/'))
    
        application=default_app()
    else:
        import commands
        from bottle import run

        print "AdNail - Interfaces disponibles: "
        print commands.getoutput("/sbin/ifconfig | egrep -o '^[a-z].......'")
        intfz = raw_input('Introduce la interfaz a utilizar: ')
        comand = "/sbin/ifconfig "+intfz+" | egrep -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | egrep -v '*(0|255)$'"
        iphost = commands.getoutput(comand)
        print "La IP del Servidor es: ", iphost
        run(host=iphost, port=8080, debug=True)