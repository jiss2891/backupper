from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html', context={})

@login_required
def users_list(request):
    titles = ["Usuario", "Nombre", "Apellido", "e-Mail", "Backups realizados"]
    rows = []

    users = User.objects.all()
    for user in users:
        data_row = [user.username, user.first_name, user.last_name, user.email,
                user.backup_set.all().count]
        rows.append(data_row)

    return render(request, 'index.html', context={'rows': rows, 'titles':
        titles})
