from django.conf.urls import url
from .views import backups, new_schedule


urlpatterns = [
    url(r'^backups/$', backups, name="backups_list"),
    url(r'^schedules/new/$', new_schedule, name="new_schedule"),
    # url(r'^backups/new$', databases, name="databases_new"),
    # url(r'^backups/backup/$', make_backup, name="databases_backup")
]

