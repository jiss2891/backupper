from __future__ import unicode_literals

from datetime import datetime as dt
from tiger import tiger

from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from dbb.apps.databases.models import Database


def calculate_path(instance, filename):
    """
        Calculates a name for the backup.
    """
    return 'backups_storage/{}/{}/{}.sql'.format(instance.user.username, instance.db.name,
            dt.strftime(dt.now(), "%s"))


class Backup(models.Model):
    db = models.ForeignKey(Database, verbose_name="Database",
            related_name='backups')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    backup_file = models.FileField(upload_to=calculate_path, null=True,
            blank=True)
    user = models.ForeignKey(User, verbose_name="Creator")
