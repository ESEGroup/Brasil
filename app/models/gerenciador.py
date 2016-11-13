from django.db import models
from app.models import NotificadorAgendamento

class GerenciadorAgendamento ():

    acesso = None
    notificador = models.ForeignKey (NotificadorAgendamento)

    def dataUltimaChecagem ():
        return 0

    def rotina ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
