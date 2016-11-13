from django.db import models

class Recurso(models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    nome       = models.CharField(max_length=200)
    endereco   = models.CharField(max_length=200)
    descricao  = models.CharField(max_length=200)
    patrimonio = models.PositiveIntegerField()

    # state choices:
    ESTADO_CHOICES = (
        ('AV', 'Disponível'),
        ('UV', 'Indisponível'),
        ('MA', 'Em manutenção'),
    )
    estado = models.CharField(
        max_length = 2,
        choices = ESTADO_CHOICES,
        default = 'UV',
    )

    # category choices:
    CATEGORIA_CHOICES = (
        # unknown
        ('000', 'Desconhecido'),
        # classroom equipments
        ('001', 'Monitor'),
        ('002', 'Projetor'),
        ('003', 'Acessório para computador'),
        ('004', 'Computador'),
        ('005', 'Material de escritório'),
        ('006', 'Móvel'),
        # rooms and buildings
        ('007', 'Sala de Aula'),
        ('008', 'Auditório'),
        ('009', 'Imóvel'),
        # other equipments
        ('010', 'Equipamento laboratorial'),
        ('011', 'Equipamento de limpeza'),
        ('012', 'Equipamento métrico'),
        ('013', 'Equipamento de manutenção'),
        ('014', 'Outro equipamento'),
    )
    estado = models.CharField(
        max_length = 3,
        choices = CATEGORIA_CHOICES,
        default = '000',
    )

    class Meta:
        db_table = 'Recursos'
        app_label = 'app'
