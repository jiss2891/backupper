#! -*- coding: utf-8 -*-
from datetime import datetime as dt
from collections import OrderedDict

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from dbb.apps.backups.models import Backup


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
