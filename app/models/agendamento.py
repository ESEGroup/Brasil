from django.db import models
from app.models import Recurso, Usuario

class Agendamento (models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    usuario = models.ForeignKey(Usuario)
    recurso = models.ForeignKey(Recurso)
    inicio  = models.DateTimeField()
    periodo = models.PositiveIntegerField() #seconds
    # state choices:
    ESTADO_CHOICES = (
        ('Agendado', 'Agendado'),
        ('Cancelado', 'Cancelado'),
        ('Confirmado', 'Confirmado'),
    )
    estado = models.CharField(
        max_length = 12,
        choices = ESTADO_CHOICES,
        default = 'Agendado',
    )

    def __str__(self):

        return self.recurso.nome + ' - '+ str(self.inicio)

    class Meta:
        db_table = 'Agendamentos'
        app_label = 'app'
