# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, getpass # para detectar al usuario

from django.db import models
from django.conf import settings


class Database(models.Model):
    name = models.CharField(max_length=100)

    def get_dump(self):
        pass


class RemoteDatabase(Database):
    host = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    port = models.IntegerField()

    def get_dump(self):
        pass

class SqliteBackend(Database):
    path = models.CharField(max_length=100)

    def get_dump(self):
        return "No implementado"


class MysqlBackend(RemoteDatabase):

    def get_dump(self):
        return "No implementado"


class PsqlBackend(RemoteDatabase):

    def save(self, *args, **kwargs):
        # añado al archivo ~/.pgpass la contraseña nueva.
        usuario = getpass.getuser()
        # genero el archivo, si no existe
        os.system("touch ~/.pgpass")
        # corrijo los permisos
        os.system("chmod 600 ~/.pgpass")
        # abro archivo con permisos de append
        pgpass = open(os.path.join('/home', usuario, '.pgpass'), 'a+')

        pg_line = u"%s:%s:%s:%s:%s\n" % (self.host, self.port, self.name, self.username, self.password)
        pgpass.write(pg_line)
        pgpass.close()
        super(PsqlBackend, self).save(args, kwargs)


    def get_dump(self):
        """
        retorna un popen sin leer
        """
        print "pg_dump -h {} -p {} -U {} -d {} ".format(self.host, self.port, self.username, self.name)
        return os.popen("pg_dump -h {} -p {} -U {} -d {} ".format(self.host, self.port, self.username, self.name))
