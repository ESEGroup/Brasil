import sys
import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from app.models import BuscaRecurso, Recurso
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes  
from rest_framework.authentication import TokenAuthentication
from .permissions import AllowAll,AdminOnly,SuperAdminOnly
from .models import CadastroUsuario, SettingsUserGroups, Usuario
from rest_framework.authtoken.models import Token

#static pages

def index(request):
    return render(request, 'app/index.html', {})

def catalog(request):
    return render(request, 'app/catalog.html', {})

def about(request):
    return render(request, 'app/about.html', {})

def people(request):
    return render(request, 'app/people.html', {})

def person(request):
    return render(request, 'app/person.html', {})

def newResource(request):
    return render(request, 'app/new_resource.html', {})

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
    return render(request, 'app/resource.html', context)

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


from .models import Usuario
@api_view(['POST','GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def getInfoUsuario(request):
    data ={}
    if settings.DEBUG: 
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        request.usuario = Usuario.objects.get(user=request.user)
        data = {
            'username:': request.usuario.user.username, 
            'group:':request.usuario.user.groups.all()[0].name,
            'first_name': request.usuario.user.first_name,
            'last_name': request.usuario.user.last_name,
            'is_active': request.usuario.user.is_active,
            'last_login': request.usuario.user.last_login,
            'date_joined': request.usuario.user.date_joined,
            'departamento':request.usuario.departamento,
            'registro': request.usuario.registro
            }
        
        return Response(data,status=status.HTTP_202_ACCEPTED)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    finally:
        if settings.DEBUG: print ("Output: ",data)

@api_view(['POST','DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def logout(request):
    data ={}
    if settings.DEBUG: 
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        t=Token.objects.get(user=request.user)
        t.delete()
        Token.objects.create(user=request.user)
        data = {"status":"sucesso"}
        return Response(data,status=status.HTTP_202_ACCEPTED)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)


@api_view(['POST','GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AdminOnly,))
def CadastroFuncionario(request,typeOp):
    settingsUserGroups = SettingsUserGroups()
    jsonInput=json.loads(request.body.decode("utf-8"))
    data ={}
    group = settingsUserGroups.FuncGroup
    if settings.DEBUG: 
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print (jsonInput)
    try:
        cad = CadastroUsuario()
        cad.parser(jsonInput)
        cad.solicitante = request.user
        if not(cad.has_permission()):
            data = {"detail": "Você não tem permissão para executar essa ação."}
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)

        if typeOp == "cadastrar" or typeOp == "cadastro" or typeOp == "create":    
            data["PrimaryKey"] = cad.cadastrar(group=group)
        elif typeOp == "atualizar" or typeOp == "atualizacao" or typeOp == "update":
            cad.atualizar()
        elif typeOp == "deletar" or typeOp == "delecao" or typeOp == "delete":
            cad.deletar()

        data["status"] = "sucesso" 
        return Response(data,status=status.HTTP_202_ACCEPTED)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)

@api_view(['POST','GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((SuperAdminOnly,))
def CadastroAdministrador(request,typeOp):
    settingsUserGroups = SettingsUserGroups()
    jsonInput=json.loads(request.body.decode("utf-8"))
    data ={}
    group = settingsUserGroups.AdminGroup
    if settings.DEBUG: 
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print (jsonInput)
    try:
        cad = CadastroUsuario()
        cad.parser(jsonInput)
        cad.solicitante = request.user

        if typeOp == "cadastrar" or typeOp == "cadastro" or typeOp == "create":    
            data["PrimaryKey"] = cad.cadastrar(group=group)
        elif typeOp == "atualizar" or typeOp == "atualizacao" or typeOp == "update":
            cad.atualizar()
        elif typeOp == "deletar" or typeOp == "delecao" or typeOp == "delete":
            cad.deletar()

        data["status"] = "sucesso" 
        return Response(data,status=status.HTTP_202_ACCEPTED)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)    

@api_view(['POST','GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((SuperAdminOnly,))
def CadastroSuperAdministrador(request,typeOp):
    settingsUserGroups = SettingsUserGroups()
    jsonInput=json.loads(request.body.decode("utf-8"))
    data ={}
    group = settingsUserGroups.SuperAdminGroup
    if settings.DEBUG: 
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print (jsonInput)
    try:
        cad = CadastroUsuario()
        cad.parser(jsonInput)
        cad.solicitante = request.user

        if typeOp == "cadastrar" or typeOp == "cadastro" or typeOp == "create":    
            data["PrimaryKey"] = cad.cadastrar(group=group)
        elif typeOp == "atualizar" or typeOp == "atualizacao" or typeOp == "update":
            cad.atualizar()

        data["status"] = "sucesso" 
        return Response(data,status=status.HTTP_202_ACCEPTED)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data) 
        
# Create your views here.