#! -*- coding: utf-8 -*-
from django import forms
from dbb.widgets import *
from ..databases.models import RemoteDatabase


class DelayedBackupForm(forms.Form):
    unico = forms.BooleanField(label=u'Único', widget=bootCheckbox(),
            help_text=u"Elegir si el respaldo se hará una única vez.", required=False)
    fecha = forms.DateField(label=u'Fecha', widget=bootDate(),
            help_text=u"Fecha para respaldo único.", required=False)
    cron_entry = forms.CharField(label=u"Entrada con formato crontab", widget=bootTextInput(), 
            help_text=u"m h dom mon dow user command")
    database = forms.ModelChoiceField(label=u"Base de datos",
            queryset=RemoteDatabase.objects.all(), widget=bootSelect(),
            help_text=u"Base de datos a la cual se le realizará el respaldo")
