from django.db import models
from app.models import  Usuario, Recurso, NotificadorCadastro

class Cadastro (models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    acesso = None
    notificador = models.ForeignKey(NotificadorCadastro)

    def cadastrar ():
        return False

    def atualizar ():
        return False

    def deletar ():
        return False

    def notificar ():
        return False

    class Meta:
        abstract = True
        managed = False
        app_label = 'app'


class CadastroUsuario(Cadastro):

    usuario = models.ForeignKey(Usuario)
    solicitante = models.ForeignKey(Usuario)

    def cadastrar ():
        return False

    def atualizar ():
        return False

    def deletar ():
        return False

    def notificar ():
        return False

    class Meta:
        managed = False
        app_label = 'app'


class CadastroRecurso(Cadastro):

    recurso = models.ForeignKey(Recurso)
    solicitante = models.ForeignKey(Usuario)

    def cadastrar ():
        return False

    def atualizar ():
        return False

    def deletar ():
        return False

    def notificar ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
