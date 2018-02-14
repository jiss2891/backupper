import os, codecs


def _real_open(filename):
    # genero el archivo, si no existe
    os.system(u"touch {}".format(filename))
    # corrijo los permisos
    os.system(u"chmod 600 {}".format(filename))
    # abro archivo con permisos de append
    return codecs.open(filename, 'a+', encoding='utf-8')

def open_access_table(backend, username):
    filename = ""
    if backend == 'mysql':
        filename = u"/home/{}/.my.cnf".format(username)
    elif backend == 'psql':
        filename = u"/home/{}/.pgpass".format(username)
    else:
        raise ValueError("Unknown database backend")

    return _real_open(filename)

# TODO: create an write access table
