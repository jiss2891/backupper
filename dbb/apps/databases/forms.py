#! -*- coding: utf-8 -*-
from django import forms


class bootTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        attrs = {'class': 'form-control'}
        super(bootTextInput, self).__init__(attrs, *args, **kwargs)


class bootNumberInput(forms.NumberInput):
    def __init__(self, *args, **kwargs):
        attrs = {'class': 'form-control'}
        super(bootNumberInput, self).__init__(attrs, *args, **kwargs)


class bootPasswordInput(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        attrs = {'class': 'form-control'}
        super(bootPasswordInput, self).__init__(attrs, *args, **kwargs)

class bootSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        attrs = {'class': 'form-control'}
        super(bootSelect, self).__init__(attrs, *args, **kwargs)


class RemoteDatabaseForm(forms.Form):
    choices = [
        ('mysql', u'MySQL/MaríaDB'),
        ('psql', 'PostgreSQL'),
        ('sqlite', 'SQLite'),
        ('mongo', 'MongoDB'),
    ]
    name = forms.CharField(label='Nombre', max_length=100, widget=bootTextInput(),
            help_text=u"Nombre de la base de datos registrada en el servidor (case sensitive)")
    backend = forms.CharField(label='Backend', max_length=100, widget=bootSelect(choices=choices))
    host = forms.CharField(label='Host', max_length=100, widget=bootTextInput(),
            help_text=u"IP, URL o dominio por el cual llegaremos a la base de datos.")
    username = forms.CharField(label='Username', max_length=100, widget=bootTextInput(),
            help_text=u"Nombre del usuario que tiene acceso a la base de datos (case sensitive)")
    password = forms.CharField(label='Password', max_length=100, widget=bootPasswordInput())
    port = forms.IntegerField(label='Port', widget=bootNumberInput(),
            help_text=u"De no ser ingresado, se colocará el por defecto para el motor elegido.")
