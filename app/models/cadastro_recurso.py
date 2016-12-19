from django.db import models
from app.models import  Usuario, Recurso, Cadastro, BuscaRecurso

class CadastroRecurso(Cadastro):

    notificador = None #NotificadorCadastro
    recurso = None
    solicitante = None

    def cadastrar (self, nome, patrimonio, endereco, categoria, descricao):
        s = BuscaRecurso()
        s.params = '{"type": "match", "id": ' + str(patrimonio) + '}'
        print(s.params)
        res = s.buscar()

        if res != "DoesNotExist ERROR":
            return False

        rec = Recurso(nome=nome, patrimonio=patrimonio, endereco=endereco, categoria=categoria, descricao=descricao)
        rec.save()
        return True

    def atualizar (self, patrimonio, nome, descricao, endereco, categoria, estado):

        s = BuscaRecurso()
        s.params = '{"type": "match", "id": ' + str(patrimonio) + '}'
        print(s.params)
        res = s.buscar()

        if res == "DoesNotExist ERROR":
            # if resource already exists..
            return False

        res.nome=nome
        res.endereco=endereco
        res.categoria=categoria
        res.descricao=descricao
        res.estado=estado
        res.save()
        return True

    def deletar ():
        return False

    def notificar ():
        return False

    class Meta:
        managed = False
        app_label = 'app'
