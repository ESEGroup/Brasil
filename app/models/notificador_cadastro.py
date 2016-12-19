from django.db import models
from app.models import Notificador

class NotificadorCadastro (Notificador):

    cadastro_usuario = None #CadastroUsuario

    def construirMensagem ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
