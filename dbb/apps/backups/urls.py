from django.conf.urls import url
from .views import backups, delay_backup


urlpatterns = [
    url(r'^backups/$', backups, name="backups_list"),
    url(r'^delay-backup/$', delay_backup, name="delay_backup"),
    # url(r'^backups/new$', databases, name="databases_new"),
    # url(r'^backups/backup/$', make_backup, name="databases_backup")
]

