from django.conf.urls import url
from .views import backups, ScheduleView


urlpatterns = [
    url(r'^backups/$', backups, name="backups_list"),
    url(r'^schedules/new/$', ScheduleView.as_view(), name="new_schedule"),
    # url(r'^backups/new$', databases, name="databases_new"),
    # url(r'^backups/backup/$', make_backup, name="databases_backup")
]

