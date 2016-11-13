from django.db import models

class BancoAcesso(models.Model):

    nome_servidor = "<NOME DO SERVIDOR>"
    usuario = "<NOME DO USUARIO>"
    senha = "<SENHA>"

    def getConexao(self):
        res = None
        return res

    class Meta:
        managed = False
        app_label = 'app'
