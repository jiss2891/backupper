# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from dbb.apps.databases.models import Database, PsqlBackend


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
        'status': 'success',
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
                    psqlB.save()
                    context['result'] = '¡Base registrada correctamente!'
                else:
                    context['result'] = 'El puerto debe ser un valor entero'
                    context['status'] = 'danger'
            else:
                context['result'] = 'Ningún campo debe estar vacío'
                context['status'] = 'danger'
        else:
            context['result'] = 'Backend no soportado'
            context['status'] = 'warning'
    elif request.method == 'GET':
        pass

    for db in PsqlBackend.objects.all().order_by('-pk')[:5]:
        databases.append(u"{} ({})".format(db.name, db.host))

    context['db_list'] = databases

    return render(request, 'crud_databases.html', context)

@login_required
def make_backup(request):
    # obtengo el id de la base de datos
    db_id = request.POST.get("db_id", None)

    if (db_id):
       db = Database.objects.get(pk=db_id)
       return HttpResponse(db.name + u"-->" + unicode(isinstance(db, PsqlBackend)))
    else:
        raise Exception("Todo mal vieja")


@login_required
def databases_list(request):
    titles = ["Nombre", "Host", "Puerto", "Usuario", "Password", "Backend"]
    rows = []

    databases = PsqlBackend.objects.all()
    for db in databases:
        data_row = [db.name,db.host, db.port, db.username, '***', 'PostgreSQL']
        rows.append(data_row)

    return render(request, 'index.html', context={'rows': rows, 'titles':
        titles})

