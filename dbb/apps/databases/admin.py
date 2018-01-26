from django.contrib import admin
from models import SqliteBackend, MysqlBackend, PsqlBackend

# Register your models here.
admin.site.register(SqliteBackend)
admin.site.register(MysqlBackend)
admin.site.register(PsqlBackend)
