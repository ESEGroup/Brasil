from django.db import models
from app.models import Recurso, Usuario

class Agendamento ():
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    usuario = models.ForeignKey(Usuario)
    recurso = models.ForeignKey(Recurso)
    inicio  = models.DateTimeField()
    periodo = models.PositiveIntegerField() #seconds
    # state choices:
    ESTADO_CHOICES = (
        ('AG', 'Agendado'),
        ('CA', 'Cancelado'),
        ('CF', 'Confirmado'),
    )
    estado = models.CharField(
        max_length = 2,
        choices = ESTADO_CHOICES,
        default = 'AG',
    )

    class Meta:
        db_table = 'Agendamentos'
        app_label = 'app'
