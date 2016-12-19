from django.test import TestCase
from app.models import BuscaRecurso, CadastroRecurso

#=====[ testes para tratamento de recursos ]====================================

class RecursoTests( TestCase ):
    def setUp (self):
        pass

    def test_cadastro(self):
        nome = "nome"
        patrimonio = 1
        endereco = "endereco"
        categoria = "000"
        descricao = "test resource"

        cr = CadastroRecurso()

        # simple (pass)
        self.assertEqual(cr.cadastrar (nome, patrimonio, endereco, categoria, descricao), True)
        # same id (fail)
        self.assertEqual(cr.cadastrar (nome, patrimonio, endereco, categoria, descricao), False)
        # 200 character name (pass)
        patrimonio += 1
        nome = "nxe40kpXTvCPa0T88aJSXemKYWZDXv06ssZfE4gW0xsJgsHKLRWIgamYlYceoZ5hcHGVDAeLZQNJm4tEJxcVypHhV0liPtI9mInlcm0MQemP1qS9qPf1I8bVgniH3Y2OFXF5tOPmX4NTz2q73YfL660sMYtz7JVQQZfBR8jchSUEo2PRrOBFHuxj52rNMy2ToJ49BvMP"
        self.assertEqual(cr.cadastrar (nome, patrimonio, endereco, categoria, descricao), True)
        # 201 character name (pass)
        patrimonio += 1
        nome += "A2323"
        self.assertEqual(cr.cadastrar (nome, patrimonio, endereco, categoria, descricao), True)

#===============================================================================
