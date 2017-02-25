from __future__ import unicode_literals

from django.db import models
from dbb.apps.databases.models import Database

# Create your models here.
class Backup(models.Model):
    db = models.ForeignKey(Database, verbose_name="Database",
            related_name='backups')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    # user ??
