#! -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from dbb.apps.backups.models import Backup


@login_required
def backups(request):
    titles = [u"Base de datos", u"Fecha", u"Ubicación"]
    rows = {}

    backups_qs = Backup.objects.all()
    for bkp in backups_qs:
        data_row = [[bkp.db.name, bkp.date, bkp.backup_file.name], {}]
        rows[bkp.pk] = data_row

    return render(request, 'index.html', context={'rows': rows, 'titles':
        titles})
