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

