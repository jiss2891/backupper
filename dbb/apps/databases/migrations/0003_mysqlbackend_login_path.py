# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-06 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0002_remotedatabase_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysqlbackend',
            name='login_path',
            field=models.CharField(default='__badfood__', max_length=100),
        ),
    ]
