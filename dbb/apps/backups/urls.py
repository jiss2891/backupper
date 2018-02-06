from django.conf.urls import url
from .views import backups


urlpatterns = [
    url(r'^backups/$', backups, name="backups_list"),
    # url(r'^backups/new$', databases, name="databases_new"),
    # url(r'^backups/backup/$', make_backup, name="databases_backup")
]

