from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from app.models import BuscaRecurso


def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def catalog(request):
    template = loader.get_template('app/catalog.html')
    context = {}
    return HttpResponse(template.render(context, request))

def resource(request, id):
    # prepare the layout
    template = loader.get_template('app/resource.html')
    # search
    s = BuscaRecurso()
    s.params = '{"type": "match", "id": ' + id + '}'
    res = s.buscar()
    # go to 404 if not found
    if res == "DoesNotExist ERROR":
        raise Http404("Nenhum recurso possui o número de patrimônio buscado!")
    # set the data
    #context = {'id': id}
    context = {'res': res}
    # do it
    return HttpResponse(template.render(context, request))

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
