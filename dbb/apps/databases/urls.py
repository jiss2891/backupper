from django.conf.urls import url
from .views import new_database, databases, make_backup, databases_list


urlpatterns = [
    url(r'^databases/$', databases_list, name="databases_list"),
    url(r'^databases/new$', new_database, name="databases_new"),
    url(r'^databases/backup/$', make_backup, name="databases_backup")
]

