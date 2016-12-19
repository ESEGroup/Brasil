from django.db import models
from app.models import  Cadastro, Usuario, Agendamento, Recurso
from django.contrib.auth.models import User, Group
from .settingsgroups import SettingsUserGroups

class CadastroAgendamento(Cadastro):

    notificador = None #NotificadorAgendamento
    solicitante = Usuario()
    settingsUserGroups = SettingsUserGroups()
    agendamento = Agendamento()
    agendamentoTemplate = Agendamento()
    agendamentoTemplate.usuario = Usuario()
    agendamentoTemplate.recurso = Recurso()


    def has_permission(self):
        #if self.solicitante.groups.all()[0].pk == self.settingsUserGroups.AdminGroup:
         #   if Usuario.objects.get(user=self.solicitante).departamento != self.usuarioTemplate.departamento:
        #        return False
            #if self.usuario.departamento != self.usuarioTemplate.departamento:
            #    return False  
        return True    
        
    def parser (self,json):
        #model : {"pk":"9","username":"anything", "patrimonio":"7","inicio":"2006-10-25 14:30:59","periodo":"7"}
        self.agendamentoTemplate.inicio = json["inicio"]
        self.agendamentoTemplate.periodo = json["periodo"]
        user = User.objects.get(username=json["username"])
        self.agendamentoTemplate.usuario = Usuario.objects.get(user=user)
        self.agendamentoTemplate.recurso = Recurso.objects.get(patrimonio=int(json["patrimonio"]))
        if 'pk' in json.keys() and json['pk'] != '':
            self.agendamentoTemplate.pk=int(json['pk'])
            self.agendamento = Agendamento.objects.get(pk=self.agendamentoTemplate.pk)
        
        
    def cadastrar (self):
        self.agendamento = Agendamento.objects.create(
            usuario= self.agendamentoTemplate.usuario,
            recurso = self.agendamentoTemplate.recurso,
            inicio  = self.agendamentoTemplate.inicio,
            periodo = self.agendamentoTemplate.periodo,
            estado = "Agendado"
            )

        return self.agendamento.pk
        #falta notificação

    def deletar (self):
        self.agendamento.estado = "Cancelado"
        self.agendamento.save()

    '''
    def atualizar (self):
        

        

    def notificar (self):
        return False
    '''
    class Meta:
        managed = False
        app_label = 'app'
