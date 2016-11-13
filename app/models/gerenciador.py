from django.db import models

class GerenciadorAgendamento ():

    acesso = None
    notificador = None

    def dataUltimaChecagem ():
        return 0

    def rotina ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
