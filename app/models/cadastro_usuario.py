from django.db import models
from app.models import  Cadastro, Usuario
from django.contrib.auth.models import User, Group

class CadastroUsuario(Cadastro):

    notificador = None #NotificadorCadastro
    usuario = Usuario()
    solicitante = Usuario()

    def parser (self,json):
        #model : {"username":"anything", "password":"pass", "email":"somethind@mail.com", "first_name" : " ", 
        #"last_name" : " ", "registro" : "5", "departamento" : ""}
        self.usuario.usr = User()
        self.usuario.usr.username = json['username']
        self.usuario.usr.email = json['email']
        self.usuario.usr.first_name = json['first_name']
        self.usuario.usr.last_name = json['last_name']
        self.usuario.registro = int(json['registro'])
        self.usuario.departamento = json['departamento']
        if 'password' in json.keys():
            self.usuario.usr.set_password(json['password'])
        
    def cadastrar (self):
        self.usuario.usr = User.objects.create_user(
            username=self.usuario.usr.username,
            email=self.usuario.usr.email, 
            first_name=self.usuario.usr.first_name, 
            last_name=self.usuario.usr.last_name
            )
        self.usuario.usr.groups.add(Group.objects.get(id=7))

        self.usuario =  Usuario.objects.create(
            user=self.usuario.usr,
            registro=self.usuario.registro,
            departamento=self.usuario.departamento
            )
        #falta notificação

    def atualizar (self):
        self.usuario.save()

    def deletar (self):
        return False

    def notificar (self):
        return False

    class Meta:
        managed = False
        app_label = 'app'
