from django.db import models
from app.models import Notificador

class NotificadorAgendamento (Notificador):

    agendamento = None #Agendamento

    def construirMensagem ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
