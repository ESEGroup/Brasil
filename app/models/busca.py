from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from app.models import Recurso, Usuario
import json

class Busca (models.Model):

    acesso           = None
    params           = "{}"
    # {
    #                       'type': 'match'/'text',
    #   (if type == match)  'id': integer id,
    #   (if type == 'text') 'text' : queried text
    #}
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

    def buscar (self):

        if self.params == '{}':
            return None

        # creating dynamic object from json
        query = lambda:None
        query.__dict__ = json.loads(self.params)

        # returns single resource, if found
        if query.type == 'match':
            try:
                return Recurso.objects.get(patrimonio = query.id)
            except ObjectDoesNotExist:
                return "DoesNotExist ERROR"

        # returns list of resources
        elif query.type == 'text':
            # this is actually an OR
            return Recurso.objects.filter(nome__icontains=query.text).filter(descricao__icontains=query.text)

        return None

    class Meta:
        managed = False
        app_label = 'app'


class BuscaUsuario (Busca):

    def buscar ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
