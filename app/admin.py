from django.contrib import admin

from app.models import Agendamento, Recurso, Usuario

admin.site.register(Agendamento)
admin.site.register(Recurso)
admin.site.register(Usuario)
