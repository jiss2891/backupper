#! -*- coding: utf-8 -*-
from datetime import datetime as dt
from collections import OrderedDict

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from dbb.apps.backups.models import Backup, ScheduledBackup
from dbb.apps.backups.forms import ScheduledBackupForm


@login_required
def backups(request):
    titles = [u"Base de datos", u"Fecha", u"Ubicación", "Opciones"]
    rows = OrderedDict()

    backups_qs = Backup.objects.order_by('-id')
    if not request.user.is_staff:
        # filtro solo por las que pertenecen al usuario
        backups_qs = backups_qs.filter(db__creator=request.user)

    for bkp in backups_qs:
        data_row = [[bkp.db.name, bkp.date, bkp.backup_file.name],
                {"/media/backups_storage/{}/{}/{}.sql".format(
                    bkp.user.username,
                    bkp.db.name,
                    dt.strftime(bkp.date, "%s")
            ): 'icon ion-ios-cloud-download-outline'}
        ]

        rows[bkp.pk] = data_row

    return render(request, 'list.html', context={'rows': rows, 'titles':
        titles})

def new_schedule(request):
    context = {}
    if request.method == 'GET':
        form = ScheduledBackupForm()
        form.fields['database'].queryset = form.fields['database'].queryset.filter(creator=request.user)
        form.fields['only_once'].widget.attrs = {'checked': 'true'}
    elif request.method == 'POST':
        form = ScheduledBackupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                scheduled = ScheduledBackup(**data)
                scheduled.save()
                context['result'] = '¡Respaldo programado correctamente!'
                context['status'] = 'success'
            except Exception as e:
                context['form'] = form # evita que el usuario tenga que completar el formulario de nuevo.
                context['result'] = unicode(e)
                context['status'] = 'danger'
    base_context = {
        'form': form,
        'form_title': 'Programar respaldo'
    }
    base_context.update(context)
    return render(request, 'create_database.html', base_context)
