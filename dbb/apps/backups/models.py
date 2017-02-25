from __future__ import unicode_literals

from datetime import datetime as dt
from tiger import tiger

from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save

from dbb.apps.databases.models import Database


def calculate_path(instance, filename):
    hex_code = tiger(instance.backup_file.open().read()).hexdigest()
    return 'backups_storage/{}/{}/{}.sql'.format(instance.db.name,
            dt.strftime(dt.now(), "%d_%b_%Y"), hex_code)


# Create your models here.
class Backup(models.Model):
    db = models.ForeignKey(Database, verbose_name="Database",
            related_name='backups')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    backup_file = models.FileField(upload_to=calculate_path, null=True,
            blank=True)
    #1user ??
