from django.db import models

class Cadastro (models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    acesso = None

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
