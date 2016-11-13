from django.db import models
from app.models import Agendamento, CadastroUsuario

class Notificador(models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    remetente = "<EMAIL DO SISTEMA>"

    mensagem      #= models.CharField(max_length=2000)
    assunto       #= models.CharField(max_length=200)
    tipo_mensagem #= models.PositiveSmallIntegerField()

    def enviarMensagem ():
        res = None
        return res

    def construirMensagem ():
        return False

    class Meta:
        abstract = True
        managed = False
        app_label = 'app'


class NotificadorAgendamento (Notificador):

    agendamento = models.ForeignKey(Agendamento)

    def construirMensagem ():
        return False

    class Meta:
        managed = False
        app_label = 'app'


class NotificadorCadastro (Notificador):

    cadastro_usuario = models.ForeignKey(CadastroUsuario)

    def construirMensagem ():
        return False
        
    class Meta:
        managed = False
        app_label = 'app'
