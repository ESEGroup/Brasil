from django.db import models

class Notificador(models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    remetente = "<EMAIL DO SISTEMA>"

    mensagem      = ""
    assunto       = ""
    tipo_mensagem = 0

    def enviarMensagem ():
        res = None
        return res

    def construirMensagem ():
        return False

    class Meta:
        abstract = True
        managed = False
        app_label = 'app'
