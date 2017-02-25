# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 06:16
from __future__ import unicode_literals

import dbb.apps.backups.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backups', '0002_auto_20170225_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='backup_file',
            field=models.FileField(null=True, upload_to=dbb.apps.backups.models.calculate_path),
        ),
    ]
