from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={})

def users_list(request):
    titles = ["Nombre", "Apellido", "e-Mail", "Backups realizados"]
    rows = []

    users = User.objects.all()
    for user in users:
        data_row = [user.username, user.last_name, user.email,
                user.backup_set.all().count]
        rows.append(data_row)

    return render(request, 'index.html', context={'rows': rows, 'titles':
        titles})
