# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, codecs, getpass # para detectar al usuario

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from dbb.utils import sanitize, files


class Database(models.Model):
    '''Manage minimal database config'''
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User)

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
        return "'{}'@'{}'".format(self.name, self.host)

    def __str__(self):
        return self.get_label()

    def __unicode__(self):
        return self.get_label()


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
        sanitize_status, matches = sanitize.bash_sanitize(
            [
                self.host,
                self.port,
                self.username,
                self.name
            ]
        )
        if sanitize_status:
            mylogin = files.open_access_table('mysql', usuario)
            # genero el nombre de la instancia
            self.login_path = u"{}".format(self.name)
            mylogin.write(u"[client{}]\n".format(self.login_path))
            mylogin.write(u"user={}\n".format(self.username))
            mylogin.write(u"password={}\n".format(self.password))
            mylogin.write(u"host={}\n".format(self.host))
            mylogin.write(u"port={}\n".format(self.port))
            mylogin.close()
            super(MysqlBackend, self).save(args, kwargs)
        else:
            raise ValueError("Cadenas ingresadas inválidas: {}".format(matches))

    def get_dump(self):
        command = u"mysqldump --defaults-group-suffix={} -u {} -h {} -P {} {}".format(self.login_path, self.username, self.host, self.port,
            self.name)
        print command
        return os.popen(command)


class PsqlBackend(RemoteDatabase):

    def get_backend_label(self):
        return "PostgreSQL"

    def save(self, *args, **kwargs):
        # añado al archivo ~/.pgpass la contraseña nueva.
        usuario = getpass.getuser()
        sanitize_status, matches = sanitize.bash_sanitize(
            [
                self.host,
                self.port,
                self.username,
                self.name
            ]
        )
        if sanitize_status:
            pgpass = files.open_access_table('psql', usuario)
            pg_line = u"{}:{}:{}:{}:{}\n".format(self.host, self.port, self.name, self.username, self.password)
            pgpass.write(pg_line)
            pgpass.close()
            super(PsqlBackend, self).save(args, kwargs)
        else:
            raise ValueError("Cadenas ingresadas inválidas: {}".format(matches))


    def get_dump(self):
        """
        retorna un popen sin leer
        """
        return os.popen(u"pg_dump -h {} -p {} -U {} -d {} ".format(self.host, self.port, self.username, self.name))
