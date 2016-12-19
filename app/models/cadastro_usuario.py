from django.db import models
from app.models import  Cadastro, Usuario
from django.contrib.auth.models import User, Group
from .settingsgroups import SettingsUserGroups

class CadastroUsuario(Cadastro):

    notificador = None #NotificadorCadastro
    usuario = Usuario()
    usuarioTemplate = Usuario()
    solicitante = Usuario()
    settingsUserGroups = SettingsUserGroups()

    def has_permission(self):
        if self.solicitante.groups.all()[0].pk == self.settingsUserGroups.AdminGroup:
            if Usuario.objects.get(user=self.solicitante).departamento != self.usuarioTemplate.departamento:
                return False
            if self.usuario.departamento != self.usuarioTemplate.departamento:
                return False  
        return True    

    def parser (self,json):
        #model : {"pk":"1","username":"anything", "password":"pass", "email":"somethind@mail.com", "first_name" : " ", 
        #"last_name" : " ", "registro" : "5", "departamento" : ""}
        self.usuarioTemplate.usr = User()
        self.usuarioTemplate.usr.username = json['username']
        if 'password' in json.keys():
            self.usuarioTemplate.usr.set_password(json['password'])
        self.usuarioTemplate.usr.email = json['email']
        self.usuarioTemplate.usr.first_name = json['first_name']
        self.usuarioTemplate.usr.last_name = json['last_name']
        if 'pk' in json.keys() and json['pk'] != '':
            self.usuarioTemplate.pk=int(json['pk'])
            self.usuario = Usuario.objects.get(pk=self.usuarioTemplate.pk)
        self.usuarioTemplate.registro = int(json['registro'])
        self.usuarioTemplate.departamento = json['departamento']
        
    def cadastrar (self,group):
        self.usuario.usr = User.objects.create_user(
            username=self.usuarioTemplate.usr.username,
            email=self.usuarioTemplate.usr.email, 
            first_name=self.usuarioTemplate.usr.first_name, 
            last_name=self.usuarioTemplate.usr.last_name
            )
        self.usuario.usr.groups.add(Group.objects.get(pk=group))

        self.usuario =  Usuario.objects.create(
            user=self.usuario.usr,
            registro=self.usuarioTemplate.registro,
            departamento=self.usuarioTemplate.departamento
            )
        return self.usuario.pk
        #falta notificação

    def atualizar (self):
        self.usuario.user.username = self.usuarioTemplate.usr.username
        self.usuario.user.password = self.usuarioTemplate.usr.password
        self.usuario.user.email = self.usuarioTemplate.usr.email
        self.usuario.user.first_name = self.usuarioTemplate.usr.first_name
        self.usuario.user.last_name = self.usuarioTemplate.usr.last_name
        self.usuario.registro = self.usuarioTemplate.registro
        self.usuario.departamento = self.usuarioTemplate.departamento
        self.usuario.user.save()
        self.usuario.save()

    def deletar (self):
        self.usuario.user.is_active = False
        self.usuario.user.save()

    def notificar (self):
        return False

    class Meta:
        managed = False
        app_label = 'app'
