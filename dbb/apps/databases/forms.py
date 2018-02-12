from django import forms

class bootTextInput(forms.TextInput):
    '''
    input que se renderiza con la clase de bootstrap
    '''
    def __init__(self, *args, **kwargs):
        attrs = {'class': 'form-control'}
        super(bootTextInput, self).__init__(attrs, *args, **kwargs)

class RemoteDatabaseForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, widget=bootTextInput())
    backend = forms.CharField(label='Backend', max_length=100, widget=bootTextInput())
    host = forms.CharField(label='Host', max_length=100, widget=bootTextInput())
    username = forms.CharField(label='Username', max_length=100, widget=bootTextInput())
    password = forms.CharField(label='Password', max_length=100, widget=bootTextInput())
    port = forms.IntegerField(label='Port', widget=bootTextInput())
