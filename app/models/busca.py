from django.db import models
#from app.models import Recurso, Usuario

class Busca (models.Model):

    acesso           = None
    params           = "{}"
    resultados_busca = "{}"
    lista_resultados = []

    def busca (json):
        return False

    def buscar ():
        return False

    class Meta:
        abstract = True
        managed = False
        app_label = 'app'


class BuscaRecurso (Busca):

    def buscar ():
        return False

    class Meta:
        managed = False
        app_label = 'app'


class BuscaUsuario (Busca):

    def buscar ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
