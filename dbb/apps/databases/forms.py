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
    name = forms.CharField(label='Nombre', max_length=100, widget=bootTextInput())
    backend = forms.CharField(label='Backend', max_length=100, widget=bootSelect(choices=choices))
    host = forms.CharField(label='Host', max_length=100, widget=bootTextInput())
    username = forms.CharField(label='Username', max_length=100, widget=bootTextInput())
    password = forms.CharField(label='Password', max_length=100, widget=bootPasswordInput())
    port = forms.IntegerField(label='Port', widget=bootNumberInput())
