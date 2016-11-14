from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def catalog(request):
    template = loader.get_template('app/catalog.html')
    context = {}
    return HttpResponse(template.render(context, request))

def resource(request, id):
    template = loader.get_template('app/resource.html')
    context = {'id': id}
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
