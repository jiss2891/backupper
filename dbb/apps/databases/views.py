# -*- coding: utf-8 -*-
import os
from datetime import datetime as dt

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from .forms import RemoteDatabaseForm

from dbb.apps.databases.models import MysqlBackend, Database, RemoteDatabase, PsqlBackend
from dbb.apps.backups.models import Backup
from dbb.utils.content_type import get_backend_type as bknd


@login_required
def new_database(request, *args, **kwargs):
    databases = []
    context = {}

    # ultimas creaciones
    for db in RemoteDatabase.objects.all().order_by('-pk')[:5]:
        databases.append(u"{} ({})".format(db.name, db.host))

    if request.method == 'POST':
        form = RemoteDatabaseForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            backend = data.pop('backend', None)

            context['result'] = '¡Base registrada correctamente!'
            context['status'] = 'success'
            try:
                if backend == 'psql':
                    psqlB = PsqlBackend(**data)
                    psqlB.save()
                elif backend == 'mysql':
                    mysqlB = MysqlBackend(**data)
                    mysqlB.save()
                else:
                    context['result'] = 'Backend no soportado'
                    context['status'] = 'warning'
            except ValueError as e:
                context['result'] = unicode(e)
                context['status'] = 'danger'
        else:
            context['result'] = 'Datos incorrectos' # TODO: capturar mensajes del is_valid
            context['status'] = 'danger'

    form = RemoteDatabaseForm()
    base_context = {
        'form': form,
        'form_title': 'Nueva base de datos',
        'posturl': '/databases/new',
        'db_list': databases
    }

    base_context.update(context)

    return render(request, 'create_database.html', base_context)


@login_required
def make_backup(request):
    # TODO: implementar commit atómico
    # obtengo el id de la base de datos
    db_id = request.GET.get("db_id", None)

    if (db_id):
        real_backend = bknd(db_id)
        dump = real_backend.get_dump()

        path = settings.MEDIA_ROOT + '/backups_storage/{}/{}/'.format(
            request.user.username,
            real_backend.name,
        )
        if not os.path.exists(path):
            os.makedirs(path)

        bkp = Backup(
            db=real_backend,
            user=request.user
        )
        bkp.save() # genero la fecha en la bbdd

        dump_file = open(path + dt.strftime(bkp.date, "%s") + '.sql', 'w+')
        bkp.backup_file = dump_file.name
        bkp.save() # guardado final

        dump_file.writelines(dump.readlines())

        dump_file.close()

        return HttpResponse("Backup creado correctamente en {}".format(dump_file.name))
    else:
        raise Exception("Backend no soportado aún.")


@login_required
def databases_list(request):
    titles = ["Nombre", "Host", "Puerto", "Usuario", "Password", "Backend", "Opciones"]
    rows = {}
    options = {}

    databases = RemoteDatabase.objects.all()
    for db in databases:
        db = bknd(db)
        data_row = [[db.name, db.host, db.port, db.username, '***', db.get_backend_label()],
                {"/databases/backup?db_id={}".format(db.pk): 'glyphicon glyphicon-hdd'}]
        rows[db.pk] = data_row

    return render(request, 'index.html', context={'options': options, 'rows': rows, 'titles':
        titles})
