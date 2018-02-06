# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, getpass # para detectar al usuario

from django.db import models
from django.conf import settings

from dbb.utils import sanitize


class Database(models.Model):
    '''Manage minimal database config'''
    name = models.CharField(max_length=100)

    def get_dump(self):
        pass

    def get_backend_label(self):
        return "Not specified"


class RemoteDatabase(Database):
    ''' Manage databases on remote hosts'''
    host = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    port = models.IntegerField()

    def get_dump(self):
        pass

    def get_label(self):
        return "RemoteDatabase {} on {}".format(self.name, self.host)

class SqliteBackend(Database):
    path = models.CharField(max_length=100)

    def get_dump(self):
        return "No implementado"

    def get_backend_label(self):
        return "SQlite"

class MysqlBackend(RemoteDatabase):

    login_path = models.CharField(max_length=100, default="__badfood__")

    def get_backend_label(self):
        return "MySQL"

    def save(self, *args, **kwargs):
        # añado al archivo ~/.pgpass la contraseña nueva.
        usuario = getpass.getuser()
        sanitize_control = sanitize.bash_sanitize(
            [
                self.host,
                self.port,
                self.username,
                self.name
            ]
        )
        if sanitize_control:
            # genero el archivo, si no existe
            os.system("touch ~/.my.cnf")
            # corrijo los permisos
            os.system("chmod 600 ~/.my.cnf")
            # abro archivo con permisos de append
            mylogin = open(os.path.join('/home', usuario, '.my.cnf'), 'a+')
            #pg_line = unicode(self.host) + ":" + self.port + ":" + unicode(self.name) + ":" + self.username + ":" + self.password
            # genero el nombre de la instancia
            self.login_path = "{}".format(self.name)
            mylogin.write("[client{}]\n".format(self.login_path))
            mylogin.write("user={}\n".format(self.username))
            mylogin.write("password={}\n".format(self.password))
            mylogin.write("host={}\n".format(self.host))
            mylogin.write("port={}\n".format(self.port))
            mylogin.close()
            super(MysqlBackend, self).save(args, kwargs)
        else:
            raise ValueError("Cadenas ingresadas inválidas.")

    def get_dump(self):
        command = "mysqldump --defaults-group-suffix={} -u {} -h {} -P {} {}".format(self.login_path, self.username, self.host, self.port,
            self.name)
        print command
        return os.popen(command)


class PsqlBackend(RemoteDatabase):

    def get_backend_label(self):
        return "PostgreSQL"

    def save(self, *args, **kwargs):
        # añado al archivo ~/.pgpass la contraseña nueva.
        usuario = getpass.getuser()
        sanitize_control = sanitize.bash_sanitize(
            [
                self.host,
                self.port,
                self.username,
                self.name
            ]
        )
        if sanitize_control:
            # genero el archivo, si no existe
            os.system("touch ~/.pgpass")
            # corrijo los permisos
            os.system("chmod 600 ~/.pgpass")
            # abro archivo con permisos de append
            pgpass = open(os.path.join('/home', usuario, '.pgpass'), 'a+')
            pg_line = unicode(self.host) + ":" + self.port + ":" + unicode(self.name) + ":" + self.username + ":" + self.password
            pgpass.write(pg_line)
            pgpass.close()
            super(PsqlBackend, self).save(args, kwargs)
        else:
            raise ValueError("Cadenas ingresadas inválidas.")


    def get_dump(self):
        """
        retorna un popen sin leer
        """
        return os.popen("pg_dump -h {} -p {} -U {} -d {} ".format(self.host, self.port, self.username, self.name))
