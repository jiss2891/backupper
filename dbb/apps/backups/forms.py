#! -*- coding: utf-8 -*-
from django import forms
from dbb.widgets import *
from ..databases.models import RemoteDatabase


class ScheduledBackupForm(forms.Form):
    only_once = forms.BooleanField(label=u'Único', widget=bootToggle(),
            help_text=u"Elegir si el respaldo se hará una única vez.", required=False)
    crontab_rule = forms.CharField(label=u"Entrada con formato crontab", widget=bootTextInput(),
            help_text=u"m h dom mon dow")
    database = forms.ModelChoiceField(label=u"Base de datos",
            queryset=RemoteDatabase.objects.all(), widget=bootSelect(),
            help_text=u"Base de datos a la cual se le realizará el respaldo")
