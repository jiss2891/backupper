# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 00:07
from __future__ import unicode_literals

import dbb.apps.backups.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('databases', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('backup_file', models.FileField(blank=True, null=True, upload_to=dbb.apps.backups.models.calculate_path)),
                ('db', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backups', to='databases.Database', verbose_name='Database')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
        ),
    ]