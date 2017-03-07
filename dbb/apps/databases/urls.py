from django.conf.urls import url
from .views import databases


urlpatterns = [
    url(r'^databases/$', databases, name="crud-database")
]

