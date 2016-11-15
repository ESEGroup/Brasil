from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from app.models import Recurso, Usuario
import json

class Busca (models.Model):

    acesso           = None
    params           = "{}"
    # {
    #                       'type': 'match'/'complex',
    #   (if type == match)  'id': integer id,
    #   (if type == 'complex') 'texto' : queried text or '' (empty)
    #   (if type == 'complex') 'categorias' : string array,
    #   (if type == 'complex') 'enderecos' : string array,
    #   (if type == 'complex') 'disponibilidades' : string array
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
        elif query.type == 'complex':
            # Remember: querySets are lazy – the act of creating a QuerySet doesn’t involve any database activity.
            # You can stack filters together all day long, and Django won’t actually run the query until the QuerySet is evaluated.
            res = Recurso.objects.exclude(nome="")
            if query.texto.strip():
                # this is actually an OR
                res = res.filter(nome__icontains=query.texto) | res.filter(descricao__icontains=query.texto)
            if len(query.categorias) > 0:
                res = res.filter(categoria__in=query.categorias)
            if len(query.enderecos) > 0:
                res = res.filter(endereco__in=query.enderecos)
            if len(query.disponibilidades) > 0:
                res = res.filter(estado__in=query.disponibilidades)
            try:
                return res
            except DoesNotExist:
                return "DoesNotExist ERROR"

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
