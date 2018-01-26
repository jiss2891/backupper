# -*- coding: utf-8 -*-
import os
from datetime import datetime as dt

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from dbb.apps.databases.models import Database, PsqlBackend
from dbb.apps.backups.models import Backup
from dbb.utils.content_type import get_backend_type as bknd


def empty_validator(data, fields):
    for field in fields:
        if not data.get(field, None):
            return False
    return True

def number_validator(data, fields):
    i = 0
    isNum = True
    while (i < len(fields) and isNum):
        isNum = data.get(fields[i]).isdigit()
        i += 1

    return (isNum)


@login_required
def databases(request, *args, **kwargs):
    databases = []

    context = {
        'status': 'danger', # caso más común
    }

    if request.method == 'POST':
        # recibo la data de las base de datos nueva
        data = request.POST
        if data.get('db_backend') == 'psql':
            if empty_validator(data, ['db_name', 'db_host', 'db_user', 'db_pass', 'db_port']):
                if number_validator(data,['db_port']):
                    psqlB = PsqlBackend(
                        name=data.get('db_name', None),
                        host=data.get('db_host', None),
                        username=data.get('db_user', None),
                        password=data.get('db_pass', None),
                        port=data.get('db_port', None)
                    )
                    try:
                        psqlB.save()
                        context['result'] = '¡Base registrada correctamente!'
                        context['status'] = 'success'
                    except ValueError as e:
                        context['result'] = unicode(e)
                else:
                    context['result'] = 'El puerto debe ser un valor entero'
            else:
                context['result'] = 'Ningún campo debe estar vacío'
        else:
            context['result'] = 'Backend no soportado'
            context['status'] = 'warning'

    for db in PsqlBackend.objects.all().order_by('-pk')[:5]:
        databases.append(u"{} ({})".format(db.name, db.host))

    context['db_list'] = databases

    return render(request, 'crud_databases.html', context)

@login_required
def make_backup(request):
    # obtengo el id de la base de datos
    db_id = request.GET.get("db_id", None)

    if (db_id):
        real_backend = bknd(db_id)
        dump = real_backend.get_dump()

        path = settings.MEDIA_ROOT + '/backups_storage/{}/{}'.format(
            request.user.username,
            real_backend.name,
        )
        if not os.path.exists(path):
            os.makedirs(path)

        dump_file = open(path + dt.strftime(dt.now(), "%s"), 'w+')
        dump_file.writelines(dump.readlines())

        bkp = Backup(
            db=real_backend,
            backup_file=dump_file.name,
            user=request.user
        )

        bkp.save()
        dump_file.close()

        return HttpResponse("Backup creado correctamente en {}".format(dump_file.name))
    else:
        raise Exception("Backend no soportado aún.")


@login_required
def databases_list(request):
    titles = ["Nombre", "Host", "Puerto", "Usuario", "Password", "Backend", "Opciones"]
    rows = {}

    databases = PsqlBackend.objects.all()
    for db in databases:
        data_row = [db.name, db.host, db.port, db.username, '***', 'PostgreSQL']
        rows[db.pk] = data_row

    return render(request, 'index.html', context={'rows': rows, 'titles':
        titles})
