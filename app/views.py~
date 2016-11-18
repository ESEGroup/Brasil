from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from app.models import BuscaRecurso, Recurso
from django.core import serializers
from .serializers import UserSerializer, GroupSerializer
import json

def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def catalog(request):
    template = loader.get_template('app/catalog.html')

    context = {}
    # do it
    return HttpResponse(template.render(context, request))

    # ajax
def searchCatalog(request):
    if request.method == 'GET':

        texto = str(request.GET.get('texto')) or ''
        categorias = str(request.GET.get('categorias')) if str(request.GET.get('categorias')) != 'None' else '[]'
        enderecos = str(request.GET.get('enderecos')) if str(request.GET.get('enderecos')) != 'None' else '[]'
        disponibilidades = str(request.GET.get('disponibilidades')) if str(request.GET.get('disponibilidades')) != 'None' else '[]'

        s = BuscaRecurso()
        s.params = '{"type": "complex",'
        s.params += '"texto": "' + texto + '",'
        s.params += '"categorias": ' + categorias + ','
        s.params += '"enderecos": ' + enderecos + ','
        s.params += '"disponibilidades": ' + disponibilidades + ' }'
        res = s.buscar()

        if res == "DoesNotExist ERROR":
            raise Http404("Nenhum recurso possui o número de patrimônio buscado!")

        response_data = {}
        response_data['result'] = serializers.serialize('json', res)
        #print()
        print (s.params)
        #print (response_data)
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"Info": "request method not supported"}),
            content_type="application/json"
        )

def resource(request, id):
    # prepare the layout
    template = loader.get_template('app/resource.html')
    # search
    s = BuscaRecurso()
    s.params = '{"type": "match", "id": ' + str(id) + '}'
    res = s.buscar()
    # go to 404 if not found
    if res == "DoesNotExist ERROR":
        raise Http404("Nenhum recurso possui o número de patrimônio buscado!")
    # set the data
    #context = {'id': id}
    context = {'res': res}
    # do it
    return HttpResponse(template.render(context, request))

def newResource(request):
    template = loader.get_template('app/new_resource.html')
    context = {}
    return HttpResponse(template.render(context, request))

def createNewResource(request):
        if request.method == 'GET':

            nome = str(request.GET.get('nome'))
            patrimonio = str(request.GET.get('patrimonio'))
            endereco = str(request.GET.get('endereco'))
            categoria = str(request.GET.get('categoria'))
            descricao = str(request.GET.get('descricao'))

            s = BuscaRecurso()
            s.params = '{"type": "match", "id": ' + str(patrimonio) + '}'
            print(s.params)
            res = s.buscar()

            if res != "DoesNotExist ERROR":
                # if resource already exists..
                response_data = {}
                response_data['result'] = '""'
                response_data['error'] = "Resource already exists"
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )

            rec = Recurso(nome=nome, patrimonio=patrimonio, endereco=endereco, categoria=categoria, descricao=descricao)
            rec.save()

            response_data = {}
            response_data['result'] = patrimonio 
            response_data['error'] = ""
            #print()
            #print (s.params)
            #print (response_data)
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"Info": "request method not supported"}),
                content_type="application/json"
            )

def updateResource(request,patrimonio):
        if request.method == 'GET':

            nome = str(request.GET.get('nome'))
            endereco = str(request.GET.get('endereco'))
            categoria = str(request.GET.get('categoria'))
            descricao = str(request.GET.get('descricao'))
            estado = str(request.GET.get('estado'))

            s = BuscaRecurso()
            s.params = '{"type": "match", "id": ' + str(patrimonio) + '}'
            print(s.params)
            res = s.buscar()

            if res == "DoesNotExist ERROR":
                # if resource already exists..
                response_data = {}
                response_data['result'] = '""'
                response_data['error'] = "Resource not found"
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )

            # rec = Recurso(nome=nome, patrimonio=patrimonio, endereco=endereco, categoria=categoria, descricao=descricao)
            res.nome=nome
            res.endereco=endereco
            res.categoria=categoria
            res.descricao=descricao
            res.estado=estado
            res.save()

            response_data = {}
            response_data['result'] = patrimonio 
            response_data['error'] = ""
            #print()
            #print (s.params)
            #print (response_data)
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"Info": "request method not supported"}),
                content_type="application/json"
            )

def about(request):
    template = loader.get_template('app/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def people(request):
    template = loader.get_template('app/people.html')
    context = {}
    return HttpResponse(template.render(context, request))

def person(request):
    template = loader.get_template('app/person.html')
    context = {}
    return HttpResponse(template.render(context, request))
# Create your views here.
