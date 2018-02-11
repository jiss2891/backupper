from django import forms


class RemoteDatabaseForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    host = forms.CharField(label='Host', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    port = forms.IntegerField(label='Port')
