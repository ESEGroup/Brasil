from django.test import TestCase
from app.models import BuscaRecurso, CadastroRecurso
from random import randint


class RecursoTests( TestCase ):

    test_registers_number = 0
    nome = "nome"
    patrimonio_inicial = 1
    endereco = "endereco"
    categoria = "000"
    descricao = "test resource"

    def setUp (self):
        self.test_registers_number = randint(10, 100)
        print ("Testing for " + str(self.test_registers_number) + " resources")
        patrimonio = self.patrimonio_inicial
        cr = CadastroRecurso()
        for i in range(self.test_registers_number):
            cr.cadastrar (self.nome, patrimonio, self.endereco, self.categoria, self.descricao)
            patrimonio += 1

#=====[ testes de cadastro ]====================================================

    def test_cadastro(self):
        patrimonio = self.patrimonio_inicial + self.test_registers_number + 1

        cr = CadastroRecurso()

        # simple (pass)
        self.assertEqual(cr.cadastrar (self.nome, patrimonio, self.endereco, self.categoria, self.descricao), True)
        # same id (fail)
        self.assertEqual(cr.cadastrar (self.nome, patrimonio, self.endereco, self.categoria, self.descricao), False)
        # delete last register
        self.assertEqual(cr.deletar (patrimonio), True)
        self.assertEqual(cr.deletar (patrimonio), False)
        # 200 character name (pass)
        patrimonio += 1
        nome = "nxe40kpXTvCPa0T88aJSXemKYWZDXv06ssZfE4gW0xsJgsHKLRWIgamYlYceoZ5hcHGVDAeLZQNJm4tEJxcVypHhV0liPtI9mInlcm0MQemP1qS9qPf1I8bVgniH3Y2OFXF5tOPmX4NTz2q73YfL660sMYtz7JVQQZfBR8jchSUEo2PRrOBFHuxj52rNMy2ToJ49BvMP"
        self.assertEqual(cr.cadastrar (self.nome, patrimonio, self.endereco, self.categoria, self.descricao), True)
        self.assertEqual(cr.deletar (patrimonio), True)
        # 201 character name (pass)
        patrimonio += 1
        nome += "A2323"
        self.assertEqual(cr.cadastrar (self.nome, patrimonio, self.endereco, self.categoria, self.descricao), True)
        self.assertEqual(cr.deletar (patrimonio), True)

#=====[ testes de busca ]=======================================================

    def test_busca(self):
        # search all
        s = BuscaRecurso()
        s.params = '{"type": "complex",'
        s.params += '"texto": "",'
        s.params += '"categorias": [],'
        s.params += '"enderecos": [],'
        s.params += '"disponibilidades": [] }'
        res = s.buscar()
        self.assertEqual(len(res), self.test_registers_number)
        # search all by one of the categories
        s.params = '{"type": "complex",'
        s.params += '"texto": "",'
        s.params += '"categorias": ["000"],'
        s.params += '"enderecos": [],'
        s.params += '"disponibilidades": [] }'
        res = s.buscar()
        self.assertEqual(len(res), self.test_registers_number)
        s = BuscaRecurso()
        s.params = '{"type": "complex",'
        s.params += '"texto": "",'
        s.params += '"categorias": [],'
        s.params += '"enderecos": [],'
        s.params += '"disponibilidades": ["Indisponível"] }'
        res = s.buscar()
        self.assertEqual(len(res), self.test_registers_number)
        s = BuscaRecurso()
        s.params = '{"type": "complex",'
        s.params += '"texto": "",'
        s.params += '"categorias": [],'
        s.params += '"enderecos": ["endereco"],'
        s.params += '"disponibilidades": [] }'
        res = s.buscar()
        self.assertEqual(len(res), self.test_registers_number)


#=====[ testes de atualização e deleção ]=======================================

    def test_edit(self):
        patrimonio = self.patrimonio_inicial
        cr = CadastroRecurso()
        for i in range(self.test_registers_number):
            self.assertEqual(cr.atualizar ( patrimonio, "novo nome", "", "novo endereco", "001", "Disponível"), True)
            s = BuscaRecurso()
            s.params = '{"type": "match", "id": ' + str(patrimonio) + '}'
            res = s.buscar()
            self.assertEqual(res.nome, "novo nome")
            self.assertEqual(res.estado, "Disponível")
            self.assertEqual(res.descricao, "")
            self.assertEqual(res.endereco, "novo endereco")
            self.assertEqual(res.categoria, "001")
            cr.deletar(patrimonio)
            patrimonio += 1

#===============================================================================
