from django.db import models
from app.models import  Cadastro, Usuario

class CadastroUsuario(Cadastro):

    notificador = None #NotificadorCadastro
    usuario = None
    solicitante = None

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
