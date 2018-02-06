from dbb.apps.databases.models import PsqlBackend, SqliteBackend, MysqlBackend

def get_backend_type(pk):
    """

    Recibe una instancia de database y retorna un
    PsqlBackend, MysqlBackend o SqliteBackend

    """
    # TODO: cambiar esto por algo decente.

    if PsqlBackend.objects.filter(pk=pk).count() > 0:
        # es un psqlbackend
        return PsqlBackend.objects.get(pk=pk)
    elif MysqlBackend.objects.filter(pk=pk).count() > 0:
        # es un mysqlbackend
        return MysqlBackend.objects.get(pk=pk)
    elif SqliteBackend.objects.filter(pk=pk).count() > 0:
        # es un sqlitebackend
        return SqliteBackend.objects.get(pk=pk)
    else:
        raise Exception("Backend no reconocido")
